# Double-check package — 350 Marsden Rd, Carlingford

Run: 2026-07-05 | S3→S5→S4 | **VERIFY: PASS** (0 failing checks)
Outputs: `tenancies.csv` (22 tenancies), `vacancy_gaps.csv` (15 gaps), `timeline.html`.

## Overrides applied (3 exclusions, action=exclude, ruled_by=pipeline-pending-Kurian)
1. [1215240103348912](https://app.asana.com/0/0/1215240103348912/f) — Noah, **Cancelled Sale** (non-refundable), Room 7. Not a tenancy event.
2. [1216098477207302](https://app.asana.com/0/0/1216098477207302/f) — Md Aftab Ovi, **out-of-window duplicate** move-out (Due 2026-07-03), superseded by [1215355847925679](https://app.asana.com/0/0/1215355847925679/f). Dropped per window discipline.
3. [1210517519257845](https://app.asana.com/0/0/1210517519257845/f) — Room 4 (1172) **ICR admin task**, no tenant/departure. Excluded.

## Decisions needing Kurian confirmation

### D1 — Mahyar 1175 transfer-OUT does NOT close his tenancy (PIPELINE LIMITATION) ‼️
- Mahyar's move-IN to Room 7 #1175 [1215448897492309](https://app.asana.com/0/0/1215448897492309/f) (2026-06-06) currently shows **status=ongoing** in `tenancies.csv`.
- His effective move-out — the PERM transfer-OUT of 1175 [1215478013034340](https://app.asana.com/0/0/1215478013034340/f) (2026-06-08, subtask of [1215477961015358](https://app.asana.com/0/0/1215477961015358/f)) — is marked `is_subtask=yes`, so `s3_timeline.py` **hard-skips it** before overrides are consulted. `overrides.csv` only supports `action=exclude`; there is no `include`/`force` action to surface a subtask departure.
- **Result:** Room 1175 does NOT show Mahyar's ~2-day tenancy closing, contrary to the ruling that this transfer-OUT is an effective move-out.
- **Needs:** confirmation to (a) add an `include`/`force-move_out` capability to s3 for this subtask, or (b) reclassify the transfer-out row as top-level. This is a code change outside this sub-agent's write scope — not hand-editing outputs. Flagged, not silently fixed.

### D2 — Mohd Amaan move-out room ambiguity (1173 vs 1169)
- [1211381594929794](https://app.asana.com/0/0/1211381594929794/f) resolved to **Room 5 #1173** via the Name field, but the move-out review notes the task's dropdown selected **Room 1 #1169**. Currently placed in 1173 (as pre_window move_out). Flagged for confirmation — not silently picked.

### D3 — Two ongoing/open tenancies flagged (real anomalies, hr=yes)
- **1169:** three overlapping open tenancies — Muhammad Faizan [1213025038066578](https://app.asana.com/0/0/1213025038066578/f), Dhruv [1213260614973706](https://app.asana.com/0/0/1213260614973706/f), Sudipta [1213473479987837](https://app.asana.com/0/0/1213473479987837/f). Missing move-outs for the earlier two? Confirm current occupant.
- **1170:** Malik [1210520924114448](https://app.asana.com/0/0/1210520924114448/f) (pre-window dual-occupant title) overlaps Basith/Chu Haur chain — Malik likely departed with Yasir; needs a move-out.
- **1175:** Liam [1210817071437686](https://app.asana.com/0/0/1210817071437686/f) and Mursel [1211677946964542](https://app.asana.com/0/0/1211677946964542/f) both open before later move-ins — no move-out captured. (Mursel's move-in cites foreign code #1816; attribution to 1175 is via parenthetical only — review-flagged.)

### D4 — Overlap (negative) vacancy gaps flagged (hr=yes)
- **1170:** Yasir orphan-out (2025-09-27) vs Malik pre-window move-in (2025-06-27) = -92d OVERLAP. Artifact of pre-window Malik + Yasir orphan_out; resolves once Malik gets a move-out.
- **1173:** Jason orphan-out (2026-05-22) vs Binshaj move-in (2025-10-06) = -228d OVERLAP. Jason [1214700730665014](https://app.asana.com/0/0/1214700730665014/f) has no paired move-in in-window; sits as orphan_out against Toni's ongoing tenancy.

### D5 — Benjamin Dunstan 1175 move-out possibly RETRACTED
- Move-out [1211407198436857](https://app.asana.com/0/0/1211407198436857/f) (2025-10-02) paired to move-in [1211255777029826](https://app.asana.com/0/0/1211255777029826/f). Move-out review flags subtasks "remove move out dates" — notice may be retracted, not a departure. If retracted, this pairing is spurious. Confirm in comments.

## Notes
- Config complete: rooms 1169–1176 labeled; 1172 & 1176 in `closed_rooms`.
- Unresolved move_in ×1 = Mahyar parent [1215477961015358](https://app.asana.com/0/0/1215477961015358/f) (foreign #1812) — correctly NOT attributed to 1175.
