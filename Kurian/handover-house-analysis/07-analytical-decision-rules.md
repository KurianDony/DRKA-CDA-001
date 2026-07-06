# 07 — Analytical Decision Rules (CDA-001 Portfolio Diagnostic)

**Written:** 2026-07-04 · **Engagement:** DRKA consulting for CDA Co-Living — 12-month rebuild of every house/room: stay length, vacancy, turnover, real occupancy, maintenance, tenant signal, area read.
**Builds on:** handover docs 01–04 in this folder. This doc does not repeat their mechanics (pagination, opt_fields, token limits, collision lists) — it defines the DECISION rules. Where a rule depends on a doc section, it cites it as `(0N §x)`. Where a rule depends on a live Asana value, that value was pulled read-only on 2026-07-04 and is recorded verbatim in Appendix A.
**Prime directive (Kurian, verbatim intent):** the columns tell you *that* a task was cancelled for full refund — they do not tell you *why*. Read the comments. Be very analytical, very precise. Always check. 100% sure before you make a decision. No classification is final without cited evidence.
**All systems READ-ONLY** (01 header). Real tenant names in evidence — outputs use first names or `[gid:…]`/`[id:…]` citations (01 privacy note).

---

## 0. Escalation levels (referenced by every rule)

| Level | Name | When | Action |
|---|---|---|---|
| L1 | **Inline assumption** | Low-stakes gap; a stated default resolves it | Proceed; print the assumption next to the number it affects |
| L2 | **UNVERIFIED label** | Finding is probably right but the evidence chain is incomplete | Report it, tagged `UNVERIFIED`, excluded from headline aggregates unless stated |
| L3 | **Question-queue** | Only Kurian can resolve; analysis can continue around it | Add to the running "Questions for Kurian" list in the deliverable; continue |
| L4 | **KURIAN BLOCKER** | The gap invalidates a whole metric or a whole house | Halt that metric/house; emit the exact phrase `KURIAN BLOCKER:` + what is needed (see R12) |

Never silently upgrade an assumption into a fact. Never average an UNVERIFIED value into a headline number without saying so.

---

## R1. Event classification taxonomy

**Definition.** Every Asana task in scope maps to **exactly one** event class. One tenancy may span several tasks (move-in task + offboarding task + retention task); one task never carries two classes.

Classes:

| Class | Meaning |
|---|---|
| `MOVE_IN_CONFIRMED` | Tenancy started; room physically occupied |
| `CANCELLATION_FULL` / `CANCELLATION_PARTIAL` / `CANCELLATION_NONREF` | Sale cancelled before occupancy; subtype = refund treatment |
| `MOVE_OUT_CONFIRMED` | Tenancy ended; room physically vacated |
| `EARLY_BREAK` | Subtype of MOVE_OUT_CONFIRMED: left before Lease End Date |
| `NATURAL_END` | Subtype of MOVE_OUT_CONFIRMED: left at/after Lease End Date |
| `TRANSFER` | Same tenant, different room/house — paired A-out / B-in |
| `RETAINED_NOTICE` | Move-out notice cancelled; tenant stayed — no vacancy event |
| `STUB_EXCLUDED` | TEMP OCR/ICR holding tasks, batch-created stubs, admin/prep tasks |
| `DUPLICATE` | Redundant task for an event already classified on another task |

**Data source.**
- Moving In project `1209877764947329` (01 §2): sections incl. `Completed` `1209877767371600`, `Cancelled Sale - Full Refund` `1209877767371602`, `Cancelled Sale - Partial Refund (HD not included)` `1210434893279203`, `Cancelled Sale - Non Refundable` `1209877767371604` — all re-verified live 2026-07-04 (Appendix A.2). Fields: `Date and Time Paid` `1209877767266405`, `Room Code` `1209877764947364` (02 §3.1).
- Off boarding team `1206596901916034` (01 §2): fields `Lease Start Date` `1209276344420857`, `Lease End Date` `1206946403745907`, `% of Lease Expired` `1209276344420861`, `Break Fee (if applicable)` `1209276344420859`, `Room Status` `1207132850522766` (options "Still in the house"/"Already left" — live), `Form Reason` `1207446664940687`, `Type of Retention Request` `1211097732837374` — all re-verified live 2026-07-04.
- Title-prefix taxonomy (02 §3.1 / offboarding-recipe.html): `⏰ EOL`, eviction prefixes, `Room Transfer`, `PERM`, `TEMP OCR/ICR`, `[Duplicate]`, `LR |`.
- Retention Team `1210587789196546` and section "Retention Success (Cancelled Move Out)" (02 §3.1, §4.4).

**Procedure.**
1. Pull the task with restricted opt_fields (02 §7.1); record project, section, title, dates, key custom fields.
2. **Stub filter first:** empty name/notes AND no due date → `STUB_EXCLUDED` (02 §7.4). Title contains `TEMP OCR` / `TEMP ICR` → `STUB_EXCLUDED` (holding room, 02 §4.8). `LR |` lease renewals are not move-ins — exclude from event counts, but record as tenancy-continuation evidence for stay length (R4).
3. **Cancellations:** Moving In task whose section is one of the three Cancelled Sale sections → `CANCELLATION_*` by section. Subtype meaning: Full Refund = all money returned; Partial Refund = section name is literally "Cancelled Sale - Partial Refund (HD not included)" — the Holding Deposit is excluded from the refund, i.e. retained (HD = Holding Deposit per 01 glossary, *inferred* — L1 assumption, stated); Non Refundable = nothing returned. A cancellation means the tenancy **never started** — zero occupancy, zero turnover (02 §4.4).
4. **Move-ins:** Moving In task, section `Completed` (or For Move In Confirmation with confirming comment). Evidence hierarchy for "confirmed": (a) `Date and Time Paid` populated **and** section Completed → confirmed-paid (strongest); (b) section Completed with `due_on` only → confirmed-by-due-date (due_on = move-in date, 02 §3.1); (c) anything weaker (pipeline section, no payment, no completion) → not confirmed; check comments; if still ambiguous → phantom-move-in check (step 8).
5. **Move-outs:** offboarding task with a move-out date resolvable via the 02 §3.1 priority order (form text > sibling task names > timeline blocks > attachment screenshot > `due_on` with cited ambiguity). Confirmation boosters: `Room Status` = "Already left"; comment confirming vacancy ("Room is empty as per Salim", 02 §3.1).
6. **Early break vs natural end:** compute stay vs lease term yourself (R4), then cross-check Asana's `% of Lease Expired`; `Break Fee (if applicable)` populated ⇒ early break (02 §3.1). Disagreement between your math and the field → recheck dates before trusting either; unresolved → L3.
7. **Transfers:** `Form Reason` ∈ {"I want to transfer to a different room", "I want to transfer to a different house"} (live enum), or `Type of Retention Request` transfer/relocation options (Appendix A.5), or `Room Transfer`/`PERM` title prefix (02 §3.1). Pair the A-out and B-in tasks by tenant name and date proximity; classify the pair as one `TRANSFER`.
8. **Retained notices / phantoms:** task in "Retention Success (Cancelled Move Out)" section, or `Retention Successful - Reason` ∈ {"Move Out Cancelled", "Occupant Decided to Cancel the Move Out", "Will Finish The Contract", "Decided to Stay in the Current Room", …} (live enum, Appendix A.5) → `RETAINED_NOTICE`. Move-in with no subsequent trace and quickly superseded by another tenant → phantom, treat as never materialised, caveat it (02 §4.4).
9. **Duplicates:** `[Duplicate]` mark, notice→retraction→re-notice chains, same tenant+room+date on two tasks → keep the canonical task (latest complete one), mark others `DUPLICATE` (02 §4.3, §7.6).

