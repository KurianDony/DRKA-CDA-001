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
