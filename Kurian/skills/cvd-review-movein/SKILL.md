---
name: cvd-review-movein
description: Reviews each MOVE-IN task for one CVD house and writes one-liner verdicts with HUMAN REVIEW flags. Use after cvd-house-extract when asked to "review the move-ins", "check the move-in tasks", "do the movein review for [house]", or as the move-in leg of a full house review.
---

# CVD Move-in Task Review

**Goal:** `data/houses/<slug>/review_movein.md` — exactly one line per top-level move-in task.
**Input:** `data/houses/<slug>/movein_filtered.csv`, rows where `is_subtask` is empty.
Also read `data/houses/<slug>/rulings.md` (owner decisions — apply them, don't re-flag settled items).

## Line format (links are MANDATORY — use the task_url column)
```
- [<Task ID>](<task_url>) <room> | <tenant first name> | <one-liner>  **HUMAN REVIEW: <reason>** (only if flagged)
```
Header: `## Move-in tasks (top-level: N reviewed, M flagged)`.

## What to check on EVERY move-in task
1. **Move-in date** = Due Date. Does any date in the Name or Notes disagree? Mismatch → flag.
2. **Payment**: `Date and Time Paid` must be ≤ move-in date. Paid-after or missing payment on a completed sale → flag.
3. **Room code**: code in Name matches Room Code column and belongs to this house? Wrong/foreign code → flag (possible other-house task).
4. **Section**: `Cancelled Sale*` → flag; it is NOT a tenancy (it will be excluded via overrides at the timeline stage).
5. **Transfers** (`Type of Transfer`, "PERM/TEMP", "OCR/ICR", arrows in name): note direction (INTO or OUT OF this room). Direction ambiguous → flag. Temp-room chains (tenant parked in another house first): describe the sequence.
6. **Duplicates/renewals**: same tenant+room twice, "LR" tasks (lease renewal — not a move-in), empty stub tasks → flag with suspected cause.
7. **New/Replacement** field vs reality (was there a prior tenant in the room?): contradiction → note.
8. `in_window=no` rows (padding zone): still review, append "outside audit window".

## Rules
- Date-altering anything (transfers, cancellations, date mismatches, duplicates) = HUMAN REVIEW — but NOT things a standing rule already answers (see rulings.md + pipeline/README.md): those are notes. Flag = Kurian must LOOK at it.
- Cross-house junk check: if the task's own address/room belongs to another property (mention of this house only in free-text notes), mark `belongs-to-other-house` — it should not be in this house's dataset; S1's ≥3-digit rule catches most, you catch the rest.
- CSV exports have NO task comments. If the decisive fact would live in comments, write `needs Asana comment check` in the line.
- Keep each line under ~25 words of judgment. No task notes pasted into the file.
- Do NOT edit any CSV. Do NOT re-date anything — that's the timeline stage's job.
- Finish: append a RUNLOG.md line (`<timestamp> | <slug> | review:movein | <who> | done | N reviewed, M flagged`).
