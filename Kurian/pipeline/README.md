# CVD House Pipeline

Script-driven, traceable pipeline that rebuilds per-house / per-room move-in, move-out and
maintenance history from the three Asana CSV exports in `data/Raw Data/`. Stdlib Python only.

## Stages

| Stage | Script | Output (under `data/houses/<slug>/`) |
|---|---|---|
| S1 filter | `s1_filter_house.py <slug>` | `{movein,moveout,maintenance}_filtered.csv`, `filter_report.md` |
| S2 pre-flag | `s2_preflag.py <slug>` | adds flag columns in place, `preflag_report.md` |
| S3 timeline | `s3_timeline.py <slug>` | `timeline.csv`, `rooms_report.md` |
| AI review | (agent step, not a script) | `review_{movein,moveout,maintenance}.md` |
| S4 verify | `s4_verify.py <slug>` | `review.md` (assembled), `VERIFY.md` (PASS/FAIL) |
| Fees review | (agent step) | `fees.csv`, `review_fees.md` — fees/waivers/bond per move-out |
| S5 tenancies + visual | `s5_tenancies_html.py <slug>` | `tenancies.csv`, `vacancy_gaps.csv`, `timeline.html` (per-room visual) |
| S6 gap hunt | `s6_gap_hunt.py <slug>` | `gap_hunt.md/.csv` — fuzzy portfolio-wide search for missed tasks behind every anomaly |

### S6 gap-hunt interpretation (run after S5, before the double-check package)
For every ongoing tenancy, pre-window/orphan row and over-occupied room, S6 fuzzy-hunts the
raw export (tenant-name tokens, room-code family incl. A/B beds, address, date plausibility).
How to act on candidates:
- **In-window missed move-out/move-in** (e.g. a transfer or a task with mangled codes) →
  attach via overrides (`promote_move_out` / `reassign_room` / `set_move_out_date`), re-run
  S3→S5→S4. Verify by Task ID before attaching.
- **Post-window move-out found** → the ongoing row is CONFIRMED correct; note the future
  date in the review, do not attach (window discipline).
- **Pre-window move-in found** → do not add an event (window discipline), but record the
  real start date in rulings.md as stay-length reference for the pre-window tenant.
- **No candidates** → genuinely absent; note it and move on.

Run in order. Every stage appends a pipe-delimited line to `RUNLOG.md` (Sydney time).

## Key conventions

- **House registry:** `pipeline/config/houses.json` — canonical address, house-number-anchored
  match patterns (collision guard: never match bare "Cleveland"), room codes, room labels.
- **Windows (ENFORCED):** `pipeline/config/settings.json` — audit window 2025-07-01→2026-06-30.
  Rows outside the padded window are DROPPED at S1 (Kurian 2026-07-05). Padding: move-in/move-out
  ±7 days, maintenance ±31 days. Event date per source: movein=Due Date, moveout=Due Date,
  maintenance=Created At (fallbacks in settings). Rows with no parseable date are kept + flagged.
  Pre-window tenants still occupying during the window are handled manually — don't chase them.
- **Task links (REQUIRED):** S1 adds a `task_url` column (`https://app.asana.com/0/0/<id>/f`).
  Every task referenced in review files or anything sent to Kurian MUST be a clickable link.
