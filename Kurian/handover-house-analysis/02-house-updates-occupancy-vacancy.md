# HANDOVER 02 — House Updates / Vacancy / Occupancy Analysis

**Prepared:** 2026-07-04 · **For:** a brand-new Claude Cowork project with zero prior context
**Owner:** Kurian (kuriandonyku@gmail.com), CDA CoLiving Sydney — co-living property operator
**Everything below is evidence-based.** Sources are cited inline as (file) or (session `local_…`). Anything not directly confirmed is marked **UNVERIFIED**.
**PRIVACY:** Contains real tenant names/IDs tied to sensitive events — internal use only; in NEW outputs prefer first names or `[id:…]` citations.

---

## 1. Purpose & trigger phrases

Kurian periodically asks for a deep, evidence-linked picture of a single house: who lived in each room, when they moved in/out, how long rooms sat empty, why tenants left, and what maintenance/comms context surrounds it. The method is **not** naive date matching — it is deep per-task Asana forensics (task bodies, custom fields, comments, subtasks, attachments), cross-referenced per room, with programmatic date verification and explicit caveats for anything unconfirmable.

Real trigger phrases from transcripts (typos included — Kurian types fast; interpret charitably):

- *"ccan you do an audit for 350 marsden. for the past 12 motnhs.. M only iuntreasted in the tennats movin in and moving out.... ANd how many days it was empty for in a time line format.... for all the rooms there"* (session `local_1791ad26`)
- *"give me a full house audit of 66 boundry Parramatta"* (session `local_2ae5d6b6`)
- *"can you rechcek agai the timelinewswith tteannts"* (re-verification pass, `local_1791ad26`)
- *"i want it in the artificate and if i clicjk on a tenant, i want their move and move out task"* (`local_1791ad26`)
- *"okay can you create another artificate using the same style for 27 swann ave strathfield"* (`local_1791ad26`)
- "give me the updates on this house" / "build me the vacancy/occupancy for the last 12 months for [house]" (paraphrase of the general request family)

Variants of the same workflow family:

| Ask | Output flavour |
|---|---|
| "12-month vacancy/occupancy audit for [house]" | Interactive Gantt-style HTML timeline artifact, per-room, with vacancy day counts and clickable tenant → Asana task links |
| "full house audit / updates on [house]" | Chat report: current move-outs, retention status, maintenance, respond.io comms, action list |
| "house story for [house(s)]" | Markdown/Word doc: 6-month narrative, per-room move-in/out tables with every task link, tiny maintenance section, TLDRs |
| "why is this room vacant / offboarding investigation" | Per-room forensic table: reason, submitter (tenant vs CDA), notice days, "how CDA knows", evidence links |
| "who broke their lease early" | CSV/xlsx of early lease breaks with signed vs actual stay, break fee, move-in + move-out task links |

**Behavioural note:** every session started with `AskUserQuestion` to confirm scope (occupancy-only vs full audit; output format: chat vs file vs artifact) — this matches Kurian's global instruction to ask clarifying questions before assuming scope. Keep doing that.

---

## 2. History & evolution (dated timeline)

Dates from file mtimes in the project folder and session content.

