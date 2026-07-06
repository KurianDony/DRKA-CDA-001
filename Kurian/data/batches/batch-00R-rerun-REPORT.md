# Batch 00R — Clean-room rerun of the 5 pilot houses — REPORT

**Date:** 2026-07-06 · **Orchestrator model:** Opus · **Purpose:** prove the upgraded pipeline + v2 skills reproduce (or beat) the pilot from scratch — lower flag rates, no cross-house junk, S6 gap-hunt integrated, roster ground-truth incorporated.

## Verdict

**The pipeline is ready for batch 01 at 8–10 houses**, with the enhancements listed under *Friction for the pipeline owner*. All five houses reproduced the pilot's filtered data exactly, flag rates fell dramatically, the gap-hunt attached the two real missed events it was designed to catch, and the 342 regression benchmark stayed green throughout.

## Per-house results

| House | Top-level counts (movein/moveout/maint) pilot→rerun | Move-in flags pilot→rerun | Move-out flag rate pilot→rerun | Gap-hunt / ruling changes | Eval vs old golden |
|---|---|---|---|---|---|
| 287 Cleveland | 39/27/58 → **identical** | 12 → **1** | 65% → **7.7%** | Leonardo #36 move-out date fixed (set_move_out_date 2025-11-22) | FAIL = intended (Leonardo pairing) |
| 1-148 Liverpool | 7/6/24 → **identical** | 4 → **1** | 62.5% → **0%** | none | **PASS** |
| 350 Marsden | 20/14/45 → **identical** | 8 → **0** | 64% → **0%** | Dhruv #1169 transfer-out promoted (2026-02-20) | FAIL = intended (Dhruv close) |
| 66 Boundary | 17/11/59 → **identical** | 10 → **3** | 91% → **45.5%** | Adriano slot-method: reassign→#7 + promote-out (2025-09-23); Room 10 double-ongoing resolved | FAIL = intended (Adriano) |
| 71 Therry | 17/15/33 → **identical** | 8 → **1** | 73% → **6.7%** | Owen #172 move-in excluded (completes never-moved-in ruling) | FAIL = intended (Owen) |
| 342 Surry Hills (benchmark) | — | — | — | untouched | **PASS (regression green)** |

Every eval FAIL maps to exactly one intended Stage C change; **zero unexplained divergences.** 1-148 and 342 pass unchanged.

## Junk removed / integrity

- **66 Boundary:** the four pilot round-1 cross-house leaks (Kapil, Gabriel, Malik, Tung) are **absent** — the ≥3-digit code-only rule held (0 code-only matches; all address-matched). This was the headline regression the rerun was meant to prove.
- **A0 gate:** cleaner than pilot (287 had one documented C3 orphan `038B` vs the pilot's two).
- **Standing rulings preserved:** every house's `overrides.csv` retained all pilot rows; new entries are additive and tagged `ruled_by=gap-hunt`.

## Gap-hunt (S6) outcome

Two genuine in-window missed events found and attached (both Asana-verified by Task ID):
- **350 Dhruv Janghu** #1169 → move-out 2026-02-20 (transfer completed: PME/Portfolio updated, OCR clear, endorsed).
- **66 Michael Adriano** → reassigned to #7 and closed 2025-09-23 (slot-method; cleared the Room 10 double-ongoing).

Plus two ruling completions surfaced by the sanity-read: 287 Leonardo (date fix) and 71 Owen (move-in exclude). All other gap-hunt candidates were correctly classified as post-window (confirmed ongoing), pre-window (recorded for stay-length), or lookalikes (ignored).

## Roster ground-truth (Tenant Name column)

The `New Raw Data - trimmed.csv` **Tenant Name** column was incorporated as the source of truth for the current occupant of each room. It resolved almost the entire double-check package: every over-occupied room's real current tenant is now known (the others departed with no move-out task in the export), vacant rooms are identified, and pre-window occupants are named. Artifact: `data/batches/batch-00R-roster-reconciliation.md`. Convention applied: `Name1 / Name2` = Name1 current, Name2 successor after Name1 departs.

## Interactive dashboard

`data/final/batch-00R-timelines.html` (self-contained) — live per-house timelines; click any tenant for move-in/move-out task links, move-in facts, signed-vs-actual stay, months-past-term, and any human-review reason; a Flag-buckets tab grouping every flag by category; vacancy gaps rendered with day counts; roster current-occupant shown per room.

## Still needs Kurian (before goldens re-freeze)

1. **Sign-off to re-freeze goldens** for the 4 changed houses (287, 350, 66, 71). 1-148 & 342 unchanged.
2. **Tangled code-crosses** (held — not auto-applied to avoid corrupting data):
   - 287 #40/#41 — a code-label swap: roster puts Udaya in #40 and Jack in #41a, but the timeline codes are crossed. Needs a room↔code ruling.
   - 71 Mischa Abbott — roster says #168A, timeline has her under #479 and #168 with José in #168A. Needs a slot ruling.
3. **Missing move-out dates:** the roster confirms many tenants departed (e.g. 287 #035A Tanguy/Chung/Roxx, 350 #1169 Faizan, 71 #479 Jayden/Mischa) but their move-out tasks are absent from the export, so they still render as "ongoing (roster: departed)". Decision: pull move-out dates from PME/Portfolio, or infer move-out = next tenant's move-in date (flagged as inferred)?
4. **Open fee/date items** from Stage B/P5: 66 Bruno (Oct 5 vs Oct 20 date), 66 Ananta (Sep 4 vs Sep 15), 66 Orisi (arrears $ not in comments), 287 Sabrina (retraction/fee/bond).

## Friction for the pipeline owner (batch-01 hardening)

1. **Wire the roster Tenant Name column into the pipeline** (S5/verify) as a ground-truth check on every ongoing tenancy + auto-flag missing move-outs. This batch reconciled it by hand; it should be automatic. *(Highest-value enhancement.)*
2. **Move-out completeness gap:** the off-boarding export is missing move-out tasks that clearly happened (roster shows the departures). This is a data-source issue, not a pipeline bug — decide how to close these (PME dates vs inference).
3. **Bed-code / code-label swaps** (287-type) recur on houses with A/B beds — the registry room↔code mapping needs a cleanup pass before those houses run.
4. **Comment-dependent items** still require a live Asana pull (P5) — connector availability is a dependency for any house with unresolved fees/dates.
5. **66-type messy houses** will sit above the 35% move-out flag target legitimately (evictions, arrears, disputes); the target should be read per-house, not as a hard gate.
