# Task review — 1/148 Liverpool Rd, Enfield (1-148-liverpool-rd-enfield)
Assembled: 2026-07-05T18:52+10:00
One line per top-level task. **HUMAN REVIEW** = date-altering or house-attribution issue needing Kurian's eyes. Subtasks excluded (tagged is_subtask in the CSVs).

# Move-in review — 1/148 Liverpool Rd, Enfield

## Move-in tasks (top-level: 7 reviewed, 4 flagged)

- [1211814391913995](https://app.asana.com/0/0/1211814391913995/f) 433 | Umashankar | New tenant, direct move-in; due 2025-11-09, paid 2025-11-02 (≤ move-in), room 433 matches. Clean.
- [1212748792334048](https://app.asana.com/0/0/1212748792334048/f) 431 | Sharayu | New tenant, direct move-in; due 2026-02-06, paid 2026-01-12, room 431 matches. Clean.
- [1212735719553897](https://app.asana.com/0/0/1212735719553897/f) 432 | Jai | New tenant, direct move-in; due 2026-02-06, paid 2026-01-12, room 432 matches. Clean.
- [1213815313186065](https://app.asana.com/0/0/1213815313186065/f) 433(temp) | Diego | Permanent room sold is #281, 33 George St Burwood Heights — 433 is only his TEMPORARY room (Mar 30). Not a permanent tenancy here.  **HUMAN REVIEW: permanent move-in belongs to another house (#281); 433 is temp-room parking, exclude from 433 permanent timeline; payment=0 needs Asana comment check**
- [1215086750451275](https://app.asana.com/0/0/1215086750451275/f) 432 | Raghav | New tenant, direct move-in; due 2026-06-15, paid 2026-05-24, room 432 matches. Clean.
- [1215086750573147](https://app.asana.com/0/0/1215086750573147/f) 433 | Subhojit | Direct move-in, room 433, due 2026-06-15, paid 2026-05-24. Notes say New Tenant but New/Replacement column = "Room Transfer".  **HUMAN REVIEW: New/Replacement field ("Room Transfer") contradicts notes ("New Tenant") — likely data-entry slip; confirm fresh tenancy, not a transfer**
- [1215086767147674](https://app.asana.com/0/0/1215086767147674/f) 431 | Abhinav | Section = Cancelled Sale - Non Refundable, Sale Status = Cancelled; due/paid 2026-06-15/05-24.  **HUMAN REVIEW: cancelled sale — NOT a tenancy, exclude via overrides at timeline stage**

### Note — Room 433 extra move-in
Room 433 shows three move-in tasks: Umashankar (2025-11-09) → Diego temp (2026-04-03) → Subhojit (2026-06-15). The Diego entry is a temporary parking in 433 while his permanent room #281 (Burwood Heights) was prepared, sitting between Umashankar's exit (move-out 2026-03-18) and Subhojit's move-in — consistent with an interim occupancy, not a fourth permanent tenancy. Flagged above.

# Move-out review — 1/148 Liverpool Rd, Enfield

Date rule: move-out = LATEST of {Due Date, Earliest Date to Move Out, name date}, unless it overlaps next move-in by >1 day (ruling #7). No `rulings.md` for this house.

- [1213954074830792](https://app.asana.com/0/0/1213954074830792/f) Room 2 #432 | Jai Padmakar Telang | Move-out 2026-05-05 (due=lease end=form date); on-time notice, no break fee; OCR all clear; next move-in Raghav 2026-06-15 no conflict. Has [Duplicate] subtask 1214048720100752.
- [1214129032497582](https://app.asana.com/0/0/1214129032497582/f) Room 1 #431 | Sharayu Sonekar | Move-out 2026-05-05 (due date; form said Apr 5 — later date wins); 4-week notice waived to 2 weeks; fees $100 (dirty beddings $30 + key $70).
- [1213450431910672](https://app.asana.com/0/0/1213450431910672/f) Room 3 #433 | Umashankar Sivagnanam | Permanent room TRANSFER to #1475 Strathfield 2026-03-18; OCR key charge $209.80; old-room deposit to be refunded.  **HUMAN REVIEW: room transfer not a true departure; duplicate pair with 1213291114470159**
- [1213815366058872](https://app.asana.com/0/0/1213815366058872/f) Room 3 #433 | Diego Alejandro Lasso Zapata | TEMPORARY OCR/ICR 2026-04-03, returned to permanent/original room; OCR all clear.  **HUMAN REVIEW: temporary transfer, not a departure; has subtask 1213893724824026**
- [1213291114470159](https://app.asana.com/0/0/1213291114470159/f) Room 3 #433 | Umashankar Sivagnanam | [Duplicate] permanent transfer 2026-03-18; no fees on this record.  **HUMAN REVIEW: duplicate of 1213450431910672; transfer not a departure**
- [1212217104104404](https://app.asana.com/0/0/1212217104104404/f) Room 2 #432 | Hassan Simiyu Juma | Move-out 2025-12-25 (earliest-move-out; late notice, rent payable to 24 Dec); OCR all clear; lease end Sep 1 2025 < move-out (expected, stayed on).  **HUMAN REVIEW: NOT COMPLIANT flag — late notice, confirm rent-until date in comments**
- [1211582567868953](https://app.asana.com/0/0/1211582567868953/f) Room 1 #431 | Yoshiki Isu | Transfer to different house 2025-11-16; RELOCATED; $150 transfer fee refunded; OCR all clear.  **HUMAN REVIEW: relocation/transfer, not a true departure**
- [1210816362712739](https://app.asana.com/0/0/1210816362712739/f) Room 3 #433 | Jinson Jasmany Alava Zambrano | EVICTION (non-payment) 2025-07-22 (name+form date); fees $850 (items $200, cleaning $100, table $120, curtain $60, bed disposal $370); next move-in Umashankar 2025-11-09 no conflict.

## Round-3 note (Kurian 2026-07-05)
- [1212217104104404](https://app.asana.com/0/0/1212217104104404/f) Room 2 #432 | Hassan Simiyu Juma | Event move-out date set to **2025-12-24** (paid-to/billed, later-date rule) via set_move_out_date override. **Physical vacate 2025-11-30** is recorded as a note only, NOT the event date.