| Date (2026) | Session (title, id) | What happened / what it produced |
|---|---|---|
| **May 15–20** | "Build tenant offboarding dashboard and CSV" (`local_80b25612`), plus related sessions incl. "Find employee move-out dates in Asana" (`local_2a507ff6`, **UNVERIFIED** — not re-read) | The foundational bulk-extraction work: paged 500→850+ tasks out of the Off boarding project into `offboarding-*.csv`, built `offboarding-50-table.html` dashboard and — critically — **`offboarding-recipe.html`**, a self-documenting recipe of the whole method (pagination, opt_fields, where move-out dates live, task-name prefix taxonomy, gotchas). Final enriched CSV: `offboarding-final-v4.csv` (450 rows × 66 cols) with `submitted_by`, `tenant_email_date`, `submission_screenshot_type` columns derived by reading attachment screenshots of tenant emails. Also surfaced the batch-created "stub task" data-quality problem. |
| **Jun 2** | "7a Harvey St maintenance issues" (`local_5f5391b2`) | First single-house deep dive (maintenance-focused): pulled all Maintenance/Offboarding tasks for 7A Harvey St, paraphrased each update thread, excluded the similarly-named "12 Harvey St". Output `7A_Harvey_St_Issues_Mar-Jun_2026.md`. |
| **Jun 11** | "Incomplete lease departures" (`local_2176eed0`) | Early-lease-break analysis: 39 tenants who moved out Mar 11–Jun 11 before lease end. Off-boarding universe filtered to tasks with lease dates/break fee, each matched back to its Moving In task by parallel `search_tasks` calls. Math validated against Asana's own "% of Lease Expired" field. Outputs `early_lease_breaks.csv`, `CDA_early_lease_breaks_Mar-Jun_2026.xlsx`. Follow-up: outlier classification (walked-in-days vs barely-early vs odd terms). |
| **Jun 21** | "Vacancy Sydney listing analysis" (`local_fa784c01`) | Week-over-week vacancy listing comparison from two exports of the **"NEW CDA Rental Portfolio Rep"** Google Sheet ("Vacancies SYD" tab): 313 vs 316 listings, 57 appeared / 54 disappeared, lead-time analysis. Output `Vacancies_SYD_WoW_Analysis.xlsx` (7 tabs incl. Methodology). Key learning: the Vacancies SYD tab is a live FILTER view that exports blank — reconstruct from the "NEW Raw Data" tab (Vacancy Status = Empty/Upcoming, keyed on unique full Room ID). This produced the room lists that fed the next step. |
| **Jun 21–22** | "Room offboarding tasks analysis" (`local_f926363c`) | Offboarding investigations of the rooms surfaced above: first the 10 no-warning vacant rooms, then the 22 upcoming ones, fanned out to subagents (5 rooms each). Per room: reason, submitter (tenant vs CDA), notice→move-out days, "how CDA knows", Gmail cross-check, every Asana link. Outputs `Offboarding_Investigation_10rooms_2026-06-22.md`, `Offboarding_Investigation_22upcoming_2026-06-22.md`. Established: offboarding tasks live in "Off boarding team" — **there is no separate "moveout team" project**. |
| **Jun 23** | "Property management tasks audit" (`local_61c4a8af`) | The "House Story" run: 4 parallel subagents, one per house (327 Crown St, 172 Bronte Rd, 12 Erskineville Rd, 200 Victoria St), each pulling Asana (Onboarding_v2, Offboarding_v2, Off boarding team, Maintenance Requests) + respond.io, 6-month scope, a permalink behind every claim. Then combined into one doc per Kurian's format spec (heavy summary; per-room move-in/out **tables** Event·Tenant·Date·Detail·Link; tiny maintenance paragraph + links; ~25-30-word TLDR per house), converted to Word via pandoc with link-count verification (189 links, 28 tables). Outputs: 4 × `House Story - *.md`, `CDA House Stories - Combined (4 Houses).md/.docx`. Key learning: **Onboarding_v2/Offboarding_v2 were mostly empty for these houses — real move-in/out data lives in "Off boarding team" and the Moving In project.** |
| **Jun 30** | "350 Marsden tenant audit" (`local_1791ad26`) | The canonical 12-month vacancy/occupancy audit (see §8 worked example): 350 Marsden (7 rooms), then re-verification pass, then upgrade to interactive artifact with click-through tenant drawers, then repeat for 27 Swan Ave (8 rooms). Outputs `350_Marsden_vacancy_audit.html`, `350_marsden_vacancy_audit_artifact.html`, `27_swan_ave_vacancy_audit_artifact.html`. |
| **Jun 30** | "66 Boundary Parramatta house audit" (`local_2ae5d6b6`) | Current-state "full house audit" in chat (no file): active move-outs table, maintenance open/overdue, respond.io comm threads, compliance flags, action list. Demonstrated the Asana + respond.io dual-source pattern for "give me the updates on this house". |

Related but distinct: "193 John St offboarding" (`local_08be3e99`, **UNVERIFIED** — not re-read) appears to be another single-house offboarding instance.

**Evolution arc:** bulk CSV extraction (May) → single-house maintenance report (early Jun) → cross-referenced early-break analysis (mid Jun) → sheet-driven vacancy pipeline + per-room forensics (21–22 Jun) → multi-house narrative House Stories (23 Jun) → polished per-room 12-month occupancy timelines as interactive artifacts (30 Jun). Each stage's method notes got reused in the next.

---

## 3. Data sources

### 3.1 Asana (primary source of truth)

- **Workspace:** `cdacoliving.com`, GID **1201789231542521** (verified live 2026-07-04 via `get_project`).
- **Connector:** Asana MCP (read tools used: `search_tasks`, `search_objects`, `get_task`, `get_tasks`, `get_project`, `get_projects`, `get_attachments`). In this machine's config the tools are prefixed `mcp__cf562c96-37b8-469f-a431-051dc4ff0fec__…` — **the UUID prefix is connector-instance-specific and will differ in a new project**; match on the tool-name suffix.

#### Projects (names + GIDs, all verified from live Asana and/or task permalinks)

| Project | GID | Role |
|---|---|---|
| **2025_Applications/Moving In** | `1209877764947329` | Move-ins ("Applications" and "Moving In" are the same project). ~10,157 tasks (99 incomplete) as of 2026-07-04. Task **due date = move-in date**; created/payment date = sale date. |
| **Off boarding team** (note trailing space in the actual name: `"Off boarding team "`) | `1206596901916034` | Move-outs / "Moving Out". ~5,387 tasks (240 incomplete). This is where the Tenant Move Out Notice form lands. **There is no separate "moveout team" project** (confirmed in `Offboarding_Investigation_10rooms_2026-06-22.md`). |
| Onboarding_v2 | `1209578123856239` | Mostly empty for audited houses — do not rely on it (House Story session finding). |
| Offboarding_v2 | `1209628578897032` | Same — mostly empty. |
| Maintenance Requests | `1204018834894343` | Maintenance tickets (used for House Story / full-audit context). |
| Retention Team | `1210587789196546` | Retention/relocation workflow; some move-outs only exist here (e.g. retention relocations). |
| Tenant Accounts Payables | `1206992141381753` | Refunds/charges tasks linked from offboardings. |

