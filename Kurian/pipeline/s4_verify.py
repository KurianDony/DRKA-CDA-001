#!/usr/bin/env python3
"""S4 — Assemble review.md + integrity checks for one house.

Checks (doc 08 §4 adapted for CSV source):
  1. Task-ID exclusivity across the three filtered CSVs (a task lives in one project only)
  2. No duplicate Task IDs within a file
  3. Timeline date sanity: all event dates within (window start - 24 months … today + 3 months)
  4. Per room: move_out count vs move_in count delta reported (context, not a hard fail)
  5. Row-count deltas: filtered top-level rows vs timeline events per source (must be 0)

Usage: python3 pipeline/s4_verify.py <house-slug>
Output: data/houses/<slug>/review.md (header + 3 review sections) + VERIFY.md
"""
import sys
from collections import Counter, defaultdict
from datetime import date, timedelta
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent / "lib"))
from common import (PROJECT_ROOT, load_settings, house_config, read_csv, parse_date,
                    now_sydney_iso, append_runlog)

def main(slug):
    st = load_settings()
    hc = house_config(slug)
    outdir = PROJECT_ROOT / st["houses_dir"] / slug

    # --- assemble review.md ---
    parts = [f"# Task review — {hc['canonical_address']} ({slug})",
             f"Assembled: {now_sydney_iso()}",
             "One line per top-level task. **HUMAN REVIEW** = date-altering or house-attribution "
             "issue needing Kurian's eyes. Subtasks excluded (tagged is_subtask in the CSVs).", ""]
    for src in st["sources"]:
        f = outdir / f"review_{src}.md"
        if f.exists():
            parts.append(f.read_text(encoding="utf-8").strip())
            parts.append("")
    (outdir / "review.md").write_text("\n".join(parts), encoding="utf-8")

    # --- integrity checks ---
    results, fail = [], False
    ids_by_src, top_counts = {}, {}
    for src in st["sources"]:
        rows, _ = read_csv(outdir / f"{src}_filtered.csv")
        ids = [r["Task ID"] for r in rows]
        dupes = [i for i, c in Counter(ids).items() if c > 1]
        results.append(f"[{'FAIL' if dupes else 'PASS'}] {src}: duplicate Task IDs within file: {dupes or 'none'}")
        fail |= bool(dupes)
        ids_by_src[src] = set(ids)
        top_counts[src] = sum(1 for r in rows if r.get("is_subtask") != "yes")
    # Exclusivity: shared IDs are OK when the task is genuinely multi-homed (Projects column
    # or a subtask exported under both projects). Only unexplained sharing fails.
    rows_by_src = {}
    for src in st["sources"]:
        rows, _ = read_csv(outdir / f"{src}_filtered.csv")
        rows_by_src[src] = {r["Task ID"]: r for r in rows}
    srcs = list(ids_by_src)
    for i in range(len(srcs)):
        for j in range(i + 1, len(srcs)):
            inter = ids_by_src[srcs[i]] & ids_by_src[srcs[j]]
            unexplained = [t for t in inter
                           if rows_by_src[srcs[i]][t].get("is_subtask") != "yes"
                           and len([p for p in (rows_by_src[srcs[i]][t].get("Projects") or "").split(",") if p.strip()]) < 2]
            results.append(f"[{'FAIL' if unexplained else 'PASS'}] Task-ID exclusivity {srcs[i]}∩{srcs[j]}: "
                           f"{len(inter)} shared ({len(inter)-len(unexplained)} multi-homed/subtask, "
                           f"unexplained: {unexplained or 'none'})")
            fail |= bool(unexplained)

    tl, _ = read_csv(outdir / "timeline.csv")
    lo = parse_date(st["audit_window"]["start"]) - timedelta(days=max(st["window_padding_days"].values()))
    hi = parse_date(st["audit_window"]["end"]) + timedelta(days=max(st["window_padding_days"].values()))
    bad = [e["task_id"] for e in tl if e["event_date"] and not (lo <= parse_date(e["event_date"]) <= hi)]
    results.append(f"[{'FAIL' if bad else 'PASS'}] timeline dates within {lo}…{hi}: {len(bad)} outside {bad or ''}")
    fail |= bool(bad)
    nodate = [e["task_id"] for e in tl if not e["event_date"]]
    results.append(f"[{'WARN' if nodate else 'PASS'}] events with no parseable date: {len(nodate)} {nodate or ''}")

    # One event per unique top-level task (S3 dedupes multi-homed tasks across sources)
    top_ids = set()
    for src in st["sources"]:
        top_ids |= {t for t, r in rows_by_src[src].items() if r.get("is_subtask") != "yes"}
    ov_path = outdir / "overrides.csv"
    n_excluded = n_promoted = 0
    all_ids = set()
    for src in st["sources"]:
        all_ids |= set(rows_by_src[src])
    if ov_path.exists():
        for r in read_csv(ov_path)[0]:
            if r["action"] == "exclude" and r["task_id"] in top_ids:
                n_excluded += 1
            elif r["action"] == "promote_move_out" and r["task_id"] in all_ids and r["task_id"] not in top_ids:
                n_promoted += 1  # subtask promoted to a move-out event
    delta = len(top_ids) - n_excluded + n_promoted - len(tl)
    results.append(f"[{'FAIL' if delta else 'PASS'}] row-count: top-level {len(top_ids)} - {n_excluded} excluded "
                   f"+ {n_promoted} promoted-subtasks vs timeline events {len(tl)} (delta {delta})")
    fail |= bool(delta)

    # Room-resolution gate (pilot finding #3 — the 66 Boundary blind spot):
    # an UNRESOLVED move-out whose Name contains a '#code' that IS a valid house code
    # means room attribution failed, not that the room is unknown.
    from common import room_codes_in_text
    hc = house_config(slug)
    valid = set(c.upper() for c in hc["room_codes"])
    strand = [e["task_id"] for e in tl if e["event_type"] == "move_out" and not e["room_code"]
              and room_codes_in_text(e["task_name"]) & valid]
    results.append(f"[{'FAIL' if strand else 'PASS'}] room-resolution: move-outs stranded UNRESOLVED "
                   f"despite valid #code in name: {strand or 'none'}")
    fail |= bool(strand)
    n_unres_mo = sum(1 for e in tl if e["event_type"] == "move_out" and not e["room_code"])
    results.append(f"[{'WARN' if n_unres_mo else 'PASS'}] unresolved move-outs (no code anywhere): {n_unres_mo}")

    per_room = defaultdict(Counter)
    for e in tl:
        per_room[e["room_code"] or "UNRESOLVED"][e["event_type"]] += 1
    balance = {rc: f"in={c['move_in']} out={c['move_out']}" for rc, c in sorted(per_room.items())}
    results.append(f"[INFO] per-room in/out balance: {balance}")

    verdict = "FAIL" if fail else "PASS"
    (outdir / "VERIFY.md").write_text(
        f"# VERIFY — {slug}\nRun: {now_sydney_iso()}\nVerdict: **{verdict}**\n\n"
        + "\n".join(f"- {r}" for r in results) + "\n", encoding="utf-8")
    append_runlog(f"{now_sydney_iso()} | {slug} | s4-verify | script:s4_verify.py | {verdict} | "
                  f"{sum(r.startswith('[FAIL') for r in results)} failing checks")
    print(f"Verdict: {verdict}")
    print("\n".join(results))
    if fail:
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
