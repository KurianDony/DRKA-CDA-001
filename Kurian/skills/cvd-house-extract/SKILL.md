---
name: cvd-house-extract
description: Runs the CVD house-extraction pipeline (S1 filter → S2 pre-flag → S3 timeline → S4 verify) for one house from the Asana CSV exports. Use when asked to "extract a house", "run the pipeline for [address]", "filter the data for [house]", "do [address]", or to onboard a new house into the CVD dataset. One house per run — never batch.
---

# CVD House Extract (S1–S4)

**Goal:** one house's move-in/move-out/maintenance data filtered, flagged, timelined, verified.
**Unit of work: ONE house.** Never process a second house in the same run.

## Before you start
1. Read `pipeline/README.md` (conventions) and `pipeline/config/settings.json` (windows).
2. Slug format: `<number>-<street-name>-<street-type>-<suburb>`, lowercase, hyphens, suburb ALWAYS included (e.g. `342-cleveland-st-surry-hills`).
3. If the house is not in `pipeline/config/houses.json`, add it:
   - `match_patterns`: house-number-anchored, lowercase (e.g. `"342 cleveland"`). NEVER a bare street name — check the raw CSVs for same-street collisions first and note them in `exclusions_note`.
   - `room_codes`: whatever codes you can find; missing ones are OK — S3 name-parsing surfaces them (342 Cleveland's 1106 and 1110 were found this way).
   - Bed rule: letter suffix or paired code = a BED in the same room (#1110 = Room 6B of Room 6 #1109), NOT an extra room.

## Run (scripts only — never filter by hand)
```
python3 pipeline/s1_filter_house.py <slug>
python3 pipeline/s2_preflag.py <slug>
python3 pipeline/s3_timeline.py <slug>
python3 pipeline/s4_verify.py <slug>
```
Each stage appends to `RUNLOG.md` automatically. If a script errors, fix the config (not the script) or STOP and report `BLOCKED: <reason>`.

## After each stage, check its report
- `filter_report.md`: kept counts sane for the room count? (rule of thumb: top-level ≈ 2–6 tasks/room/year for move-in+out). Huge counts = collision leak; zero = bad pattern.
- `rooms_report.md`: unknown room codes appearing? Add to houses.json, re-run S1–S3. Unresolved maintenance rows are normal (house-level).
- `VERIFY.md` must end **PASS**. On FAIL: read the failing check, fix cause, re-run. Two consecutive FAILs → report `BLOCKED`.

## Hard rules
- Audit window is ENFORCED (move-in/out ±7d, maintenance ±31d). Never widen it. Pre-window occupants are handled at the tenancy stage, not by chasing old tasks.
- READ-ONLY everywhere except `data/houses/<slug>/` and RUNLOG.md.
- Every task referenced in anything human-facing gets its link: `https://app.asana.com/0/0/<TaskID>/f`.
- Anomalies → one line each in `QUESTIONS-FOR-KURIAN.md` (date | house | question | why it matters | assumption). Never resolve ambiguity silently.

## Done when
`VERIFY.md` = PASS, reports reviewed, RUNLOG lines present, questions logged. Then hand off to `cvd-review-movein` + `cvd-review-moveout` (task reviews) and `cvd-tenancy-timeline` (S5).
