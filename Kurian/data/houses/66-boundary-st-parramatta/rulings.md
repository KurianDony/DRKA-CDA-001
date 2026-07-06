# Rulings — 66 Boundary St Parramatta

Source: P5 Asana comment sweep, ruled_on 2026-07-05, ruled_by asana-comment.

## Final move-out date statements (from Asana comments)

- **Devarsh Lokwani** — Room 5 (#11) — [1210634462854630](https://app.asana.com/0/0/1210634462854630/f):
  Comments confirm final move-out date = **Jul 22, 2025** (tenant confirmed Jul 22, not the form-stated Jul 15). S3 timeline already uses 2025-07-22 (earliest_move_out) — CONSISTENT, no action needed.

- **Bruno Mc Cubbin Villegas** — Room 7 (#13) — [1211518876691623](https://app.asana.com/0/0/1211518876691623/f):
  Actual physical move-out Oct 5, 2025. After escalation (Andres/Ouanne/Kurian), rent obligation **adjusted to Oct 20, 2025** because new tenant (Aadhvik Oberoi) moved in Oct 21. Final billed move-out date = **Oct 20, 2025**.
  FINDING (date discrepancy, no override action taken): S3 timeline row uses move_out 2025-10-05 (due_date_conflict_fallback). Asana-confirmed final/billed date is 2025-10-20. Flagged for Kurian; no date-override applied in this sweep (out of scope — needs explicit ruling on whether to use physical Oct 5 or billed Oct 20).
  Also: Bruno later handled as a **transfer** to Room 8 #1315, 7A Harvey St, Parramatta (granny flat), new contract, Oct 30 2025 — foreign house, not part of 66 Boundary timeline.

- **Thibault Harmand** — Room 5 (#11) — [1212001694753543](https://app.asana.com/0/0/1212001694753543/f):
  Move-out confirmed **Jan 12, 2026** (Ouanne: "Move out confirmed. Photos sent"). S3 timeline uses 2026-01-10 (due_date). Minor 2-day difference (form/lease-end Jan 10 vs confirmed Jan 12); within tolerance, noted only.

- **Orisi Vasukiwai** — Room 1 (#7) — [1212597849366110](https://app.asana.com/0/0/1212597849366110/f):
  EVICTED. Occupant moved out ~week of Jan 5, 2026 (comment Jan 5: "occupant already moved out"). S3 uses 2026-01-03 (due_date). Consistent enough; noted.

## Cross-house transfer — Michael Brian Adriano

- [1211433880033810](https://app.asana.com/0/0/1211433880033810/f) — "Michael Brian Landingin Adriano, Room 7, #958, 4 Gay St, Castle Hill":
  Comments confirm a **Permanent Room Transfer** processed by Antonio. Rent "paid for this week in 66 Boundary"; $840 security deposit transferred from old room ($720 new bond + $120 transfer fee). This confirms Michael Adriano's EXIT from a 66 Boundary room INTO Castle Hill #958, effective move-in Sep 23, 2025.
  FINDING / DISCREPANCY: The task states **Previous/Temporary Room Code = 7** (i.e. Room 1 #7), NOT Room 4 (#10) as posited in the sweep instruction. Comments do NOT explicitly name Room 4/#10 as the origin room. Therefore this sweep does NOT confirm "his exit from Room 4 (#10)". Origin room per this task = code 7. Left for Kurian — prev-room code conflict (7 vs the Room 4/#10 move-in 1211349889089732 attributed to Adriano in the timeline) is unresolved by comments.

## Retractions / superseded

- None found. No flagged task's comments retract or supersede the task itself. No new exclude/promote overrides added.

## Fee resolutions (see fees.csv)

- Devarsh $0 (OCR clear) — resolved.
- Saksham $540 break fee + OCR clear — resolved (not retracted).
- Bruno — cleaning $150 & blinds $120 WAIVED; mattress cover & light bulb reduced to $40 + $40; balance transferred to new room — resolved.
- Thibault $50 cleaning + $270 break fee — resolved (not retracted).
- Ratu — $75 + $50 tenant charges Asana-confirmed; $1360 break-fee field NOT substantiated by any comment — flag kept (review-break-fee).
- Orisi — $150 cleaning confirmed; eviction confirmed; arrears present but NO dollar amount stated — flag kept (arrears-amount-not-stated).
- Tanisha — OCR/ICR pending (scheduled 2026-07-04), no fees determined — flag kept (ocr-pending).

## Kurian rulings 2026-07-05 (round 3)
- Room 6 (#12): occupied continuously by a tenant to this day — full-window occupant
  (no move-in task expected). Kurian believes a move-out task MAY exist in-window; search for
  it (Task-ID verified, #12 + address). If found and in-window, reconcile with "occupied till
  now" before applying — conflict = ask Kurian. Otherwise configure full_window_occupants.
- Adriano-type code tangles: pipeline's handling accepted; resolve with the same slot logic.

## Applied 2026-07-05 (round 3)
- Room 6 (#12): searched raw off-boarding export for in-window #12 move-out (Task-ID verified) — NONE found. Only pre-window (Siddharth Bagdey, Feb 2025) and POST-window (Rohit Shinde, 1216188786381563, Due 2026-07-25). No conflict with "occupied till now" → added #12 to full_window_occupants in houses.json (occupant per post-window task = Rohit Shinde).

## P5 comment sweep 2026-07-06 (batch 00R)

All lines ruled_by=asana-comment, ruled_on=2026-07-06. Comments read via Asana connector (comment_limit=40). No overrides applied; date/room decisions recorded as PROPOSED for Kurian only.

- **Tanisha Saurabh Mathur** — Room 1 (#7) — [1216155071311506](https://app.asana.com/0/0/1216155071311506/f) — RESOLVED:
  OCR/ICR (previously scheduled 2026-07-04) now completed 2026-07-05. OCR = clear, no deductions. ICR notes "A new mattress cover was installed" (CDA-side restock, not posted as a tenant charge). No TENANT CHARGES block; Notes = ON TIME NOTICE / NO BREAK FEE. Fee outcome: **$0 applied, no break fee**. Flag cleared (needs_asana_check=no). ruled_by=asana-comment, ruled_on=2026-07-06.

- **Orisi Vasukiwai** — Room 1 (#7) — [1212597849366110](https://app.asana.com/0/0/1212597849366110/f) — PARTIALLY RESOLVED (flag kept):
  EVICTED. TENANT CHARGES = Room cleaning $150 (OCR reviewed 2026-01-15, endorsed to accounting). Occupant moved out ~week of Jan 5, 2026. Arrears: eviction "with arrears" confirmed but **NO arrears dollar amount is stated in any comment** — figure remains unknown. Cleaning $150 resolved; arrears-amount flag kept (needs_asana_check=yes). ruled_by=asana-comment, ruled_on=2026-07-06.

- **Ratu Epeli Bigitibau** — Room 4 (#10) — [1211321633842981](https://app.asana.com/0/0/1211321633842981/f) — RESOLVED:
  OCR REVIEWED TENANT CHARGES block (2025-09-16) lists ONLY Room cleaning $75 + Mattress cover $50. The **$1360 Break Fee field is NOT real** — no comment states $1360. Task carries a "w/break fee" / non-compliant-notice flag (4 weeks) but no break-fee dollar charge was ever posted; the only substantiated charges are $75+$50. $1360 excluded. Fee outcome: **$125 applied**. Flag cleared (needs_asana_check=no). ruled_by=asana-comment, ruled_on=2026-07-06.

- **Bruno Mc Cubbin Villegas** — Room 7 (#13) — [1211518876691623](https://app.asana.com/0/0/1211518876691623/f) — FEES RESOLVED; DATE = PROPOSED FOR KURIAN (no override applied):
  DATE EVIDENCE (Kurian decision): physical move-out Oct 5, 2025 (form + Chriszsa 2025-10-27). After Andres/Ouanne/Kurian escalation, Ouanne 2025-10-28 directed adjusting rent to **Oct 20, 2025** because new tenant (Aadhvik Oberoi, task 1211678251809806) moved in **Oct 21, 2025**. Billed/final rent date = **Oct 20, 2025** CONFIRMED in comments. S3 timeline currently uses 2025-10-05 (due_date_conflict_fallback). PROPOSED to Kurian: use billed Oct 20 vs physical Oct 5 — **no date-override applied this sweep**.
  FEES: cleaning $150 WAIVED (wear & tear), blinds $120 WAIVED (photo not evident) — Ouanne 2025-11-03. Mattress cover $40 + light bulb $40 (Andres agreement 2025-10-30), remainder transferred to new room (Room 8 #1315, 7A Harvey St, Parramatta, new contract). Fee outcome: **$80 applied, $270 waived, balance transferred**. Flag cleared on fees (needs_asana_check=no). ruled_by=asana-comment, ruled_on=2026-07-06.

- **Ananta Debnath** — Room 2 (#8) — [1211087711997455](https://app.asana.com/0/0/1211087711997455/f) — FEES RESOLVED; DATE = PROPOSED FOR KURIAN (no override applied):
  DEPARTURE EVIDENCE (Kurian): relocation/transfer to Hornsby (transfer task 1211156603238829, confirmed 2025-08-27). Notice non-compliant → "must be paid until Sept 15" (Chriszsa 2025-08-19). Comment 2025-09-04: "new tenant already moved in Sept 4" — so actual vacate on/before **Sept 4, 2025**, rent billed to **Sept 15, 2025**. Form-stated intended move-out was Sept 7. PROPOSED to Kurian: confirmed departure ~Sept 4 (new tenant in) with billing to Sept 15 vs ruling-#7 fallback Due Sep 1 — **no date-override applied this sweep**.
  FEES: OCR REVIEWED TENANT CHARGES (2025-09-04) = Room cleaning $100 + Mattress cover $85 + Mattress $100 = **$285 applied**, none waived. Confirmed (needs_asana_check=no). ruled_by=asana-comment, ruled_on=2026-07-06.

### Retractions / supersessions (P5 2026-07-06)
- None. No flagged task's comments retract or supersede the task. No exclude/promote overrides added; overrides.csv untouched.

## Stage C gap-hunt 2026-07-06 (batch 00R)
ATTACHED (override, ruled_by=gap-hunt): Adriano exit — reassign_room move-in 1211349889089732 -> #7 and promote_move_out exit 1211433879109640 (move-out 2025-09-23, Asana-verified). Slot-method: both his events name Room 1 #7; #10 coding was a room-sold artifact. Result: clean #7 tenancy 2025-09-15..09-23; Room 10 double-ongoing RESOLVED (Nikita sole ongoing).
Post-window move-outs found (ongoing CONFIRMED, not attached): Nikita #10 ([1216088270775873](https://app.asana.com/0/0/1216088270775873/f), 2026-07-24); Priyal #11 ([1216088329877131](https://app.asana.com/0/0/1216088329877131/f), 2026-07-24); Aadhvik #13 ([1215808201843817](https://app.asana.com/0/0/1215808201843817/f), 2026-07-12).
Pre-window move-in start dates (reference only): Devarsh ([1209440985887906](https://app.asana.com/0/0/1209440985887906/f)); Ananta ([1209604946617003](https://app.asana.com/0/0/1209604946617003/f)); Thiviru ([1209720673214563](https://app.asana.com/0/0/1209720673214563/f)); Saksham ([1210093703603273](https://app.asana.com/0/0/1210093703603273/f)); Bruno ([1209923912642954](https://app.asana.com/0/0/1209923912642954/f)).
