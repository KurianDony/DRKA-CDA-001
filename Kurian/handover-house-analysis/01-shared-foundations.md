# 01 — Shared Foundations (CDA House-Analysis Handover)

**Generated:** 2026-07-04, from the "Random CDA stuff" Cowork project. Read this before docs 02–04.
Everything below was verified live on 2026-07-04 unless marked **UNVERIFIED**.
All external systems are **READ-ONLY** for these workflows unless Kurian explicitly says otherwise.

**PRIVACY:** these docs contain real tenant names/IDs tied to sensitive events — internal use only;
when producing NEW outputs, prefer first names or `[id:…]` citations.

---

## 1. What CDA CoLiving is

CDA CoLiving is a Sydney-based co-living operator (multi-state footprint — not Sydney-only) renting
furnished rooms and studios in shared houses to students and young professionals, all-bills-included.
The user, **Kurian** (kuriandonyku@gmail.com; Asana identity "Kurian Kurichieal", lm1@cdacoliving.com),
runs analysis/automation workflows on top of the company's Asana workspace, respond.io messaging,
Google Workspace and internal spreadsheets. This handover pack covers three analysis workstreams:
house updates / occupancy & vacancy (doc 02), maintenance requests (doc 03), and respond.io
conversations (doc 04).

### Glossary

- **OCR** = Outgoing Condition Report (move-out inspection)
- **ICR** = Incoming/Ingoing Condition Report (move-in inspection)
- **HD** = Holding Deposit *(inferred)*
- **TC** = Tenant Coordinator (matches the "Tenant's Coordinator" Asana field)
- **CR** = Credit/Charge entry *(inferred — verify contextually)*

## 2. Asana environment reference

