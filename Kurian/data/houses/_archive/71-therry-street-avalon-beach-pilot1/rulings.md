# Rulings — 71 Therry Street, Avalon Beach

Source: P5 Asana comment sweep, ruled_on 2026-07-05. Facts extracted from task comments only.

## Melany Gimenez — Room 4 #170 move-out (task 1212400034885354)
- Form move-out date: Jan 7, 2026. Tenant CONFIRMED "already moved out" 2026-01-07 (comment 1212671573979256). OCR/ICR ran 2026-01-10 (Pilar).
- S3 recorded date = 2026-01-08 (date_source=due_date_conflict_fallback) because earliest 2026-01-15 overlapped next 170 move-in 2026-01-10 by >1d.
- FINDING: Real move-out is on/about 2026-01-07 (tenant-confirmed). The Jan 15 "earliest" that triggered the fallback is NOT supported by comments. S3 fallback date 2026-01-08 is within 1d of true date, so no date-override action taken, but true confirmed date is Jan 7.
- No fee: OCR all clear. Move-out non-compliant (rent due to Jan 14, mandatory shutdown) but no $ charge stated.

## Harrison Kukla — Room 9 #479 (move-out 1212806681561534; move-in 1212536724556765; transfer 1212735854614604)
- COLLISION RESOLVED: transfer task comments confirm Harrison was originally scheduled for Room 4 (#170) but AGREED TO MOVE INTO ROOM 9 (#479) to accommodate Jayden Wilkinson's unauthorized transfer into Room 4/#170.
- FINDING: Harrison's real room is 479 (Room 9), NOT 172 (Room 6). Move-in task 1212536724556765 (form: "Room 9, #479") is mis-placed under room 172 in timeline.csv; belongs to 479. Move-out 1212806681561534 already correctly under 479.
- Move-out: "Already left" 19 Jan 2026; never actually stayed — checked room condition, did not proceed, requested refund (comment 1213040364083554). Break Fee WAIVED (comment 1212873127117771). OCR all clear, no charge.

## Owen Philip Bell — Room 6 #172 move-out (task 1213033868651850)
- FINDING: Owen DID NOT MOVE IN. Father confirmed room empty (comment 1213075214621451); tenant's first email 19 Jan said not moving in. PME move-out date set to 2026-01-19 (NOT the form's Jan 30). OCR all clear, no charge. Full reimbursement demanded (NCAT/Council threat).
- Non-departure: never occupied. Added exclude override.

## Jayden Wilkinson — transfer INTO Room 4 #170 (movein task 1212735854614604)
- Initial payment / transfer effective date: 2026-01-10. Weekly rent $330 first 3 months, then $380 (form's $360 overridden per Ariadna/James approval). Resolves movein payment-date flag (was "Please see comment section").

## Muhammad Ahmed — Room 9 #479 move-out (task 1211173126609348)
- FINDING: Real move-out corrected to 2025-09-04 (comment 1211275633933580 "Move out date updated to 4th September 2025"), NOT form's Sep 5. S3 has 2025-09-05 (due_date), within 1d. New tenant (Jayden) in 21 Sep. Charge: Personal items left behind $200.

## Fees confirmed via comments (no departure/date issue)
- Jorge Martini 168: Break Fee $390 confirmed (75%+ bracket, 1 wk rent). OCR clear.
- Blake Lester 171: Door $250 (confirmed by Maintenance); Room cleaning $150 (waivable per tenant cleanliness reports); Blinds/Curtains $120 (proof unclear). Endorsed to Accounting; NCAT dispute ongoing.
- Juliana 174: Blinds $120 + Mattress protector $85 + Personal items $150 = $355; tenant disputing.
- Ruben 174 (evicted): Personal items $100 + Dirty carpet $60 = $160.
- Guillermo 174: Break fee waived (house maintenance); SD refund prioritized (NCAT threat); OCR clear, no charge.

## Kurian rulings 2026-07-05 (round 3)
- Harrison: room #479 CONFIRMED (per comments). Apply.
- Owen Bell: never-moved-in exclude CONFIRMED.

## Applied 2026-07-05 (round 3)
- Harrison Kukla = #479 (Room 9): excluded the mis-roomed 172 move-in 1212536724556765; his 479 move-out 1212806681561534 carries the Room 9 association (he never actually stayed). NOTE: no reassign-room override action exists — exclude is the in-scope approximation; a proper reassign_room action would let both his events sit under 479. Flagged as residual for owner.
- Owen Bell exclude CONFIRMED (already applied).