- **Bed codes:** a letter suffix or second code within a room = a separate BED in the same room
  (e.g. #1110 = Room 6B, bed B of Room 6 #1109). Don't count beds as extra rooms.
- **Overrides:** `data/houses/<slug>/overrides.csv` (task_id,action,reason,ruled_by,ruled_on)
  applies Kurian's rulings scriptably — `exclude` drops a task from the timeline (it stays in
  the filtered CSVs); `promote_move_out` turns a task (typically a transfer-out SUBTASK, which
  S3 otherwise skips) into a move_out event — this is how perm transfer-outs close tenancies
  (pilot defect #2); `set_move_out_date` (with a `date` column value, YYYY-MM-DD) forces the
  event date — for comment-derived corrections; exempt from the ruling-#7 conflict pass;
  `reassign_room` (with a `room` column value) forces the event's room code — for
  code-crossers resolved by the slot method (a tenant's events collapse onto the room they
  actually occupied; flag `room_reassigned`). Rulings prose lives in `rulings.md` per house.
- **Shared-bed semantics (Kurian 2026-07-05):** A/B codes = two beds, one room, normally two
  separate tenants/leases. BUT sometimes one person (or a couple) takes the WHOLE room —
  both beds under one arrangement — and their tasks may reference either/both codes.
  Very rarely a whole-room arrangement is converted back into two separate bed leases.
  So cross-code events for one person usually mean a whole-room takeover, not an error:
  resolve with the slot method (exit code = confirmed room) and `reassign_room`.
  Bed-level occupancy analytics are DEFERRED — model at room level for now.
- **Tenant derivation (defect #2b):** rows with a blank Tenant Name column (transfer subtasks)
  get their tenant extracted from the task Name (flag `tenant_derived_from_name`). S5 also has
  a chronological fallback: an unmatched move-out with no/derived tenant closes the room's
  single open tenancy when unambiguous — always hr=yes for review.
- **Room codes are 1–4 digits** (single-digit codes are real — 66 Boundary #7/#8/#9; pilot
  defect #1). S4 gates on room-resolution: a move-out stranded UNRESOLVED while its name
  contains a valid house code = FAIL.
- **Matching:** a row belongs to a house if ANY field mentions the address pattern, or its room
  code matches (Room Code column or `#code` in text). Room codes are portfolio-unique.
- **Subtasks:** kept in filtered CSVs (`is_subtask=yes`) but excluded from timeline + review.
- **Multi-homed tasks:** one timeline event per Task ID (priority movein > moveout > maintenance).
- **HUMAN REVIEW:** anything date-altering (transfers, cancellations, duplicate events, date
  mismatches) is flagged in S2 columns and in the per-task one-liners in `review.md`.
- **Move-in date** = Due Date on Moving In tasks; maintenance events use Created At.
- **Move-out date (ruling #7):** the LATEST of {Due Date, Earliest Date to Move Out, date
  written in the task name} — unless that overlaps the room's next move-in by >1 day, then
  the latest non-conflicting candidate is used and the event is flagged HUMAN REVIEW
  (`date_source` = `*_conflict_fallback`). Tie-breakers when task fields conflict: an explicit
  "final move out date" statement in comments beats everything; else the Final ICR date.
  `date_source` column always records what was used.

- **Move-out fees (REQUIRED in every move-out review):** each move-out task's review must
  state fees applied (amount + what for), anything waived (+reason), and bond status.
  Sources: CR Charges / Bond Held / Break Fee fields, Notes, and "Endorsed to
  Accounting/Finance" subtasks (they carry the fee evidence). CSV exports do NOT include
  task comments — where fields/notes/subtasks are silent, mark
  `NO FEE DATA IN EXPORT — check task comments in Asana`, never guess. Outputs:
  `fees.csv` + `review_fees.md` per house.
- **S5 tenancy pairing:** move_out is paired ONLY with a name-matched move_in (fuzzy:
  shared ≥4-char token prefix; Danny≈Daniel). Never pair across different names. Unmatched
  move_out before the first move_in = pre-window occupant; unmatched move_in = ongoing.
  Two open-ended tenancies in one room = HUMAN REVIEW. Cancelled sales and lease-renewal
  (LR) tasks are excluded via overrides.csv — they are not tenancies.

## AI review step (between S3 and S4)

Dispatch one sub-agent per dataset (never more than one house per agent). Each agent reads the
filtered CSV (top-level rows only), writes `review_<source>.md` with exactly one line per task
(`- [Task ID] room | tenant | note` + `**HUMAN REVIEW: reason**` where applicable), and returns
only a ≤10-line summary. S4 assembles the three files into `review.md`.

## Adding a house

1. Add an entry to `config/houses.json` (address variants + known room codes; leave codes you're
   unsure about — S3's name-parsing will surface missing ones, as it did for 1106/1110).
2. Run S1→S3, dispatch review agents, run S4.
3. New/unknown room codes or anomalies → `QUESTIONS-FOR-KURIAN.md`, never silently resolved.
