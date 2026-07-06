---
name: cvd-tenancy-timeline
description: Builds the per-room tenancy timeline for one CVD house — pairs move-ins/move-outs, computes vacancy gaps, renders the visual HTML, applies owner rulings via overrides, and prepares the double-check package for Kurian. Use after the review skills when asked to "build the timeline", "make the room timelines for [house]", "pair the tenancies", "apply the rulings", or "prepare [house] for double-check".
---

# CVD Tenancy Timeline (S5 + double-check package)

**Goal:** `tenancies.csv`, `vacancy_gaps.csv`, `timeline.html` for one house, with owner rulings applied, ready for Kurian's visual double-check.

## Order of operations
1. **Apply review outcomes as overrides.** Any task the reviews established as NOT a tenancy event goes into `data/houses/<slug>/overrides.csv`
   (`task_id,action,reason,ruled_by,ruled_on`; action=`exclude`): cancelled sales, retracted evictions, superseded duplicate move-outs, LR lease renewals. If Kurian hasn't ruled yet, use `ruled_by=pipeline-pending-Kurian` and add it to `QUESTIONS-FOR-KURIAN.md`.
2. **Config completeness** (`pipeline/config/houses.json` for this house): every room labeled; beds recorded as beds (letter suffix = bed of same room); `closed_rooms` for dead beds/rooms; `full_window_occupants` for tenants in place the entire window with no in-window tasks (e.g. eviction retracted, real move-out post-window).
3. **Run** (re-run S3 first if overrides changed):
```
python3 pipeline/s3_timeline.py <slug>
python3 pipeline/s5_tenancies_html.py <slug>
python3 pipeline/s4_verify.py <slug>   # must PASS
python3 pipeline/s6_gap_hunt.py <slug> # fuzzy hunt for missed tasks behind every anomaly
```
3b. **Act on gap_hunt.md** (see pipeline/README.md "S6 gap-hunt interpretation"): attach
   real in-window finds via overrides and re-run S3→S5→S4; post-window move-out found =
   ongoing confirmed (note it); pre-window move-in found = record real start in rulings.md
   only. Verify every candidate by Task ID before attaching — fuzzy scores suggest, never decide.
4. **Sanity-read tenancies.csv yourself** — the pairing is fuzzy-name-based; verify:
   - No tenant paired across two different people (start_task and end_task must be the same person — open both links if unsure).
   - `pre_window` rows only for tenants genuinely in place before the window.
   - Two `ongoing` rows in one room = real anomaly → confirm it's flagged (hr=yes) and in the questions file.
   - Negative/overlap gap rows carry `OVERLAP` notes and hr=yes.
5. **Freeze nothing yourself.** Golden datasets (`pipeline/eval/golden/<slug>/`) are frozen ONLY after Kurian approves the house.

## Double-check package for Kurian (chat message)
- Link `timeline.html` + the CSVs.
- List every decision YOU made that needs his confirmation — each with its Asana task link inline in the chat message (links in files are not enough).
- List open anomalies (overlapping tenancies, unresolved rooms) with links.
- After he rules: update `rulings.md` (append, dated) + `overrides.csv`, re-run step 3, then run the eval loop: `python3 pipeline/eval/run_eval.py <slug>`.

## Rules
- One house per run. Scripts only — never hand-edit tenancies.csv or timeline.html.
- RUNLOG.md lines are appended by the scripts; add one for the double-check handoff (`… | double-check-package | … | sent | N confirmations requested`).
