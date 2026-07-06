---
name: cvd-review-moveout
description: Reviews each MOVE-OUT (off-boarding) task for one CVD house — dates per the later-date rule, fees applied/waived, bond — and writes one-liner verdicts with HUMAN REVIEW flags plus a fees file. Use after cvd-house-extract when asked to "review the move-outs", "check the offboarding tasks", "do fees for [house]", or as the move-out leg of a full house review.
---

# CVD Move-out Task Review (+ fees)

**Goal:** two files in `data/houses/<slug>/`:
1. `review_moveout.md` — one line per top-level move-out task.
2. `fees.csv` + `review_fees.md` — fees/waivers/bond per task.
**Input:** `moveout_filtered.csv` — top-level rows for verdicts; SUBTASK rows (`is_subtask=yes`) are evidence, especially "Endorsed to Accounting/Finance" ones. Read `rulings.md` first and apply owner decisions.

## Line format (links MANDATORY — task_url column)
```
- [<Task ID>](<task_url>) <room> | <tenant> | <one-liner>  **HUMAN REVIEW: <reason>** (only if flagged)
```

## Date checks (ruling #7 — memorize this)
- Move-out date = **LATEST** of {Due Date, Earliest Date to Move Out, date written in the task name} — team edits names later than fields, so name dates usually win.
- Exception: if the latest date overlaps the room's NEXT move-in by MORE than 1 day, that's a conflict → the earlier non-conflicting date applies → flag.
- Bad field conflicts (4+ scattered dates): an explicit "final move out date …" statement beats everything; else the Final ICR date; both usually live in COMMENTS (not in the CSV) → flag `needs Asana comment check`.
- Also flag: lease start > lease end, move-out before lease start, missing dates, retention/cancelled notices (a retention-cancelled notice is NOT a departure), relocations/transfers, duplicate move-outs for one tenant+room (one may be retracted — comments!), tasks that belong to another house (foreign address/room code in name).

## What is NOT a flag (Kurian 2026-07-05 — keep the flag rate down)
- **Lease end BEFORE move-out = NORMAL** (initial term finished, tenant went month-to-month).
  Do not flag. Note it as `+N.N months past term` instead — S5 computes `months_past_term`
  in tenancies.csv from the move-in's Agreed Lease Term; cite that number.
- **Name-date vs Due-Date mismatch that ruling #7 already resolves** (later date wins,
  automatic in S3) = a NOTE ("rule-#7 applied, using <date>"), not HUMAN REVIEW. Only flag
  when the dates conflict in a way the rule does NOT resolve (e.g. >1-day overlap fallback,
  4+ scattered dates, contradictory comments).
- **Physical vacate before paid-to date = NORMAL** — tenancy ends at the billed/paid-to date;
  note the physical date, don't flag.
- A retraction/letter dated EARLIER than the move-out date never overrides it (later stands).
Flag = Kurian must LOOK at it. If a standing rule already answers it, it's a note.

## Fee checks (REQUIRED on every move-out task)
For each task record: **fees applied** (amount + purpose: cleaning, damage, break fee, unpaid rent…), **anything waived** (+ stated reason), **bond status**, and the **evidence source** (field / notes text / which subtask).
- Sources in order: `CR Charges`, `Break Fee (if applicable)`, `Bond Held` fields → Notes → "Endorsed to Accounting" subtask Name/Notes.
- Nothing found → `NO FEE DATA IN EXPORT — check task comments in Asana`. NEVER guess amounts.
- `fees.csv` columns: `task_id,task_url,tenant,room,fees_applied,fee_breakdown,waived,bond_status,evidence_source,needs_asana_check`.

## Rules
- One house per run. No CSV edits. No notes pasted into outputs. Every flag reason ≤ ~15 words.
- Anything unresolvable → `QUESTIONS-FOR-KURIAN.md` entry (date | house | question | why | assumption).
- Finish: RUNLOG.md line (`… | review:moveout | … | done | N reviewed, M flagged, $X fees, Y need comment check`).
