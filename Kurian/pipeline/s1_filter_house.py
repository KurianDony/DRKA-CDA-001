#!/usr/bin/env python3
"""S1 — Filter the three raw Asana CSV exports down to one house.

Match logic (per Kurian's spec):
  1. ANY field contains a house match_pattern (e.g. '342 cleveland') — not just task name,
     because temporary sales / temp rooms mention the house in notes etc.
  2. OR the row's Room Code column / '#<code>' text reference matches one of the house's
     room codes (codes are portfolio-unique).
Collision guard: patterns are house-number-anchored, so 285/287/289/295/390/394/398
Cleveland St never match.

Window (Kurian 2026-07-05): rows whose event date falls OUTSIDE the padded window are
DROPPED. Padding per source: movein/moveout ±7 days, maintenance ±31 days around the audit
window. Event date = first parseable field in settings event_date_fields for that source.
Rows with NO parseable event date are kept and flagged (never silently dropped).
`in_window` column = inside the unpadded audit window proper.
Also adds `task_url` (Asana permalink built from Task ID) — required on everything sent
for human review.

Usage: python3 pipeline/s1_filter_house.py <house-slug>
Output: data/houses/<slug>/{movein,moveout,maintenance}_filtered.csv + filter_report.md
"""
import sys
from datetime import timedelta
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent / "lib"))
from common import (PROJECT_ROOT, load_settings, house_config, read_csv, write_csv,
                    parse_date, room_codes_in_text, now_sydney_iso, append_runlog)

def main(slug):
    st = load_settings()
    hc = house_config(slug)
    patterns = [p.lower() for p in hc["match_patterns"]]
    codes = set(c.upper() for c in hc["room_codes"])
    a_start = parse_date(st["audit_window"]["start"])
    a_end = parse_date(st["audit_window"]["end"])
    outdir = PROJECT_ROOT / st["houses_dir"] / slug
    outdir.mkdir(parents=True, exist_ok=True)
    report = [f"# S1 filter report — {hc['canonical_address']} ({slug})",
              f"Run: {now_sydney_iso()}",
              f"Audit window: {a_start} → {a_end}; padding: {st['window_padding_days']}", ""]

    for source, fname in st["sources"].items():
        pad = timedelta(days=st["window_padding_days"][source])
        w_start, w_end = a_start - pad, a_end + pad
        rows, fields = read_csv(PROJECT_ROOT / st["raw_data_dir"] / fname)
        kept = []
        n_addr = n_code_only = n_inwin = n_dropped = n_nodate = 0
        for row in rows:
            blob = " ".join(v for v in row.values() if v).lower()
            addr_hit = any(p in blob for p in patterns)
            code_col = (row.get("Room Code") or "").strip().upper()
            code_hits = ({code_col} | room_codes_in_text(blob)) & codes
            # Room-code-ONLY matching (no address) requires codes of >=3 chars: short codes
            # (#7, #8…) are ordinary room NUMBERS at every house, and free text like
            # "the room is #8 at that property" pulls in other houses' tasks
            # (66 Boundary Kapil/Gabriel/Malik case, Kurian 2026-07-05).
            strong_hits = {c for c in code_hits if len(c) >= 3}
            if not addr_hit and not strong_hits:
                continue
            ev_date = next((d for f in st["event_date_fields"][source]
                            if (d := parse_date(row.get(f, ""))) is not None), None)
            if ev_date and not (w_start <= ev_date <= w_end):
                n_dropped += 1
                continue  # outside padded window — dropped (Kurian 2026-07-05)
            if not ev_date:
                n_nodate += 1
            reason = ("address+room_code" if (addr_hit and code_hits)
                      else "address" if addr_hit else "room_code_only")
            if addr_hit: n_addr += 1
            if reason == "room_code_only": n_code_only += 1
            in_window = bool(ev_date) and a_start <= ev_date <= a_end
            if in_window: n_inwin += 1
            row = dict(row)
            row["match_reason"] = reason
            row["matched_room_codes"] = "|".join(sorted(code_hits))
            row["event_date"] = ev_date.isoformat() if ev_date else ""
            row["in_window"] = "yes" if in_window else ("no" if ev_date else "no_date")
            row["is_subtask"] = "yes" if (row.get("Parent task") or "").strip() else ""
            row["task_url"] = st["asana_url_template"].format(task_id=row.get("Task ID", ""))
            kept.append(row)
        n_sub = sum(1 for r in kept if r["is_subtask"])
        out_fields = list(fields) + ["match_reason", "matched_room_codes", "event_date",
                                     "in_window", "is_subtask", "task_url"]
        out = outdir / f"{source}_filtered.csv"
        write_csv(out, kept, out_fields)
        report += [f"## {source} ({fname})",
                   f"- raw rows scanned: {len(rows)}",
                   f"- padded window: {w_start} → {w_end}",
                   f"- rows kept: {len(kept)} (address hits: {n_addr}, room-code-only: {n_code_only}, "
                   f"subtasks: {n_sub}, top-level: {len(kept) - n_sub})",
                   f"- house matches dropped as outside padded window: {n_dropped}",
                   f"- kept with no parseable event date: {n_nodate}",
                   f"- rows in audit window proper: {n_inwin}",
                   f"- output: {out.relative_to(PROJECT_ROOT)}", ""]
        append_runlog(f"{now_sydney_iso()} | {slug} | s1-filter:{source} | script:s1_filter_house.py | done | "
                      f"{len(kept)} kept of {len(rows)} ({n_dropped} out-of-window dropped; {n_nodate} no-date kept)")
    (outdir / "filter_report.md").write_text("\n".join(report), encoding="utf-8")
    print("\n".join(report))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