**Connector:** Asana MCP, tool prefix in the old project `mcp__cf562c96-37b8-469f-a431-051dc4ff0fec__*`
(prefix will differ in a new project — it's per-connection). Authenticates as
**Kurian Kurichieal, lm1@cdacoliving.com, user GID `1208280814774236`**.

**Workspace GID: `1201789231542521`** (the only workspace on this account).

### Key projects (verified via live search 2026-07-04)

This table is the **canonical project list** — the project tables in docs 02–04 defer to it.

| Project | GID | Used for |
|---|---|---|
| **2025_Applications/Moving In** | `1209877764947329` | Move-ins / sales pipeline. One task per application; the get-move-ins / get-sales-data skills run off it. |
| **Off boarding team** (note trailing space in Asana name) | `1206596901916034` | THE live offboarding/move-out project — all offboarding CSVs and vacancy-audit task lookups came from here. There is **no** separately named "Moving Out"/"moveout team" project. |
| **Maintenance Requests** | `1204018834894343` | All maintenance tasks (7A Harvey analysis, doc 03). |
| **Onboarding_v2** | `1209578123856239` | Mostly empty for audited houses — do not rely on it (doc 02 finding). |
| **Offboarding_v2** | `1209628578897032` | Secondary offboarding project; referenced in offboarding investigations. Also mostly empty for audited houses. |
| **Retention Team** | `1210587789196546` | Early-lease-break / retention tasks; offboarding tasks are sometimes cross-linked here. |
| **Tenant Accounts Payables** | `1206992141381753` | Refunds/charges tasks linked from offboardings. |
| 2023-2024_Applications/Moving In | `1203876611687048` | Historical move-ins only. |
| Duplicado de 2025_Applications/Moving In | `1210195775668505` | A duplicate — do NOT use. |

### Moving In project internals (from the get-move-ins / get-sales-data skills)

- Dashboard URL: `https://app.asana.com/1/1201789231542521/project/1209877764947329/dashboard/1209877767371577`
- "Room Code" custom field GID: `1209877764947364`
- Section GIDs: Lease Renewal `1209877767371584` · Cancelled Sale – Full Refund `1209877767371602` ·
  Cancelled Sale – Partial Refund (HD not incl.) `1210434893279203` · Cancelled Sale – Non Refundable
  `1209877767371604` · Completed `1209877767371600` · For Move In Confirmation `1209877767371598`

### Off boarding team custom fields (sampled from live project)

Tenant Name, Email Address, Bond Held, CR Charges, Earliest Date to Move Out, Lease Start Date,
Lease End Date, Submission Date, Paid to Dates, Deadline for Replacement,
Days Diff (Submission–Move Out), % of Lease Expired, Break Fee (if applicable), Estimated time.
(Full custom-field dump is ~97 KB — re-pull with `get_project` when needed.)

### Conventions

- **Task naming (offboarding):** `Room <n>, #<room code>, <street address>, <suburb>` —
  e.g. `Room 5, #1839, 216 Burnett St, Parramatta`. The `#NNNN` is the **room code** — stable per
  room and unique portfolio-wide (see doc 02 §3.1) — **NOT** a tenant/contract number. The tenant
  name is appended after the address with a comma OR an em dash (varies), and tasks may carry
  emoji prefixes — e.g. `🔴 Room 5, #1839, 216 Burnett St, Parramatta, Oliver Owain Shute`.
- **Address collisions (canonical list — docs 02 §4.1 and 03 §4 defer here):** exclude explicitly
  when searching: 12 Harvey St ≠ 7A Harvey St (Parramatta); 604 King St, Erskineville ≠
  12 Erskineville Rd, Newtown; 516 Crown St ≠ 327 Crown St (Surry Hills); 24 Swan Ave ≠ 27 Swan Ave
  (Strathfield — Kurian sometimes types "Swann"; Asana has single-n "Swan").
- Task permalinks follow `https://app.asana.com/1/<workspace>/project/<projectGid>/task/<taskGid>`.
- Teams exist for Leasing Department, Maintenance Team, Offboarding Team, Property Managers, etc. —
  rarely needed; projects above are the entry points.
- `search_objects` is flaky on partial names (e.g. "Moving Out", "Vacan", "House" return nothing) —
  prefer the GIDs above; when hunting a new project try several name fragments.

## 3. Connector inventory & required permissions

Connect in the new project, roughly in this order:

1. **Asana** (essential — docs 02 & 03). Sign in as lm1@cdacoliving.com. Read-only usage.
2. **respond.io** (essential — docs 02 & 04). Tool prefix `mcp__respond-io__*`. Channels verified live:
   | ID | Name | Source |
   |---|---|---|
   | 390890 | CDA House Updates | whatsapp_business |
   | 373819 | Andres - Your CDA Coliving Assistant | whatsapp_business |
   | 373392 | Sofia - CDA | whatsapp_business |
   | 357318 | Telegram | telegram |
   | 348751 | CDA Co Living | whatsapp_business |
   | 348479 | Website Chat | webchat |
   "CDA House Updates" (390890) is the channel behind the house-updates workflow (doc 02/04 detail).
   Note trailing spaces in channel names: `"CDA Co Living "` (348751) and
   `"Andres - Your CDA Coliving Assistant "` (373819) both carry a trailing space in the actual
   name — exact-match lookups must include it.
   The MCP has write tools (send_message, update_contact…) — do not use them; read-only.
3. **Folder access** to `Random CDA stuff` (or a new project folder seeded with the files in §4).
4. **Google Drive** (useful — portfolio spreadsheets, House Story sources). Old prefix `mcp__cb093ea3-*`.
   Key sheets: "NEW CDA Rental Portfolio Rep" (id `1D5GEuYWB7BsVHEBQVsggIDLiZspuwXkRBsggu1H40Pk`,
   Vacancies SYD tab) and "CDA Property Portfolio" (id `1_n6xk_PqbCXEkQqBQ-5iixEU5vPZ2-6g8dttPqKO6SA`).
5. **Gmail** (occasional — offboarding cross-checks used Gmail evidence). Old prefix `mcp__442284e6-*`.
6. **Google Calendar** (only if the inspection tracker ever moves — not core to these three workstreams).
   Old prefix `mcp__e745585e-*`.
7. **Claude in Chrome** (fallback for anything without an API, e.g. Asana dashboard charts).

Present in the old project but NOT needed for this handover: HubSpot, Supabase, Vercel,
Cloudinary-style asset MCP, iMessage/Apple Notes/Mac control (those serve the Flatmates bot,
G2 pipeline and listings workstreams that stay behind).

## 4. File/folder conventions

- Read/Write tool path (host): `/Users/stuff/Documents/Claude/Projects/Random CDA stuff/`
- bash (Linux workspace) path in the old project: `/sessions/eager-hopeful-pascal/mnt/Random CDA stuff/`
  (session-specific — a new project gets a different mount name; same folder underneath).

### Files that belong to the three handover workstreams (move/copy to new project)

**Occupancy / vacancy / house updates (doc 02):**
- `350_Marsden_vacancy_audit.html`, `350_marsden_vacancy_audit_artifact.html`,
  `27_swan_ave_vacancy_audit_artifact.html` — per-house vacancy audit outputs (Jun 30)
- `Vacancies_SYD_WoW_Analysis.xlsx` — week-over-week vacancy analysis
- `House Story - 12 Erskineville Newtown.md`, `House Story - 172 Bronte Road Waverley.md`,
  `House Story - 200 Victoria Street Potts Point.md`, `House Story - 327 Crown St Surry Hills.md`,
  `CDA House Stories - Combined (4 Houses).md` / `.docx`
- `CDA_Tenant_Profiles.pdf`, `active_properties.csv`
- Offboarding extracts: `Offboarding_Investigation_10rooms_2026-06-22.md`,
  `Offboarding_Investigation_22upcoming_2026-06-22.md`, `offboarding-recipe.html` (the extraction
  recipe), `offboarding-final-v4.csv` (the enriched 450-row × 66-col dataset — doc 02 relies on it),
  `offboarding-850-tasks.csv` (largest/latest cumulative raw pull; the other
  `offboarding-*-tasks.csv` and `offboarding-final*/slim/merged/clean` files are earlier iterations —
  keep only if you want history)
- Early lease breaks: `early_lease_breaks.csv`, `CDA_early_lease_breaks_Mar-Jun_2026.xlsx`
- `BUSINESS_RULES.md` — Flatmates-bot scoped, but doc 02 uses its commercial facts (lease terms,
  bond, occupancy limits) when interpreting early breaks; see §5

**Maintenance (doc 03):**
- `7A_Harvey_St_Issues_Mar-Jun_2026.md` (note inside it: "12 Harvey St" is a *different* property)

**respond.io conversations (doc 04):** no large local artifacts — the workflow lives in the connector.

### Files that STAY in the old project (do not copy)

- `Flatmates-Bot/`, `templates/`, `flatmates-chats/`, `flatmates-profile-prefill*`, `backtest/`,
  `business-rules/`, `age-cutoffs/`, `JC/`, `Janet/`, `template-crosscheck/`, `QUALIFYING_QUESTIONS.md`,
  `TEMPLATE_PHASE_MAP.md`, `PHASE_QUESTIONS.md`, `BOT_LUCA.md`, `MASTER_PLAN.md`, `HANDOFF_PROMPTS.md`
  — all Flatmates leasing-bot build
- `EOD_LeadGen_*` (csv/xlsx/html), `eod_data.json` — EOD lead-gen extract + dashboard
- `listings/` — listings workstream
- `inspections_detail_*.csv`, `week_*_inspector_performance.csv`, `_inspect*.py`, `_run_jun1_7.py`,
  `cda-performance-checks-951c12a2ef49.json` (Google service-account key for the Sheets API) — weekly
  inspection tracker
- `lead_meta_analysis.html`, `lead_ml_categories.html`, `lead_progressive_model.html`,
  `flatmates-chat-extractor-review.html` — Flatmates analysis
- `scripts/`, `costs/`, `faqs/` — misc other workstreams
- G1/G2 market data lives outside this folder (skills + their own data dirs) — unrelated.

## 5. Business rules relevant to these workflows

Caveat: `BUSINESS_RULES.md` (confirmed by Kurian 2026-06-20) is scoped to the **Flatmates bot**, but
these commercial facts are house-wide and matter when reading occupancy/vacancy data:

- **Rent is weekly, all-bills-included** (FL: electricity, water, Wi-Fi, gas; studio: electricity, water, Wi-Fi).
- Extra person in same room: **+$80/wk private room, +$50/wk studio**; max 2 per room, 1 is standard.
- **Bond = 2 weeks bond + 2 weeks rent in advance.**
- **Min lease: rooms 3 months, studios 6 months.** No pets; no children; tenants are students/young professionals.
- **10-day window rule:** max 10 days between inspection and move-in; for an upcoming (not-yet-vacant)
  room the window starts 10 days after it becomes empty. Rent starts after the 10-day period.
  Vacancy audits use "avail date − today" style day counts against this.
- **Multi-state:** CDA is not Sydney-only.
- **+$20 markup convention:** the "CDA Property Portfolio" public mirror shows Advertising Rent +$20
  over the internal "Vacancies SYD" source (hidden SYD_source sheet does the markup). When comparing
  rents, know which sheet a number came from.
- Advertising Rent source of truth: column Z ("Advertising Rent") of the **NEW Raw Data** tab in the
  CDA Rental Portfolio sheet; address = column B, room number = column E (per pick-up-room /
  get-advertising-rent skills).
- **Week definition:** operational weeks run **Monday–Sunday** (used by the inspection tracker and
  weekly reports). **UNVERIFIED** whether every vacancy WoW analysis used Mon–Sun, but assume it.
- Room/task naming: see §2 conventions (`Room <n>, #<id>, <address>, <suburb>`).

## 6. Memory entries to port

Current auto-memory (6 entries) is mostly about workstreams that stay behind. For the new project:

- **Port (recreate):** `cda-portfolio-syd-mirror.md` — Vacancies SYD → CDA Property Portfolio
  IMPORTRANGE mirror with hidden +$20 markup, incl. both spreadsheet IDs. Directly relevant to
  vacancy analysis.
- **Do not port:** `leasing-inspection-tracker.md`, `flatmates-chat-archive.md`,
  `flatmates-meta-analysis.md`, `flatmates-templates-project.md`, `eod-leadgen-extract.md`.
- **Create new memories** in the new project as the 02–04 workflows are first run: Asana GIDs table
  (§2), respond.io channel IDs (§3), and the file inventory (§4).

## 7. Related skills

Installed skills (in the old project's `.claude/skills/`) that touch these workflows — copy if the
new project will run the same pipelines, otherwise just keep this doc's GID tables:

- `get-move-ins` — Moving In tasks by **due date** → 37-column CSV. Contains the GID tables in §2.
- `get-sales-data` / `asana-weekly-sales-report` (near-duplicates) — weekly move-in sales CSV by
  creation/payment date.
- `get-salesdata-csv` — CSV-export variant with Chrome dashboard cross-check.
- `get-advertising-rent` — enriches a move-in CSV with Advertising Rent from the portfolio sheet.
- `pick-up-room` — single room price+photos bundle (portfolio sheet column mapping documented there).

Not relevant (leave): cda-weekly-inspections, dashboard-v2, markell-mich-report-data, all flatmates-*,
g1a/g1b/g2-*, market-data-fetcher, plus generic doc/pdf/xlsx/pptx skills (reinstall generics as needed).

Note: none of the installed skills cover the three handover workflows themselves — vacancy audits,
7A-Harvey-style maintenance digests and respond.io analysis were done ad hoc in sessions. Docs 02–04
are the only procedure record.

## 8. UNVERIFIED items

- **respond.io auth identity / workspace name** — list_channels works but which respond.io user the
  token belongs to was not checked (no get_me equivalent tried).
- Whether "Offboarding_v2" (`1209628578897032`) is still actively used vs superseded by
  "Off boarding team " — the June investigations pulled from "Off boarding team".
- Gmail/Calendar/Drive connector auth account (assumed kuriandonyku@gmail.com or lm1@cdacoliving.com;
  not re-verified today).
- Mon–Sun week convention for the vacancy WoW workbook specifically (see §5).
- The exact provenance of `active_properties.csv` (May 21) — may be stale.
- ~600 past sessions exist; relevant ones follow naming like "350 Marsden tenant audit",
  "66 Boundary Parramatta house audit", "Vacancy Sydney listing analysis", "Room offboarding tasks
  analysis", "7a Harvey St maintenance issues", "Respond.io workspace audit", "Incomplete lease
  departures", "Build tenant offboarding dashboard and CSV", "193 John St offboarding", "Find employee
  move-out dates in Asana". Docs 02–04 mine these; transcripts are only readable from the OLD project.
