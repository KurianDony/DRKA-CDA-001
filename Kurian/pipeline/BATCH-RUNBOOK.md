# CVD Batch Runbook — 200+ houses, 1500+ rooms

Operating model: one chat session = one batch = up to 15 houses. The orchestrator (main chat)
dispatches ONE sub-agent per house, receives ≤10-line summaries only, evaluates, orders re-runs,
and closes the batch with the eval loop. Sub-agents are told explicitly which skill to use.
Executor model: Opus (skills carry all judgment); orchestrator enforces, never extracts.

## Phases

| # | Phase | What happens | Done when | Limiting factor |
|---|---|---|---|---|
| P0 | Registry & setup | Kurian supplies authoritative house list (+ entity grouping). Script-assisted build of `houses.json` entries: slugs, house-number-anchored patterns, collision matrix (every same-street pair listed), known room codes. | Every house has a registry entry + collision note; batch manifests created (`data/batches/batch-NN.json`) | **Kurian input**: house list + any room rosters. Collision detection quality — similar titles/streets are the #1 contamination risk. |
| P1 | Pilot batch (5 houses, not 15) | Full loop end-to-end on 5 diverse houses (big/small/messy). Calibrate skills, flag rates, context costs per house. Update skills with what breaks. | 5 houses Kurian-approved + goldens frozen + skill fixes committed | Skill quality unknowns; this is where they surface cheaply. |
| P2a | **Room-code gate (A0)** | Before ANY extraction: `python3 pipeline/a0_roomcode_check.py <batch.json>` — cross-house duplicate codes, within-house repeats, bed-code orphans, and data-level ambiguity (codes whose #-mentions point at other addresses). Per-house PASS/FAIL. Policy: C3 bed-orphans → documented assumption (bed of same-numbered room) + question queue, proceed; C1/C2/C4 ambiguity → code demoted to address+code matching or house parked. | Every batch house PASS or explicitly parked | Roster quality (Kurian's own data) — this gate exists because dupes/repeats are known to exist. |
| P2 | Extraction waves | Per batch: 15 sub-agents run `cvd-house-extract` (S1–S4). Orchestrator checks each VERIFY.md = PASS + filter sanity (kept-counts vs room count), orders re-runs (fresh agent, never continue a blown one). | All houses in batch VERIFY PASS, RUNLOG lines complete | Orchestrator context — summaries only, never raw rows. Registry errors surface here as weird counts. |
| P3 | Review waves | Per house, sequential: `cvd-review-movein` then `cvd-review-moveout` (fees mandatory). Orchestrator spot-audits 2 random lines per house against the CSV (Task-ID-based, never title-based — many titles are near-identical). | review_*.md + fees.csv per house; spot-audits clean | Opus judgment consistency; flag-rate drift (pilot baseline: ~30–50% of move-outs flagged). |
| P4 | Timeline & double-check | `cvd-tenancy-timeline` per house. Orchestrator batches the double-check packages: ONE consolidated message to Kurian per batch — anomalies + decisions with Asana links inline. | Kurian ruled on the batch; rulings.md + overrides.csv updated; re-run clean | **KURIAN — the true bottleneck.** ~3–6 confirmations/house × 15 = 45–90 decisions per batch. Mitigate: only decision-required items go to him, everything else is assumption+question-queue. |
| P5 | Comment sweep (per Kurian 2026-07-05) | End of each phase/batch-group: every task marked `needs Asana comment check` gets a LIVE Asana API pull (comments/stories). Resolve retractions, "final move out date" statements, fee evidence. Update overrides → re-run affected houses → re-verify. Strict Task-ID matching only. | Zero unresolved `needs_asana_check` rows in the batch | Asana connector availability + rate limits; comment volume unknown. |
| P6 | Eval & freeze | `run_eval.py` per house. After Kurian approval, freeze goldens (`pipeline/eval/golden/<slug>/`). Any later script change must re-PASS every frozen golden (regression suite). | Eval PASS + golden frozen for every house in batch | Nothing hard — cheap and scriptable. |
| P7 | Aggregation (later) | Portfolio rollups: turnover, vacancy days, stay length per house/entity; dashboards. Not designed yet — starts only when P2–P6 done for a full entity group. | TBD with Kurian | Depends on clean per-house data; do not start early. |

Cadence per batch: P2 → P3 → P4 → (P5 at phase end) → P6. ~14 batches for 200 houses.

## Batch mechanics

- **Manifest:** `data/batches/batch-NN.json` — `{slug: {stage, status, agent, attempts, notes}}`.
  Orchestrator updates it on every dispatch/return; any new session rebuilds state from manifests + RUNLOG.
- **Sub-agent prompt must contain:** the ONE house (canonical address + slug + collision exclusions), which skill to use, output paths, "≤10-line summary back, no raw rows", READ-ONLY rule.
- **Re-run policy:** discrepancy → re-run that house with a FRESH agent + the specific correction; 2 consecutive fails → park house (`status: blocked`), continue batch, escalate in batch report.
- **Batch report to Kurian:** houses done/parked, flag counts, decisions needed (with links), eval verdicts.
- **15 is the ceiling, not the target.** If houses are big (>10 rooms), run 8–10 per batch; context per sub-agent is the constraint, and P1 measures it.

## Hard rules (apply to every phase)
1. One house per sub-agent context. No exceptions.
2. Task-ID-based verification everywhere; titles are ambiguous (many near-duplicates portfolio-wide).
3. Every human-facing item carries its Asana link — in chat too, not just files.
4. Windows enforced: move-in/out ±7d, maintenance ±31d (maintenance parked for now per Kurian).
5. All decisions land in rulings.md/overrides.csv; all runs land in RUNLOG.md; nothing silent.
6. Comments: blank on initial pass, resolved only in P5 sweeps — never guessed.

## Known limiting factors (summary)
1. **Kurian review bandwidth (P4)** — the schedule driver. Everything else parallelizes.
2. **Registry/collision quality (P0)** — bad patterns poison everything downstream silently.
3. **CSV export staleness** — exports are a 2026-07-04 snapshot; a multi-week campaign means late batches read old data. Decide: refresh exports per batch-group, or fix the snapshot date as the data cutoff.
4. **Comment blindness until P5** — accepted by design; P5 closes it.
5. **Orchestrator context** — solved by summaries-only + manifests, but discipline must hold.
6. **Opus consistency** — solved by skills + spot-audits + eval regression; pilot calibrates.
