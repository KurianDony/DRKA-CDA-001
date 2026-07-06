# Kurian rulings — 342 Cleveland St, Surry Hills

2026-07-05, from review of the first pipeline run:

1. **#1110 is Room 6B, not Room 7.** Letter suffix / paired code = separate BED in the same
   room (#1109 = Room 6, #1110 = bed B of Room 6). Room 6B is CLOSED since its last tenant
   (Omer) — the current Room 6 tenant takes both beds. House therefore has 6 active rooms.
2. **Room 3 (#1106) duplicate move-outs:** the 2026-07-18 task is the REAL move-out. The
   2026-05-25 eviction was RETRACTED (see last comment on that Asana task).
3. **Room 2 (#1105) Wing sequence:** moved into a Marrickville temp room first, moved into
   Room 2 on 2026-03-18, moved out 2026-06-17. The 2026-05-27 move-out task is superseded.
4. **Omer / Francis cross-house mentions:** keep them in the dataset (context for later
   issues), but they are historical (2024, outside the audit window) — not this window's events.
5. **Maintenance requests flagged in review (open rubbish/pest/cost items):** keep as-is,
   no action from the pipeline.
6. **Pre-window tenants still occupying during the window:** found manually later — the
   pipeline should NOT chase move-ins before the padded window.

Added 2026-07-05 (second review round):

7. **Move-out date rule (GENERAL):** always use the LATER of the available dates (task-name
   date, form move-out, earliest-move-out, Due Date) — UNLESS that creates a conflict, i.e.
   an overlap of MORE than 1 day with the next tenant's move-in for the same room. On
   conflict, fall back to the latest non-conflicting candidate and flag HUMAN REVIEW.
8. **Baldiri (R4) resolved:** actual move-out 2025-07-20 (tenant confirmed "final move out
   date July 20" in task comments; Final ICR 2025-07-24). Due Date 2025-07-20 is correct —
   consistent with rule 7. Where dates conflict in future, prefer an explicit "final move
   out date" statement, else the Final ICR date.
9. **Adrien (R6) resolved:** the $360 break fee DOES apply.
