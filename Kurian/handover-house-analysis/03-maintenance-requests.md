# Handover 03 — Asana Maintenance Requests / House Issues Analysis

_Written 2026-07-04 for a fresh Claude Cowork project. Everything below is evidence-based; sources cited inline. Items that could not be confirmed are marked **UNVERIFIED**._

---

## 1. Purpose & trigger phrases

When Kurian asks for an update, audit, or "story" about a specific house, part of the answer comes from the **Asana "Maintenance Requests" project**: what issues are open, what got fixed, how long things took, and what problems recur. Output is either an in-chat report, a saved `.md` file, or an "issues" section inside a larger per-house document ("House Story" / house audit).

Observed trigger phrasings (verbatim from transcripts):

- "can you look thorugh the maintaince project offboarding projects, and find me everyhting in in the past 3 months for 7a Harvey st, Parramatta .. both the house and granny flats. I want all the task links and what th eupdates... im lokking for issues in the house" (session `local_5f5391b2`, "7a Harvey St maintenance issues")
- "give me a full house audit of 66 boundry Parramatta" (session `local_2ae5d6b6`, "66 Boundary Parramatta house audit")
- Maintenance also appears as a standard section in "House Story" requests (4 houses, docs dated 2026-06-23)

Note his typing style: misspellings and loose addresses are normal ("boundry", "maintaince", "Swann" for "Swan"). Always resolve the property name against Asana before searching (see Gotchas §7).

What he wants in the answer:
- **All task links** (Asana permalinks) — non-negotiable, he clicks through
- Paraphrase of the **update/comment thread** per task, not just the title
- Clear **open vs resolved** split, with dates
- **Recurring problems / patterns** flagged ("Patterns worth flagging" section)
- Granny flats treated as part of the house but reported separately
- Routine/admin tasks (bins, lawns, cleaning schedules) separated from genuine defects

---

## 2. History & evolution (dated)

| Date | Event | Evidence |
|---|---|---|
| 2023-02-22 | Asana "Maintenance Requests" project created (live `get_project`, `created_at`) | Live Asana, verified 2026-07-04 |
| 2026-06-02 | First dedicated run: session **"7a Harvey St maintenance issues"** (`local_5f5391b2`). One-house, 3-month window, maintenance + offboarding projects. Produced `7A_Harvey_St_Issues_Mar-Jun_2026.md` | Transcript + file mtime Jun 2 |
| 2026-06-21/22 | Offboarding investigations (`Offboarding_Investigation_10rooms_2026-06-22.md`, `_22upcoming_`) — adjacent workflow (covered in handover doc on offboarding), but established the subagent-per-room fan-out pattern and confirmed where offboarding tasks live | Files + session `local_f926363c` "Room offboarding tasks analysis" |
| 2026-06-23 | **House Story** format matured: 4 per-house docs + `CDA House Stories - Combined (4 Houses).md` + `.docx`. 6-month scope, multi-source (Maintenance Requests + Off boarding team + Moving In + respond.io), maintenance as a dedicated table per house. **UNVERIFIED which session generated these** — no local session title matches ("house story", house names, "combined" all return nothing in the 601-session list); possibly generated in a Claude Desktop chat or a differently-titled session | Files dated Jun 23; grep of session list |
| 2026-06-30 | Live in-chat **house audit** style: "66 Boundary Parramatta house audit" (`local_2ae5d6b6`) — no file, answer in chat, combines active move-outs + open maintenance + respond.io, ends with "what needs a response" action list. Same day: "350 Marsden tenant audit" / "27 Swan Ave" interactive HTML vacancy artifacts (vacancy-focused, separate handover doc) | Transcripts |

Evolution summary: **single-house file report (Jun 2) → multi-source 6-month "House Story" docs (Jun 23) → fast conversational audits with action items (Jun 30)**. The maintenance-pull mechanics stayed the same throughout; what changed is scope, packaging, and how much respond.io/offboarding context is blended in.

There is **no skill and no memory file** for this workflow (memory dir checked 2026-07-04: only leasing-inspection, portfolio-mirror, flatmates, EOD files). It has been re-derived from scratch each time.

