# Pilot chat prompt (copy-paste everything below the line into a fresh chat)

---

You are the ORCHESTRATOR for the CVD pilot batch (P1). Project folder: CVD.

Read these first, in order — they are the law for this run:
1. `pipeline/BATCH-RUNBOOK.md` (operating model, hard rules)
2. `pipeline/README.md` (stage conventions)
3. `data/batches/batch-00-pilot.json` (your 5 houses + why each was picked)
4. `QUESTIONS-FOR-KURIAN.md` (known open items — don't re-ask)

Skills your sub-agents must use (installed): `cvd-house-extract`, `cvd-review-movein`,
`cvd-review-moveout`, `cvd-tenancy-timeline`. Registry entries for every house are in
`pipeline/config/registry.json` (copy each pilot house's entry into
`pipeline/config/houses.json` before dispatching it; hand-curated entries in houses.json
always win over generated registry entries).

## Your job, per house (one sub-agent per house, all 5 in parallel per stage)

STAGE A0 — room-code gate (run FIRST, yourself, no sub-agents):
`python3 pipeline/a0_roomcode_check.py data/batches/batch-00-pilot.json`
Per-house PASS required before that house may be extracted. Resolution policy:
- C3 orphan bed codes (e.g. 038B with no 038A): treat as a bed of the same-numbered room,
  record the assumption in the house's houses.json entry + one line in
  QUESTIONS-FOR-KURIAN.md, then proceed. (287 Cleveland currently fails on exactly this.)
- C1 cross-house duplicate codes: that code must NEVER be matched bare — address+code only;
  note it in the house entry; proceed.
- C2 within-house repeats or C4 data-level ambiguity: park the house
  (manifest status=blocked), log the question, continue with the rest.
Re-run A0 after fixes; each house needs a PASS (or documented park) logged in RUNLOG.

STAGE A — extract: dispatch one sub-agent per house → skill `cvd-house-extract`.
Accept only: VERIFY.md = PASS + sane counts. Re-run with a FRESH agent on failure (max 2
attempts, then mark blocked in the manifest and move on).

STAGE B — reviews: per house, one sub-agent → `cvd-review-movein`, then one →
`cvd-review-moveout` (fees mandatory). Spot-audit 2 random lines per house yourself
against the filtered CSV — verify by Task ID, NEVER by title (titles repeat portfolio-wide).

STAGE C — timeline: per house, one sub-agent → `cvd-tenancy-timeline`.
Then YOU sanity-read each tenancies.csv (pairing correctness, pre_window rows, double-ongoing).

STAGE D — eval + report: run `python3 pipeline/eval/run_eval.py <slug>` per house
(342-cleveland-st-surry-hills must also still PASS — regression check). Then write
`data/batches/batch-00-pilot-REPORT.md`: per house — counts, flags, anomalies, eval verdict,
context/token observations; plus ONE consolidated decisions-needed list for Kurian, every
item with its Asana link inline. Post that list in chat too (links in chat, always).

## Rules you enforce (non-negotiable)
- One house per sub-agent context. Sub-agents return ≤10-line summaries — no raw rows/notes.
- Update `data/batches/batch-00-pilot.json` after every dispatch/return.
- Comments are NOT in the CSVs: anything comment-dependent is marked
  `needs Asana comment check` and left for the P5 sweep — nobody guesses.
- Windows enforced (move-in/out ±7d; maintenance ±31d). Maintenance is extracted but NOT
  reviewed this phase (Kurian: parked).
- Every decision → rulings.md / overrides.csv; every run → RUNLOG.md; anomalies →
  QUESTIONS-FOR-KURIAN.md. Nothing silent.
- Goal of the pilot: find where the skills/scripts break. Log every friction point in the
  report — that feedback is the deliverable, not just the data.

Start with STAGE A now.
