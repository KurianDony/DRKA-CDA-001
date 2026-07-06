#!/usr/bin/env python3
"""S6 — Gap hunt: find the tasks the strict filter missed (Kurian 2026-07-05:
"the move-out tasks ARE there — search fuzzier").

1. Detect anomalies in tenancies.csv:
   T1 ongoing tenancy            → hunt for a MISSED MOVE-OUT
   T2 pre_window / orphan_out    → hunt for a MISSED MOVE-IN (in-window only)
   T3 room over-occupancy        → >1 concurrent tenancy in a room (>2 for A/B bed rooms)
                                   → hunt for the missing move-out of the earlier tenant
2. For each hunt target, scan the ENTIRE raw export (all houses, top-level AND subtasks —
   transfer-outs hide in subtasks) with fuzzy matching:
   - tenant name: token-level (any two tokens sharing a >=3-char prefix = strong; one
     >=4-char token = weak) — tolerates missing/reordered/misspelt name parts
   - room code family: exact code, or A/B bed-fuzzy (41 ≈ 41A ≈ 41B ≈ 041 — strip leading
     zeros + letter suffix)
   - house address pattern
   - date plausibility (candidate event date vs tenancy start)
3. Score and report top candidates per target. NOTHING is auto-applied — the orchestrator
   attaches finds via overrides (promote_move_out / set_move_out_date / reassign_room) and
   re-runs S3→S5→S4.

Usage: python3 pipeline/s6_gap_hunt.py <house-slug>
Output: data/houses/<slug>/gap_hunt.md + gap_hunt.csv + RUNLOG line
"""
import csv, re, sys
from collections import defaultdict
from datetime import timedelta
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent / "lib"))
from common import (PROJECT_ROOT, load_settings, house_config, read_csv, write_csv,
                    parse_date, now_sydney_iso, append_runlog)

ASANA = "https://app.asana.com/0/0/{}/f"

def toks(s):
    return [t.lower() for t in re.split(r"[^A-Za-z]+", s or "") if len(t) >= 3]

def name_score(target, text):
    tt, xt = toks(target), toks(text)
    strong = sum(1 for a in tt if any(a[:3] == b[:3] and (a[:4] == b[:4] or min(len(a), len(b)) < 4)
                                      for b in xt))
    if strong >= 2:
        return 2.0
    if any(a[:4] == b[:4] for a in tt for b in xt if min(len(a), len(b)) >= 4):
        return 1.0
    return 0.0

def code_family(c):
    return (c or "").upper().rstrip("ABCDEFGH").lstrip("0") or (c or "").upper()