Dashboard (used by the sales/move-in CSV skills, not required for house audits): `https://app.asana.com/1/1201789231542521/project/1209877764947329/dashboard/1209877767371577`, chart "Total Move ins for the week" (get-move-ins SKILL.md).

#### Key custom fields — 2025_Applications/Moving In (verified live; GID = field GID)

| Field | GID | Notes |
|---|---|---|
| Room Code (text) | `1209877764947364` | Sometimes wrong — always cross-check against task name (see §7) |
| Tenant Name (text) | `1209877767251639` | |
| Weekly Rent (text) | `1209877767251645` | |
| Full House Address (text) | `1209999213063054` | |
| (General) House Address (enum, **trailing space in name**) | `1204003179103604` | |
| Date and Time Paid (date) | `1209877767266405` | Sale/payment timestamp |
| Agreed Lease Term (enum) | `1209877767294379` | |
| New/Replacement (enum) | `1209877767251651` | |
| Sale Status (enum) | `1210528558933224` | |
| Room Status (enum) | `1209507722216395` | |
| Lease (enum) `1209877767258421`, Payment (enum) `1209877767258431`, Type of Transfer `1211392700936936`, Temporary Room `1211583366110944`, Temporary Room Address `1212684396965170`, Move-in Delayed `1215351268241628`, Sale to Move In (number) `1209877767301045` | | |

Sections (move-in pipeline): Submitted Sales → Landing → … → Pending Lease → Pending Payment → Pending ICR → For Move In → For Move In Confirmation → **Completed**, plus **Lease Renewal** (`1209877767371584`), **Temporary Room**, and the three cancellation sections: **Cancelled Sale - Full Refund** (`1209877767371602`), **Cancelled Sale - Partial Refund (HD not included)** (`1210434893279203`), **Cancelled Sale - Non Refundable** (`1209877767371604`).

#### Key custom fields — Off boarding team (verified live)

| Field | GID | Notes |
|---|---|---|
| Lease Start Date (date) | `1209276344420857` | **= move-in date of the departing tenant** — this is how tenancies that began before the audit window get reconstructed |
| Lease End Date (date) | `1206946403745907` | |
| Submission Date (date) | `1208735103664565` | When the notice was submitted |
| Paid to Dates (date) | `1208735103664567` | For non-compliant notices, rent liability end = often the advertised availability date |
| Earliest Date to Move Out (date) | `1206946403745905` | |
| Days Diff (Submission-Move Out) (number) | `1208735103664577` | Asana-computed notice period |
| % of Lease Expired (text) | `1209276344420861` | Use to validate your own date math (early-break session did exactly this) |
| Break Fee (if applicable) (text) | `1209276344420859` | Presence ⇒ early lease break |
| Move Out Reason (enum) `1207446664940684`, Form Reason (enum) `1207446664940687`, Move out notice (enum) `1208188466766361`, NPS (enum) `1208918493626092`, Tenant Feedback (text) `1208971237351877`, Room Status (enum) `1207132850522766`, Tenant Name (text) `1206596902698023`, Full Property Address (text) `1213022101263920`, Type of Retention Request `1211097732837374`, Retention Contact Status `1208431099493795`, Retention Successful/Unsuccessful reasons, Who is reporting `1206838443377171` | | |

Sections (offboarding pipeline, 24 total): Tenant's Move Out Notices → Retention - Ongoing / For Follow Up → **Retention Success (Cancelled Move Out)** → For Move Out → … → Pending Condition Report → OCR/ICR Done - Check next steps → OCR Done - Needs Cleaning / Needs Maintenance → **For Refund - Pending Charges (💰 HOLD - )** → Pending Bank Details → For Refund → With Issues → **Completed**; plus Termination Notices Sent, For Shutting Down Properties / House Reset, Vacant Rooms Submitted by CdA Team.

#### Task naming conventions