**Tie-breaker order when signals conflict** (apply top-down, stop at first decisive signal):
1. Section membership (Cancelled Sale sections; Retention Success section).
2. Explicit structured fields (`Form Reason`, `Type of Retention Request`, `Break Fee`, `Room Status`).
3. Title-prefix taxonomy (02 §3.1).
4. Comments/stories content (who said what, when).
5. Date heuristics (`due_on`, `created_at`) — weakest; never decisive alone.
If levels 1–2 contradict each other (e.g. Completed section but transfer Form Reason) → read comments (level 4) to adjudicate; still contradictory → L3.

**Tenancy-level `event_class` (deliverable enum).** The task-level classes above collapse to exactly one tenancy-level `event_class` per tenancy row — 09 §1 tenancies.csv uses this enum verbatim:

| `event_class` | Maps from (R1 task-level) |
|---|---|
| `active` | `MOVE_IN_CONFIRMED` with no exit event — still in residence, censored (R4.6) |
| `natural_end` | `NATURAL_END` |
| `early_break` | `EARLY_BREAK` |
| `transfer` | `TRANSFER` pair — ONE tenancy-ending event (room A) + one start (room B); never two separate churn events (R6.3) |
| `cancelled_full_refund` | `CANCELLATION_FULL` |
| `cancelled_partial_refund` | `CANCELLATION_PARTIAL` |
| `cancelled_nonrefundable` | `CANCELLATION_NONREF` |
| `unknown_exit` | `MOVE_OUT_CONFIRMED` whose early/natural subtype is unresolvable |

Rules: `CANCELLATION_*` rows are never occupancy rows — kept for cancellation analysis only (step 3). `STUB_EXCLUDED` and `DUPLICATE` never become tenancy rows. `RETAINED_NOTICE` creates no exit — the tenancy stays `active` until a real exit reclassifies it. **Which wins:** a tenancy's `event_class` = its EXIT classification; entry evidence lives in the date columns (`actual_move_in`, `lease_start`).

**Evidence required.** Every classified event carries: task GID, the deciding signal (section name / field value / comment quote+author+date), and the tie-breaker level used. No event enters a metric without this.

