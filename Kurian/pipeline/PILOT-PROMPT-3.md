# Pilot round-3 prompt (paste into the SAME pilot chat)

---

Pipeline owner update — re-read `pipeline/README.md` (Overrides + Tenant derivation sections
changed) — and Kurian has ruled on the round-2 decisions. His rulings are recorded in each
house's `rulings.md` (dated 2026-07-05, round 3). Apply them exactly; they override your
round-2 assumptions where they differ.

Owner fixes already done — do NOT redo:
- Defect #2b FIXED and re-run: all four promoted transfers CLOSE (Mahyar #1175, Umashankar +
  Diego #433, Jin #035B). 287/350/1-148 VERIFY PASS; all 5 + 342 regression eval PASS.
- NEW override action `set_move_out_date` (add `date` column, YYYY-MM-DD; exempt from
  ruling-#7 conflict pass; `ruled_by` + evidence in `reason`).

Round-3 tasks, in order:

1. **Apply Kurian's rulings** (each house's rulings.md, round-3 section):
   - 287 Sabrina: NO change — 2026-06-24 stands (retraction letter is earlier; later date wins).
   - 287 Leonardo: fees.csv correction — $1,980 was a typo; record $313 rent owed (verify the
     $313 on the task first, Task-ID check).
   - 1/148 Hassan: event date stays 2025-12-24 (paid-to). Add physical-vacate 2025-11-30 as a
     note in review_moveout.md + fees.csv evidence, NOT as the event date.
   - 350 Md Aftab: current tenant — ongoing is CORRECT; close the question.
   - 71 Harrison = #479 (fix config, re-run 71-therry, confirm Rooms 6/9 repair) and Owen
     exclude confirmed.
   - 66 Room 6 (#12): treat as full-window occupant, BUT first search the raw data for an
     in-window #12 move-out task (Task-ID verified). If one exists, it contradicts "occupied
     till now" — STOP on that item and ask Kurian; otherwise add to full_window_occupants.

2. **287 slot resolution for 40↔41 (Kurian APPROVED the method):** lay Masato, Giordano, Zaid,
   Haroun + all other #40/40A/40B/41 events into logical timeline slots (chronological,
   per-person, no overlaps within one bed) and deduce which room/bed each actually occupied.
   Apply the resolution via config aliases/overrides with the reasoning documented in
   rulings.md (`ruled_by=slot-method-per-Kurian`). Questions only if the slots genuinely
   don't resolve it.

3. **Apply any remaining comment-derived date corrections** from your sweep via
   `set_move_out_date` — but re-check each against the clarified rule first: LATER date always
   wins; earlier retraction letters and earlier physical-vacate dates do NOT override
   (they're notes). Melany (71): real move-out 7 Jan per comments vs fallback 8 Jan — apply
   7 Jan via set_move_out_date (comment states the actual date; 1-day difference, no
   conflict exemption abuse).

4. **Re-run S3→S5→S4 for every touched house + eval for all 5 + 342 regression** — all PASS.

5. **Round-3 report section + final decisions list in chat** (links inline). Should be short
   now — only genuinely new findings.

6. **Freeze goldens** for every house with no open items (expected: all 5): copy each house's
   tenancies.csv + vacancy_gaps.csv to `pipeline/eval/golden/<slug>/` as `*_golden.csv`,
   RUNLOG line each, manifest → `golden-frozen`. That closes the pilot.

Same non-negotiables: one house per sub-agent (slot work is orchestrator-level, that's fine),
≤10-line summaries, Task-ID verification only, manifest + RUNLOG updated, links in chat.
Start with task 1.
