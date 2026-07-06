# Double-check package — 287 Cleveland St, Redfern

Prepared 2026-07-05 (pipeline-pending-Kurian). VERIFY = PASS.
Deliverables: `tenancies.csv` (44), `vacancy_gaps.csv` (23), `timeline.html`.

Room/bed model in play (from A0 C3 assumption): Room 1 = beds 035A+035B; Room 3 = 037A+037B; Room 4 = 38+038B; Room 5 = 39+039A/039B; Room 6 = 40+40A+40B; Room 7 = 41+41A+41B. Because pairing is per-room-code and fuzzy-name-based, departures logged under a paired bed code leave the other bed's tenancy showing as `ongoing`. Most flags below stem from that.

## A. Decisions I made needing your confirmation

1. **Overrides applied — 7 exclusions.** All entered as `pipeline-pending-Kurian`. Please confirm each is correctly NOT a tenancy:
   - Cancelled Sale — Charlie #40A: https://app.asana.com/0/0/1212431175562746/f
   - Cancelled Sale — Julian #39: https://app.asana.com/0/0/1211582986718236/f
   - Cancelled Sale + transfer — Bryan #40A: https://app.asana.com/0/0/1212843836646006/f
   - Cancelled Sale — Andres #035A: https://app.asana.com/0/0/1210779236783683/f
   - Cancelled Sale, temp-only at 287 — Josue #035A (perm room #165 Surry Hills): https://app.asana.com/0/0/1211792711161342/f
   - LR lease-renewal stub — Inga #38 (no payment/tenant fields): https://app.asana.com/0/0/1212897058415733/f
   - Retracted/superseded duplicate move-out — Haroun Zouari #40B Nov 19 (kept the Dec 9 one https://app.asana.com/0/0/1212152556949219/f as real): https://app.asana.com/0/0/1211917167195053/f

2. **Kept Haroun's Dec 9 move-out as the real departure** (excluded the no-data Nov 19). Confirm Dec 9 is correct: https://app.asana.com/0/0/1212152556949219/f

