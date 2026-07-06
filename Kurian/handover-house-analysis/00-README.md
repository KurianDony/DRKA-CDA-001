# CDA House-Analysis Handover Pack

**What this is:** everything a brand-new Claude Cowork project (fresh context, no memory, no
connectors yet) needs to take over three CDA CoLiving analysis workstreams from the "Random CDA
stuff" project: (1) house updates / occupancy & vacancy, (2) maintenance requests, (3) respond.io
conversations. The old project keeps the Flatmates bot, EOD lead-gen, G1/G2 market data, templates
and inspection-tracker workstreams — those are out of scope here.

All workflows are **READ-ONLY** against external systems (Asana, respond.io, Google) unless Kurian
explicitly asks for writes.

**PRIVACY:** these docs contain real tenant names/IDs tied to sensitive events — internal use only;
when producing NEW outputs, prefer first names or `[id:…]` citations.

## Doc map

| Doc | Contents |
|---|---|
| `00-README.md` | This file — pack overview + quick-start checklist. |
| `01-shared-foundations.md` | Shared plumbing: business context, Asana workspace/project GIDs and naming conventions, connector inventory, file/folder inventory (what moves vs stays), business rules (rent/bond/week conventions, +$20 mirror markup), memories to port, related skills, UNVERIFIED list. |
| `02-house-updates-occupancy-vacancy.md` | Per-house updates ("give me updates on X"), vacancy audits (350 Marsden, 27 Swan Ave pattern), Vacancies SYD WoW analysis, House Stories, offboarding CSV extraction, early lease breaks. |
| `03-maintenance-requests.md` | Maintenance Requests project analysis — the 7A Harvey St issues-digest pattern (open vs resolved, chargebacks, urgency). |
| `04-respondio-conversations.md` | respond.io workflows — channels (main tenant line is 348751 "CDA Co Living " — trailing space in the real name), contacts/messages analysis. |
| `05-project-brief.md` | CDA-001 engagement brief — client/vendor, the 7 measures, deliverables, W3/W5/W8 gates, kickoff inputs, out-of-scope. |
| `06-project-instructions.md` | Operating rules for the new project — paste-in project instructions, session-start checklist, escalation ladder, KURIAN BLOCKER protocol, file/RUNLOG/question-queue conventions. |
| `07-analytical-decision-rules.md` | Numbered analytical decision rules (R-rules) — the edge-case rulings every metric computation must follow. |
| `08-subagent-orchestration-qa.md` | Sub-agent pipeline — per-house stages, context hygiene, house-slug and file layout (canonical), integrity checks, verification protocol, RUNLOG/question-queue formats. |
| `09-deliverable-specs.md` | Deliverable specifications — CSV schemas, dashboard spec, report and one-pager templates. |
| `CDA-001-proposal.pdf` | The CDA-001 engagement proposal — source for scope, fee and timeline. |

**Read order for the CDA-001 engagement:** `00` → `01` → `05` → `06` → `07` → `08` → `09`.
Docs `02`–`04` are method reference — read the relevant one in full before first executing that
workstream.

## Quick-start checklist for the new project

**FILE MIGRATION (decision):** Create/attach a NEW project folder in the new project. Kurian
manually copies (a) this `handover-house-analysis/` folder and (b) the copy-list in step 3 below
into it before the first session. All absolute paths in docs 02–04 that reference
`…/Random CDA stuff/` should then be read as relative to the new project folder. Do NOT attach the
old "Random CDA stuff" folder to the new project.

1. **Connect Asana** — sign in as `lm1@cdacoliving.com`. Verify with `get_me`
   (expect user GID `1208280814774236`, workspace `1201789231542521`). Asana Premium
   search is assumed (`search_tasks` works).
2. **Connect respond.io** — install the respond.io connector (search the MCP registry, or the
   token-based setup in doc 04 §2 — token comes from respond.io Settings → Integrations →
   Developer API, requires Growth plan or higher; ask Kurian for the token location). Verify with
   `list_channels` (expect 6 channels; the main tenant line is 348751 "CDA Co Living " — trailing
   space in the real name). Channel 390890 "CDA House Updates" should appear in `list_channels`;
   its purpose is UNVERIFIED.
3. **Grant folder access** to the new project folder (see FILE MIGRATION above); Kurian copies in
   the workstream files — this list exactly matches `01-shared-foundations.md` §4's "move" list:
   `350_Marsden_vacancy_audit.html`, `350_marsden_vacancy_audit_artifact.html`,
   `27_swan_ave_vacancy_audit_artifact.html`; `Vacancies_SYD_WoW_Analysis.xlsx`;
   the 4 `House Story - *.md` files + `CDA House Stories - Combined (4 Houses).md` **and** `.docx`;
   `CDA_Tenant_Profiles.pdf`, `active_properties.csv`;
   `Offboarding_Investigation_10rooms_2026-06-22.md`, `Offboarding_Investigation_22upcoming_2026-06-22.md`,
   `offboarding-recipe.html`, `offboarding-850-tasks.csv`,
   `offboarding-final-v4.csv` (enriched 66-col dataset used for lease-break/why investigations);
   `BUSINESS_RULES.md`; `early_lease_breaks.csv` + `CDA_early_lease_breaks_Mar-Jun_2026.xlsx`;
   `7A_Harvey_St_Issues_Mar-Jun_2026.md`; and this `handover-house-analysis/` folder itself.
   Never copy `cda-performance-checks-951c12a2ef49.json` — it is a CREDENTIAL (see `01` §4).
4. **Optionally connect** Google Drive (portfolio sheets), Gmail (offboarding cross-checks),
   Claude in Chrome (dashboard fallback) — see `01` §3.
5. **Recreate memories** — at minimum the CDA-Portfolio-SYD-mirror entry (spreadsheet IDs + hidden
   +$20 markup, `01` §6), plus a memory holding the Asana GID table and respond.io channel IDs.
6. **Verify — two tiers.**
   **(a) Light smoke test (every session):** Asana `get_me` (step 1 expectations); respond.io
   `list_channels` (step 2 expectations); cross-check one known fact: 216 Burnett St Room 5 task
   GID `1215355847925607` exists in "Off boarding team " (GID `1206596901916034`).
   **(b) ONE-TIME end-to-end pilot (run once, in the first working session — not repeated per
   session):** *"Give me updates on 350 Marsden"* — expect the flow in doc 02: find the house's
   tasks in "Off boarding team " + Moving In (`1209877764947329`) + Maintenance Requests
   (`1204018834894343`); then resolve tenants via the Asana roster → respond-io `list_contacts`
   by name → `list_messages` per contact (traffic is mostly on channel 348751 "CDA Co Living "),
   and summarize.
7. Read `01-shared-foundations.md` §8 (UNVERIFIED) before trusting anything not verified there.
8. **Ready to start the engagement?** Once step 6(a) passes and the 6(b) pilot has succeeded
   once, collect the kickoff inputs in `05-project-brief.md` §6 — the CDA-001 engagement does
   not start without them.

**Connector-version fallback:** if a documented tool name/param is missing in the new project's
connector version (tool prefixes WILL differ), don't assume the doc is wrong — verify identity via
`get_users`/workspace lookup and restrict `opt_fields` instead of relying on undocumented params.

## Provenance

Generated **2026-07-04** from the "Random CDA stuff" Cowork project (session mount
`eager-hopeful-pascal`), by live queries against Asana and respond.io plus the project folder,
memory dir and installed skills. Owner: Kurian (kuriandonyku@gmail.com).