---

## 3. Data sources

### 3.1 Asana workspace
- Workspace GID: **1201789231542521** (appears in every permalink: `https://app.asana.com/1/1201789231542521/project/{project_gid}/task/{task_gid}`)
- MCP server: Asana connector, tools prefixed `mcp__cf562c96-37b8-469f-a431-051dc4ff0fec__*` in the current setup (server ID will differ in a new project — look for the Asana connector). **READ-ONLY use for this workflow.**

### 3.2 Primary project: Maintenance Requests
Verified live 2026-07-04 via `get_project`:
- **Name:** `Maintenance Requests`
- **GID:** `1204018834894343`
- **Scale:** 33,144 tasks total; 31,853 completed; **1,291 incomplete** (as of 2026-07-04). It is one giant shared project for the whole portfolio — you always filter, never browse.

**Sections** (25, live-verified; GID → name):
| GID | Section |
|---|---|
| 1208130450946751 | New request |
| 1208130711599327 | Close Down / Reset Properties |
| 1207272355421848 | Routine Inspections / Council Inspection |
| 1206690056110194 | New Houses |
| 1208015932384622 | OCR Maintenance |
| 1204625269283523 | Plumbing \| Leak \| Hot Water |
| 1204020244776326 | Electrical |
| 1204625269283571 | Internet |
| 1206391365889658 | Gas |
| 1204018835133391 | Appliances \| Kitchenware |
| 1204018834894344 | Cleaning \| Lawn \| Rubbish |
| 1209372975706463 | Cleaning Inspections |
| 1209244361545164 | Routine Cleaning |
| 1211283210054281 | Deep Cleaning |
| 1206460080535291 | Tenant Security |
| 1204625269283524 | Pest Control |
| 1204018835133390 | Furniture Replacement |
| 1206846891606320 | Council Clean Ups \| Bins Issues |
| 1204625269283525 | Repairs \| Installations |
| 1211145040267535 | Painting / Mould |
| 1206295316097022 | Bins |
| 1206771641635406 | Keys and door locks |
| 1206732751760629 | Ready for Invoicing |
| 1204018835133397 | Resolved |
| 1204625269283547 | To Sort |

Caution: section membership is **inconsistent** — in a live search of open 7A Harvey tasks, several tasks had empty `memberships` (no section at all). Do not rely on sections to find a house's issues; use text search. Sections are useful for classifying issue type after the fact.

**Custom fields** (23, live-verified; the load-bearing ones bolded):
| Field | GID | Type | Notes (observed values) |
|---|---|---|---|
| **(General) House Address** | 1204003179103604 | enum | e.g. `7A Harvey St, Parramatta` — canonical property identifier |
| **Type of Request** | 1204519334409278 | enum | e.g. `Electrical (lights, powerpoints)` |
| **Priority** | 1206747551682434 | enum | e.g. `High - 3 days ` (trailing space in option name) |
| **Who is reporting** | 1206838443377171 | enum | e.g. `Other` (also tenant/cleaner) |
| Maintenance coordinator | 1208084968038499 | enum | e.g. `Jhon ` |
| Tenant's Coordinator | 1208084968038504 | enum | e.g. `Angelica` |
| Owner | 1204054944017779 | enum | e.g. `CLS VIC - Navid and James` (landlord entity) |
| Department | 1210596748119881 | enum | e.g. `Offboarding` (routing origin) |
| Maintenance Zone | 1211402698051792 | enum | e.g. `Zone 3 ` |
| CDA Suburbs | 1212884360378495 | enum | e.g. `Parramatta` |
| Room Code | 1209957038228171 | text | mostly null in observed tasks |
| Tenant Name | 1207262863675709 | text | often null |
| Maintenance Status | 1210527716102350 | enum | often null |
| Cost | 1204683472936259 | number | |
| Is this a routine inspection? | 1208004387723930 | enum | |
| Type of Inspectio [sic] | 1204429811032185 | enum | |
| Will be fix by | 1206733248799345 | enum | |
| Area of maintenance | 1206690579510221 | enum | |
| Manager Approval | 1206771554264021 | enum | |
| Email Address | 1207252627982923 | text | |
| Property Manager | 1208050723229487 | enum | |
| Percent allocation / Estimated time | 1205685951153101 / 1203934295521295 | number | |