def main(slug):
    st = load_settings()
    hc = house_config(slug)
    outdir = PROJECT_ROOT / st["houses_dir"] / slug
    patterns = [p.lower() for p in hc["match_patterns"]]
    a_start, a_end = parse_date(st["audit_window"]["start"]), parse_date(st["audit_window"]["end"])
    tens, _ = read_csv(outdir / "tenancies.csv")
    known_ids = set()
    for src in st["sources"]:
        p = outdir / f"{src}_filtered.csv"
        if p.exists():
            known_ids |= {r["Task ID"] for r in read_csv(p)[0]}

    # ---- targets ----
    targets = []
    for t in tens:
        if t["end_kind"] == "ongoing" and t["tenant"]:
            targets.append(("T1_missing_moveout", t["tenant"], t["room_code"], parse_date(t["start"])))
        if t["start_kind"] in ("pre_window", "orphan_out") and t["tenant"]:
            targets.append(("T2_missing_movein", t["tenant"], t["room_code"], parse_date(t["end"])))
    # T3 over-occupancy: count concurrent tenancies per room-family per day (weekly steps)
    fam_caps = defaultdict(set)
    for c in hc["room_codes"]:
        fam_caps[code_family(c)].add(c.upper())
    by_fam = defaultdict(list)
    for t in tens:
        by_fam[code_family(t["room_code"])].append(t)
    overocc = []
    for fam, rows in by_fam.items():
        cap = max(1, len(fam_caps.get(fam, {1})))
        d = a_start
        while d <= a_end:
            conc = [t for t in rows
                    if (parse_date(t["start"]) or a_start) <= d <= (parse_date(t["end"]) or a_end)]
            if len(conc) > cap:
                overocc.append((fam, d, [t["tenant"] for t in conc]))
                for t in conc:
                    if t["end_kind"] == "ongoing" and t["tenant"]:
                        targets.append(("T3_overocc_moveout", t["tenant"], t["room_code"],
                                        parse_date(t["start"])))
                break  # one hit per family is enough to trigger the hunt
            d += timedelta(days=7)
    # dedupe targets
    seen, uniq = set(), []
    for tg in targets:
        k = (tg[0], tg[1].lower(), tg[2])
        if k not in seen:
            seen.add(k)
            uniq.append(tg)

    # ---- hunt ----
    hunts = {"T1_missing_moveout": "moveout", "T3_overocc_moveout": "moveout",
             "T2_missing_movein": "movein"}
    raw_cache = {}
    results = []
    for kind, tenant, room, refdate in uniq:
        src = hunts[kind]
        if src not in raw_cache:
            raw_cache[src] = list(csv.DictReader(
                open(PROJECT_ROOT / st["raw_data_dir"] / st["sources"][src], encoding="utf-8-sig")))
        fam = code_family(room)
        cands = []
        for row in raw_cache[src]:
            text = " ".join(filter(None, [row.get("Name"), row.get("Tenant Name")]))
            ns = name_score(tenant, text)
            if ns == 0:
                continue
            blob = " ".join(v for v in row.values() if v).lower()
            cs = 1.5 if (fam and (fam == code_family(row.get("Room Code") or "")
                         or re.search(r"#\s?0*" + re.escape(fam) + r"[A-Za-z]?\b", blob))) else 0.0
            ads = 1.0 if any(p in blob for p in patterns) else 0.0
            dd = next((parse_date(row.get(f, "")) for f in ("Due Date", "Completed At", "Created At")
                       if parse_date(row.get(f, ""))), None)
            ds = 0.5 if (dd and refdate and dd >= refdate - timedelta(days=3)) else 0.0
            score = ns + cs + ads + ds
            if score >= 2.5:
                cands.append((score, row, dd))
        cands.sort(key=lambda x: -x[0])
        for score, row, dd in cands[:5]:
            tid = row.get("Task ID", "")
            results.append({
                "target_kind": kind, "tenant": tenant, "room_code": room,
                "candidate_task_id": tid, "candidate_url": ASANA.format(tid),
                "candidate_name": (row.get("Name") or "")[:110],
                "candidate_date": dd.isoformat() if dd else "",
                "is_subtask": "yes" if (row.get("Parent task") or "").strip() else "",
                "score": round(score, 1),
                "already_in_dataset": "yes" if tid in known_ids else "",
            })

    write_csv(outdir / "gap_hunt.csv", results, list(results[0].keys()) if results else
              ["target_kind", "tenant", "room_code", "candidate_task_id", "candidate_url",
               "candidate_name", "candidate_date", "is_subtask", "score", "already_in_dataset"])
    lines = [f"# S6 gap hunt — {slug} — {now_sydney_iso()}", "",
             f"Targets hunted: {len(uniq)} (over-occupancy families: {[(f, d.isoformat(), n) for f, d, n in overocc] or 'none'})", ""]
    for kind, tenant, room, refdate in uniq:
        rs = [r for r in results if r["tenant"] == tenant and r["target_kind"] == kind]
        lines.append(f"## {kind} — {tenant} (room {room}, ref {refdate})")
        if not rs:
            lines.append("- no candidates found anywhere in the export (genuinely absent or "
                         "name/code too different — manual Asana search advised)")
        for r in rs:
            lines.append(f"- score {r['score']}: [{r['candidate_task_id']}]({r['candidate_url']}) "
                         f"{r['candidate_name']} | {r['candidate_date']}"
                         f"{' | SUBTASK' if r['is_subtask'] else ''}"
                         f"{' | ALREADY IN DATASET (check its disposition)' if r['already_in_dataset'] else ' | NOT in filtered set — attach via override if real'}")
        lines.append("")
    (outdir / "gap_hunt.md").write_text("\n".join(lines), encoding="utf-8")
    append_runlog(f"{now_sydney_iso()} | {slug} | s6-gap-hunt | script:s6_gap_hunt.py | done | "
                  f"{len(uniq)} targets, {len(results)} candidates, overocc: {len(overocc)}")
    print("\n".join(lines))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
