# Double-check package — 71 Therry Street, Avalon Beach

Prepared: 2026-07-05 | For: Kurian
Files: `timeline.html`, `tenancies.csv`, `vacancy_gaps.csv`, `overrides.csv`
VERIFY: **PASS** | 25 tenancies · 15 vacancy gaps · 1 override

---

## Decisions I made (need your confirmation)

1. **Override — excluded Jayden Wilkinson's 479 move-out as a transfer-request duplicate.**
   [1212724286262600](https://app.asana.com/0/0/1212724286262600/f) is a Transfer/Relocation request (170->479), NOT a departure. His real departure is the 170 "Already left" task [1212987109464098](https://app.asana.com/0/0/1212987109464098/f). Excluded the transfer-request; kept the 170 move-out. Confirm.

2. **Harrison Kukla — code collision #479 (name) vs 172 (room code).** FLAGGED, not reassigned.
   Move-in [1212536724556765](https://app.asana.com/0/0/1212536724556765/f): name says "Room 9 #479" but Room Code + "room sold" = 172 -> attributed to **172**.
   Move-out [1212806681561534](https://app.asana.com/0/0/1212806681561534/f): "Already left" attributed to **479** (orphan_out).
   Same person appears in two rooms. Which room is his real tenancy? Need your call before pairing.

3. **Kept all three legit transfer chains** (both legs each), excluded only the duplicate above:
   - Mischa 479->168: [1214566169446128](https://app.asana.com/0/0/1214566169446128/f) (in 479) -> [1215743701942249](https://app.asana.com/0/0/1215743701942249/f) (in 168).
   - Jayden 479->170: [1211257085451086](https://app.asana.com/0/0/1211257085451086/f) (in 479) -> [1212735854614604](https://app.asana.com/0/0/1212735854614604/f) (in 170).
   - Zarrar into 171: [1215488996086112](https://app.asana.com/0/0/1215488996086112/f) (permanent transfer from foreign-house #721).

4. **168 / 168A treated as same physical Room 2** (single labelled bed), per config alias. Jorge (168) and Teruya/Jose/Ramiro (168A) all Room 2.

---

## Open anomalies (all hr=yes in tenancies.csv)

- **479 — four open/ongoing rows** (TWO ONGOING flag). Jayden [1211257085451086](https://app.asana.com/0/0/1211257085451086/f) and Mischa [1214566169446128](https://app.asana.com/0/0/1214566169446128/f) show ongoing because their real move-outs were transfers into 170/168; successive real occupant is Ahmer [1216088775783935](https://app.asana.com/0/0/1216088775783935/f). Chain needs your read.
- **479 overlap -120d** (Harrison orphan_out 2026-01-19 vs Jayden move-in 2025-09-21) — artifact of Harrison collision + orphan pairing. OVERLAP flagged.
- **172 — two ongoing** (Harrison [1212536724556765](https://app.asana.com/0/0/1212536724556765/f) + Ghulam re-entry [1213563538695232](https://app.asana.com/0/0/1213563538695232/f)) + **overlap -11d** (Owen move-out 2026-01-30 [1213033868651850](https://app.asana.com/0/0/1213033868651850/f) vs Harrison move-in 2026-01-19). Owen re-books own room after Harrison; sequence needs confirming.
- **174 — overlap -118d + two ongoing.** Juliana orphan_out 2025-10-28 [1211465089994732](https://app.asana.com/0/0/1211465089994732/f) vs Yeray move-in 2025-07-02 [1210672370927302](https://app.asana.com/0/0/1210672370927302/f); Yeray/Juliana are a couple with no Yeray move-out task -> Yeray left open (ongoing). Artifact, not a real double-occupancy.
- **168A — two ongoing.** Jose [1210665277197897](https://app.asana.com/0/0/1210665277197897/f) (couple replacement, no move-out task) left ongoing before Teruya [1212304781816325](https://app.asana.com/0/0/1212304781816325/f). Confirm Jose/Jorge couple vacated.
- **170 — Melany fallback** already flagged: [1212400034885354](https://app.asana.com/0/0/1212400034885354/f) used due_date_conflict_fallback (Earliest 15 Jan overlapped next move-in 10 Jan by >1d).
- **Joshua/Zarrar 171 same-day handover** 2026-06-30 (<=1d ok): Joshua out [1214988906368527](https://app.asana.com/0/0/1214988906368527/f), Zarrar in [1215488996086112](https://app.asana.com/0/0/1215488996086112/f). Joshua still-in-house/relocation notice — confirm actual departure.
