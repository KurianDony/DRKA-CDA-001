# 08 — Sub-Agent Orchestration & QA (CDA-001 Portfolio Diagnostic)

**Project:** CDA-001 Portfolio Diagnostic — DRKA consulting for CDA Co-Living. Rebuild 12 months of per-house/per-room data from Asana + respond.io. All client systems **READ-ONLY** (01 header, 04 §3.7 write-tool warning).
**Companion docs:** 01 (GIDs, collisions, connectors), 02 (extraction method), 03 (maintenance), 04 (respond.io), 09 (deliverable specs). Cite, don't duplicate.
**Non-negotiables embedded throughout:** sub-agents used liberally; zero cross-house data contamination; no context/token blowouts; independent verification before anything is reported; `KURIAN BLOCKER:` protocol (§8).

---

## 1. Pipeline architecture

**Unit of work = one house.** Never batch houses in one agent context. The orchestrator (main session) is a dispatcher and bookkeeper only.

Stages per house, in order (each writes files, each is resumable — §6):

| # | Stage | Agent | Output |
|---|---|---|---|
| 1 | Roster build | orchestrator or extractor | `data/houses/<slug>/roster.csv` — rooms + room codes, address-collision guard applied (01 §2 conventions) |
| 2 | Event extraction | extractor agent(s) | `events_raw.csv` — every move-in/move-out/cancel/transfer event with GIDs (method: 02 §4.1–4.4) |
| 3 | Maintenance pull | extractor agent | `maintenance_raw.csv` (method: 03 §4) |
| 4 | respond.io pull | extractor agent | `respondio/` message files + `tenant_signals.csv` (method: 04 §4; roster from stage 1, never address search — 04 §8.1) |
| 5 | Why-mining | why-miner agent(s) | `departures.csv` — reason + confidence per departing tenant (02 §4.9; consumes the stage-4 contact/message files) |
| 6 | Tenancy assembly + metric computation | orchestrator script (bash/python) | Per house: `tenancies.csv` rows, `vacancy_gaps.csv` rows, one `metrics_house.csv` row (the 7 measures: stay length, vacancy, turnover, real occupancy, maintenance, tenant signal, area read inputs), and `occupancy_monthly.csv` rows (monthly occupancy series for dashboard sparklines) |
| 7 | Verification | **verifier agent (fresh context)** | `VERIFY.md` — PASS/FAIL + discrepancy list (§5) |
| 8 | Report fragment | writer agent | `fragment.md` + dashboard JSON block |