Full enum option lists were not extracted (**UNVERIFIED** — fetch via `get_project` with `opt_fields=custom_field_settings.custom_field.enum_options.name` if needed; warning: the full project payload is ~90k chars).

**Task naming convention** (verified in live search): `{Address} - {Issue}`, e.g.
- `7A Harvey St, Parramatta - Power Outlet`
- `7A Harvey St, Parramatta - Lawns | Gardening`
- Monthly umbrella tasks: `7A Harvey St, Parramatta H1 - June 2026`, `... H1 - Cleaning Schedules 2026` (recurring pre-created for the whole year; "H1" meaning **UNVERIFIED** — likely House 1 where a lot has multiple dwellings)
- Room usually appears in the title suffix or subtask: `... Power Outlet Repair (Room6)`, or in the description/comments. Room licence codes (`#1313` style) mostly live in offboarding tasks, not maintenance.
- Owner-blocked items get the owner's name bracketed: `[Bill] Kitchen ceiling leak` (House Story 12 Erskineville).

### 3.3 Supporting projects (used alongside maintenance for house reports)
GIDs cited from the House Story docs and offboarding session; the Off boarding team GID also appears in dozens of live permalinks. Not all re-verified live — treat GIDs as reliable (they appear consistently across independent outputs) but re-confirm names on first use:
| Project | GID | Role in house analysis |
|---|---|---|
| Off boarding team | 1206596901916034 | Move-out notices, reasons, NPS, break fees; tenants' own complaints about house condition |
| 2025_Applications / Moving In | 1209877764947329 | Move-ins / re-lets (dates, rent) |
| Retention Team | 1210587789196546 | Retention/relocation and eviction-adjacent tasks |
| Tenant Accounts Payables | 1206992141381753 | Charges/refunds tied to move-outs |
| Onboarding_v2 | 1209578123856239 | Consistently **empty** for the houses checked — House Stories note "no tasks for this house by name" |
| Offboarding_v2 | 1209628578897032 | Also returned no tasks for the checked houses; real offboarding lives in "Off boarding team" |

### 3.4 respond.io (optional corroboration)
House audits blend in respond.io (WhatsApp) threads to corroborate maintenance complaints in tenants' own words (`list_contacts` by name → `list_messages`). See 66 Boundary and House Story docs. Covered in more depth in the house-story/offboarding handover docs.

---

## 4. Methodology — step by step

Reconstructed from the 7A Harvey transcript (`local_5f5391b2`), the 66 Boundary transcript (`local_2ae5d6b6`), the House Story docs, and re-verified live.

**Step 0 — Resolve the property name.**
Run a broad `search_objects` or `search_tasks` on the address fragment first. Purpose: catch (a) Asana's canonical spelling, (b) name-collision properties to exclude. Real examples encountered: `12 Harvey St` ≠ `7A Harvey St`; `604 King St, Erskineville` ≠ `12 Erskineville Rd, Newtown`; `516 Crown St` ≠ `327 Crown St`; `24 Swan Ave` ≠ `27 Swan Ave` (and user wrote "27 Swann"); typos inside Asana itself ("Erskinville", "Nowtown"). Canonical address-collision list lives in 01-shared-foundations.md.

**Step 1 — Pull the maintenance footprint for the window.**
`search_tasks` with:
- `text` = address (e.g. `"7A Harvey St"`)
- `projects_any` = `1204018834894343`
- `created_on_after` = window start (e.g. 3 or 6 months back). Default windows used: **3 months** (7A Harvey) or **6 months** (House Stories). If user says "past X months", window = today − X months.
- Run **twice**: once `completed=true`, once `completed=false` (or omit `completed` — but the transcripts show two passes: closed-in-window, then still-open regardless of age; long-open tasks created *before* the window still matter, e.g. Room 4 Erskineville open since Feb).
- `opt_fields` minimal: `name,created_at,completed,completed_at,due_on,memberships.section.name,permalink_url`. **Do not request `notes`** — the 7A Harvey session's first call blew the token limit because of notes bloat and had to be re-run.

