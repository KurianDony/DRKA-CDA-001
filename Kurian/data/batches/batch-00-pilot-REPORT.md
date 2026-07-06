# Batch 00 — Pilot Report (P1)

Prepared 2026-07-05 by the orchestrator. Scope: 5 diverse houses end-to-end (A0 → extract → review → timeline → eval). 342-cleveland-st-surry-hills carried as golden/regression.

**Headline:** all 5 houses completed the pipeline with S4 VERIFY = PASS and eval PASS; none parked. The 342 golden regression still PASSes. The pilot surfaced **two real script-level defects** and several calibration findings — that feedback is the primary deliverable (below).

---

## Per-house results

### 287 Cleveland St, Redfern — `287-cleveland-st-redfern`
- **A0:** C3 documented-proceed (038B/039B beds of Rooms 4/5). Extract surfaced 4 more bed codes (039A, 40A, 40B, bare 41) — added under the bed rule, assumption logged.
- **Counts:** move-in 39 top-level / 12 flagged; move-out 26 / 17 flagged; maintenance 58. Tenancies 44, vacancy gaps 23.
- **Fees:** ~$4,700 found ($3,080 break fees + ~$1,620 cleaning/items; $300 break fee waived — Felipe). 11 tasks need Asana comment check.
- **Anomalies:** heavy bed-code pairing artifacts — 035A shows 4 open, 41 shows 3 open (both physically 2-bed rooms), Masato Okazaki split across #40/#41 producing −111/−137 overlaps. 6 ruling-#7 date conflicts resolved. 1 no-date WARN (Lisa Wilson OFFER RELOC).
- **Eval:** PASS (no golden yet).
- **Context:** extract 54k tok / review-moveout **93k tok, 31 tool calls (heaviest sub-agent in batch)** / timeline 59k.