**Context rule for the orchestrator:** it holds only per-house summaries (≤10 lines each), file pointers, and RUNLOG state. ALL raw evidence — task payloads, comment paraphrases, message threads — goes to files under `data/houses/<slug>/`. If the orchestrator ever contains a full comment thread or notes field, something has already gone wrong (the #1 historical failure — 02 §7.1, 03 §7.1, 04 §8.5).

Parallelism: dispatch extractor agents for several houses concurrently (one house per agent); stages within a house are sequential. Precedent: 5-rooms-per-agent fan-out (02 §4.6.2), 4 parallel house agents (02 §2, Jun 23 House Story run).

---

## 2. Sub-agent roles & prompts

Every agent prompt MUST state: the one house (canonical address + slug + room-code range), the 12-month window, the exact output file path, the ≤10-line summary format, and the READ-ONLY rule. Every agent returns: **file path(s) written + a summary of ≤10 lines** (counts, anomalies, open questions). Nothing else comes back inline.

### 2.1 Extractor agents
- **Scope:** one house per agent. For big houses (>~10 rooms or >~40 candidate tasks), split by **source** instead: one agent for Moving In + Off boarding, one for Maintenance, one for respond.io — still the same single house.
- **Inputs given:** canonical address + known variants/typos + explicit exclusion list from 01 §2 (e.g. "24 Swan Ave is NOT 27 Swan Ave"), room-code range if known, project GIDs (01 §2 table), window dates, output path.
- **Outputs required:** `events_raw.csv` (or `maintenance_raw.csv`) with one row per event, columns incl. task_gid, room_code, event_type, date, date_source ("how_i_know" convention, 02 §7.3), permalink. Plus ≤10-line summary: rows written, rooms covered, anomalies (label conflicts, stub tasks dropped, zero-event rooms).
- **NEVER:** return task notes/comments/threads inline; request `notes`/`html_notes` in bulk opt_fields (02 §7.1); process a second house "while they're in there"; resolve ambiguities silently (flag them); write outside their house dir.

### 2.2 Why-miner agents
- **Scope:** a batch of departing tenants **from one house** (≤10 per agent).
- **Inputs given:** tenant first names + offboarding task GIDs + respond.io contact IDs and message files (from stage 4) + output path.
- **Outputs required:** `departures.csv` rows — tenant_id (first name + GID), reason, reason_confidence (verified/reported/unknown — 09 §1 schema), evidence_refs. Long message threads saved to files and grepped, never read inline (04 §3.3, §8.5). ≤10-line summary: counts per confidence level, notable patterns.
- **NEVER:** quote raw comment threads back; treat a retention-cancelled notice as a departure (02 §4.4); mix tenants from different houses in one batch.

### 2.3 Verifier agents
- **Scope:** one house. **Fresh context — never the agent that extracted, and given no access to the extractor's summary reasoning**, only the intermediate CSVs and live Asana. Protocol in §5.
- **NEVER:** "fix" data themselves (they report discrepancies, extraction re-runs); skip the live spot re-pulls; PASS a house with unexplained count mismatches.

### 2.4 Report-fragment writers
- **Scope:** one house. **Inputs:** verified CSVs + `VERIFY.md` (must be PASS) + the one-pager template (09 §3).
- **Outputs:** `fragment.md` + the house's JSON block for the dashboard. First names only (01 privacy header).
- **NEVER:** compute new numbers (everything comes from `metrics_house.csv`); include full surnames or contact details; write before verifier PASS.

---

## 3. Context-hygiene rules

The #1 historical failure mode is token blowout from pulling full comment threads / notes fields into one context (02 §7.1: a single task's `html_notes` + comments exceeded the token cap; 03 §7.1: first 7A Harvey query blew the limit on `notes`; 04 §8.5: message pages flood context). Hard rules:

1. **Minimal `opt_fields` always.** First pass: `name,due_on,created_at,completed,completed_at,permalink_url,custom_fields.name,custom_fields.display_value,memberships.section.name`. Never request `notes`/`html_notes` in bulk; `include_comments: false, include_subtasks: false` by default (02 §4.2). Fetch notes/comments only per-task, only when a date/reason is ambiguous, and paraphrase to file immediately.
2. **Paginate.** `search_tasks` has no offset — cursor-paginate via `created_at_before` + `sort_by: created_at`, `limit: 100` (02 §7.2). respond.io `list_messages` via `cursorId` (04 §3.3).
3. **Write intermediate results to CSV/MD immediately.** Extract → write → summarize. Never accumulate rows in context across API pages.
4. **Per-house working dirs:** `data/houses/<slug>/` for intermediates; deliverable CSVs land in `data/final/`. Slug = `<number>-<street-name>-<street-type>-<suburb>`, lowercase, hyphenated — suburb ALWAYS included, even when it feels redundant (collision guard: `19-burnett-st-merrylands` vs `216-burnett-st-parramatta`). E.g. `350-marsden-rd-carlingford`. Everything an agent produces lands in its house dir.
5. **Summaries, not transcripts, across agent boundaries.** ≤10 lines back to the orchestrator; the orchestrator never re-reads raw files except targeted greps.
6. **Hard rule: one house per sub-agent context.** No exceptions, including "small" houses.
7. respond.io threads: save to files, mine with Grep for keywords (04 §4 step 3). Never inline more than ~2 pages.

---

## 4. Contamination & integrity checks (run per batch, before verification)

All runnable in bash/python against the CSVs. Log results in RUNLOG.md.

1. **Room-code uniqueness across houses.** Room codes are unique portfolio-wide (02 §3.1). Script: concatenate all `roster.csv`, assert no room_code appears under two slugs. Any dupe = contamination or collision — stop the affected houses.
2. **Task-GID exclusivity.** Every task GID appears in exactly one house's dataset. Cross-house dedupe script over all `events_raw.csv` + `maintenance_raw.csv`; duplicates mean an address-collision leak or double-extraction. (Watch 22-digit concatenated GIDs — 02 §7.5.)
3. **Address-collision guard at roster stage.** Before extraction, check the target address against the canonical collision list (01 §2): 12 Harvey ≠ 7A Harvey; 604 King St Erskineville ≠ 12 Erskineville Rd; 516 ≠ 327 Crown St; 24 ≠ 27 Swan Ave (+ "Swann" spelling). Roster output must record which collisions were excluded and how many tasks that dropped.
4. **Event-count reconciliation vs live Asana.** For each house, re-run the same `search_tasks` count live and compare with rows extracted (after stub-task filtering — 02 §7.4). Mismatch >0 after accounting for filtered stubs/duplicates = re-extract.
5. **Date-order assertions** (bash/python, per 02 §4.5 "verify all arithmetic programmatically"): per tenancy `move_in < move_out`; per room, tenant N's out ≤ tenant N+1's in; all gaps ≥ 0; all dates inside plausible range (window start − 24 months … today).
6. **Row-count deltas between stages.** Log `events_raw → tenancies → metrics_house` row counts per house; every drop must have a named cause (stub filtered, duplicate merged, cancelled sale excluded, retention-cancelled). Unexplained delta = FAIL.

---

## 5. Verification protocol

Nothing enters a deliverable without a verifier **PASS** recorded in RUNLOG.md. Modeled on the re-verification pass that caught 100%-match on 350 Marsden (02 §4.6.6, §8.8).

Per house, an independent verifier agent (fresh context, §2.3):

1. **Re-derives the timeline** from the intermediate CSVs alone — rebuilds per-room event sequences and gap day-counts from `events_raw.csv` and compares against `tenancies.csv` / `vacancy_gaps.csv` / `metrics_house.csv`.
2. **Spot re-pulls 3–5 random tasks live** (`get_task`, minimal opt_fields) and compares name, dates, room code, section against the CSV rows. Random selection seeded and logged.
3. **Re-runs the §4 integrity checks** for the house.
4. Writes `VERIFY.md`: PASS/FAIL, checks run, discrepancies with GIDs.

**Discrepancy → back to extraction** for the affected rooms/tasks only; logged in RUNLOG.md with cause; verifier re-runs after the fix. Two consecutive FAILs on the same house → escalate (§8).

---

## 6. Failure & retry policy

- **Transient API failures** (timeouts, empty responses on known-good queries — search flakiness is documented, 02 §7.10): retry once with a variant query; then log to RUNLOG.md, skip the item, and flag it in the agent summary. Never silently drop.
- **Partial-house completion:** legal state. A house can sit at "extraction done, why-mining pending". It cannot enter any deliverable until stage 7 PASS.
- **Resumability — state file per house:** `data/houses/<slug>/STATE.json` — `{stage, status: pending|running|done|failed|blocked, started_at, finished_at, agent, notes}` per stage, updated by the orchestrator on every dispatch/return. On session restart, read all STATE.json files to rebuild the queue; never re-extract a `done` stage without cause.
- **Context overflow mid-house:** the agent stops, writes whatever partial CSV it has with a `PARTIAL` marker row, and reports the last completed task GID. Orchestrator dispatches a **fresh** agent to resume from that GID with tighter opt_fields / smaller pages — never "continue" the blown context. Log the overflow in RUNLOG.md (these are the events the hygiene rules in §3 exist to prevent).
- **Attachment URLs expire ~1 hr** (02 §7.9): download-and-read in the same agent turn or re-fetch.

---

## 7. RUNLOG.md and the question queue

**`RUNLOG.md`** (project root, append-only — never edit prior lines; the mounted folder is effectively append-only anyway, 02 §7.13). **Canonical format** (06 §8 cites this definition): one header block per working session — date, operator, houses in scope, and a Decisions field — containing one pipe-delimited line per pipeline event, timestamps in Sydney time:

```
## 2026-07-10 (session) | operator: Kurian | houses in scope: 350-marsden-rd-carlingford
2026-07-10T14:32+10:00 | 350-marsden-rd-carlingford | extraction | agent:ext-03 | done | 41 rows; 2 stubs filtered; R4 zero events | decision: R4 → no-data per 02 §4.5
Decisions: R4 → no-data per 02 §4.5
```

Event-line fields: timestamp (Sydney), house slug, stage, agent id, outcome (done/failed/retried/blocked/PASS/FAIL), anomalies, decisions taken. Every §4 check result, every verifier verdict, every retry, every escalation gets a line.

**`QUESTIONS-FOR-KURIAN.md`** (project root): batched **non-blocking** questions — ambiguous room statuses (350 Marsden R4-type cases, 02 §9.2), suspected stale records, entity-mapping edge cases. Format per entry: date, house, question, why it matters, what was assumed meanwhile. Present at weekly check-ins; move answered items to a resolved section with the answer. Non-blockers go here, never into a KURIAN BLOCKER.

---

## 8. Escalation & KURIAN BLOCKER

**Sub-agents never emit the phrase.** A sub-agent that is definitively blocked reports upward in its summary: `BLOCKED: <reason>` + what it tried. The orchestrator then decides:

- Workaround exists (alternate query, different source per 02 §3.1 priority list, defer the house) → apply it, log it, continue.
- Question is real but the pipeline can proceed on a stated assumption → assumption + question to `QUESTIONS-FOR-KURIAN.md`, continue.
- **Definitively blocked** — no workaround, and the block gates a deliverable or a whole stage → the orchestrator emits, verbatim, in chat:

```
KURIAN BLOCKER: <one-line statement of what is blocked, why, and the single decision/input needed>
```

Qualifying examples: house→entity mapping missing at kickoff (it comes from Kurian — cannot start entity gating without it); Asana/respond.io connector auth failure; a house's records so contradictory that both interpretations change the metrics; anything requiring a WRITE to a client system (never do it — ask).
Not qualifying: single ambiguous tenant dates (caveat + question queue), one room with no data (no-data flag per 02 §4.5), transient API errors (§6).

While blocked: park only the affected houses/stage (`STATE.json` status `blocked`), keep every other house moving, log the blocker in RUNLOG.md.
