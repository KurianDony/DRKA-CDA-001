#!/usr/bin/env python3
"""Eval loop — re-runs the deterministic pipeline for a house and diffs the outputs
against the Kurian-approved golden dataset, plus unit tests for the fragile parsers.

Golden = pipeline/eval/golden/<slug>/{tenancies_golden.csv, vacancy_gaps_golden.csv}
(frozen 2026-07-05 after Kurian approved 342 Cleveland's dates).

Checks:
  U1  unit tests: dates_in_text (name-date parsing incl. year inference)
  U2  unit tests: name_sim (fuzzy same-person matching, incl. must-NOT-match cases)
  E1  S1→S3→S5 rerun completes; S4 verify = PASS
  E2  tenancies.csv == golden (room, tenant first token, start, end, kinds)
  E3  vacancy_gaps.csv == golden (room, from, to, days)
Any diff = FAIL with a line-level report. Report → pipeline/eval/reports/, RUNLOG line.

Usage: python3 pipeline/eval/run_eval.py <house-slug>
"""
import subprocess, sys
from datetime import date
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "lib"))
from common import PROJECT_ROOT, load_settings, read_csv, now_sydney_iso, append_runlog
from common import dates_in_text, name_sim  # noqa

def unit_tests():
    fails = []
    ref = date(2025, 12, 8)
    cases = [
        ("NT Dec 10 - Room 2", ref, date(2025, 12, 10)),
        ("16 Sept 2024 handover", ref, date(2024, 9, 16)),
        ("March 31, 2025", ref, date(2025, 3, 31)),
        ("moved out Jul 6", date(2024, 7, 3), date(2024, 7, 6)),
        ("NT Jan 2", date(2025, 12, 20), date(2026, 1, 2)),  # year rollover inference
    ]
    for text, r, want in cases:
        got = dates_in_text(text, r)
        if want not in got:
            fails.append(f"U1 dates_in_text({text!r}) → {got}, want {want}")
    if dates_in_text("Room 4, #1107, 342 Cleveland St", ref):
        fails.append("U1 false positive: room/address text produced a date")
    for a, b, want in [
        ("Danny Walker", "Daniel Lewis Walked", True),
        ("Wing Ho Wong", "Wing Ho Wong", True),
        ("Bhomik Walia", "Bhomik & Yash", True),
        ("Blake Withers", "Arturo Sandoval Montiel", False),
        ("Sebastian Jhair Castro", "Seanna Connell", False),
        ("", "Anyone", False),
    ]:
        if name_sim(a, b) != want:
            fails.append(f"U2 name_sim({a!r},{b!r}) != {want}")
    return fails

def diff_csv(got_path, want_path, keys):
    got, _ = read_csv(got_path)
    want, _ = read_csv(want_path)
    norm = lambda rows: {tuple((r.get(k) or "").strip().lower().split(" ")[0] if k == "tenant"
                               else (r.get(k) or "").strip() for k in keys) for r in rows}
    g, w = norm(got), norm(want)
    out = [f"  MISSING vs golden: {sorted(w - g)}"] if w - g else []
    out += [f"  EXTRA vs golden: {sorted(g - w)}"] if g - w else []
    return out

def main(slug):
    st = load_settings()
    hdir = PROJECT_ROOT / st["houses_dir"] / slug
    gdir = Path(__file__).resolve().parent / "golden" / slug
    lines, fail = [f"# Eval report — {slug} — {now_sydney_iso()}", ""], False

    f = unit_tests()
    lines.append(f"U1/U2 parser unit tests: {'FAIL' if f else 'PASS'}")
    lines += [f"  {x}" for x in f]
    fail |= bool(f)

    for step in ["s1_filter_house.py", "s2_preflag.py", "s3_timeline.py", "s5_tenancies_html.py", "s4_verify.py"]:
        r = subprocess.run([sys.executable, str(PROJECT_ROOT / "pipeline" / step), slug],
                           capture_output=True, text=True)
        if r.returncode != 0:
            lines.append(f"E1 {step}: FAIL (exit {r.returncode})\n  {r.stdout[-300:]}{r.stderr[-300:]}")
            fail = True
        else:
            lines.append(f"E1 {step}: PASS")

    if not gdir.exists():
        lines.append(f"E2/E3: NO GOLDEN for {slug} — freeze one after Kurian approves the house")
    else:
        d = diff_csv(hdir / "tenancies.csv", gdir / "tenancies_golden.csv",
                     ["room_code", "tenant", "start", "end", "start_kind", "end_kind"])
        lines.append(f"E2 tenancies vs golden: {'FAIL' if d else 'PASS'}"); lines += d; fail |= bool(d)
        d = diff_csv(hdir / "vacancy_gaps.csv", gdir / "vacancy_gaps_golden.csv",
                     ["room_code", "vacant_from", "vacant_to", "gap_days"])
        lines.append(f"E3 vacancy gaps vs golden: {'FAIL' if d else 'PASS'}"); lines += d; fail |= bool(d)

    verdict = "FAIL" if fail else "PASS"
    lines.insert(1, f"**Verdict: {verdict}**")
    rp = Path(__file__).resolve().parent / "reports" / f"{date.today()}_{slug}.md"
    rp.write_text("\n".join(lines), encoding="utf-8")
    append_runlog(f"{now_sydney_iso()} | {slug} | eval-loop | script:eval/run_eval.py | {verdict} | report: {rp.relative_to(PROJECT_ROOT)}")
    print("\n".join(lines))
    sys.exit(1 if fail else 0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