### 1/148 Liverpool Rd, Enfield — `1-148-liverpool-rd-enfield`
- **A0:** PASS. Small clean house (3 rooms).
- **Counts:** move-in 7 / 4 flagged; move-out 8 / 5 flagged; maintenance 24. Tenancies 9, gaps 6.
- **Fees:** $1,259.80 (Jinson eviction $850; Umashankar key $209.80; Sharayu $100). 8 need comment check (fee/bond fields blank in export).
- **Anomalies:** Room 433 shows **3 ongoing** — the two closing transfer move-outs are `is_subtask=yes` and S3 skips them (defect #2 below). 3 genuine pre-window tenants.
- **Eval:** PASS. **Context:** extract 46k / reviews 51–62k / timeline 59k.

### 350 Marsden Rd, Carlingford — `350-marsden-rd-carlingford`
- **A0:** PASS. Rooms 4 (1172) & 8 (1176) closed — behaved as expected (0 / 1 event).
- **Counts:** move-in 20 / 8 flagged; move-out 14 / 9 flagged; maintenance 45. Tenancies 22, gaps 15.
- **Fees:** ~$4,010 ($3,850 break fees in fields + $160 charges; drops to ~$3,290 if Dunstan's notice was retracted). 14 need comment check.
- **Anomalies:** Mahyar 1175 transfer-out is a subtask → tenancy stays open (defect #2). Mohd Amaan room ambiguity (1173 vs 1169). Md Aftab Ovi duplicate move-out excluded. Benjamin Dunstan move-out possibly retracted (comment check).
- **Eval:** PASS. **Context:** extract 51k / reviews 54–64k / timeline 64k.

### 66 Boundary St, Parramatta — `66-boundary-st-parramatta`
- **A0:** PASS. "Clean control" house — but surfaced the batch's most serious defect.
- **Counts:** move-in 17 / 10 flagged; move-out 11 / 10 flagged; maintenance 63. Tenancies 14, gaps 8. No collision leak from bare-integer codes (address anchor held).
- **Fees:** ~$3,700 (Ratu $1,485; Orisi eviction cleaning $150 + uncaptured arrears). Bond/CR fields empty on all 11 — bond unverifiable from export. 7 need comment check.
- **Anomalies:** **Defect #1 — five single-digit `#7/#8/#9` move-outs stranded in UNRESOLVED → Rooms 1/2/3 falsely read "ongoing."** Room 6 (#12) had zero window events (closed vs missing data — decision). Adriano #7-vs-#10 code tangle + cross-house transfer 1211433880033810.
- **Eval:** PASS — **note: eval did not catch defect #1** (blind spot, below).
- **Context:** extract 53k / reviews 55–78k / timeline 64k.

### 71 Therry Street, Avalon Beach — `71-therry-street-avalon-beach`
- **A0:** PASS. #168 aliased to Room 2 (#168A) at extract.
- **Counts:** move-in 17 / 8 flagged; move-out 15 / 11 flagged; maintenance 33. Tenancies 25, gaps 15.
- **Fees:** $660 confirmed (Jorge break $390; Blake cleaning/blinds $270 — possible waiver, NCAT threat). 12 need comment check.
- **Anomalies:** Harrison Kukla code collision (#479 name vs 172 code) — flagged not reassigned. Transfer/couple pairing artifacts on 479/172/174/168A. Melany 170 ruling-#7 fallback.
- **Eval:** PASS. **Context:** extract 58k / reviews 57–58k / timeline 60k.

---

## Friction findings (the deliverable)

### Defect #1 — single-digit room codes never matched from Name text `pipeline/lib/common.py`
`ROOMCODE_TEXT_RE = re.compile(r"#\s?(\d{2,4}[A-Za-z]?)\b")` requires **2–4 digits**. Houses with single-digit room codes (66 Boundary: 7,8,9) lose every move-out whose Room Code *column* is blank and whose code lives only as `#7`/`#8`/`#9` in the Name. Result at 66 Boundary: **5 real move-outs stranded in UNRESOLVED, Rooms 1/2/3 falsely "ongoing."** Move-ins survived only because their Room Code column was populated.
- **Impact:** any house with 1-digit codes is materially corrupted. Portfolio scan recommended before those houses are batched.
- **Recommended fix:** widen to `(\d{1,4}[A-Za-z]?)`. Safe because `resolve_room_code` already intersects hits with the house's `valid_codes`, so a bare `#7` can only resolve to a code the house actually owns. Then re-run 66 Boundary and re-verify.

### Defect #2 — transfer-out move-outs recorded as subtasks are hard-skipped by S3
Permanent room transfers are logged as `is_subtask=yes` checklist rows under the parent move-in. `s3_timeline.py` skips subtasks *before* overrides are consulted, and `overrides.csv` supports only `action=exclude` — there is no `include`/`promote`. So an effective move-out via transfer never closes the tenancy.
- **Impact:** Mahyar (350, Room 1175, ~2-day tenancy) and Umashankar + Diego (1/148, Room 433) show `ongoing` instead of closing. Contradicts ruling that a perm transfer-out is an effective move-out.
- **Recommended fix:** add an override action (`promote`/`force_move_out <task_id> <date>`) or have S3 surface transfer-out subtasks as move-out events when they carry a date and a valid room code.

### Finding #3 — eval blind spot
Eval PASSes 66 Boundary despite defect #1, because it checks pipeline execution + golden diff, not room-resolution completeness. **Recommend adding an eval gate:** flag when a move-out sits in UNRESOLVED while its Name contains a `#code` that is a valid house code, and/or track the UNRESOLVED-move-out ratio.

### Finding #4 — flag rate runs higher than the runbook baseline
Move-out flag rates: 287 65%, 1/148 63%, 350 64%, 66 **91%**, 71 73% — vs the runbook's ~30–50% baseline. Much of the excess is **pairing artifacts**, not genuine issues: fuzzy-name pairing is per-room-code, so a tenant leaving under a paired bed code (287) or via a transfer subtask (defect #2) leaves a phantom "ongoing" row that gets hr=yes. Once defects #1/#2 and cross-bed-code reconciliation are addressed, the true flag rate should fall closer to baseline. **Calibration action:** consider S5 cross-bed-code reconciliation (same person across paired codes of one room) to auto-close these.

### Finding #5 — export carries almost no fee/bond data in fields
Across all 5 houses, CR Charges / Bond Held / Break Fee columns are largely empty; fee amounts came from Notes text, and bond status is frequently unverifiable. **52 tasks batch-wide are marked `needs Asana comment check`.** This makes the **P5 comment sweep essential, not optional** — it's where most fee/bond truth lives.

### Finding #6 — minor: link format
Some review/double-check links omit the trailing `/f` (still clickable). Cosmetic; worth normalizing in the skills.

### Context/token observations (for batch sizing)
Per-house sub-agent cost: extract ~46–58k; move-in review ~51–58k; **move-out review ~51–93k (the driver — fees + subtask evidence)**; timeline ~59–64k. Heaviest single agent: 287 move-out review at 93k / 31 tool calls. A 15-house batch of houses this size would strain orchestrator + sub-agent budgets; **8–10 per batch is the realistic ceiling** for medium/large houses, consistent with the runbook.

---

## Eval verdicts
| House | S4 VERIFY | Eval | Golden |
|---|---|---|---|
| 342-cleveland (regression) | PASS | **PASS (E2/E3 vs golden)** | frozen |
| 287-cleveland | PASS | PASS | pending Kurian |
| 1/148-liverpool | PASS | PASS | pending Kurian |
| 350-marsden | PASS | PASS | pending Kurian |
| 66-boundary | PASS | PASS* | pending Kurian |
| 71-therry | PASS | PASS | pending Kurian |

\*66-boundary passes eval but is data-degraded by defect #1 until the regex fix + re-run.

## Recommended next actions
1. Apply defect #1 and #2 fixes; re-run 66 Boundary (both defects), 350 and 1/148 (defect #2); re-verify.
2. Portfolio scan for single-digit room codes before batching those houses.
3. Run the P5 comment sweep for the 52 `needs Asana comment check` items (fees, bond, retractions, final-move-out dates).
4. Kurian rules on the consolidated decisions list (below / in chat). Then freeze goldens for approved houses.

---

# ROUND 2 (2026-07-05) — post-fix rerun

Pipeline owner shipped fixes for the two Round-1 defects (1–4-digit room-code regex; `promote_move_out` override; S4 room-resolution gate; portfolio scan = 66 Boundary is the only single-digit house). This round applied them and ran the P5 comment sweep. **All 6 houses end Round 2 at S4 VERIFY = PASS and eval = PASS, including the 342 golden regression.** One new defect (#2b) surfaced and is the only hard blocker remaining.

## NEW blocker — Defect #2b: promoted move-outs carry no tenant, so S5 can't pair them
`promote_move_out` (defect-#2 fix) creates the move-out event, but S3 sets `tenant` from the CSV **"Tenant Name" column**, which is **empty on transfer subtasks** (the name is only in the task Name). S5 pairs move-out↔move-in by name similarity, so a tenant-less promoted move-out becomes an `orphan_out` and the move-in stays `ongoing` — the transfer-out does **not** close the tenancy. VERIFY still PASSes (it doesn't gate pairing).
- **Impact:** Mahyar (350, #1175), Umashankar + Diego (1/148, #433), Jin (287, #035B) all still read `ongoing` despite correct promote overrides being in place.
- **Recommended fix (owner):** when promoting, derive `tenant` from the task Name (trailing name token after the address), **or** have S5 fall back to per-room chronological pairing when a promoted move-out has no tenant. Overrides are already committed — a plain S3→S5→S4 re-run will close all four once fixed.

## Task-by-task outcomes

**T1 — promote overrides applied** (`ruled_by=pilot-orchestrator`): 350 Mahyar `1215478013034340` (#1175); 1/148 Umashankar `1213450431910672` + Diego `1213815366058872` (#433). **287 scan** found one same-pattern case — Jin Hendrix PERM transfer 035B→037A `1213589504292986` — promoted too. All re-ran VERIFY PASS, but closures blocked by defect #2b (above). The other 287 transfer-flavoured subtasks were ICR condition-report admin, not departures — correctly left alone.

**T2 — 66 Boundary move-out review refreshed** after the regex re-run: 11 reviewed, of which **5 are the previously-stranded Rooms 1/2/3 move-outs** now correctly attributed (Orisi #7 evict 2026-01-03, Tanisha #7 2026-06-20, Saksham #7, Ananta #8, Thiviru #9). Ananta's date corrected to Due 2025-09-01 by ruling #7 (Earliest overlapped next move-in). Move-in review stands. Spot-audit (Orisi, Ananta) clean by Task ID.

**T3 — 287 bed-code reconciliation** (manual, no tenancies.csv edits): 6 phantom `ongoing` rows marked `bed-pairing artifact` in `review_moveout.md` + `double_check.md`. Two are clean same-room bed pairs (Francisco 035A/B; Syed 38/038B). Four span the **40↔41 code boundary** (Masato, Giordano, Zaid, Haroun) — the same-person-across-a-Room-6-code-and-a-Room-7-code pattern suggests #40 and #41 were used interchangeably; registry room split for 40/41 may need revisiting.

**T4 — P5 Asana comment sweep** (connector verified working — `get_task` returns stories/comments): 54+ flagged tasks swept across the 5 houses. Highlights:
- *287:* 10 fees resolved (Chanwoo $50→$222.50; Zaid $310 + $775 arrears; Lisa $75→$100 break-fee waived; Federico/Giordano $0 full refunds). +1 comment-exclude: Lisa OFFER-RELOC `1210737767129253` ("Move Out Cancelled"). Sabrina retraction-letter (2026-06-19) contradicts S3's 2026-06-24 — date finding. Leonardo $1980 break fee **not** confirmed by comments (possibly waived) — flag kept.
- *1/148:* 8/8 fees resolved ($850 Jinson; $209.80 Umashankar-primary; $100 Sharayu; rest $0). Hassan date finding (S3 2025-12-25 vs vacate 29 Nov vs compliance-to 24 Dec).
- *350:* all resolved. Islam #1171 break fee **$1760 waived** + SD refunded; Patrick #1175 **bond forfeited**. +1 comment-exclude: Md Aftab June move-out `1215355847925679` retracted. **Contradiction:** with the Round-1 exclude of the July `1216098477207302`, Md Aftab #1171 now has **no in-window departure** — needs Kurian. Dunstan kept (cancelled then re-proceeded).
- *66:* fees resolved (Saksham $540 break; Thibault $50+$270; Bruno cleaning/blinds waived). Adriano transfer confirmed but prev-room code = **7, not #10** — does not confirm the Room 4 exit. Ratu $1360 break fee **unsubstantiated** by comments (kept). Orisi arrears confirmed but **no amount stated**.
- *71:* all 15 fee rows resolved. +1 comment-exclude: Owen Bell `1213033868651850` never moved in. Harrison real room = **479** (not 172). Melany real move-out **7 Jan 2026** (S3 fallback 8 Jan within 1 day). Blake door $250 stands; cleaning $150 waivable (NCAT).

**T5 — eval:** all 5 + 342 regression PASS. New S4 room-resolution gate green everywhere.

## Frozen-golden candidates (pending Kurian sign-off)
- **Ready first:** `66-boundary-st-parramatta`, `71-therry-street-avalon-beach` — no defect-#2b dependency; VERIFY+eval PASS; only Kurian rulings outstanding.
- **After defect-#2b fix + re-run:** `287-cleveland-st-redfern`, `350-marsden-rd-carlingford`, `1-148-liverpool-rd-enfield` — correct overrides are in place; they just need the tenant-pairing fix to close the promoted transfers.
- `342-cleveland-st-surry-hills` golden stays frozen (regression green).

## Round-2 residual friction (for the owner)
1. **Defect #2b** (above) — the one blocker.
2. **No date-set override.** Comment-derived "final move out date" / billed-vs-physical date corrections (Sabrina, Hassan, Bruno, Md Aftab) can't be applied scriptably — only `exclude`/`promote_move_out` exist. Consider a `set_move_out_date <task_id> <date>` override action.
3. **Registry 40/41 split** at 287 may be wrong (see T3).

---

# ROUND 3 (2026-07-05) — Kurian rulings applied; PILOT CLOSED

Owner shipped the remaining fixes (defect #2b tenant-derivation + S5 chronological fallback; new `set_move_out_date` override). All four promoted transfers now CLOSE (Mahyar #1175, Umashankar + Diego #433, Jin #035B — verified). Kurian's round-2 decisions were ruled and are recorded in each house's `rulings.md`. **Outcome: all 5 houses S4 VERIFY PASS + eval PASS, 342 regression green, and all 5 goldens frozen. Pilot closed.**

## Rulings applied
- **287 Sabrina** — no change; move-out 2026-06-24 stands (later date beats the earlier retraction letter).
- **287 Leonardo** — `$1,980` break fee was a typo; corrected `fees.csv` to **$313 rent owed** (Task-ID verified; consistent with the on-task "3 weeks rent" + arrears notice — no explicit $ in export, per Kurian's figure).
- **1/148 Hassan** — `set_move_out_date` → **2025-12-24** (paid-to/billed, later-date rule); physical vacate 2025-11-30 recorded as a note only, in `review_moveout.md` + `fees.csv`.
- **350 Md Aftab** — current tenant; ongoing is correct (both June-retracted and out-of-window-July move-outs excluded). Question closed.
- **71 Harrison = #479** — excluded the mis-roomed 172 move-in; his 479 move-out carries the Room 9 association (he never actually stayed). Room 6 (172) now clean, Room 9 (479) shows him. **Owen** exclude confirmed.
- **66 Room 6 (#12)** — searched the raw off-boarding export for an in-window #12 move-out (Task-ID verified): **none** (only pre-window Feb-2025 and post-window 2026-07-25 Rohit Shinde). No conflict with "occupied till now" → added #12 to `full_window_occupants` (renders in the HTML like 342's 1106; no tenancy row, by design).
- **71 Melany** — `set_move_out_date` → **2026-01-07** (tenant-confirmed; S3 fallback was 8 Jan, 1-day correction).

## 287 40↔41 slot resolution (ruled_by=slot-method-per-Kurian)
Using each person's own in→out with the **offboarding (exit) code as the confirmed room**, all #40/#41-family events pack into non-overlapping bed-slots:
- **Room 6 (#40):** bed 40A = Zaid (→ evict 2026-01-15) → Jack (ongoing); bed 40B = Haroun (→ evict 2025-12-09).
- **Room 7 (#41):** bed 1 = Masato (2025-06-28 → 2025-11-17); bed 2 = Juan → Callum → Radikanesha → Udaya (sequential; "Additional Bed" maintenance confirms the 2nd bed).
- **Giordano** never occupied → both events **excluded**.
Full table in `287/rulings.md`. Because S5 pairs strictly by exact room_code and no reassign-room action exists, Masato/Zaid/Haroun still show a phantom ongoing + orphan_out in `tenancies.csv` — **accepted as-is per Kurian (bed-level analytics deferred)**; the authoritative room assignment is the rulings table.

## Residual friction (for the owner — none block the pilot)
1. **No `reassign_room` override.** Needed to collapse code-crossers (287 Masato/Zaid/Haroun; 71 Harrison) into single tenancies instead of leaving documented artifacts / using exclude-approximations. Only genuine remaining capability gap.
2. **Fee-data gaps** (66 Ratu $1360 break fee unsubstantiated; 66 Orisi arrears amount not stated; 66 Tanisha OCR pending) — export/comments silent; accounting-side, not tenancy-blocking.
3. **Bruno (66)** billed date Oct 20 vs physical Oct 5 — not ruled this round; S3's Oct 5 stands.

## Final state
| House | VERIFY | Eval (incl. golden E2/E3) | Golden |
|---|---|---|---|
| 342-cleveland (regression) | PASS | PASS | frozen (unchanged) |
| 287-cleveland | PASS | PASS | **frozen** (42 tenancies / 21 gaps) |
| 1/148-liverpool | PASS | PASS | **frozen** (9 / 6) |
| 350-marsden | PASS | PASS | **frozen** (22 / 15) |
| 66-boundary | PASS | PASS | **frozen** (21 / 12) |
| 71-therry | PASS | PASS | **frozen** (24 / 14) |

**Pilot P1 complete.** Skills + scripts calibrated across three rounds; two defects (single-digit codes, subtask transfer-outs) + one follow-on (2b) found and fixed; overrides now cover exclude / promote_move_out / set_move_out_date; eval gained a room-resolution gate. Ready to scale to batch 01.