3. **Did NOT exclude any transfers.** Kept as genuine tenancies (reviews did not say they aren't tenancies):
   - Dimas PERM transfer into 037B (prev-room code #28 vs 037A history unresolved): https://app.asana.com/0/0/1213976823034682/f
   - Jin transfer into 037A out of temp 035B: https://app.asana.com/0/0/1213589118610292/f
   - Chanwoo temp-chain Strathfield → 037A, 287 move-in 25 Nov: https://app.asana.com/0/0/1211804434426920/f
   - Matias #035B is temp-only at 287 (perm room #1431 North Ryde) — I LEFT IT IN as a 287 tenancy row (shows ongoing in 035B). Confirm whether it should be excluded like Josue: https://app.asana.com/0/0/1213752002475027/f
   - Jin Hendrix #035B move-in (later transfers to 037A) kept: https://app.asana.com/0/0/1210957509085672/f

## B. Open anomalies (flagged hr=yes)

**Multiple ONGOING/open tenancies in one bed-code (pairing artifact — likely missing/cross-code move-outs):**
- **035A** — 4 open rows: Tanguy (https://app.asana.com/0/0/1210720352131274/f), Chung (https://app.asana.com/0/0/1210769346658948/f), Roxx (https://app.asana.com/0/0/1212430575073508/f), Joji (https://app.asana.com/0/0/1213574534161457/f). Room 1 holds 2 beds only; 4 open is impossible — earlier occupants' departures likely logged under 035B or unmatched. Needs your read.
- **035B** — 2 open: Jin Hendrix Vergara (https://app.asana.com/0/0/1210957509085672/f) then Matias (https://app.asana.com/0/0/1213752002475027/f). Jin transferred out to 037A (037A row: https://app.asana.com/0/0/1213589118610292/f) so his 035B row should close on that transfer date — confirm.
- **41** — 3 open: Zaid (https://app.asana.com/0/0/1211763842518318/f), Haroun (https://app.asana.com/0/0/1211763827512289/f), Udaya (https://app.asana.com/0/0/1215080592719549/f). 41A/41B = 2 beds; both Zaid+Haroun open plus Udaya = 3. Zaid later moves out of #40A (https://app.asana.com/0/0/1212289025013487/f) and Haroun out of #40B (https://app.asana.com/0/0/1212152556949219/f) — their 41 move-ins vs 40A/40B move-outs are the same people under different bed codes. Confirm bed reconciliation.
- **36** — 2 open: Leonardo Gutierrez (https://app.asana.com/0/0/1211323580275313/f) then Javier (https://app.asana.com/0/0/1211956952026118/f). Room 2 single room — one should have a move-out. Confirm.
- **38** — 2 open: Syed (https://app.asana.com/0/0/1211321764289846/f) then Inga→Emily chain. Syed #38 later moves out under #038B (https://app.asana.com/0/0/1212401032138521/f) — same person, cross-code; his 38 row should close Jan 9. Confirm.

**Negative-gap OVERLAP rows (hr=yes) — driven by MASATO OKAZAKI spanning two room codes of Room 6/7:**
- Masato has an ONGOING in #40 (move-in 28 Jun 2025, https://app.asana.com/0/0/1210608137094421/f) AND an orphan move-out in #41 (17 Nov 2025, https://app.asana.com/0/0/1211953230993252/f). Same person, split across bed codes → produces the -111 (room 40) and -137 (room 41) overlaps. Needs your call on which code his real tenancy sits under.
- **035A** -111 overlap Francisco→Tanguy: Francisco appears in both 035A (orphan_out) and 035B (ongoing, https://app.asana.com/0/0/1210885582624750/f) — cross-bed same person. Confirm.

**Date-discrepancy move-outs already resolved by ruling #7 (6 conflicts) — confirm the chosen dates:**
- Teigan #39 → Feb 8 applied (overlaps Denis Feb 10): https://app.asana.com/0/0/1212806384421277/f
- Masato #41 → Nov 17 applied (Earliest Dec 3 overlaps Callum Nov 29): https://app.asana.com/0/0/1211953230993252/f
- Yu Shinnishi #037A → Sep 23 applied (Earliest Oct 8 overlaps Edward Sep 26): https://app.asana.com/0/0/1211312533102042/f
- Santiago #037B → Apr 19 (Due Apr 2 vs Earliest Apr 19): https://app.asana.com/0/0/1213754732145800/f
- Chanwoo #037A → Mar 3 vs Earliest Mar 17: https://app.asana.com/0/0/1213307336945589/f
- Zaid #40A eviction → Jan 15 vs Due Dec 12: https://app.asana.com/0/0/1212289025013487/f

**Other:**
- Lisa Wilson #36: move-out https://app.asana.com/0/0/1211310066686372/f is paired with OFFER RELOC task (no date, dropped) https://app.asana.com/0/0/1210737767129253/f — 1 event with no parseable date (WARN in VERIFY). Confirm the relocation task is correctly not a departure.
- Pre-window move-out-only rows (genuine pre-window tenants, verified): Yu Shinnishi 037A, Kevin 037B, Syed 038B, Lisa 36, Leonardo Gomez 36, Federico 38, Zaid 40A, Haroun 40B.

---

## ROUND 2 — Bed-pairing reconciliation (2026-07-05, orchestrator, manual pass)

Six phantom `ongoing` rows are one tenant split across two room codes (S5 pairs per-code, so the move-in stays open when the move-out sits under the sibling code). Marked `bed-pairing artifact` in review_moveout.md. NOT hand-edited in tenancies.csv — need your confirmation to close each (and, for the 40/41 set, which physical room the tenant belongs to):

Clean same-room bed pairs — confirm the tenancy closes on the sibling move-out date:
1. Francisco Hernandez — 035B move-in [1210885582624750](https://app.asana.com/0/0/1210885582624750/f) closes on 035A move-out 2025-10-25 [1211422430091752](https://app.asana.com/0/0/1211422430091752/f).
2. Syed Ayaan Hussain — 38 move-in [1211321764289846](https://app.asana.com/0/0/1211321764289846/f) closes on 038B move-out 2026-01-09 [1212401032138521](https://app.asana.com/0/0/1212401032138521/f).

40↔41 code-boundary pairs — same person under a Room 6 code AND a Room 7 code; confirm closure AND which room is real:
3. Masato Okazaki — #40 move-in [1210608137094421](https://app.asana.com/0/0/1210608137094421/f) ↔ #41 move-out 2025-11-17 [1211953230993252](https://app.asana.com/0/0/1211953230993252/f).
4. Giordano Perinelli — #41 move-in [1211557559194849](https://app.asana.com/0/0/1211557559194849/f) ↔ #40 move-out 2025-10-17 [1211738290119973](https://app.asana.com/0/0/1211738290119973/f).
5. Zaid Hamsassia — #41 move-in [1211763842518318](https://app.asana.com/0/0/1211763842518318/f) ↔ #40A move-out 2026-01-15 [1212289025013487](https://app.asana.com/0/0/1212289025013487/f).
6. Haroun Zouari — #41 move-in [1211763827512289](https://app.asana.com/0/0/1211763827512289/f) ↔ #40B move-out 2025-12-09 [1212152556949219](https://app.asana.com/0/0/1212152556949219/f).

**Pattern for your call:** four tenants (Masato, Giordano, Zaid, Haroun) each carry one #40-family code and one #41 code — strongly suggests #40 and #41 were used interchangeably for the same physical beds (Room 6/Room 7 adjacency). If so, the registry room split for 40/41 may need revisiting.

Separately (not bed-pairing): Jin Hendrix 035B closes via his promoted transfer (defect #2b, pending pipeline fix); R1 #035A over-subscription (4 open move-ins) remains an open missing-move-out anomaly from Round 1.
