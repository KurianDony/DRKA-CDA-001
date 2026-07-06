# 66 Boundary St, Parramatta — Tenancy timeline double-check
Prepared: 2026-07-05 (pipeline sub-agent) · VERIFY: PASS · 14 tenancies · 8 vacancy gaps · 4 override-exclusions

Artifacts: `timeline.html`, `tenancies.csv`, `vacancy_gaps.csv`, `overrides.csv` (all in `data/houses/66-boundary-st-parramatta/`).

## Decisions I made — please confirm

### A. Override-exclusions applied (ruled_by=pipeline-pending-Kurian)
1. [1214653049426975](https://app.asana.com/0/0/1214653049426975) — "LR" lease-renewal stub, James Gong, Room 2 (#8), empty (no date/payment/room code). Excluded — not a move-in.
2. [1213275313176550](https://app.asana.com/0/0/1213275313176550) — second "LR" lease-renewal stub, James Gong, Room 2 (#8), empty. Excluded — not a move-in.
3. [1211529190796475](https://app.asana.com/0/0/1211529190796475) — Cancelled Sale (Non-Refundable), Senthuran, Room 3 (#9). Excluded — not a tenancy.
4. [1211391731924312](https://app.asana.com/0/0/1211391731924312) — Cancelled Sale (Non-Refundable), Iosefo & Elenoa, Room 5 (#11). Excluded — not a tenancy.

### B. Cross-house transfer — NOT force-excluded, left unattached
- [1211433880033810](https://app.asana.com/0/0/1211433880033810) — Name/address = "4 Gay St Castle Hill #958". Permanent Transfer OUT of 66 Boundary INTO Castle Hill, with "rent paid in 66 Boundary". Books to a non-66 room (#958), so it does NOT attach to any 66 room and sits in UNRESOLVED — it never appears in a 66 room timeline. I did NOT put it in overrides.csv (it is a real event, just belongs to another house). **Confirm:** is this the transfer OUT of Michael Adriano from Room 4 (#10)? If so his Room 4 tenancy should END on transfer, not stay "ongoing" (see anomaly 3).

## Open anomalies — need your eyes

### 1. Room 6 (#12) — zero window events
Room 6 is configured (label present, code 12) but had NO move-in/move-out/maintenance in the audit window. Decision item: genuinely vacant/closed all window, or missing data? Not a config error. **Confirm** whether to mark `closed_rooms`.

### 2. Rooms 1/2/3 (#7/#8/#9) move-OUTS stranded in UNRESOLVED — root cause found
The room-code resolver regex (`#\s?(\d{2,4}...)`, `pipeline/lib/common.py`) requires 2-4 digits, so single-digit `#7`, `#8`, `#9` in the Name text are NOT matched. Move-INS for these rooms resolved via the Room Code *column* (which holds "7"/"8"/"9"); the corresponding move-OUTS have an EMPTY Room Code column and fall through to Name text, where `#7/#8/#9` are rejected. Result: 5 real move-outs sit in UNRESOLVED and their rooms falsely show open tenancies:
  - [1212597849366110](https://app.asana.com/0/0/1212597849366110) Orisi Vasukiwai, Room 1 (#7), EVICTED, move-out 2026-01-03 — should close Orisi's Room 7 tenancy.
  - [1216155071311506](https://app.asana.com/0/0/1216155071311506) Tanisha Mathur, Room 1 (#7), move-out 2026-06-20 — should close Tanisha's Room 7 tenancy.
  - [1211145372664631](https://app.asana.com/0/0/1211145372664631) Saksham Saksham, Room 1 (#7), move-out 2025-09-08 (pre the two above).
  - [1211087711997455](https://app.asana.com/0/0/1211087711997455) Ananta Debnath, Room 2 (#8), move-out 2025-09-16 (relocation → Hornsby).
  - [1211003906429095](https://app.asana.com/0/0/1211003906429095) Thiviru Gunawardena, Room 3 (#9), move-out 2025-09-22.
**This is a pipeline-lib limitation, not a data error. I am read-only on the lib — flagging for a fix (allow single-digit `#N` when N is a valid house code) or a per-task room-code override.** Until fixed, Room 7/8/9 timelines are incomplete.

### 3. Room 4 (#10) — two ongoing/open tenancies (flagged hr=yes in vacancy_gaps.csv)
  - [1211349889089732](https://app.asana.com/0/0/1211349889089732) Michael Brian Adriano, move-in 2025-09-15 — shows as "ongoing", but per the move-in review his name says "Room 1 #7" while room-code sold = 10, and he later transferred OUT to Castle Hill via task [1211433880033810](https://app.asana.com/0/0/1211433880033810) (anomaly B). So his Room 4 tenancy should END at that transfer, not overlap Emilien.
  - [1211616103121375](https://app.asana.com/0/0/1211616103121375) Emilien Crolas, move-in 2025-10-18 → move-out 2026-01-10 — the true Room 4 occupant over that span.
  **The Adriano #7-vs-#10 tangle + missing transfer-out is why Room 4 reads two-ongoing.** Confirm Adriano's exit date so his row closes.

### 4. Room 1 (#7) — two ongoing (flagged hr=yes)
Downstream of anomaly 2: Orisi (from 2025-10-03) and Tanisha (from 2026-02-04) both read "ongoing" only because their move-outs are stranded in UNRESOLVED. Once anomaly 2 is fixed these become clean sequential tenancies (Orisi evicted 2026-01-03 → gap → Tanisha in 2026-02-04, out 2026-06-20).

## Notes
- All 14 tenancy rows carry hr=yes (fuzzy-name pairing pending your visual check).
- pre_window rows are genuine: Devarsh Lokwani (Room 5, out 2025-07-22, no in-window move-in) and Bruno Mc Cubbin Villegas (Room 7/#13, out 2025-10-05, no in-window move-in).
- No negative/overlap gaps in vacancy_gaps.csv other than the two two-ongoing flags above.