**Step 2 — Filter and classify.**
- Drop collision properties (Step 0 list).
- Split into: (a) genuine house issues/defects, (b) granny flat / secondary dwelling issues, (c) routine/admin — bins, rubbish, lawns/weeding, council pick-ups, monthly `H1 - {Month}` umbrellas, cleaning schedules, routine inspections. Routine items are listed link-only "for completeness" (7A Harvey file §"Routine / admin tasks").
- De-duplicate (duplicate tickets happen, e.g. "Bulk Waste + Red Bin [dup]" 7A Harvey; "Serious water service leak (duplicate)" Erskineville).

**Step 3 — Deep-read each genuine issue.**
`get_task` per issue (7A Harvey session did ~11 `get_task` calls) with comments and subtasks included. From the comment thread extract: who reported, staff back-and-forth (charge-back questions, contractor assignment — names like Jhon, Hakan, Thomas, Angelica recur), tenant messaging, completion confirmation. Subtasks often carry the actual fix (e.g. `Power Outlet Repair (Room6)`, "board-check subtask", "reattach subtask" — 7A Harvey file links both parent and fix subtask). If payloads get huge, re-fetch with reduced fields/comment_limit (66 Boundary session hit this and re-fetched).

**Step 4 — Determine real status.** Open vs closed is the Asana `completed` flag, but the thread overrides it:
- **Closed ≠ fixed:** the 7A Harvey "Bathroom Light" task was closed as **DENIED** (no tenant response in 24h) — never repaired; the report flags it "worth a second look".
- **Open + silent:** "no confirmed completion" is reported as open even when work may have happened (Power Outlet, 7A Harvey).
- Long-open items are usually **owner-gated** (heritage railing, ceiling leak "[Bill]") — say so.
- Reports are snapshots: the 7A Harvey "Power Outlet" (#open on 2 Jun) was completed 2026-06-28 per live Asana. Always re-pull; never trust a prior report's open list.

**Step 5 — Summarize.** Output format used in `7A_Harvey_St_Issues_Mar-Jun_2026.md`:
1. Header: window, source ("Asana — *Maintenance Requests* project (+ Offboarding routing)"), exclusions
2. 🔴 Open/unresolved — per issue: title + room + status, 1-line description with reporter + date, "Updates:" paraphrase, permalink(s)
3. ✅ Resolved (in window) — same shape, with done-date; call out denied-not-fixed
4. 🏠 Granny flat / secondary dwelling section
5. 🧹 Routine/admin — grouped link lists (bins, lawns, monthly umbrellas)
6. ⚠️ Patterns worth flagging — recurrences (e.g. "Electrical recurring... worth a full electrical check"), systemic items (undersized bins), tenant-behaviour items, plus "just outside the window" context items

House Story variant: maintenance is a **table** — `Date (created) | Issue | Area/Room | Status | Resolution / Notes | Link` — with recurring/admin subtasks consolidated into one row, plus an "open as of {date}" line and an Evidence Index of GIDs at the end. Live-audit variant (66 Boundary): short "🛠️ Maintenance — Open / Recently resolved" bullets with due-dates and overdue callouts, folded into an action list ("Overdue kitchen leak (since 10 May) — needs chasing with Jhon").

**Step 6 — Cross-reference (for full house audits/stories).** Pull the same address from Off boarding team (move-out reasons often *are* the maintenance story — "property full of bugs", "issues with the maintenance of the property"), Moving In, Retention, and respond.io. The House Stories explicitly connect exits to maintenance items (Bronte: "tenants leaving explicitly citing maintenance").

**Parallelization:** for multi-room/multi-house jobs, dispatch subagents (one per room, or 5 rooms each — offboarding session `local_f926363c`) with TaskCreate tracking, then verify their date math before compiling.

---

## 5. Assets & prior outputs

All under `/Users/stuff/Documents/Claude/Projects/Random CDA stuff/` (workspace mount: `/sessions/<session>/mnt/Random CDA stuff/`):

| File | What it is |
|---|---|
| `7A_Harvey_St_Issues_Mar-Jun_2026.md` | Canonical single-house maintenance report (2 Jun 2026); the format template for §4 Step 5 |
| `House Story - 12 Erskineville Newtown.md` | 6-month house story; richest maintenance table + Evidence Index + Data gaps section |
| `House Story - 172 Bronte Road Waverley.md` | Ditto — maintenance-driven-churn narrative |
| `House Story - 200 Victoria Street Potts Point.md` | Ditto — pest crisis + leaks + which projects returned nothing |
| `House Story - 327 Crown St Surry Hills.md` | Ditto — ~24 maintenance items, open-issues list |
| `CDA House Stories - Combined (4 Houses).md` / `.docx` | Merged deliverable (23 Jun 2026); header lists all source projects |
| `Offboarding_Investigation_10rooms_2026-06-22.md`, `Offboarding_Investigation_22upcoming_2026-06-22.md` | Adjacent offboarding deep-dives (see offboarding handover doc) |
| `350_marsden_vacancy_audit_artifact.html`, `27_swan_ave_vacancy_audit_artifact.html` | Interactive vacancy artifacts (adjacent; vacancy handover doc) |
| `CDA_early_lease_breaks_Mar-Jun_2026.xlsx` | Early-lease-break analysis (adjacent; maintenance is a common break reason) |

`BUSINESS_RULES.md` contains **no** maintenance rules (grep verified). `MASTER_PLAN.md` — no maintenance-workflow section found. `CDA_Tenant_Profiles.pdf` is tenant-demographics, not maintenance (**UNVERIFIED in detail** — skimmed by filename/context only).

---

## 6. Tools & permissions required

1. **Asana MCP connector** (read-only usage): `get_projects`, `get_project`, `search_objects`, `search_tasks` (Premium full-text search — this workspace has it), `get_task`. Never `update_tasks`/`create_tasks`/`add_comment` in this workflow.
2. **Write / Edit / present_files** — to save the `.md` report into "Random CDA stuff" and surface it as a card.
3. **respond.io MCP** (optional, for audits): `list_contacts`, `list_messages`.
4. **TaskCreate/TaskUpdate + Agent (subagents)** — for multi-room fan-outs.
5. Folder access to `Random CDA stuff`.

---

## 7. Gotchas & failure modes (all actually encountered)

1. **Token-blowout on `search_tasks`** — including `notes` in results made the first 7A Harvey query exceed limits; re-run with minimal `opt_fields`. Same for `get_project` with sections (90k chars → saved to overflow file) and `get_task` full payloads on comment-heavy tasks (66 Boundary session re-fetched with reduced fields).
2. **Property name collisions** — 12 Harvey vs 7A Harvey; 604 King St Erskineville vs 12 Erskineville Rd; 516 vs 327 Crown St; 24 vs 27 Swan Ave. Always exclude explicitly and say so in the report header.
3. **Spelling drift** — user typos ("boundry", "Swann") *and* Asana-internal typos ("Erskinville", "Nowtown"). Search loose fragments; confirm canonical spelling before filtering.
4. **Closed-as-denied looks resolved** — tasks auto-closed after 24h tenant silence were never fixed (7A Harvey bathroom light). Read the last comments before calling something resolved.
5. **Sections unreliable, custom fields patchy** — many tasks have no section; `Room Code`/`Maintenance Status`/`Tenant Name` often null. The task **title** is the primary key for property; `(General) House Address` enum is the backup.
6. **Recurring umbrella noise** — pre-created monthly `H1 - {Month} {Year}` tasks and cleaning schedules for the whole year pollute "open tasks"; classify as routine, don't report as defects.
7. **Duplicates** — same issue logged twice (bins, leaks); consolidate and mark `[dup]`.
8. **Long-open ≠ neglected** — several are owner-gated (heritage railing, "[Bill]" ceiling leak); attribute correctly or the report unfairly blames ops.
9. **Reports go stale fast** — 7A Harvey's "open" power outlet closed 26 days later. Re-pull live; use prior reports only for history/pattern context.
10. **Onboarding_v2 / Offboarding_v2 are dead ends** for these houses — don't waste calls; use Off boarding team + Moving In (House Story data-gap notes, 12 Erskineville & 200 Victoria).
11. **Comments are mention-heavy** — Asana profile URLs inline; paraphrase, don't quote raw. Anonymize to first names in outputs where possible.
12. **Move-out dates are tenant-stated intentions**, not OCR-verified (12 Erskineville data-gaps) — matters when correlating maintenance timelines with vacancies.

---

## 8. Worked example — 7A Harvey St, Parramatta (reproducing the 2 Jun 2026 report)

1. `search_objects` / `search_tasks` for "Harvey St" → two properties found; exclude `12 Harvey St`. Canonical: `7A Harvey St, Parramatta` (+ granny flat = Room 8).
2. `search_tasks(text="7A Harvey St", projects_any="1204018834894343", created_on_after="2026-03-02", opt_fields=minimal)` — completed pass + open pass. Also search the Off boarding team project (`1206596901916034`) since issues get logged from offboarding inspections (the Power Outlet was reported by Drea Barcebal via Offboarding; its `Department` field = `Offboarding`).
3. ~11 × `get_task` on the genuine issues (skip bins/lawns/umbrellas). Example task shape (live-verified 2026-07-04, `gid 1214988150299892`):
   - Name: `7A Harvey St, Parramatta - Power Outlet`; project `Maintenance Requests`, section `Resolved`; assignee Jhon; created 2026-05-21; due 2026-06-04; completed 2026-06-28.
   - Custom fields: Type of Request = `Electrical (lights, powerpoints)`; Priority = `High - 3 days`; House Address = `7A Harvey St, Parramatta`; Who is reporting = `Other`; Department = `Offboarding`; Maintenance Zone = `Zone 3`; CDA Suburbs = `Parramatta`; Owner = `CLS VIC - Navid and James`.
   - Subtask: `7A Harvey St, Parramatta - Power Outlet Repair (Room6)`.
   - Comments: Andrea asks if tenant-caused (chargeback); Jhon asks ground team to refit cover + tenants told to stop using it; Angelica confirms tenant message sent; 28 May Andrea chases completion + invoice; 2 Jun Thomas assigned for Thursday.
4. Classify: 3 open issues, 6 resolved (1 of them denied-not-fixed), 2 granny-flat, ~13 routine/admin.
5. Write `7A_Harvey_St_Issues_Mar-Jun_2026.md` in the §4 Step 5 format, incl. "Patterns worth flagging" (recurring electrical; undersized red bin recommended twice) and just-outside-window context (Feb fridge, moisture, internet).
6. `present_files` + a short chat summary leading with open items and the biggest signal.

---

## 9. Open questions / UNVERIFIED items

1. **Which session generated the House Story docs (23 Jun 2026)** — not found among 601 local session titles; method is fully recoverable from the docs themselves (each lists sources, GIDs, and data gaps), but the original prompt wording is unknown — accept as unknown; old-project transcripts are unreadable from the new project, do not attempt to verify.
2. **"H1" in umbrella task names** — presumed "House 1"; not confirmed.
3. **Enum option lists** for Type of Request / Priority / House Address etc. — not extracted (payload size); fetch on demand.
4. **Supporting-project GIDs** (§3.3) — consistent across many documents/permalinks but only Maintenance Requests (1204018834894343) and the example task were re-verified live this session.
5. **Whether Kurian wants a fixed cadence** (weekly per-house sweep) — at the end of the offboarding session Claude offered "a weekly scheduled run of this whole sweep"; no evidence he accepted. All runs so far are ad-hoc.
6. **CDA_Tenant_Profiles.pdf** relevance — assumed unrelated to maintenance; not read page-by-page.
7. **No skill / memory entry exists** for this workflow (verified: memory dir has none). A new project should consider creating one; until then this doc is the only persistent record.
