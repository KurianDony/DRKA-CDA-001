# Pilot continuation prompt (paste into the SAME pilot chat)

---

Pipeline fixes are in (done by the pipeline owner — re-read `pipeline/README.md`, the
conventions changed):
- Defect #1 FIXED: room-code regex now matches 1–4 digit codes. 66 Boundary has already been
  re-run and passes the new S4 room-resolution gate (0 stranded move-outs).
- Defect #2 FIXED: `overrides.csv` now supports `action=promote_move_out` — it turns a
  transfer-out SUBTASK into a real move_out event that closes the tenancy.
- Eval blind spot CLOSED: S4 now FAILS any house where a move-out sits UNRESOLVED while its
  name contains a valid house code.
- Portfolio scan done: 66 Boundary is the ONLY house with single-digit codes — risk contained.

Your continuation tasks, in order:

1. **Apply promote overrides** for the transfer-outs you identified: Mahyar (350 Marsden,
   Room 1175, task 1215477961015358) and the two Room 433 closers at 1/148 Liverpool
   (Umashankar, Diego — you have the task IDs). Add rows to each house's overrides.csv with
   `action=promote_move_out`, reason, `ruled_by=pilot-orchestrator`, then re-run S3→S5→S4 for
   350-marsden-rd-carlingford and 1-148-liverpool-rd-enfield. Both must show the tenancies
   CLOSED and VERIFY PASS. Check 287 Cleveland for any transfer-out subtasks of the same
   pattern while you're at it.

2. **66 Boundary reviews refresh:** the re-run changed its timeline (Rooms 1/2/3 move-outs now
   attributed). Re-dispatch `cvd-review-moveout` for 66-boundary-st-parramatta only (the
   movein review stands). Update the manifest.

3. **287 bed-code reconciliation (manual pass, no script):** for the paired bed codes
   (035A/B, 037A/B, 038B, 039A/B, 40A/B, 41), sanity-read tenancies.csv and mark phantom
   "ongoing" rows caused by one person spanning paired codes — note them in review_moveout.md
   as `bed-pairing artifact` with links, and list them in the decisions file. Do NOT
   hand-edit tenancies.csv.

4. **P5 comment sweep (the 52 `needs Asana comment check` tasks):** use the Asana connector
   (verify tool availability first; if task comments aren't retrievable via the connector,
   STOP and report BLOCKED rather than improvising). For each flagged task: pull comments,
   extract fee/bond truth, retractions, "final move out date" statements. Update fees.csv,
   overrides.csv (with `ruled_by=asana-comment`), rulings.md. Strict Task-ID matching only.
   Re-run S3→S5→S4 for any house whose dates changed.

5. **Re-run eval for all 5 houses + 342 regression:**
   `python3 pipeline/eval/run_eval.py <slug>` each. All must PASS.

6. **Update `data/batches/batch-00-pilot-REPORT.md`** (append a "Round 2" section — never
   rewrite round 1) and post the FINAL consolidated decisions list for Kurian in chat —
   every item with its Asana link inline. That list + frozen-golden candidates ends the pilot.

Same non-negotiables as before: one house per sub-agent, ≤10-line summaries, manifest updated
on every dispatch/return, everything logged to RUNLOG.md, nothing silent.

Start with task 1 now.
