# Rulings — 287 Cleveland St, Redfern

## 2026-07-05 — P5 Asana comment sweep (13 flagged tasks)

Source: Asana task comments pulled via connector, comment_limit 30. Findings are explicit-only.

### Fees / bond resolutions
- **1213754732145800 (Santiago Berbotto, R3 #037B)** — FINAL TENANT CHARGES: Room cleaning/items left behind $75; endorsed to Accounting 2026-04-13. Fee = $75 confirmed. RESOLVED.
- **1213307336945589 (Chanwoo Bae, R3 #037A)** — FINAL TENANT CHARGES: Mattress cover $50 + Drawer $172.50 = $222.50; endorsed to Accounting 2026-03-13. Prior fees.csv had $50 only. Corrected to $222.50. RESOLVED.
- **1212289025013487 (Zaid Hamsassia, R6 #40A)** — EVICTED w/ arrears. 1 week free rent applied 2025-11-04 (Ari-approved); still 3 weeks arrears + late fees, total arrears $775 at eviction. Charges: Room cleaning $150 + Items left behind $75 + Mattress cover $85 = $310. Eviction proceeded (blacklisted 2025-12-15). Fee $310 confirmed; arrears $775 outstanding. RESOLVED.
- **1212152556949219 (Haroun Zouari, R6 #40B, Dec 9)** — REAL eviction. Charge Room cleaning $75; $250 rent credit given, arrears $500. Eviction executed, returned to property 2025-12-10. Fee $75 confirmed. RESOLVED. (Duplicate task 1211917167195053 was retracted — see below.)
- **1211667884317328 (Camila Andrea Selin, R5 #39)** — Charges Mattress cover $85 + Room cleaning $75 = $160; endorsed 2025-10-31. Note: only HALF cleaning charged (sweeping). $375 SD arrears deducted from bond; collection messages ongoing. On 2025-11-20 Ariadna disputed the cleaning/mattress charge (room handed over dirty) and asked for review — no reversal recorded in comments. Fee $160 applied but partially disputed by internal staff; bond consumed by $375 arrears. RESOLVED (fee stands per record; dispute noted).
- **1211310066686372 (Lisa Wilson move-out, R2 #36)** — Initially "left without notice, bond forfeited"; tenant provided proof of notice → tagged COMPLIANT, break fee waived, bond NOT forfeited. FINAL TENANT CHARGES: Room cleaning $100 (fees.csv had $75). Corrected to $100. Bond returned less $100. RESOLVED.
- **1211255143604148 (Federico Monti, R4 #38/#038A)** — OCR clear, no deductions. Notice/break fee WAIVED due to leak/maintenance issue (pending maintenance). Bond refunded in full (tenant demanded full refund; OCR clear = no deductions). Fee $0; waiver reason = leak/maintenance. RESOLVED (bond-refund dispute resolved in tenant's favour).
- **1211738290119973 (Giordano Perinelli, R6 #40)** — Tenant "confirmed he did not move in at all." OCR clear, no deductions. Full security deposit refund. Refund scope resolved = full SD (never occupied). Fee $0. RESOLVED. (Task already flagged transfer_cancel in timeline; retained.)

### Retractions
- **1211917167195053 (Haroun Zouari, R6 #40B, Nov 19)** — Last comment 2025-11-20: "Occupant is now up to date. Retracting this termination for now." Confirmed retracted/superseded. Real move-out is Dec 9 (1212152556949219). Already excluded in overrides.csv (pre-existing). No fee applies. RESOLVED.
- **1210737767129253 (Lisa Wilson, OFFER RELOC, R2 #36)** — Relocation-offer task, NOT a move-out event. Comments: tenant "has no plans to move to a different property" / "she'll stay for now as long as maintenance issues are fixed"; maintenance resolved; staff: "we can close the task if tenant will not proceed moving out." Export tags this "Move Out Cancelled" with no_moveout_date. Actual move-out is separate task 1211310066686372 (2025-09-01). ADDED exclude to overrides.csv (retraction — offer/cancelled, not a tenancy event). No fee applies.
- **1215821222380914 (Sabrina Suriajingga Anjani, R5 #39)** — Move-out task, comments (2026-06-19): "retraction letter sent" plus "received payment"/"received a payment for only $290". A retraction letter was issued and payment received, indicating the move-out may have been retracted / tenancy continued. However, timeline.csv currently records this as an active move_out (MO 2026-06-24, due_date) and it is the latest event on Room 5. Comments do NOT give an unambiguous final move-out date, and a retraction here would leave Room 5 with no closing event. NOT excluded pending Kurian ruling — see finding below. Fee flag: no tenant charges / OCR status in comments; still no explicit fee data. FLAG KEPT.

### Move-out-date findings
- **1211738290119973 (Giordano)** — Comments confirm tenant never moved in; S3 used MO 2026-10-17 (matches move-out date field). No contradiction. Already transfer_cancel.
- **1215821222380914 (Sabrina)** — FINDING / CONTRADICTION: comments show a retraction letter was sent (2026-06-19), which contradicts S3's active move-out at 2026-06-24. No override action taken (dates not hand-edited). Needs Kurian ruling: is Sabrina's move-out retracted (tenancy ongoing) or does the 2026-06-24 move-out stand? If retracted, Room 5 needs its prior closing event reconsidered.

### Still-silent / unresolved after comment check
- **1215821222380914 (Sabrina)** — comments checked; no explicit tenant charges, break fee, or OCR clear/deduction status. Fee data still unresolved. needs_asana_check kept = yes.
- **1211929755311339 (Leonardo Gomez, R2 #36)** — comments reference break fee "3 weeks rent" and move-out confirmation email "Fixed Term [w/break fee]", move-out was COMPLIANT with replacement tenant (Javier Abascal); OCR clear, "will not charge" (dust minimal), endorsed to Accounting. NO explicit dollar figure for the break fee in comments — the $1980 in fees.csv is NOT confirmed by comments. Fee amount unresolved (break fee referenced but unquantified in comments; compliant-with-replacement may mean waived). needs_asana_check kept = yes with note.

### Move-in prior-room chain
- **1213976823034682 (Dimas Suria Natanegara, R3 #037B)** — PERM transfer INTO 037B, move-in 2026-04-19 (confirmed 04-20). Prior room #28 resolved: receipt (2026-04-13) confirms deposit for "Room 2, #28, 285 Cleveland St, Redfern" — a DIFFERENT building (285, not 287). Not 037A. Prior-room-chain HUMAN REVIEW flag resolved: tenant came from 285 Cleveland #28. Transfer fee $150, bond excess $390.

## P5 comment sweep 2026-07-06 (batch 00R)

Source: Asana task comments pulled via connector (get_task, comment_limit 40). Findings explicit-only. ruled_by=asana-comment, ruled_on=2026-07-06.

- **1211929755311339 (Leonardo Gomez, R2 #36)** — [task](https://app.asana.com/0/0/1211929755311339/f) — RESOLVED. Comments confirm break fee cited only as "3 weeks rent" (Chriszsa 2025-11-13, "Not compliant with break fee of 3 weeks rent") with NO dollar figure anywhere in the thread — the $1980 Break Fee field is unsupported by comments, consistent with Kurian r3 TYPO ruling. Replacement tenant Javier Abascal Vital supplied and room re-occupied 2025-11-22 (compliant-with-replacement). Arrears notice sent 2025-11-19 (Nadine) — supports the $313 rent-arrears figure. OCR: "will not charge, dust are very minimal" → OCR Clear, no deductions; endorsed to Accounting 2025-11-27 (bond returned). RULING: fee = $313 rent arrears only; break fee not charged (waived via replacement). needs_asana_check → no. ruled_by=asana-comment, ruled_on=2026-07-06.
- **1215821222380914 (Sabrina Suriajingga Anjani, R5 #39)** — [task](https://app.asana.com/0/0/1215821222380914/f) — PARTIAL. Comments (2026-06-18 / 2026-06-19, all Jen Cabana): "received a payment for only $290", "received payment", "retraction letter sent", and an unattributed request "please update the completion date". NO tenant charges, break fee, OCR clear/deduction status, or bond status in comments. No explicit final move-out date. FEE/BOND STILL OPEN — needs_asana_check kept = yes.
  - Date note: Kurian r3 (2026-07-05) already ruled the LATER DATE STANDS — move-out 2026-06-24 stands; the 2026-06-19 retraction letter came earlier and does NOT override. No override applied here (Stage A/B ruling stands).
  - PROPOSED ruling for Kurian (Stage C/D — NOT applied): The "retraction letter sent" + "$290 partial payment" pattern could imply the move-out was walked back / tenancy continued past 2026-06-24. If so, Room 5's closing event and bond disposition need revisiting. Recommend Kurian confirm whether (a) 2026-06-24 remains the true final move-out (current ruling), and (b) whether the $290 is a final settlement, arrears, or bond amount. No overrides.csv change made. ruled_by=asana-comment, ruled_on=2026-07-06.

## Kurian rulings 2026-07-05 (round 3)
- Bed-pairing A/B artifacts: accepted as-is; bed-level analytics deferred.
- 40↔41 ambiguity: APPROVED slot method — lay the affected tenants (Masato, Giordano, Zaid,
  Haroun) into logical timeline slots and deduce which room each actually occupied; apply the
  resolution; ask follow-ups only if slots don't resolve it.
- Sabrina: LATER DATE STANDS — move-out 2026-06-24 (retraction letter 2026-06-19 came earlier
  and does NOT override; eviction sequence ends at the later date). No date override needed.
- Leonardo: $1,980 break fee is a TYPO, not real. Actual: $313 rent owed (verify on task).
  Correct fees.csv: remove 1980, record 313 arrears.
- Lisa Wilson: fee treatment per sweep accepted.

## Applied 2026-07-05 (round 3)
- Sabrina (1215821222380914): NO change — 2026-06-24 stands (later date). No override.
- Leonardo (1211929755311339): fees.csv corrected — $1980 break-fee removed (typo); recorded $313 rent owed/arrears. Verified correct Task ID; $313 consistent with on-task "3 weeks rent" + arrears notice (no explicit $ figure in export, per Kurian's figure).

## 40↔41 SLOT RESOLUTION (ruled_by=slot-method-per-Kurian, 2026-07-05 r3)

Method (Kurian-approved): pair each person's own move-in→move-out into one continuous tenancy, use the OFFBOARDING (exit) code as the administratively-confirmed room, then pack into non-overlapping bed-slots. All events under #40/#40A/#40B (Room 6) and #41/#41A/#41B (Room 7) resolve with NO within-bed overlap:

ROOM 6 (#40 family) — 2 beds:
- Bed 40A: Zaid Hamsassia 2025-10-28 → 2026-01-15 (evict; exit #40A) → Jack Hogan-Finlay 2026-02-02 → ongoing (#40A). Sequential, clean.
- Bed 40B: Haroun Zouari 2025-10-28 → 2025-12-09 (evict; exit #40B).

ROOM 7 (#41 family) — 2 beds (an "Additional Bed" maintenance task 1211764735895363 confirms a 2nd bed):
- Bed 1: Masato Okazaki 2025-06-28 → 2025-11-17 (exit #41).
- Bed 2: Juan Carreño 2025-07-03 → 2025-10-10 → Callum Maxwell 2025-11-29 → 2026-02-14 → Radikanesha Bharly 2026-02-14 → 2026-05-05 → Udaya Gaddam 2026-05-31 → ongoing. Sequential, clean.

Crossers (move-in and move-out under different codes) — CONFIRMED ROOM per exit code:
- Masato: in #40, out #41 → real room = ROOM 7.
- Zaid: in #41, out #40A → real room = ROOM 6 (bed A).
- Haroun: in #41, out #40B → real room = ROOM 6 (bed B).
- Giordano: in #41, out #40 → NEVER OCCUPIED → EXCLUDED (both events, overrides.csv).

APPLICATION NOTE: S5 pairs strictly by exact room_code, and no reassign-room / code-remap override exists, so Masato/Zaid/Haroun still show a phantom ongoing (entry code) + orphan_out (exit code) in tenancies.csv. Per Kurian these A/B artifacts are ACCEPTED AS-IS (bed-level analytics deferred); the authoritative room assignment is THIS table. RESIDUAL for owner: a `reassign_room <task_id> <code>` override would let these collapse into single tenancies. Giordano is fully cleaned via exclude.

## Stage C gap-hunt 2026-07-06 (batch 00R) — reference only, no events added
Pre-window move-in start dates found (stay-length reference for pre_window tenants; NOT added as events per window discipline):
- Yu Shinnishi #037A — real start 2025-06-17 ([1210548991150648](https://app.asana.com/0/0/1210548991150648/f))
- Federico Monti #038A — real start 2025-06-18 ([1210549820686039](https://app.asana.com/0/0/1210549820686039/f))
- Lisa Wilson #36 — real start 2025-06-23 ([1210555340680575](https://app.asana.com/0/0/1210555340680575/f))
- Kevin #039B — real start 2025-06-10 ([1210500193440319](https://app.asana.com/0/0/1210500193440319/f))
In-window missed events: none cleanly attachable (cross-code slot cases are Kurian items, see double-check). Post-window move-outs: none.