- Canonical pattern: **`Room 4, #653, 12 Erskineville, Newtown — Teri Elaine Hemmert`** — i.e. `Room <n>, #<room code>, <address> — <tenant name>`. Room-code regex used everywhere: `#(\d+\.?\d*[A-Za-z]?)` (get-move-ins SKILL.md). Room codes are unique portfolio-wide (e.g. #1169–#1175 = 350 Marsden Rooms 1–7; #1054–#1061 = 27 Swan Ave Rooms 1–8).
- Title prefixes encode state (offboarding-recipe.html taxonomy): `⏰ EOL` / "returning property to owner" → close-down; `🔴/🟡/🟠/♠️ FOR EVICTION`, `EVICTED`, `FOR NCAT`, `AR EVICTION` → termination; `TERMINATION RETRACTED` (in attachment) → retracted; `Room Transfer`, `PERM`, `TEMP OCR/ICR` → admin, not a real move-out; `⚠️ COUNCIL` → compliance admin; `NT <month day>` → notice to terminate; `[Duplicate]` → cross-reference by tenant name; `LR |` → lease renewal (excluded from sales/move-in reports); `🟡 FOR ICR` → internal prep. Emoji like 👍👍 or ❗ get prepended over time — match on room code, not task name.

#### Where each fact lives (priority order, from offboarding-recipe.html §3)

Move-out date: 1) form text in `notes` — "When are you thinking of moving out: <date>" (most reliable); 2) sibling task names in close-down series; 3) internal timeline blocks in notes; 4) first image attachment (termination/retraction email screenshot — download via signed URL, read as image, look for "TERMINATION DATE:"); 5) fallback `due_on` (accurate for ~80% of tenant-form tasks; otherwise an internal admin deadline — cite the ambiguity).
Move-in date: Moving In task `due_on` / form; or the offboarding task's **Lease Start Date**.
Reason/NPS/feedback: offboarding custom fields + form text in notes.
Confirmations of physical vacancy: task **comments** (e.g. "Room is empty as per Salim").

### 3.2 Google Sheets

- **"NEW CDA Rental Portfolio Rep"** (Sheets id `1D5GEuYWB7BsVHEBQVsggIDLiZspuwXkRBsggu1H40Pk`), tab **Vacancies SYD** (live FILTER view over "NEW Raw Data"; Vacancy Status ∈ {Empty, Upcoming}) — the vacancy listing source used for WoW analysis and to select rooms for offboarding investigations (memory `cda-portfolio-syd-mirror.md`; session `local_fa784c01`). Exports of the FILTER tab come out blank — use the raw-data tab.
- `active_properties.csv` (May 21) — Property Address, Total Rooms, Active Rooms per house; useful to know the expected room count before auditing. Provenance: extracted from the portfolio spreadsheet in a "Get property list from spreadsheet" session (**UNVERIFIED** detail).

### 3.3 Secondary sources for "full house audit" context

