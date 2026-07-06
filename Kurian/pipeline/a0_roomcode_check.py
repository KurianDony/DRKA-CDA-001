#!/usr/bin/env python3
"""A0 — Room-code integrity gate. Runs BEFORE any extraction for a batch.

For every house in the batch manifest, verifies its room codes are legit and unambiguous:
  C1  cross-house duplicates within the ENTIRE registry (roster level)
  C2  duplicate code assigned to two rooms within the same house (roster level)
  C3  bed-code consistency: letter-suffixed codes (e.g. 050A/050B) — lists groups so
      beds are never counted as rooms; orphan letters (B with no A) flagged
  C4  DATA-LEVEL legitimacy: scans the raw move-in/move-out CSVs for '#<code>' mentions
      and checks the surrounding text contains THIS house's match pattern. A code whose
      mentions point at a different/multiple addresses is AMBIGUOUS → fails the gate
      for that house until resolved (matching for it must be address+code, never bare code).

Verdict per house: PASS / FAIL. Any FAIL blocks that house (not the batch).
Output: pipeline/config/roomcode_check_<batch>.md + RUNLOG lines.

Usage: python3 pipeline/a0_roomcode_check.py <batch-file.json>
       e.g. python3 pipeline/a0_roomcode_check.py data/batches/batch-00-pilot.json
"""
import csv, json, re, sys
from collections import defaultdict
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent / "lib"))
from common import PROJECT_ROOT, load_settings, now_sydney_iso, append_runlog

def load_registry():
    reg = json.loads((PROJECT_ROOT / "pipeline/config/registry.json").read_text())
    hand = json.loads((PROJECT_ROOT / "pipeline/config/houses.json").read_text())
    reg.update(hand)  # hand-curated wins
    return reg

def main(batch_path):
    st = load_settings()
    batch = json.loads((PROJECT_ROOT / batch_path).read_text())
    slugs = list(batch["houses"])
    reg = load_registry()

    # C1: cross-house dupes over the whole registry
    owner = defaultdict(set)
    for slug, e in reg.items():
        for c in e.get("room_codes", []):
            owner[str(c).upper()].add(slug)
    global_dupes = {c: sorted(s) for c, s in owner.items() if len(s) > 1}

    # data-level mention index: '#code' -> list of (source, name-ish context)
    mention = defaultdict(list)
    for source in ("movein", "moveout"):
        p = PROJECT_ROOT / st["raw_data_dir"] / st["sources"][source]
        for row in csv.DictReader(open(p, encoding="utf-8-sig")):
            name = row.get("Name") or ""
            blob = (name + " " + (row.get("(General) House Address ") or "") + " " +
                    (row.get("Full House Address") or "")).lower()
            for c in set(re.findall(r"#\s?(\d{1,4}[A-Za-z]?)\b", name)):
                mention[c.upper()].append(blob[:160])

    lines = [f"# A0 room-code integrity check — batch {batch.get('batch')} — {now_sydney_iso()}", ""]
    any_fail = False
    for slug in slugs:
        e = reg.get(slug)
        if not e:
            lines += [f"## {slug}: **FAIL** — no registry entry", ""]
            any_fail = True
            continue
        codes = [str(c).upper() for c in e.get("room_codes", [])]
        pats = [p.lower() for p in e.get("match_patterns", [])]
        probs, notes = [], []
        dupes_here = {c: [s for s in global_dupes[c] if s != slug] for c in codes if c in global_dupes}
        if dupes_here:
            probs.append(f"C1 cross-house dupes: {dupes_here} → these codes need address+code matching")
        seen = set()
        c2 = [c for c in codes if c in seen or seen.add(c)]
        if c2:
            probs.append(f"C2 same code listed twice in house: {c2}")
        beds = defaultdict(list)
        for c in codes:
            m = re.match(r"^(\d+)([A-Za-z])$", c)
            if m:
                beds[m.group(1)].append(m.group(2))
        for base, letters in beds.items():
            group = sorted(letters)
            notes.append(f"C3 bed group {base}{'/'.join(group)} = {len(group)} beds, ONE room")
            if "B" in group and "A" not in group and base not in codes:
                probs.append(f"C3 orphan bed code {base}B without {base}A or bare {base}")
        for c in codes:
            ms = mention.get(c, [])
            if not ms:
                notes.append(f"C4 {c}: no #-mentions in move data (quiet room — fine)")
                continue
            foreign = [m for m in ms if not any(p in m for p in pats)]
            if len(foreign) > len(ms) * 0.5 and len(ms) >= 2:
                probs.append(f"C4 {c}: {len(foreign)}/{len(ms)} mentions lack this house's pattern "
                             f"— AMBIGUOUS. Sample: {foreign[0][:100]!r}")
            elif foreign:
                notes.append(f"C4 {c}: {len(foreign)}/{len(ms)} mentions in foreign context (transfers likely) — address+code matching required")
        verdict = "FAIL" if probs else "PASS"
        any_fail |= bool(probs)
        lines.append(f"## {slug}: **{verdict}**")
        lines += [f"- PROBLEM: {p}" for p in probs]
        lines += [f"- note: {n}" for n in notes]
        lines.append("")
        append_runlog(f"{now_sydney_iso()} | {slug} | a0-roomcode-check | script:a0_roomcode_check.py | {verdict} | "
                      f"{len(probs)} problems, {len(notes)} notes")
    out = PROJECT_ROOT / "pipeline/config" / f"roomcode_check_{batch.get('batch','batch')}.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))
    print(f"\nGate: {'FAIL — fix or park failing houses before extraction' if any_fail else 'PASS — batch may proceed'}")
    sys.exit(1 if any_fail else 0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
