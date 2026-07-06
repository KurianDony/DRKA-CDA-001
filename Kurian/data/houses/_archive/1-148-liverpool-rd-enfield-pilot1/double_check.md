# Double-check package — 1/148 Liverpool Rd, Enfield

Prepared 2026-07-05. Files to review: `timeline.html`, `tenancies.csv`, `vacancy_gaps.csv`, `overrides.csv`.
Result: S4 VERIFY = **PASS**. 9 tenancies, 6 vacancy gaps, 2 overrides applied.

## Decisions I made — please confirm

1. **EXCLUDE — Abhinav, cancelled sale (431).** Section "Cancelled Sale - Non Refundable", Sale Status = Cancelled. Not a tenancy event; excluded via overrides. → [1215086767147674](https://app.asana.com/0/0/1215086767147674/f)

2. **EXCLUDE — duplicate move-out, Umashankar #433 transfer.** `[Duplicate]` permanent-transfer move-out; kept the primary transfer record [1213450431910672](https://app.asana.com/0/0/1213450431910672/f) instead. Excluded via overrides. → [1213291114470159](https://app.asana.com/0/0/1213291114470159/f)

3. **KEPT — Diego temp parking in 433 as real occupancy.** Diego's permanent room is #281 (Burwood Heights); 433 is a temporary parking (move-in 2026-04-03) between Umashankar's exit and Subhojit's move-in. Left in the 433 timeline per instructions (real interim occupancy, not excluded). Move-in → [1213815313186065](https://app.asana.com/0/0/1213815313186065/f)

4. **Subhojit 433 treated as a fresh tenancy** despite New/Replacement field reading "Room Transfer" (notes say "New Tenant" — likely a data-entry slip). Move-in 2026-06-15. → [1215086750573147](https://app.asana.com/0/0/1215086750573147/f)

## Open anomalies

A. **Room 433 has THREE ongoing/open tenancies** — Umashankar, Diego, Subhojit — none carry a closing move-out event. The two transfer/return move-outs that would close Umashankar ([1213450431910672](https://app.asana.com/0/0/1213450431910672/f)) and Diego ([1213815366058872](https://app.asana.com/0/0/1213815366058872/f)) are recorded as **is_subtask=yes** (checklist rows nested under parent move-in tasks), so S3 correctly skips them as non-standalone events — leaving no move-out to pair. Flagged `hr=yes`; 2 "TWO ONGOING/OPEN TENANCIES" notes in vacancy_gaps.csv.
   - Umashankar: permanent room TRANSFER to #1475 Strathfield, 2026-03-18 → [1213450431910672](https://app.asana.com/0/0/1213450431910672/f)
   - Diego: TEMPORARY OCR/ICR, returned to permanent room, 2026-04-03 → [1213815366058872](https://app.asana.com/0/0/1213815366058872/f)
   - **Question for Kurian:** should these subtask transfer records be promoted to move-out events (to close Umashankar & Diego in 433), or should the 433 tenancies stay open pending proper off-boarding tasks?

B. **Three pre_window tenancies** (move-in pre-dates audit window, dropped at S1; move-out in-window). Confirmed genuine — flagged `hr=yes`:
   - 431 Yoshiki Isu — transfer/relocation out 2025-11-16 → [1211582567868953](https://app.asana.com/0/0/1211582567868953/f)
   - 432 Hassan Simiyu Juma — move-out 2025-12-25 (late notice, NOT COMPLIANT) → [1212217104104404](https://app.asana.com/0/0/1212217104104404/f)
   - 433 Jinson Jasmany Alava Zambrano — eviction 2025-07-22 → [1210816362712739](https://app.asana.com/0/0/1210816362712739/f)

## Pairing integrity
Every closed tenancy's start_task and end_task belong to the same person (verified). No cross-person mispairing. No negative/overlap gaps.
