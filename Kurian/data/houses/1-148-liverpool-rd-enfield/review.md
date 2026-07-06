# Task review — 1/148 Liverpool Rd, Enfield (1-148-liverpool-rd-enfield)
Assembled: 2026-07-06T11:00+10:00
One line per top-level task. **HUMAN REVIEW** = date-altering or house-attribution issue needing Kurian's eyes. Subtasks excluded (tagged is_subtask in the CSVs).

# Move-in review — 1/148 Liverpool Rd, Enfield

## Move-in tasks (top-level: 7 reviewed, 1 flagged)

- [1211814391913995](https://app.asana.com/0/0/1211814391913995/f) 433 | Umashankar | New tenant, direct move-in; due 2025-11-09, paid 2025-11-02 (≤ move-in), room 433 matches. Clean.
- [1212748792334048](https://app.asana.com/0/0/1212748792334048/f) 431 | Sharayu | New tenant, direct move-in; due 2026-02-06, paid 2026-01-12, room 431 matches. Clean.
- [1212735719553897](https://app.asana.com/0/0/1212735719553897/f) 432 | Jai | New tenant, direct move-in; due 2026-02-06, notes say "Feb 5" — rule-resolved (Due Date governs); paid 2026-01-12, room 432 matches. Clean.
- [1213815313186065](https://app.asana.com/0/0/1213815313186065/f) 433(temp) | Diego | Permanent room sold is #281, 33 George St Burwood Heights — 433 is only his TEMPORARY room (Mar 30). Payment=0 confirmed legitimate per form/comment (temp room, $100 discount). Not a permanent tenancy here.  **HUMAN REVIEW: permanent move-in belongs to another house (#281); 433 is temp-room parking, exclude from 433 permanent timeline (HR retained per Kurian P5 ruling)**
- [1215086750451275](https://app.asana.com/0/0/1215086750451275/f) 432 | Raghav | New tenant, direct move-in; due 2026-06-15, paid 2026-05-24, room 432 matches. Clean.
- [1215086750573147](https://app.asana.com/0/0/1215086750573147/f) 433 | Subhojit | Direct move-in, room 433, due 2026-06-15, paid 2026-05-24. New/Replacement column = "Room Transfer" but notes = "New Tenant" + direct move-in; not date-altering, timeline treats as fresh tenancy (start 2026-06-15). Data-entry slip, note only.
- [1215086767147674](https://app.asana.com/0/0/1215086767147674/f) 431 | Abhinav | Section = Cancelled Sale - Non Refundable, Sale Status = Cancelled, Payment = Pending. Settled: excluded via overrides.csv (ruled 2026-07-05) — not a tenancy. Note only.

### Note — Room 433 extra move-in
Room 433 shows three move-in tasks: Umashankar (2025-11-09) → Diego temp (2026-04-03) → Subhojit (2026-06-15). The Diego entry is temporary parking in 433 while his permanent room #281 (Burwood Heights) was prepared, sitting between Umashankar's exit (move-out 2026-03-18) and Subhojit's move-in — an interim occupancy, not a fourth permanent tenancy. Flagged above.

# Move-out review — 1/148 Liverpool Rd, Enfield

Date rule: move-out = LATEST of {Due Date, Earliest Date to Move Out, name date}, unless it overlaps next move-in by >1 day (ruling #7). v2 NOT-a-flag discipline applied: items settled by overrides.csv / rulings.md are notes, not HUMAN REVIEW. All fees resolved in P5 comment sweep (needs_asana_check=no).

- [1213954074830792](https://app.asana.com/0/0/1213954074830792/f) Room 2 #432 | Jai Padmakar Telang | Move-out 2026-05-05 (due=lease end=form date, all agree); on-time notice, no break fee; OCR all clear, $0. Lease end = move-out (0 months past term). Next move-in Raghav 2026-06-15, no conflict. [Duplicate] subtask 1214048720100752 is evidence only.
- [1214129032497582](https://app.asana.com/0/0/1214129032497582/f) Room 1 #431 | Sharayu Sonekar | Move-out 2026-05-05 (due date; form Apr 5 was a typo, comment confirms May 5 — rule-#7 later date, MATCH); 4-week notice waived to 2 weeks (approved); fees $100 (dirty beddings $30 + main door key $70). 0 months past term.
- [1213450431910672](https://app.asana.com/0/0/1213450431910672/f) Room 3 #433 | Umashankar Sivagnanam | Permanent room TRANSFER out to #1475 Strathfield, move-out 2026-03-18; OCR key charge $209.80; old-room deposit refunded. NOTE: promote_move_out in overrides.csv (settled) — treated as departure from #433; duplicate 1213291114470159 stays excluded. 0 months past term.
- [1213815366058872](https://app.asana.com/0/0/1213815366058872/f) Room 3 #433 | Diego Alejandro Lasso Zapata | TEMPORARY OCR/ICR out 2026-04-03, returned to permanent room (#281 Burwood Hts); OCR all clear, $0. NOTE: promote_move_out in overrides.csv (settled) — closes the temp #433 stay. Subtask 1213893724824026 is evidence only.
- [1213291114470159](https://app.asana.com/0/0/1213291114470159/f) Room 3 #433 | Umashankar Sivagnanam | [Duplicate] permanent transfer 2026-03-18; no fees on this record. NOTE: exclude in overrides.csv (settled) — duplicate of 1213450431910672; not double-counted.
- [1212217104104404](https://app.asana.com/0/0/1212217104104404/f) Room 2 #432 | Hassan Simiyu Juma | Move-out 2025-12-24 (paid-to/billed, later-date rule) via set_move_out_date override; OCR all clear, $0. NOTE: physical vacate 2025-11-30 recorded as note, not the event date (Kurian r3, settled). Late-notice non-compliance noted; lease end Sep 1 2025 before move-out is normal (month-to-month), 0 months past term.
- [1211582567868953](https://app.asana.com/0/0/1211582567868953/f) Room 1 #431 | Yoshiki Isu | Transfer to different house, move-out 2025-11-16; retention successful/relocated; $150 transfer fee refunded; OCR all clear, $0. NOTE: relocation-out closes the #431 tenancy; treated as departure.
- [1210816362712739](https://app.asana.com/0/0/1210816362712739/f) Room 3 #433 | Jinson Jasmany Alava Zambrano | EVICTION (non-payment) 2025-07-22 (name+form date agree); fees $850 (items $200 + cleaning $100 + table $120 + curtain $60 + bed disposal $370). Next move-in Umashankar 2025-11-09, no conflict.

## Notes (v2 re-review, 2026-07-06)
- v1 flagged 5/8 (62.5%). Every prior flag is now resolved by overrides.csv (exclude/promote/set_move_out_date) or rulings.md (P5 comment sweep + Kurian r3). Under NOT-a-flag discipline these are notes, not HUMAN REVIEW. Room transfers/relocations here are settled events, not open questions.
- 0/8 HUMAN REVIEW; 0 need Asana comment check (all resolved in P5 sweep).
