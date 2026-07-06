# 05 — Project Brief: CDA-001 Portfolio Diagnostic

**Status:** scaffolding for the new Cowork project. Read after `00-README.md` and
`01-shared-foundations.md`. Operating rules live in `06-project-instructions.md`.
Methods live in docs 02–04; do not re-derive them here.

---

## 1. Engagement summary

| Item | Value |
|---|---|
| Client | CDA Co-Living (Sydney/NSW/VIC co-living operator — see `01` §1) |
| Vendor | DRKA (Kurian's AI-first consultancy), single resource |
| Engagement | CDA-001 Portfolio Diagnostic |
| Duration / fee | 8 weeks, $500/week |
| Objective | Rebuild the last 12 months for every house and room from CDA's own data (Asana + respond.io) and report on it |
| Ownership | All assets produced become CDA property |
| Nature | **Snapshot, not a maintained system.** No pipelines to keep running after Week 8 |
| Access posture | **READ-ONLY** on all client systems (Asana, respond.io, Google). No tenant contact |
| Data hygiene | Where data looks off, check with the CDA team — never guess (escalation ladder: `06` Part 2 §3) |

## 2. Scope — the 7 measures

| # | Measure | Precise definition | Primary data source |
|---|---|---|---|
| 1 | Stay length | Per tenancy: lease term as signed vs time actually lived (move-in to actual move-out). Report average, spread, outliers per room/house | Off boarding team `1206596901916034` custom fields (Lease Start/End, move-out dates — `01` §2) + Moving In `1209877764947329`; method `02` §4.2, §4.9 |
| 2 | Vacancy | Days each room sits empty between one tenant's move-out and the next tenant's move-in, per room | Move-out↔move-in matching per room (not per date) — `02` §4.3, §4.5; 10-day window rule `01` §5 |
| 3 | Turnover | Count of tenancy changes per room over the 12-month window; rate per room and per house | Per-room task history across Off boarding team + Moving In — `02` §4.6 |
| 4 | Real occupancy | Houses that look full on a given date but are churning: occupancy on paper vs tenancy stability over the window. Flag look-full-but-churning houses explicitly | Derived from measures 1–3 against the room roster (`active_properties.csv` — currency is a kickoff input, §6.4; provenance caveat `01` §8) |
| 5 | Maintenance | Per house: issue types, timing, seriousness/urgency, resolution status and time-to-resolve, chargebacks | Maintenance Requests `1204018834894343` — doc 03 (7A Harvey pattern, `03` §8) |
| 6 | Tenant signal | WhatsApp themes, response rates, complaint patterns per house/tenant, linked to maintenance tickets and departures | respond.io, mainly channel 348751 "CDA Co Living " (trailing space) — doc 04; linkage pattern `04` §5 |
| 7 | Area read | House groupings (CDA / CLS NSW / CLS VIC) compared on measures 1–6: averages, spread, outliers per grouping | Measures 1–6 aggregated via the house→entity mapping (kickoff input, §6.1) |

Every measure is computed per room, rolled up per house, then per entity grouping.

## 3. Deliverables

1. **Raw data per house/room.** Done when: every in-scope house has a per-room dataset (CSV) covering the 12-month audit window — tenancies, stay lengths, vacancy gaps, turnover events, maintenance tickets, tenant-signal summary — each row traceable to source via `[task:GID]` / `[contact id:N]` citations, anomalies labelled UNVERIFIED or resolved, and the dataset stored under the project-folder conventions in `06`.

2. **HTML dashboard.** Done when: a single self-contained HTML file renders all 7 measures per house and per entity grouping, loads from local data with no external calls to client systems, lets Kurian drill from portfolio → house → room, and matches the raw data exactly (spot-check: 3 houses reconciled row-for-row).

3. **Full written report.** Done when: it contains a per-house read for every in-scope house, portfolio-level patterns, and an explicit ranked list of which houses to focus on and why — every claim cited, every judgment traceable to evidence, no uncited characterisations. Delivered per gate (W3 CDA set, W5 CLS NSW, W8 CLS VIC).

4. **Area-level analysis + Transformation Roadmap (W8).** Done when: the three entity groupings are compared on all 7 measures with averages and outliers, cross-grouping differences are stated with evidence, and the roadmap converts findings into prioritised recommendations — each tied to specific cited findings, none speculative.

## 4. Timeline & gates

| Gate | Entry criteria | Exit criteria |
|---|---|---|
| **W1–2: build / connect / verify** (no deliverable) | Kickoff inputs received (§6); Asana + respond.io connectors pass smoke tests (`00` steps 1–2, 6) | Extraction pipeline verified against known facts (e.g. task `1215355847925607` — `00` step 6); house→entity mapping loaded; audit window confirmed; ≥1 full house rebuilt end-to-end and reconciled |
| **W3: CDA Report** | W1–2 exit met; CDA house list confirmed from mapping | Deliverables 1–3 complete for the CDA house set; open UNVERIFIED items listed; Kurian question queue cleared or logged |
| **W5: CLS NSW Report** | W3 delivered; any W3 method corrections applied | Deliverables 1–3 complete for CLS NSW houses; cumulative dashboard covers CDA + CLS NSW |
| **W8: CLS VIC Report + area analysis + Transformation Roadmap** | W5 delivered | Deliverables 1–3 complete for CLS VIC; deliverable 4 complete across all three groupings; all assets handed to CDA; RUNLOG closed out |

A gate does not open while a KURIAN BLOCKER on its entry criteria is unresolved (`06` Part 1).

## 5. Entities & batching

- CDA, CLS NSW and CLS VIC are **house groupings within the same Asana workspace and the same
  projects** (confirmed by Kurian) — not separate workspaces, projects, or data sources.
- Processing order: CDA (→ W3) → CLS NSW (→ W5) → CLS VIC (→ W8).
- The authoritative house→entity mapping is a **required kickoff input** (§6.1). Do not infer
  entity membership from addresses or naming; the live Asana "Owner" field can seed a DRAFT
  mapping only (`07` R10.1) — it is not authoritative (counter-example: a Parramatta NSW house
  carrying "CLS VIC"), and area is never inferred from suburb.
- Per-house work is batched and isolated via sub-agents — doc 08.

## 6. Required kickoff inputs (from Kurian, before W1–2 exit)

1. **House→entity mapping** — authoritative list assigning every house to CDA / CLS NSW / CLS VIC.
2. **respond.io token / connector** — working read access (setup: `04` §2; verify: `00` step 2).
3. **Folder access** — the new project folder attached, seeded per `00` FILE MIGRATION + step 3.
4. **Portfolio list confirmation** — that `active_properties.csv` (or a replacement) is the current
   full house/room roster (`01` §8 flags it as possibly stale).
5. **Audit window start date** — which 12 months the diagnostic covers (exact start/end dates).
6. **House→AREA mapping** — alongside the entity mapping (§6.1). Per `07` R10.1, the live Asana
   "Owner" field — values like "CDA - Navid ", "CLS NSW - James", "CLS VIC - Navid and James" —
   can seed a DRAFT entity mapping, but Kurian's list is authoritative.
7. **DRKA branding assets** — logo/palette for deliverables. Fallback default if not supplied:
   text wordmark "DRKA" + neutral palette.
8. **Delivery channel confirmation** — default: deliverables land in the project folder and
   Kurian presents/relays to CDA.

Missing input at the point it is needed = KURIAN BLOCKER (`06` Part 1).

## 7. Out of scope

- No system to maintain: no scheduled tasks, no live pipelines, nothing that must keep running post-W8.
- No writes to Asana, respond.io, Google Sheets/Drive, or any client system.
- No tenant contact of any kind (respond.io write tools exist — never used; `01` §3).
- No messages are ever sent to tenants under any approval path; respond.io is read-only
  throughout CDA-001.
- The old project's other workstreams (Flatmates bot, EOD lead-gen, G1/G2 market data, inspection
  tracker) — see `00` for the boundary.

## 8. Success criteria

Per the proposal, the diagnostic succeeds if it gives CDA a clear, evidence-backed read on the
three focus signals:

1. **Turnover** — which rooms/houses change hands abnormally often, and why.
2. **Maintenance** — where issues cluster, how serious they are, and how resolution performs.
3. **Vacancy** — where rooms sit empty, for how long, and what it costs in occupied-days.

Plus, cross-cutting: every number reproducible from the raw data, every judgment cited, and the
focus-house list defensible to CDA from their own records.