- **respond.io MCP** (`mcp__respond-io__list_contacts`, `list_messages`) — tenant WhatsApp/chat threads, house broadcasts, move-out initiations (`local_2ae5d6b6`, House Stories).
- **Gmail connector** — used to check whether CDA-initiated move-outs had a triggering email (finding: they never did; notices go via respond.io/PropertyMe/Tenant Care, so absence in Kurian's inbox ≠ no notice) (`local_f926363c`).
- PropertyMe and Google Drive evidence folders appear **inside** Asana comments/attachments — read them from Asana, no direct connector.

---

## 4. Methodology — step-by-step

### 4.0 Clarify first

Confirm: which house (watch spelling variants), window (e.g. "past 12 months"), scope (move-in/out timeline only vs full audit with maintenance/comms), and output form (chat / file / interactive artifact). Kurian's audits so far: 12-month window, per-room timeline, artifact.

For the "give me updates on [house]" flavour: default window = current open items + last ~8 weeks of events unless the user specifies; re-pull anything reported as 'open' live before reporting.

### 4.1 Pull the house's task universe

1. `search_tasks` with `text: "<address>"` (no completed filter — you need history), across the workspace or with `projects_any` of Moving In + Off boarding team. Try variants: "350 Marsden", "27 Swan Ave" (Kurian wrote "Swann" — Asana has single-n), "12 Erskineville" (also rendered "Erskineville Rd/St", typos "Erskinville/Nowtown").
2. **Exclude near-name collisions explicitly**: 24 Swan Ave ≠ 27 Swan Ave; 604 King St Erskineville ≠ 12 Erskineville Rd; 12 Harvey St ≠ 7A Harvey St; 516 Crown St ≠ 327 Crown St. Canonical address-collision list lives in 01-shared-foundations.md. Multi-room addresses can share a street number with distinct codes (#28–31 at 285 Cleveland St).
3. Derive the room inventory from room codes in task names (e.g. #1169–#1175). Sanity-check against `active_properties.csv` room counts.

### 4.2 Deep per-task extraction (never trust the list view alone)

For each candidate task, `get_task` with **restricted** `opt_fields` (e.g. `name,notes,due_on,created_at,permalink_url,custom_fields.name,custom_fields.display_value,memberships.section.name`) and `include_comments: false, include_subtasks: false` on the first pass — default `html_notes` + comments balloon a single response past the token cap (offboarding-recipe.html §6). Fetch comments/attachments only for tasks where the dates are ambiguous or confirmation matters.

Extract per tenancy event:
- **Move-in:** Moving In task due date; cross-check the form text in notes.
- **Move-out:** form-stated date > due date > Paid-to date (see §3.1 priority list). Note whether the notice was compliant; for non-compliant notices the room's *advertised availability* tracks the **paid-to date**, not the physical move-out (`Offboarding_Investigation_22upcoming`).
- **Lease Start Date on the offboarding task** = that tenant's move-in — this is how you reconstruct tenancies that began *before* the audit window without hunting the old move-in task (`local_1791ad26`: "The off-boarding tasks contain both lease-start and actual move-out dates").

### 4.3 Matching move-outs to move-ins (per room, not per date)

- Build each room's event sequence and check it is **internally consistent**: out-date of tenant N should precede in-date of tenant N+1.
- **Room-label conflicts:** a tenant's move-in form and move-out form can disagree on room code (data-entry error). Resolve by (a) the canonical move-out task title, and (b) sequence logic — which room's timeline only makes sense with that tenant in it. Worked case: Mohd Amaan's move-in said #1169 (Room 1) but move-out said #1173 (Room 5); Room 1 was firmly held by another tenant and Room 5's sequence (Amaan out 26 Sep → Binshaj in 6 Oct) only works with him there → Room 5, move-in task is the error (`local_1791ad26`).
- **Same tenant, multiple tasks** is normal: original notice → retraction/duplicate → new notice; transfers produce paired tasks. Cross-reference by tenant name (offboarding-recipe.html). A room legitimately appearing twice in a period (cancelled then re-sold; back-to-back tenants #1063) is valid data, not a dupe.

### 4.4 Cancellations, transfers, retention, "interest"

- **Cancelled sales** sit in the three "Cancelled Sale - …" sections of Moving In. A cancelled sale means the tenancy never started — do not count it as occupancy (350 Marsden had "a cancelled sale" handled as a caveat).
- **Retention success = cancelled move-out** ("Retention Success (Cancelled Move Out)" section): the tenant stayed; ignore the notice for vacancy purposes but flag it ("a retained move-out notice", `local_1791ad26` caveats).
- **Phantom move-ins:** move-in tasks logged with no matching move-out and quickly superseded by another tenant (Prachi/Efalata at 27 Swan Ave) — treat as never-materialised, keep in caveats.
- **Room transfers** (PERM/TEMP, `Type of Transfer` fields): tenant stays with CDA but changes rooms — a move-out for room A and a move-in for room B; temp rooms (TEMP OCR/ICR) are holding rooms, not real tenancies.
- **Evictions/terminations:** dates live in comments/attachments (Notice of Termination screenshots), not tenant-form fields ("All move-out date custom fields blank (eviction, not tenant date)").
- **"Interest" status:** the term as such was **UNVERIFIED** in the evidence; the closest concepts in the data are the Retention pipeline statuses and the Moving In "Sale Status"/pipeline sections. If Kurian says "interest", clarify whether he means retention interest or sales pipeline.

### 4.5 Vacancy gap detection

- Gap = previous tenant's move-out date → next tenant's move-in date, per room. Count the days.
- **Verify all arithmetic programmatically** (bash/python), never mentally — both audits ran a verification script before finalising (`local_1791ad26`: "Verified — all vacancy day-counts check out").
- **Only count confirmed gaps.** Rooms with no events at all (27 Swan Room 3) or a move-out and then silence (350 Marsden Room 4, ~349 days) are excluded from totals, rendered as "no data / needs confirmation", and put in the caveats panel. This distinction (581 *confirmed* empty room-days vs Room 4 unconfirmed) is central to the audit's credibility.
- Rooms with an off-boarding still open have an uncertain end date — flag ("Ovi's exact move-out in Room 3 — off-boarding still open").
- **Confirmed move-out with no successor move-in:** count vacancy from move-out date to audit date, label "ongoing". Distinguish from "no data" rooms, which are excluded from totals.

### 4.6 Long-window (12-month) builds — the mechanics

1. `search_tasks` text search for the address (both projects) — gives the full multi-year task list; filter events to the window but use pre-window offboarding tasks' Lease Start Date to anchor tenancies already in place at window start.
2. **Delegate bulk per-task extraction to subagents** — pattern used: one agent for the whole house (Marsden, ~15 tasks) or 5 rooms per agent for bigger sweeps (`local_f926363c` — Kurian explicitly asked "make sure you spin of so eaach agent gets 5 rooms to tacle"). Subagents return per-room event tables with GIDs.
3. Reconcile subagent output: chase label mismatches and empty rooms with targeted `search_tasks`/`get_task` yourself before believing them.
4. Programmatic date verification (bash).
5. Build the deliverable (see §4.7).
6. **Re-verification pass on request** ("rechcek"): independently re-fetch every tenant's move-in from source tasks and diff against the built timeline; report a confirmation table (`local_1791ad26` second pass — all 14 move-ins matched).

### 4.7 Output formats

- **Interactive vacancy-audit artifact** (`27_swan_ave_vacancy_audit_artifact.html`, `350_marsden_vacancy_audit_artifact.html`): single-file HTML, 12-month Gantt per room; green = occupied (tenant named), red = empty (day count labelled), hatched = no data; hover = exact dates; click tenant → slide-out drawer with move-in and move-out events, each with "Open in Asana ↗" (links built as `https://app.asana.com/0/0/${taskGid}/f`), copy-link button, and warning notes on flagged cases; summary stats + "Data caveats & flags" panel at the bottom. Delivered via `mcp__cowork__create_artifact` *and* saved to the folder.
- **House Story doc** (combined 4-house doc format Kurian iterated to): per house — heavy summary → per-room **tables** (Event · Tenant · Date · Detail · Link) → comms highlights → *tiny* maintenance paragraph + one-line-per-link list; plus a ~25–30-word TLDR per house delivered as a chat message. Word export via pandoc; verify hyperlink count and table count post-conversion (`local_61c4a8af`).
- **Chat-only full audit** (66 Boundary style): move-outs table, maintenance open/overdue, respond.io recap, "bottom line / what needs a response" action list.
- **Investigation MD reports** (`Offboarding_Investigation_*.md`): summary table + per-room forensic sections with GIDs and links.
- **CSV/xlsx** for cohort analyses (early breaks): columns as in `early_lease_breaks.csv` — tenant, property, room, move_in, lease_end, move_out, signed_term, signed_days, actual_stay, actual_days, left_early_by_days, pct_completed, reason, break_fee, movein_url, moveout_url.

### 4.8 Edge cases actually encountered (checklist)

- Move-in form room code ≠ move-out form room code (Mohd Amaan) → trust move-out title + sequence logic.
- Room with zero events in window (27 Swan R3) → probably stable long-term tenant; exclude from totals, flag.
- Move-out logged, never re-let, no move-in ever (350 Marsden R4) → don't assume vacancy; "either ~349 days empty or the tenancy was never recorded" — ask Kurian to confirm.
- Task raised *after* the physical move-out (retroactive: R4 #101 Bronte +3d, R2 #302 Harris +26d, R10 #1811 Gipps +15d) → creation date ≠ notice date.
- Offboarding exists only in Retention (relocations, R3 #134 Stanmore) or only as TEMP OCR/ICR (holding rooms, R3 #1478) → not genuine offboardings.
- Reversed transfer (~1 day occupancy, R9 #1705 Carlingford) → treat as unoccupied.
- Cancelled/retained notices, phantom move-ins, still-open offboardings → caveats panel, never silently resolved.
- Unnamed tenant on offboarding task → recover the name from the paired move-out/move-in task (Daniel Santiago Bonilla Garcia case, `local_2176eed0`).
- Whole-property closures (EOL series) → move-out dates live in sibling task names.

### 4.9 Single-tenant "why did X leave / break lease early" recipe

1. Find the tenant's offboarding task in "Off boarding team " (`search_tasks` by tenant name and/or room code).
2. Read the **Move Out Reason, Tenant Feedback, NPS, Break Fee, % of Lease Expired** custom fields.
3. Pull respond.io message history for that contact: name search via `list_contacts`; fallback phone/email — NOTE: where phone lives on Moving In tasks is **UNVERIFIED**; Off boarding team has an "Email Address" field.
4. Build a chronological timeline interleaving Asana events + messages.
5. Conclude with a facts-vs-hearsay verdict.

Message-mining detail in 04-respondio-conversations.md §4.

---

## 5. Assets & prior outputs (file inventory)

All under `/Users/stuff/Documents/Claude/Projects/Random CDA stuff/` (sandbox path `/sessions/<name>/mnt/Random CDA stuff/`).

| File | What it is |
|---|---|
| `350_Marsden_vacancy_audit.html` (Jun 30) | First static 12-month Gantt timeline for 350 Marsden St (7 rooms, #1169–1175) |
| `350_marsden_vacancy_audit_artifact.html` (Jun 30) | Interactive artifact version — click tenant → Asana links drawer |
| `27_swan_ave_vacancy_audit_artifact.html` (Jun 30) | Same style for 27 Swan Ave, Strathfield (8 rooms, #1054–1061) |
| `House Story - 12 Erskineville Newtown.md` / `- 172 Bronte Road Waverley.md` / `- 200 Victoria Street Potts Point.md` / `- 327 Crown St Surry Hills.md` (Jun 23) | Per-house 6-month stories: summary, room vacancy timeline table with task links, maintenance log, tenant comms |
| `CDA House Stories - Combined (4 Houses).md` + `.docx` (Jun 23) | Combined doc in Kurian's preferred format (per-room tables, tiny maintenance, 189 task links, 28 tables) |
| `Offboarding_Investigation_10rooms_2026-06-22.md` | Forensics on 10 no-warning vacant rooms: submitter, reason, evidence chain, links |
| `Offboarding_Investigation_22upcoming_2026-06-22.md` | Same for 22 upcoming vacancies (all tenant-initiated) |
| `Vacancies_SYD_WoW_Analysis.xlsx` (Jun 21) | Week-over-week vacancy listing comparison (313→316; appeared/disappeared/transitions + Methodology tab) |
| `early_lease_breaks.csv` + `CDA_early_lease_breaks_Mar-Jun_2026.xlsx` (Jun 11) | 39 early lease breaks, signed vs actual stay, break fees, clickable move-in/out links |
| `offboarding-recipe.html` (May 19) | **The method doc** — recipe for pulling 500+ offboarding tasks, where move-out dates live, prefix taxonomy, gotchas. Read this first. |
| `offboarding-final-v4.csv` (May 18) | 450 rows × 66 cols enriched offboarding dataset (form fields + asana.* custom fields + submitted_by / tenant_email_date / screenshot type) |
| `offboarding-350/450/500/600/650/700/750/800/850-tasks.csv`, `offboarding-merged/slim/clean/final*.csv` (May 15–20) | Incremental raw pulls & merges (9-col raw schema: rank, created_date, moveout_date, days_notice, type, category, task_name, how_i_know, asana_url) |
| `offboarding-50-table.html`, `offboarding-50-latest.html` (May) | Sortable 500-row dashboard + earlier card view |
| `7A_Harvey_St_Issues_Mar-Jun_2026.md` (Jun 2) | Single-house maintenance/issue report |
| `active_properties.csv` (May 21) | Property Address, Total Rooms, Active Rooms — room-count sanity check |
| `BUSINESS_RULES.md` (Jun 26) | Leasing-bot qualification rules; background only (min terms: rooms 3 mo, studios 6 mo; max 2/room; bond 2+2) — useful when interpreting "early break" and couple/extra-occupant flags |
| `CDA_Tenant_Profiles.pdf` (Jun 2) | Tenant profile doc (**UNVERIFIED** relevance) |

---

## 6. Tools & permissions required

1. **Asana MCP connector** (read-only use): `search_tasks`, `search_objects`, `get_task`, `get_tasks`, `get_project`, `get_attachments`. Workspace `cdacoliving.com` / `1201789231542521`. Premium search available (`search_tasks` works). **Never modify Asana** in this workflow.
2. **Folder access:** "Random CDA stuff" attached to the session (Read tool: `/Users/stuff/Documents/Claude/Projects/Random CDA stuff/`; bash: `/sessions/<session>/mnt/Random CDA stuff/`).
3. **Workspace bash** — date arithmetic verification scripts, pandoc for docx, python/openpyxl for xlsx.
4. **Cowork artifacts** (`mcp__cowork__create_artifact`) for interactive timelines; `present_files` for saved files.
5. **Subagents** (Agent tool) for parallel per-room/per-house extraction.
6. **respond.io MCP** — only for "full house audit / updates" flavour (tenant comms context).
7. **Gmail connector** — only when investigating whether a notice/email exists.
8. **Chrome MCP** — *not* needed for house audits. It is required only by the adjacent sales/move-in CSV skills (`get-move-ins`, `get-sales-data`, `get-salesdata-csv` in the skills folder) that read the Asana dashboard chart. Those skills are also the best written reference for Asana fetch mechanics (pagination, opt_fields, room-code regex, bad-Room-Code list).
9. Google Sheets access (via Chrome or Drive connector) — only if the request starts from the Vacancies SYD listing side. **UNVERIFIED:** exact connector used for the Jun 21 exports (files were uploaded exports).

---

## 7. Gotchas & failure modes actually hit

1. **Token bombs from `get_task`** — default `html_notes` + comments can exceed the token cap on a *single* task (80+ KB). Always restrict `opt_fields`, set `include_comments`/`include_subtasks` false unless needed (offboarding-recipe.html; re-hit in `local_2ae5d6b6`: "The full task payloads are huge… re-fetch just the fields I need").
2. **Pagination:** `search_tasks` has **no offset param** — cursor-paginate by setting `created_at_before` to the oldest timestamp of the previous page, `sort_by: created_at`, `limit: 100` (offboarding-recipe.html). `get_projects`/`get_tasks` use `offset` next_page tokens.
3. **`due_on` ambiguity** — for tenant-form offboardings it's the move-out date ~80% of the time; for admin/stub tasks it's an internal deadline. Cite your source per row ("how_i_know" column convention).
4. **Batch-created stub tasks** — sequential-GID empty tasks categorized "Tenant form" with zero form data (64 of 450 in offboarding-final-v4). Filter out: empty name/notes + no due date = Asana glitch/placeholder (`local_80b25612`).
5. **Room Code custom field is unreliable** — known-bad rooms: `1806, 1970, 1990, 423B, 1807 (says "1810"), 821 (says "816")`; fall back to task-name regex (get-move-ins SKILL.md). Also 22-digit "GIDs" = two GIDs concatenated → re-search.
6. **Duplicate/multi-task tenants** — notice + retraction + re-notice, `[Duplicate]` marks, transfer pairs. Dedupe by tenant name, keep the canonical task.
7. **Address spelling variants & collisions** — "Swann/Swan", "Erskinville/Nowtown", "boundry"; exclude 24 Swan Ave, 604 King St Erskineville, 12 Harvey St. Search several variants before declaring "no tasks".
8. **Onboarding_v2 / Offboarding_v2 look authoritative but are mostly empty** — real data is in "Off boarding team" + "2025_Applications/Moving In" (`local_61c4a8af`).
9. **Attachment signed URLs expire (~1 hr)** — download and read promptly; copy to a Read-visible path. The bash sandbox cannot see `/var/folders/...` overflow paths — use the Read tool.
10. **Search flakiness** — some name searches return nothing first try (Semereab case) → retry with name-only or different token combinations; fire independent searches **in parallel** (both the early-breaks session and get-move-ins do 20+ concurrent `search_tasks`/`search_objects`).
11. **Rate limits:** no explicit 429 handling was found in transcripts or skills (**UNVERIFIED** whether limits were ever hit); the mitigations actually used are small batches, restricted opt_fields, and parallel-but-bounded calls.
12. **Vacancies SYD FILTER tab exports blank** — reconstruct from "NEW Raw Data" (Vacancy Status ∈ Empty/Upcoming), key on the unique full Room ID; "Days Empty" is a frozen field — never use it to age vacancies (`local_fa784c01`).
13. **Don't overwrite deliverables** — the mounted folder is effectively append-only from the sandbox (can't delete); write new filenames/versions (offboarding-recipe.html).
14. **Gmail absence ≠ no notice** — staff notices go via respond.io/PropertyMe/Tenant Care, not Kurian's inbox (`local_f926363c`).

---

## 8. Worked example — 350 Marsden St (session `local_1791ad26`, 30 Jun 2026)

**Request:** "audit for 350 marsden. for the past 12 motnhs… only interested in the tenants moving in and moving out… and how many days it was empty for, in a timeline format… for all the rooms."

1. **Clarify** (AskUserQuestion): confirmed source and output shape.
2. **Universe pull:** `search_tasks` for "350 Marsden" → Rooms 1–7 (#1169–#1175); move-in tasks in Moving In, move-outs in Off boarding/Retention.
3. **Probe two tasks** (`get_task`) to locate the date fields: off-boarding tasks carry Lease Start Date (= move-in) *and* actual move-out; move-in tasks carry move-in date.
4. **Delegate extraction** to a subagent → per-room event list with GIDs. Subagent surfaced: Mohd Amaan's room label conflict (move-in says R1, move-out says R5) and Room 4 having *no events*.
5. **Verify anomalies personally:** targeted `search_tasks` + `get_task` on Room 4 (#1172) → single move-out ~16 Jul 2025, no move-in since → major flag, excluded from totals. Confirmed Hoang Le's 2025-10-10 move-out. Resolved Amaan to Room 5 via title + sequence logic.
6. **Programmatic verification** (bash): all gap day-counts recomputed — R1: 135, R2: 37, R3: 87, R5: 93, R6: 118, R7: 111 = **581 confirmed empty room-days**; R4 ~349 *unconfirmed*.
7. **Build & deliver:** Gantt HTML (green/red/hatched, hover dates, caveats panel) → saved + presented; headline findings in chat (longest void R6 118 days; open items: R4 status, Ovi's open off-boarding).
8. **Re-check on request:** second subagent independently re-fetched all 14 move-ins → 100% match; confirmation table posted; Amaan reasoning restated.
9. **Upgrade to artifact:** rebuilt as `mcp__cowork__create_artifact` with click-tenant drawers linking both Asana tasks (`app.asana.com/0/0/<gid>/f`), warnings on flagged tenants (open off-boarding, transfer, cancelled notice, mislabel).
10. **Repeat for 27 Swan Ave** on request: caught "Swann"→"Swan" spelling, excluded 24 Swan Ave, reconstructed 8 rooms largely from off-boarding lease-start dates (sparse move-ins in window), verified 282 confirmed empty days, flagged R3 (no data) and phantom move-ins.

Total effort shape: ~2 subagent dispatches + ~10 direct Asana calls + 2 bash verification runs + 2 artifacts, in one session.

---

## 9. Open questions / UNVERIFIED items

1. **"Interest" status** — the request-writer's term; no Asana field or session usage named "interest" was found. Likely maps to Retention pipeline status or Moving In sale pipeline. Ask Kurian.
2. **Room 4 at 350 Marsden** and **Room 3 at 27 Swan Ave** — real-world status never confirmed by Kurian in the transcripts; audits still carry the caveat.
3. `local_2a507ff6` "Find employee move-out dates in Asana" and `local_08be3e99` "193 John St offboarding" — not re-read; assumed to be earlier/adjacent instances of the same method — accept as unknown; old-project transcripts are unreadable from the new project, do not attempt to verify.
4. Exact provenance of `active_properties.csv` and of the two spreadsheet exports behind `Vacancies_SYD_WoW_Analysis.xlsx` (which connector/manual upload).
5. Rate-limit behaviour of the Asana MCP under heavy parallel search (never explicitly hit in evidence).
6. Whether Kurian wants these audits **scheduled/recurring** — offered multiple times ("monthly house-story refresh", "weekly sweep"), never accepted in the transcripts.
7. The Asana MCP tool prefix (`mcp__cf562c96-…`) will differ in a new project — re-discover via ToolSearch ("asana search tasks").
8. A "2025_Applications" project separate from "2025_Applications/Moving In" does not appear to exist — Applications and Moving In are one project (**verified live**); noted here because the workflow description names them as if separate.
9. No memory file exists for this workflow (memory dir holds only inspection-tracker, SYD-mirror, flatmates, EOD files) — consider writing one after the first run in the new project.
