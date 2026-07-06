#!/usr/bin/env python3
"""S2 — Heuristic pre-flags on the S1-filtered CSVs, ahead of AI review.

Adds columns:
  flag_transfer_cancel  transfer / cancellation / retention markers (rewrite the timeline)
  flag_date_keyword     notes/name text suggesting a date was altered
  flag_inconsistency    machine-checkable date-field inconsistencies
  human_review          yes if ANY flag fired (per Kurian: date-altering => human review)

Usage: python3 pipeline/s2_preflag.py <house-slug>
Rewrites data/houses/<slug>/*_filtered.csv in place (adds columns) + preflag_report.md
"""
import re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent / "lib"))
from common import (PROJECT_ROOT, load_settings, house_config, read_csv, write_csv,
                    parse_date, now_sydney_iso, append_runlog)

DATE_KEYWORDS = [
    "moved to", "pushed back", "push back", "postpon", "reschedul", "new move in date",
    "new move-in date", "new moveout date", "new move-out date", "changed date",
    "date change", "change of date", "extend", "brought forward", "bring forward",
    "delay", "earlier date", "later date", "new due date", "moving date",
]
TRANSFER_CANCEL_RE = re.compile(
    r"transfer|cancel|\bcx\b|retention|relocat|withdraw|refund", re.I)

def check_inconsistency(row, source):
    probs = []
    ls, le = parse_date(row.get("Lease Start Date", "")), parse_date(row.get("Lease End Date", ""))
    if ls and le and ls > le:
        probs.append("lease_start_after_lease_end")
    mo = parse_date(row.get("Earliest Date to Move Out", ""))
    if ls and mo and mo < ls:
        probs.append("move_out_before_lease_start")
    sd, dd = parse_date(row.get("Start Date", "")), parse_date(row.get("Due Date", ""))
    if sd and dd and sd > dd:
        probs.append("start_after_due")
    ca, comp = parse_date(row.get("Created At", "")), parse_date(row.get("Completed At", ""))
    if ca and comp and comp < ca:
        probs.append("completed_before_created")
    if source == "movein":
        paid = parse_date(row.get("Date and Time Paid", ""))
        if paid and dd and paid > dd:
            probs.append("paid_after_move_in_due")
        if not dd:
            probs.append("no_due_date_movein")
    if source == "moveout" and not dd and not mo:
        probs.append("no_moveout_date")
    return probs

def main(slug):
    st = load_settings()
    house_config(slug)  # validate slug
    outdir = PROJECT_ROOT / st["houses_dir"] / slug
    report = [f"# S2 pre-flag report — {slug}", f"Run: {now_sydney_iso()}", ""]
    for source in st["sources"]:
        path = outdir / f"{source}_filtered.csv"
        if not path.exists():
            sys.exit(f"ERROR: {path} missing — run s1 first")
        rows, fields = read_csv(path)
        n_tc = n_kw = n_inc = n_hr = 0
        for row in rows:
            blob = " ".join(filter(None, [row.get("Name"), row.get("Notes"),
                                          row.get("Section/Column"),
                                          row.get("Type of Transfer"),
                                          row.get("Type of Transfer Tenant"),
                                          row.get("New/Replacement"),
                                          row.get("Relocation Option"),
                                          row.get("Move Out Reason"), row.get("Form Reason")]))
            tc = bool(TRANSFER_CANCEL_RE.search(blob))
            kws = sorted({k for k in DATE_KEYWORDS if k in blob.lower()})
            probs = check_inconsistency(row, source)
            row["flag_transfer_cancel"] = "yes" if tc else ""
            row["flag_date_keyword"] = "|".join(kws)
            row["flag_inconsistency"] = "|".join(probs)
            hr = tc or kws or probs
            row["human_review"] = "yes" if hr else ""
            n_tc += tc; n_kw += bool(kws); n_inc += bool(probs); n_hr += bool(hr)
        new_cols = ["flag_transfer_cancel", "flag_date_keyword", "flag_inconsistency", "human_review"]
        write_csv(path, rows, [f for f in fields if f not in new_cols] + new_cols)
        report += [f"## {source}",
                   f"- rows: {len(rows)}; transfer/cancel: {n_tc}; date-keyword: {n_kw}; "
                   f"inconsistency: {n_inc}; human_review: {n_hr}", ""]
        append_runlog(f"{now_sydney_iso()} | {slug} | s2-preflag:{source} | script:s2_preflag.py | done | "
                      f"{n_hr}/{len(rows)} flagged for human review (tc:{n_tc} kw:{n_kw} inc:{n_inc})")
    (outdir / "preflag_report.md").write_text("\n".join(report), encoding="utf-8")
    print("\n".join(report))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
