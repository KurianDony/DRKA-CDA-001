# Batch 00R — fresh-chat rerun of the 5 pilot houses with the v2 skills

Paste these into ONE new chat, in order, each after the previous stage completes.
Before starting: install the v2 skill cards (cvd-review-movein-v2, cvd-review-moveout-v2,
cvd-tenancy-timeline-v2) — they replace the old review/timeline skills. cvd-house-extract is
unchanged. New chat in the CVD project, model = Opus.

---

## PROMPT 1 — setup + extraction

You are the ORCHESTRATOR for batch 00R: a clean-room RERUN of the 5 pilot houses using the
upgraded pipeline + skills. Purpose: prove the improved system reproduces (or beats) the
pilot from scratch — lower flag rates, no cross-house junk, gap-hunt integrated.

Read first: `pipeline/BATCH-RUNBOOK.md`, `pipeline/README.md` (it changed — overrides now
include promote_move_out / set_move_out_date / reassign_room; S6 gap-hunt exists; ≥3-digit
rule for code-only matching), `data/batches/batch-00-pilot.json` (history), and each house's
`rulings.md` + `overrides.csv` (STANDING Kurian rulings — keep them, they apply).

Setup steps:
1. Create `data/batches/batch-00R-rerun.json` — same 5 houses, fresh stage/status fields.
2. Archive the pilot outputs for comparison: for each house copy
   `data/houses/<slug>/` → `data/houses/_archive/<slug>-pilot1/` (keep the originals in
   place; the rerun will overwrite generated files but MUST NOT touch overrides.csv,
   rulings.md).
3. Run the A0 gate: `python3 pipeline/a0_roomcode_check.py data/batches/batch-00R-rerun.json`
   (create the manifest first). Known C3 orphans at 287 are already documented — proceed.

Then STAGE A: one sub-agent per house (all 5 parallel) → skill `cvd-house-extract`.
Accept only VERIFY.md = PASS. Compare each house's filter counts against the pilot's
(manifest history): 66 Boundary should now keep FOUR fewer cross-house rows than pilot
round 1 (Kapil/Gabriel/Malik/Tung are out by design). Any house whose counts differ from
pilot in an UNEXPLAINED direction → investigate before proceeding.
Non-negotiables: one house per sub-agent, ≤10-line summaries, manifest + RUNLOG updated,
Task-ID verification only, links in anything human-facing. Report a stage summary when done.

---

## PROMPT 2 — reviews (v2 skills)

STAGE B: per house sequentially — one sub-agent → skill `cvd-review-movein`, then one →
`cvd-review-moveout` (fees mandatory: applied/waived/bond + evidence source).
The v2 skills carry a NOT-a-flag list (rule-resolved date mismatches, month-to-month
overstay, billed-vs-physical). Enforce it: spot-audit 2 random lines per house by Task ID;
additionally reject any review that flags something the standing rules already answer.
Target: move-out flag rate ≤35% (pilot round-1 was 63–91%). Cite `months_past_term` from
tenancies.csv instead of flagging lease-end-before-move-out (run S5 first if tenancies.csv
is missing: `python3 pipeline/s5_tenancies_html.py <slug>`).
Comment-dependent items: mark `needs Asana comment check`, then run the P5 comment sweep at
the end of this stage for ALL flagged tasks (Asana connector, get_task stories; STOP if the
connector can't read comments). Update fees.csv/rulings with `ruled_by=asana-comment`.
Report per-house flag rates old-vs-new when done.

---

## PROMPT 3 — timeline + gap hunt + package

STAGE C: per house — one sub-agent → skill `cvd-tenancy-timeline` (v2: it now runs S6
`s6_gap_hunt.py` after S5). Then YOU process each `gap_hunt.md` per the README
interpretation rules:
- In-window missed events (e.g. 66 Boundary: Adriano's exit — his Castle Hill transfer
  chain) → verify by Task ID, attach via overrides (promote_move_out / reassign_room /
  set_move_out_date, ruled_by=gap-hunt), re-run S3→S5→S4.
- Post-window move-out found → note "confirmed ongoing (exits <date>, post-window)" in the
  review; do NOT attach.
- Pre-window move-in found → record the real start date in rulings.md (stay-length
  reference); do NOT add events.
- Lookalike names (Sakshi/Sakshyam-type) → ignore, note nothing.
Sanity-read every tenancies.csv (pairing, pre_window rows, double-ongoing, overstay
columns populated). Build the consolidated double-check package: per house, only items
needing Kurian's eyes, each with its Asana link INLINE IN CHAT. Post it and wait.

---

## PROMPT 4 — eval, drift report, close (after Kurian replies to the package)

STAGE D:
1. Apply Kurian's rulings (rulings.md + overrides), re-run affected houses S3→S5→S4.
2. `python3 pipeline/eval/run_eval.py <slug>` for all 5 + 342-cleveland-st-surry-hills.
   Houses where the rerun legitimately improved on the pilot (junk removed, gap-hunt
   attachments, new overstay columns) will FAIL against the OLD golden — that is expected
   drift. For each: diff the eval report, confirm every divergence is an intended
   improvement (junk out / real event in / ruling applied), list any that are NOT.
3. With Kurian's sign-off in this chat: re-freeze goldens for the changed houses
   (copy tenancies.csv + vacancy_gaps.csv → `pipeline/eval/golden/<slug>/*_golden.csv`),
   RUNLOG line each.
4. Write `data/batches/batch-00R-rerun-REPORT.md`: per house — counts pilot-vs-rerun, flag
   rate pilot-vs-rerun, junk removed, gap-hunt attachments made, eval outcome; plus a
   verdict: is the pipeline ready for batch 01 at 8–10 houses? List any remaining friction
   for the pipeline owner. Post the summary + decisions (if any remain) in chat with links.