**Edge cases (real, from 02).** Room-label conflict between move-in and move-out forms (Mohd Amaan #1169 vs #1173 — resolve by move-out title + sequence logic, 02 §4.3); reversed transfer with ~1 day occupancy → treat as unoccupied (02 §4.8); retroactive tasks created days after physical move-out — creation date ≠ notice date (02 §4.8); offboarding existing only in Retention (relocations) (02 §4.8); whole-property EOL closures — dates in sibling task names (02 §4.8); unnamed tenant — recover name from the paired task (02 §4.8); back-to-back re-lets of one room are valid, not dupes (02 §4.3).

**Escalate when.** Stub/duplicate judgement call → L1 (state it). Confirmed-by-due-date only → proceed, tag date `UNVERIFIED` if form/comments silent. Contradiction unresolved after comments → L3. A house where >20% of tasks are unclassifiable → L4.

---

## R2. The WHY determination (most important rule)

**Definition.** For every departure, cancellation, or eviction, the *reason* is a separate finding from the *event*. The event can be proven from columns; the reason cannot. NEVER infer a reason from timing alone (e.g. "left 2 weeks after a mould ticket ⇒ left because of mould" is forbidden as a conclusion; it is permitted as a flagged hypothesis).

**Data source — 4-level evidence hierarchy:**
- **(a) Structured fields:** `Move Out Reason` `1207446664940684` (14 live options, Appendix A.1), `Tenant Feedback` `1208971237351877`, `NPS` `1208918493626092` (1–5), `Break Fee` `1209276344420859`, `Retention - Tenant Feedback` `1208971237351879` (rich enum, Appendix A.5) — all on Off boarding team (01 §2, verified live).
- **(b) Asana comments/stories:** `get_task` with `include_comments: true` on the offboarding + cancellation task (02 §4.2 — fetch comments only at this stage, token discipline per 02 §7.1). Record author + timestamp.
- **(c) respond.io thread:** doc 04 §4 method — roster from Asana, `list_contacts` by name, `list_messages`, dates from `messageId // 1_000_000` (04 §3.3); facts-vs-hearsay discipline (04 §4 step 6).
- **(d) Adjacent tasks:** maintenance history for that room/house around the departure (doc 03 method), sibling offboardings in the same house, Tenant Accounts Payables task.

**Procedure.**
1. Exhaust (a): read all four fields. Note: `Move Out Reason` = "I want to provide my move out notice" is the form's default non-answer — it is **not a reason**; treat as reason-absent and continue.
2. Exhaust (b): pull comments on the offboarding (and, for cancellations, the Moving In) task. A staff comment quoting the tenant, or the tenant's form text in notes, counts as first-party evidence. Record who said it and when.
3. Exhaust (c): pull the tenant's respond.io thread across the departure window. Tenant's own messages = fact of what they said; a staff member's summary of what the tenant said = hearsay (04 §4 step 6).
4. Exhaust (d): check maintenance tickets and housemate complaints for the room/house ±60 days. These are **context only** — they corroborate a stated reason or motivate a hypothesis; they never establish the reason alone.
5. Classify (taxonomy in R3) and assign confidence:
   - ≥1 citation from (a) **or** first-party (b)/(c) → **verified reason**.
   - Only hearsay (staff paraphrase, second-hand claims) → **"reported reason (unverified)"** — quote the hearsay and its source.
   - Nothing after a–d → **"reason unknown — evidence absent"**. Do not fill it.
6. If (a) and (b/c) conflict (form says "Relocation", chat says "rent too high"), report both, prefer the tenant's own words (c) for the primary code, flag the conflict.

**Evidence required.** The reason cell in any output carries: reason code + citation (`field:` value, or `comment:` author/date/task GID, or `[id:contactId]` + message date). Classification is not final without it.

**Worked micro-example (illustrative, method from 02 §2 Jun 22 / 04 §9).**
Task: `Room 2, #1443, <address> — <tenant>` sits in "Cancelled Sale - Full Refund". Columns alone ⇒ `CANCELLATION_FULL`, reason unknown.
(a) Moving In has no reason field → nothing. (b) `get_task` comments: staff comment 14 May, "Tenant's visa was refused, approved full refund per <manager>" → first-party staff record of cause. (c) respond.io thread: tenant message 13 May "my visa got denied, I can't come to Australia" `[id:407…]` → first-party confirmation. (d) not needed.
Verdict: `CANCELLATION_FULL`, reason = `personal/visa` — **verified** (b + c cited). Had only the staff comment existed with no tenant message and no field, it would still be verified (level b). Had the only trace been another tenant saying "I heard he got refused", it would be "reported reason (unverified)". Had there been nothing: "reason unknown — evidence absent" — even though the timing (2 weeks before semester) is suggestive.

**Edge cases.** Eviction reasons live in comments/attachment screenshots, not tenant fields — "All move-out date custom fields blank (eviction, not tenant date)" (02 §4.4). Gmail absence ≠ no notice — notices travel via respond.io/PropertyMe/Tenant Care (02 §7.14). Quiet tenants prove nothing (04 §8.8). Attachment URLs expire ~1 hr — read promptly (02 §7.9). Staff-submitted notices ("Who is reporting" = staff) mean the "tenant reason" is already second-hand — max confidence = reported-unverified unless the tenant's own words appear in (c).

**Escalate when.** Reason unknown on a departure that materially drives a house's story → L3. Systematic pattern (e.g. 5+ departures at one house all reason-unknown) → L3 with the pattern named. Conflicting verified reasons that change a recommendation → L3. Never L1 on a reason — reasons are not assumable.

---

## R3. Reason taxonomy (departures & cancellations)

**Definition.** Closed list of reason codes. Every departure/cancellation gets exactly one primary code (+ optional secondary), or `unknown`.

**Data source.** Live `Move Out Reason` enum (Appendix A.1), `Retention - Tenant Feedback` enum (Appendix A.5), categories observed in docs 02 (early-breaks, offboarding investigations) and 04 (chat evidence).

**Procedure — mapping table** (enum values verbatim incl. trailing spaces):

| Code | Maps from Move Out Reason | Also maps from (feedback/chat/prefix) |
|---|---|---|
| `price` | "Found a more affordable option", "Rent Increase" | "Secured a cheaper alternative beforehand", "Rent Increase issue…", "Did not meet the budget" |
| `maintenance_condition` | "Issues with the maintenance of the property ", "Issues with the cleanliness of the property " | "Cleanliness and maintenance issues", "Good Experience - But with issue/feedback with Maintenance", mould/pest chat evidence |
| `house_dynamics` | "Issue with housemates" | "Uncleanliness of the housemates", "ISSUE with the housemate", "Crowded", "Unsafe/uneasy in his accommodation", noise complaints |
| `product_mismatch` | "Looking for a private room/studio", "Looking for a smaller household (with fewer tenants)" | "Room with walls that do not isolate outside noise", "No available property with parking " |
| `relocation_travel` | "Moving to a different city/country", "Relocation for Work/University/College" | "Going back to their Country", "Moving to another City", "Leaving Australia- Moving to another Country", "Overseas Job Transfer", "Will go on a vacation" |
| `personal_financial` | "Moving in with friends/family ", "Visa denied " | "Personal Matter", "Verified move-in with friends or family member", "Taking Leave for Visa Compliance" |
| `evicted_breach` | — (no enum option) | Title prefixes `FOR EVICTION`/`EVICTED`/`FOR NCAT`/`NT …` (02 §3.1); `Type of Retention Request` = "Move Out - Eviction"; "EVICTED/NON-RENEW", "EVICTED", "Theft item"; rent-arrears breach evidence |
| `found_elsewhere` | — | "Found their own place", "Secure an alternative provider before retention" — use when the pull factor is known but the push factor is not |
| `operator_withdrawn` | "Property is being returned to the owner " | `⏰ EOL` prefix (02 §3.1), "Return to Owner", "Agent of the property will take over tenancy", "Poperty return to owner" [sic] |
| `natural_end` | — | Lease completed, no negative signal (R1 NATURAL_END with no other reason) |
| `other_verbatim` | "Other " | Anything real that fits no code — **quote the tenant/staff verbatim** in the reason cell |
| `unknown` | "I want to provide my move out notice" (default non-answer) with no other evidence | Evidence absent after R2 a–d |

**Rules.** (1) Field value maps mechanically per the table, but R2 still applies — a mapped field value is level-(a) evidence, citable as-is. (2) Chat/comment evidence maps by meaning; when in doubt use `other_verbatim` with the quote rather than forcing a code. (3) Secondary code allowed when two verified causes coexist (e.g. `price` + `maintenance_condition`); primary = the one the tenant states first/strongest. (4) Match enum strings **trimmed and case-folded** — several live options carry trailing spaces (Appendix A.1). (5) `operator_withdrawn` and `evicted_breach` are CDA/owner-driven — report them separately from tenant-choice churn in any "why tenants leave" aggregate.

**Evidence required.** Per R2 — code + citation + confidence tag.

**Edge cases.** Retention-feedback enum values that describe the *retention outcome*, not the departure reason ("SUCCESSFUL RELOCATED", "Transferred to another room") — never map these to departure reasons. "Prefer not to provide feedback" / "No response - unable to contact the tenant" → `unknown`, note the refusal. Early break with Break Fee but friendly feedback — break ≠ bad reason; code on evidence.

**Escalate when.** A reason that fits no code and matters → `other_verbatim` + L3 (propose a new code to Kurian; the list only changes with his sign-off). Portfolio-level reason distribution where `unknown` > 30% → L3, flag data-quality issue.

---

## R4. Stay length

**Definition.** Two distinct measures, never blended: **lease term** = `Lease Start Date` → `Lease End Date` (contractual); **actual stay** = actual move-in date → actual move-out date (physical). Report both; deltas between them drive the early-break analysis (02 §2 Jun 11).

**Data source.** Off boarding team fields `Lease Start Date` `1209276344420857`, `Lease End Date` `1206946403745907` (verified live); actual move-in = Moving In task `due_on`/form (02 §3.1); actual move-out = 02 §3.1 priority order; `% of Lease Expired` `1209276344420861` as cross-check; `early_lease_breaks.csv` column schema (02 §4.7) as output template.

**Procedure.**
1. Actual move-in: Moving In task `due_on` (cross-check form text in notes). If no Moving In task in window, use the offboarding task's `Lease Start Date` (this is the sanctioned pre-window reconstruction, 02 §4.2).
2. Actual move-out: apply 02 §3.1 priority strictly — form-stated date > sibling task names > timeline blocks in notes > attachment screenshot > `due_on` (cite which level supplied the date; `due_on` is right ~80% for tenant-form tasks, 02 §7.3).
3. **Conflict rule (which date wins):** if Moving In `due_on` and offboarding `Lease Start Date` both exist and differ — ≤3 days apart → use Moving In `due_on`, L1 note; >3 days → check comments/form; unresolved → use Moving In `due_on`, tag stay `UNVERIFIED`, L3. For move-out conflicts the 02 §3.1 priority order IS the tie-breaker — a higher-priority source always wins; never average dates.
4. Compute days programmatically (R11); validate against `% of Lease Expired` where present (02 §2 Jun 11: math was validated against this field).
5. Missing dates: no resolvable move-in → stay not computable; report event with `UNVERIFIED` dates, exclude from stay averages. No resolvable move-out on a *closed* tenancy → same.
6. **Still-in-residence (censored):** tenant with confirmed move-in and no move-out → stay is censored at the analysis date. Report "tenure to date" in a **separate** column/series; NEVER average censored tenures into completed-stay statistics silently. If a blended figure is ever shown, label it "incl. current tenants (censored)".
7. **Outliers:** (i) data-error outliers — negative stay, or stay <7 days (reversed transfers ~1 day, 02 §4.8): investigate, usually reclassify (transfer/phantom), exclude from averages with a caveat; (ii) statistical outliers per the R10 definition (mean±2σ) — keep in data, flag in narrative.

**Evidence required.** Per tenancy: both date sources named (e.g. "in: Moving In due_on [gid]; out: form text [gid]"), the computed days, and the `% of Lease Expired` check result.

**Edge cases.** Room-label conflict changes which room the stay belongs to (Amaan case, 02 §4.3). Lease renewals (`LR |`) extend one tenancy — do not split one tenant's continuous residence into two stays. Transfers: stay in room A ends at transfer date; tenant-level tenure continues (R6 handles counting). Paid-to date ≠ physical move-out — for non-compliant notices rent liability runs to Paid to Dates while the room may already be empty (02 §4.2); stay length uses the physical date, vacancy economics may use paid-to — never conflate.

**Escalate when.** `% of Lease Expired` contradicts recomputed value by >5pp after recheck → L3. A house where >30% of stays are UNVERIFIED → L4 for that house's stay-length metric.

---

## R5. Vacancy

**Definition.** Per-room vacancy gap = previous tenant's **actual move-out date** → next tenant's **actual move-in date**, in days (02 §4.5). House vacancy = sum of confirmed room gaps in window.

**Data source.** Events from R1/R4; room identity = room code `#NNNN` in task names, regex `#(\d+\.?\d*[A-Za-z]?)` — codes stable per room, unique portfolio-wide (02 §3.1); known-bad Room Code custom-field list (02 §7.5: 1806, 1970, 1990, 423B, 1807→"1810", 821→"816") — task-name regex wins over the custom field; address-collision canonical list (01 §2): 12 Harvey ≠ 7A Harvey; 604 King St Erskineville ≠ 12 Erskineville Rd; 516 ≠ 327 Crown St; 24 ≠ 27 Swan Ave.

**Procedure.**
1. Build each room's event sequence keyed on room code from task names (not the Room Code field); exclude collision addresses explicitly and say so in the output header (03 §7.2).
2. Reconstruct tenancies already in place at window start from pre-window offboarding tasks' `Lease Start Date` (02 §4.2, §4.6).
3. Check internal consistency: out(N) precedes in(N+1); overlaps → resolve per R1 tie-breakers (label conflict, duplicate, transfer) before computing gaps (02 §4.3).
4. Gap per re-let: `next_move_in − move_out` days, computed programmatically (02 §4.5).
5. **Ongoing rule (02 §4.5):** confirmed move-out with no successor move-in → count move-out → analysis date, label **"ongoing"**; include in totals but always show it as its own line.
6. **No-data exclusion (02 §4.5):** rooms with zero events (likely stable long-term tenant) or a move-out followed by silence that cannot be confirmed (350 Marsden R4 ~349 days) → EXCLUDE from vacancy totals, render "no data / needs confirmation" in the caveats panel. The confirmed/unconfirmed split is the audit's credibility (02 §4.5: 581 confirmed vs R4 unconfirmed).
7. Clip gaps at window edges: only in-window days count toward 12-month totals (R11.4).
8. Sanity-check room inventory against `active_properties.csv` room counts (02 §4.1) — missing rooms are findings, not omissions.

**Evidence required.** Per gap: both bounding task GIDs, both date sources (which 02 §3.1 level), day count from the verification script. Per excluded room: why excluded.

**Edge cases.** Open offboarding → uncertain gap start; flag ("Ovi's exact move-out — off-boarding still open", 02 §4.5). Retained notices create no gap (02 §4.4). Cancelled sales create no occupancy, so they never bound a gap — the gap runs to the next *confirmed* move-in (02 §4.4). Phantom move-ins do not close a gap (02 §4.4). "Days Empty" in the portfolio sheet is frozen — never use it to age vacancies (02 §7.12).

**Escalate when.** Room-4-style silence (move-out then nothing for months) → L3 by default; if that room dominates the house's number → L4 for that house ("either ~N days empty or the tenancy was never recorded — need confirmation", 02 §4.8). Inventory mismatch vs active_properties.csv → L3 (file may be stale, 01 §8).

---

## R6. Turnover

**Definition.** Turnover = completed tenancies per room per 12 months (a tenancy "counts" the period it ends in; ongoing tenancies don't add turnover). House-level turnover = **mean** and **max** across the house's in-service rooms — report both (max exposes the problem room the mean hides).

**Data source.** R1 event classes; transfer detection per R1 step 7; window handling per R11.4.

**Procedure.**
1. Count, per room, `MOVE_OUT_CONFIRMED` events (incl. `EARLY_BREAK`, `NATURAL_END`, `evicted_breach`) with in-window move-out dates.
2. **Does NOT count:** cancellations (never occupied — R1 step 3); `RETAINED_NOTICE` (tenant stayed); phantoms; stubs; duplicates; reversed transfers (<7-day occupancy, 02 §4.8).
3. **Transfers count once.** A transfer is one tenant-retention event, not two churn events: at the **room** level, room A records a tenancy end (its room genuinely turned over — it needs re-letting) and room B records a tenancy start; at the **house/entity ("tenant churn")** level, the paired A-out/B-in is ONE `TRANSFER`, excluded from tenant-loss counts. Every turnover table states which basis it uses (room-turnover vs tenant-churn).
4. House-level: mean(room turnover) and max(room turnover) over in-service rooms only (R7 defines in-service). Denominator shown always (R10).

**Evidence required.** Per counted tenancy-end: task GID + classification citation (R1). The reconciliation total (R11.3) must match the sum of per-room counts.

**Edge cases.** Same room legitimately re-let twice in the window = 2 counts, not a dupe (02 §4.3). Tenant leaves and later returns = 2 tenancies. Whole-house EOL closure: room tenancy-ends count as `operator_withdrawn` turnover but are reported separately from tenant-choice churn (R3 rule 5).

**Escalate when.** Transfer pair where only one side is findable → L2 on the pair + L3. Turnover computed on <9 months of in-service days for a room → annualise only with an L1 note ("annualised from N days").

---

## R7. Real occupancy

**Definition.** Real occupancy = occupied room-days ÷ **available** room-days, per room and per house, over the window. "Available" = days the room was in service (offered or occupiable), not calendar days.

**Data source.** Occupied intervals from R4 tenancies; in-service detection from: `⏰ EOL` / return-to-owner series and "For Shutting Down Properties / House Reset" section (02 §3.1 offboarding sections); Maintenance "Close Down / Reset Properties" section `1208130711599327` (03 §3.2); `Type of Retention Request` = "Return to Owner" (live enum); TEMP holding-room status (R1 step 2); `active_properties.csv` Total vs Active Rooms (02 §3.2, provenance UNVERIFIED per 01 §8).

**Procedure.**
1. Per room, sum occupied days (confirmed tenancies, clipped to window; censored tenancies count their elapsed in-window days as occupied).
2. Determine available days: window days minus out-of-service intervals. Detect out-of-service by: (a) property closed/returned (EOL evidence — from the sibling-task series, 02 §4.8); (b) room under reset/renovation (Close Down / Reset section tasks naming the room); (c) room used as TEMP holding room. Detection is evidence-based — no evidence of out-of-service ⇒ room counts as available (conservative: unexplained emptiness shows up as vacancy, not as shrunken denominator).
3. Occupancy = occupied ÷ available; report per room, then house = Σoccupied ÷ Σavailable (not mean of ratios). Show all three numbers (numerator, denominator, ratio) — R10 denominator rule.
4. No-data rooms (R5.6) are excluded from both numerator and denominator, listed in caveats — same exclusion set as vacancy, so occupancy and vacancy reconcile.
5. **Churn-mask flag:** flag any room/house where occupancy ≥ **90%** AND turnover ≥ **3 tenancies/room-year**. High occupancy achieved by rapid back-to-back re-lets is operationally expensive churn masked by a good-looking ratio. Thresholds are **DEFAULTS Kurian can override** — print them wherever the flag is used.

**Evidence required.** Per room: occupied-day sum with tenancy GIDs, out-of-service intervals with the detecting task GID, script-verified arithmetic.

**Edge cases.** Room out of service part-window (reset for 3 weeks between tenants): those days leave the denominator only with cited evidence — otherwise they are vacancy. Whole-house closure mid-window → available days end at closure. Censored tenancy + open offboarding on the same room → use the earlier defensible boundary, tag UNVERIFIED. Occupancy >100% ⇒ overlap error — go back to R5.3, never clamp.

**Escalate when.** In-service status undeterminable for a room whose treatment swings house occupancy >5pp → L3. `active_properties.csv` contradicts task-derived room inventory → L3 (stale-file suspicion, 01 §8). Threshold overrides → only via Kurian (record his values in the kickoff-inputs note, R10).

---

## R8. Maintenance

**Definition.** Per house/room: issue counts by type, severity mix, open vs genuinely-resolved vs denied, resolution time, recurrence.

**Data source.** Maintenance Requests `1204018834894343` (33k+ tasks — always filter, never browse; 03 §3.2). Fields verified live 2026-07-04: `Type of Request` `1204519334409278` (~60 options, Appendix A.4 pointer), `Priority` `1206747551682434` (Appendix A.3 — note trailing spaces), `Maintenance Status` `1210527716102350` = {"Resolved", "Ongoing", "Declined"}, `(General) House Address ` `1204003179103604` (trailing space in field name), `Department` `1210596748119881`, `Who is reporting ` `1206838443377171`. Sections list 03 §3.2 — membership unreliable, use text search (03 §3.2 caution). Method mechanics: 03 §4.

**Procedure.**
1. Pull per 03 §4 steps 0–3 (resolve address, exclude collisions, two-pass search: closed-in-window + open-any-age, minimal opt_fields, deep-read genuine issues only).
2. **Issue typing:** primary = `Type of Request` enum value; fallback = section name; fallback = title keyword. Record which source typed it. Collapse the ~60 raw options into reporting groups (electrical, plumbing/water, gas, appliances/whitegoods, internet, pests, mould/painting, cleaning, security/keys, structural, routine/admin, other) — keep raw value in the evidence column.
3. **Severity mapping** — live `Priority` options verbatim: `"Urgent - 2 days"`, `"High - 3 days "` (trailing space), `"Medium - 5 days"`, `"Low - 10 days "` (trailing space), `"Routine task "` (trailing space). Match trimmed+case-folded; the trailing-space gotcha (03 §3.2) breaks exact-match joins. Null priority → "unset", not "low".
4. **Status:** `completed` flag is the start, the thread overrides (03 §4 step 4). Three buckets: open; closed-genuinely-resolved (completion confirmed in comments/subtask); **closed-as-DENIED/declined ≠ fixed** (auto-closed after 24h tenant silence, or `Maintenance Status` = "Declined") — report these separately and never as resolved (03 §7.4; 7A Harvey bathroom light).
5. **Resolution time:** `created_at` → genuine resolution date (confirmed fix date from thread/subtask; else `completed_at` tagged "completed-at, fix-unconfirmed"). Denied tasks get NO resolution time. **Re-pull live before reporting anything as open** — reports go stale in days (03 §7.9: "open" power outlet had closed 26 days later).
6. **Umbrella/noise exclusion:** monthly `{Address} H1 - {Month Year}` umbrellas, cleaning schedules, bins/lawns/council pick-ups, routine inspections → classify routine/admin, exclude from defect counts, list link-only (03 §4 step 2, §7.6). "H1" meaning UNVERIFIED (03 §9.2).
7. **Recurrence detection:** same reporting group + same room (or same house for common areas) with a new task created within **N = 90 days** (DEFAULT, Kurian-overridable) of the previous task's resolution → recurrence flag; 3+ in window → systemic flag ("worth a full electrical check" pattern, 03 §4 step 5). Dedupe `[dup]` tickets first (03 §7.7).
8. Cross-reference departures: where R3 coded `maintenance_condition`, link the specific tickets (03 §4 step 6 — exits explicitly citing maintenance).

**Evidence required.** Per issue: task GID + permalink (Kurian clicks through — non-negotiable, 03 §1), typing source, status bucket with the overriding comment cited for denied/unconfirmed cases.

**Edge cases.** Long-open ≠ neglected — owner-gated items (`[Bill]`, heritage railing) attributed correctly (03 §7.8). Granny flat / secondary dwelling reported separately within the house (03 §1). Department = "Offboarding" tickets originate from OCR inspections — count them to the house, note origin (03 §8). Empty `memberships` on many tasks (03 §3.2). Room Code custom field mostly null in maintenance — room comes from title suffix/subtask (03 §3.2).

**Escalate when.** Denied task on a safety issue (gas, electrical, smoke alarm, security) → L3 immediately, flagged in-report. Resolution unconfirmable on >30% of a house's closed tickets → L2 on the house's resolution-time metric. N-day recurrence default challenged by results (e.g. seasonal lawn tickets flagged) → L1 adjust reporting group, note it.

---

## R9. Tenant signal

**Definition.** Per house: what tenants are saying, how much, about what, and how CDA responds. Complement to R8 (tickets) — chat evidence in tenants' own words.

**Data source.** respond.io per doc 04: `list_contacts` (name-only search — roster MUST come from Asana first, 04 §4 step 1, §8.1), `list_messages` (newest-first, cursor pagination, dates from `messageId // 1_000_000`, 04 §3.3), channels (main tenant line = "CDA Co Living " id 348751 — trailing space, 04 §3.4), `sender.source` + `broadcastHistoryId`/`workflowId` for attribution (04 §3.3).

**Procedure.**
1. **Locate contacts (04 §4):** Asana roster (Moving In + Off boarding + Retention) → `list_contacts(search: name)` in parallel batches; fallback phone/email from the Asana task (`get_contact("phone:+61…")`); record contact id as citation key `[id:…]`. Custom fields `Room_Details`/`general_address` corroborate only — they go stale after transfers (04 §3.2, §8.2).
2. Pull messages across the window; save long threads to files and Grep (04 §3.3, §8.5).
3. **Theme coding — closed list:** `maintenance`, `cleanliness`, `housemate_conflict`, `noise`, `safety_security`, `payments_bond_refund`, `moveout_notice`, `internet_utilities`, `inspection_access`, `other_verbatim` (quote it). Same discipline as R3 — don't force a code.
4. **Volume + response rate:** per contact and house — incoming count (`sender.source: "contact"`), outgoing human replies (`"user"` + `userId`; resolve agent via `list_users`), response rate = incoming threads that got a human reply, lag = first human reply time − incoming time (messageId-derived, computed programmatically).
5. **Broadcast dedup:** messages with `broadcastHistoryId`/`workflowId` non-null are automation — appear in every housemate's thread; count once as a "CDA → house" event, never as per-tenant traffic, and exclude from response-rate denominators (04 §3.3, §8.4).
6. **Linking messages ↔ maintenance tickets:** link a message to a ticket only when **BOTH** hold: (i) time proximity — message within **±7 days** (DEFAULT) of ticket creation or resolution; (ii) topic match — theme code corresponds to the ticket's reporting group (R8.2). One criterion alone = "possible link", listed but not counted. Linked pairs feed the R2(d) context layer.
7. **Quiet-tenant caveat:** absence of messages ≠ absence of problems (04 §8.8, Nazir case). Never score a room "no issues" from chat silence — state "no chat signal" instead. New tenants may have no history (04 §8.8).

**Evidence required.** Every quoted/coded message: `[id:contactId]` + message date; every volume/lag stat: the counting script + raw file path.

**Edge cases.** "(CDA)" lastName suffixes and spelling drift vs Asana names — retry via phone/email before declaring no-contact (04 §8.7). Multi-channel contacts: annotate by `channelId` (04 §4). `lifecycle`/`tags`/closing notes unused in this workspace — build nothing on them (04 §8.9). Facts-vs-hearsay: a tenant reporting on another tenant is hearsay about the second tenant (04 §4 step 6).

**Escalate when.** Contact unresolvable for a tenant central to a house's story → L2 + L3. Response-rate findings that look reputationally damaging → present with denominators and lag distribution, L3 before any personnel-adjacent conclusion. No messages are ever sent to tenants in CDA-001, under any approval path — 05 §7 governs. respond.io is read-only.

---

## R10. Area read

**Definition.** Comparisons across areas and operating entities (CDA / CLS NSW / CLS VIC …). Valid only on confirmed mappings and sufficient sample.

**Data source.** Candidate entity signal: `Owner` enum on tasks (live options incl. "CDA - Navid ", "CLS NSW - James", "CLS VIC - Navid and James", "KAS - Michael", "Furnished Properties - Navid, James & Johann", "#N/A" — Appendix A.6). Candidate area signals: `CDA Suburbs ` enum `1212884360378495`, `Maintenance Zone ` `1211402698051792` ("Zone 1/2/3 "). None of these is authoritative for the diagnostic.

**Procedure.**
1. **house→entity and house→area mappings are KICKOFF INPUTS.** Obtain the definitive lists from Kurian at engagement start; store them as the canonical mapping table in the project folder. NEVER infer entity or area from suburb alone without confirmation. The `Owner` field may pre-populate a *draft* mapping — every row of that draft goes to Kurian for sign-off before any entity-level number is published (until then all entity cuts are `UNVERIFIED`). Note: `Owner` values observed contradicting geography (7A Harvey St, Parramatta NSW carries Owner "CLS VIC - Navid and James" — live example) — treating Owner as ground truth is exactly the trap this rule blocks.
2. **Minimum-sample rule:** flag (and demote to appendix) any area/entity comparison where **n < 3 houses** or **< 10 room-years** of available room-days. Small-n comparisons are directional at best; say so in the cell.
3. **Outlier definition (one rule, portfolio-wide): beyond mean ± 2σ** of the comparison group. (Decile rule rejected: most cuts here have n < 10 houses, where deciles are meaningless.) State the group, its n, mean, σ next to every outlier call.
4. **Always show denominators:** every rate/ratio in an area table carries its numerator and denominator (room-days, tenancy counts, house counts). No naked percentages.

**Evidence required.** The signed-off mapping table version used; per comparison: n houses, room-years, and the aggregation script.

**Edge cases.** Houses changing entity/status mid-window (return-to-owner) — pro-rate by in-service days and note it. "#N/A" Owner values and multi-dwelling lots (House 2 / Granny Flat variants in the address enum, Appendix A.6) — resolve in the kickoff mapping, not ad hoc. Launceston/VIC addresses in the enum confirm multi-state (01 §5) — do not assume "SYD" covers the portfolio.

**Escalate when.** No kickoff mapping yet → L4 for all entity/area cuts, emitted per the 06 §4 template: `KURIAN BLOCKER: entity/area cuts blocked — no signed-off house→entity/area mapping. Needed to unblock: kickoff mapping sign-off.` Mapping conflict (Owner field vs Kurian's list) → Kurian's list wins; log the conflict to the question-queue (field may be stale/wrong).

---

## R11. Cross-cutting integrity rules

**Definition.** Non-negotiable hygiene applied to every metric above.

**Procedure.**
1. **Traceability:** every intermediate CSV carries an evidence column — task GID(s) + the "how_i_know" source tag per row (convention from the offboarding dataset, 02 §7.3, §4.7). Any number in a deliverable must be reproducible by filtering those CSVs.
2. **Programmatic date math:** all day-counts, gaps, lags, ratios computed via bash/python scripts in the workspace — never mentally (02 §4.5; both audits ran verification scripts before finalising). Keep the scripts with the CSVs.
3. **Reconciliation before reporting:** compare category counts against Asana project totals — live anchors 2026-07-04: Moving In 10,159 tasks (98 incomplete); Off boarding team 5,389 (242 incomplete); Maintenance 33,144 (1,291 incomplete, 03 §3.2). Per house: classified events + exclusions must sum to the pulled task universe; unexplained residue → hunt it before publishing (02 §4.6 step 3: chase mismatches yourself before believing subagents).
4. **Window boundary (12 months):** an event belongs to the window by its **event date** (move-in date, move-out date, ticket created date), not task creation date (retroactive tasks, 02 §4.8). Room-day metrics (vacancy, occupancy) clip intervals at the window edges. Tenancies straddling the start are reconstructed via `Lease Start Date` (02 §4.2) and contribute only in-window days; tenancies straddling the end are censored (R4.6). State the window's exact dates in every deliverable header; the required window record is `data/final/manifest.json` (09 §1).
5. **Re-verification pass:** on request ("recheck"), independently re-fetch every event from source tasks and diff against the built dataset; report a confirmation table (02 §4.6 step 6 — the 350 Marsden second pass matched 14/14).
6. **Freshness:** anything reported as "open"/"ongoing" is re-pulled live at report time (03 §7.9); prior reports are history only.
7. **File discipline:** never overwrite deliverables — new versioned filenames (02 §7.13).

**Evidence required / Edge cases / Escalate when.** Reconciliation residue >2% of a house's tasks after investigation → L3 with the residue listed. Any metric whose script and CSV cannot regenerate the published number → the number is withdrawn, not defended.

---

## R12. Ambiguity ladder & KURIAN BLOCKER protocol

### Ambiguity ladder (condition → action)

| # | Condition | Action (level) |
|---|---|---|
| 1 | Documented default exists (e.g. Mon–Sun weeks 01 §5; due_on-as-move-out ~80% 02 §7.3) | Apply it, print the assumption — **L1** |
| 2 | Date/classification resolvable but evidence chain incomplete (due_on-only date; hearsay-only reason) | Report with **UNVERIFIED** / "reported (unverified)" tag — **L2** |
| 3 | Two evidence sources conflict; comments don't adjudicate | Prefer per-rule tie-breaker; tag UNVERIFIED; queue it — **L2 + L3** |
| 4 | Only Kurian knows (room status never confirmed; "interest" meaning 02 §9.1; threshold overrides; new reason code) | Question-queue, continue around it — **L3** |
| 5 | Gap flips a house-level conclusion (350 Marsden R4-style: "349 days empty OR never recorded") | **L4** for that house/metric |
| 6 | Missing kickoff input (house→entity/area mapping; window confirmation; scope) | **L4** for the dependent analysis |
| 7 | >20% of a house's tasks unclassifiable, or >30% reasons unknown, or reconciliation residue >2% unexplained | **L3/L4** per rule — named data-quality finding, never silent |
| 8 | Temptation to infer reason from timing alone | Forbidden. Downgrade to flagged hypothesis; reason stays `unknown` — no level cures absent evidence |

### KURIAN BLOCKER protocol

- Emit exactly the canonical template (06 §4): `KURIAN BLOCKER: <one-line description>. Needed to unblock: <specific ask>.` — at the top of the deliverable section it blocks and in the chat summary. Emitted by the orchestrator only; sub-agents report `BLOCKED:` upward (08 §8).
- One blocker per decision needed; no bundling. Include the evidence pointers (task GIDs/links) he needs to decide in one click.
- Everything not dependent on the blocker continues; the blocked metric is rendered as "BLOCKED" (not zero, not blank, not an estimate).
- When resolved, record the resolution + date in RUNLOG.md's Decisions field (06 §8) so the same question is never asked twice.

---

## Appendix A — Live-captured enum values (Asana, read-only, 2026-07-04)

Trailing spaces are real and preserved inside quotes — match trimmed+case-folded (R3.4, R8.3).

### A.1 Move Out Reason — Off boarding team, field `1207446664940684` (14 options, verbatim)
1. "I want to provide my move out notice"
2. "Found a more affordable option"
3. "Issue with housemates"
4. "Issues with the maintenance of the property " *(trailing space)*
5. "Issues with the cleanliness of the property " *(trailing space)*
6. "Moving in with friends/family " *(trailing space)*
7. "Moving to a different city/country"
8. "Property is being returned to the owner " *(trailing space)*
9. "Relocation for Work/University/College"
10. "Rent Increase"
11. "Looking for a private room/studio"
12. "Looking for a smaller household (with fewer tenants)"
13. "Visa denied " *(trailing space)*
14. "Other " *(trailing space)*

### A.2 Moving In sections — project `1209877764947329` (verbatim, live)
Submitted Sales · Landing · OPS TASK (for confirmation) · from Custom Build (Hubspot) · Temporary Room · Lease Renewal `1209877767371584` · Pending Lease · Pending Payment · Pending ICR · For Move In · For Move In Confirmation `1209877767371598` · TIMED CODES · Completed `1209877767371600` · New Houses · **"Cancelled Sale - Full Refund"** `1209877767371602` · **"Cancelled Sale - Partial Refund (HD not included)"** `1210434893279203` · **"Cancelled Sale - Non Refundable"** `1209877767371604`.
(Matches 01 §2 / 02 §3.1; "TIMED CODES" and "OPS TASK (for confirmation)" additionally observed live.)

### A.3 Priority — Maintenance Requests, field `1206747551682434` (verbatim, live)
"Urgent - 2 days" · "High - 3 days " *(trailing space)* · "Medium - 5 days" · "Low - 10 days " *(trailing space)* · "Routine task " *(trailing space)*

### A.4 Other maintenance fields (live)
`Maintenance Status` `1210527716102350`: "Resolved" / "Ongoing" / "Declined". `Department` `1210596748119881`: "Sales & Leasing Managers" / "Cleaners " / "Onboarding" / "Offboarding" / "Maintenance". `Area of maintenance` `1206690579510221`: "Common area " / "My room" / "Empty rooms". `Type of Request` `1204519334409278`: ~60 options captured live (Bins … Windows issues | broken glass), several with trailing spaces ("Cleaning ", "Mould issue ", "Routine cleaning ", "Rubbish pick up ", "No water supply ", "Vacuum not working "); full list retained in the pull, collapse per R8.2.

### A.5 Offboarding classification enums (live, load-bearing subsets)
`Form Reason` `1207446664940687`: "I want to provide my move out notice" / "I want to transfer to a different room" / "I want to transfer to a different house".
`Room Status` `1207132850522766`: "Still in the house" / "Already left".
`Move out notice` `1208188466766361`: "4 weeks" / "3 weeks".
`NPS` `1208918493626092`: "1"–"5".
`Type of Retention Request` `1211097732837374` incl.: "Move Out Notice", "Transfer - Occupant Request", "Transfer / Relocation Request", "Temporary  Relocation - Maintenance", "Permanent Relocation - Maintenance", "Move Out - Eviction", "Return to Owner", "Council", "Maintenance Tasks - FYI ".
`Retention Successful - Reason` `1208415868427478` incl.: "Move Out Cancelled", "Occupant Decided to Cancel the Move Out", "Will Finish The Contract", "Decided to Stay in the Current Room", "Permanently Relocated", "Temporarily Relocated", "Transfer to a different room", "Replacement Provided", "Move Out - Evicted", "Move Out - Forfeited", "EVICTED/NON-RENEW", "Retention Unsuccessful - For Move Out" (+ ~13 more Retention Unsuccessful variants).
`Retention - Tenant Feedback` `1208971237351879`: ~55 options captured live (mapped in R3 where relevant — e.g. "Secured a cheaper alternative beforehand", "Found their own place", "EVICTED", "Personal Matter", "Going back to their Country", "Occupant did not disclose reason").

### A.6 Owner (entity candidate) — field `1204054944017779` (verbatim, live)
"CDA - Navid " *(trailing space)* · "CLS NSW - James" · "#N/A" · "KAS - Michael" · "CLS VIC - Navid and James" · "Furnished Apartments - Navid and James" · "Inndeavor" · "Furnished Properties - Navid, James & Johann" · "Furnished Apartments - Navid & James".
Draft signal only — R10.1 makes the mapping a kickoff input. Live counter-example: 7A Harvey St, Parramatta (NSW) task carries "CLS VIC - Navid and James".

## Appendix B — GIDs re-verified live this session (2026-07-04)

| Object | GID | Status |
|---|---|---|
| Off boarding team project | 1206596901916034 | ✅ (task counts 5,389 / 242 incomplete) |
| 2025_Applications/Moving In project | 1209877764947329 | ✅ (10,159 / 98 incomplete) |
| Move Out Reason field | 1207446664940684 | ✅ + full enum |
| Lease Start / Lease End / Submission / Paid to Dates | 1209276344420857 / 1206946403745907 / 1208735103664565 / 1208735103664567 | ✅ |
| % of Lease Expired / Break Fee | 1209276344420861 / 1209276344420859 | ✅ |
| NPS / Tenant Feedback / Room Status / Form Reason | 1208918493626092 / 1208971237351877 / 1207132850522766 / 1207446664940687 | ✅ |
| Cancelled Sale sections (Full / Partial / Non-Ref) | 1209877767371602 / 1210434893279203 / 1209877767371604 | ✅ |
| Priority / Maintenance Status / Type of Request (Maintenance) | 1206747551682434 / 1210527716102350 / 1204519334409278 | ✅ + enums (via task 1214988150299892) |
| Maintenance Requests project | 1204018834894343 | Cited from 03 §3.2 (verified there 2026-07-04); not re-pulled this session |

**UNVERIFIED this session:** "H1" umbrella meaning (03 §9.2); HD = Holding Deposit expansion (01 glossary, inferred); active_properties.csv provenance (01 §8); Mon–Sun week for vacancy WoW (01 §5); respond.io retention cap and channel purposes (04 §10); whether `Sale Status`/`Room Status` on Moving In carry cancellation reasons (fields exist per 02 §3.1 — enum options not pulled; fetch on first use).
