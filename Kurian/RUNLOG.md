# RUNLOG — CDA-001 Portfolio Diagnostic

Append-only. Format per doc 08 §7.

## 2026-07-04 (session) | operator: Kurian | houses in scope: none (session bootstrap)
2026-07-04T21:21+10:00 | - | bootstrap | orchestrator | done | Project folder empty on arrival; created data/houses, data/final, dashboards, reports, RUNLOG.md, QUESTIONS-FOR-KURIAN.md; handover pack copied to handover-house-analysis/ | —
2026-07-04T21:21+10:00 | - | smoke-test | orchestrator | PASS | Asana get_me: GID 1208280814774236, ws 1201789231542521 [task:get_me]; respond.io list_channels: 6 channels incl. 348751 "CDA Co Living " (trailing space); known-fact: task 1215355847925607 in Off boarding team 1206596901916034 [task:1215355847925607] | —
2026-07-04T21:21+10:00 | - | state-check | orchestrator | done | data/ empty — no houses extracted; no kickoff inputs on file; 6(b) end-to-end pilot (350 Marsden) not yet run | —
Decisions: none
Blockers: KURIAN BLOCKER: kickoff inputs missing (05 §6) — no house→entity/area mapping, no audit-window dates, no roster confirmation, no seeded workstream files (active_properties.csv, offboarding-final-v4.csv etc. per 00 step 3). Needed to unblock: Kurian to supply kickoff inputs and copy the 00 step-3 file list into the project folder.
Next: run one-time 6(b) pilot (350 Marsden updates) — does not require kickoff inputs
2026-07-04T21:22+10:00 | - | decision | orchestrator | done | Kurian: hold work until kickoff inputs supplied; 6(b) pilot deferred to next session | decision: wait for kickoff inputs

## 2026-07-05 (session) | operator: Kurian | houses in scope: 342-cleveland-st-surry-hills
2026-07-05T11:13+10:00 | 342-cleveland-st-surry-hills | s1-filter:movein | script:s1_filter_house.py | done | 102 kept of 19476 (57 in window; 0 room-code-only)
2026-07-05T11:13+10:00 | 342-cleveland-st-surry-hills | s1-filter:moveout | script:s1_filter_house.py | done | 159 kept of 23810 (158 in window; 1 room-code-only)
2026-07-05T11:13+10:00 | 342-cleveland-st-surry-hills | s1-filter:maintenance | script:s1_filter_house.py | done | 264 kept of 49791 (157 in window; 0 room-code-only)
2026-07-05T11:14+10:00 | 342-cleveland-st-surry-hills | s1-filter:movein | script:s1_filter_house.py | done | 102 kept of 19476 (57 in window; 0 room-code-only)
2026-07-05T11:14+10:00 | 342-cleveland-st-surry-hills | s1-filter:moveout | script:s1_filter_house.py | done | 159 kept of 23810 (158 in window; 1 room-code-only)
2026-07-05T11:14+10:00 | 342-cleveland-st-surry-hills | s1-filter:maintenance | script:s1_filter_house.py | done | 264 kept of 49791 (157 in window; 0 room-code-only)
2026-07-05T11:14+10:00 | 342-cleveland-st-surry-hills | s2-preflag:movein | script:s2_preflag.py | done | 20/102 flagged for human review (tc:20 kw:0 inc:0)
2026-07-05T11:14+10:00 | 342-cleveland-st-surry-hills | s2-preflag:moveout | script:s2_preflag.py | done | 68/159 flagged for human review (tc:32 kw:0 inc:36)
2026-07-05T11:14+10:00 | 342-cleveland-st-surry-hills | s2-preflag:maintenance | script:s2_preflag.py | done | 2/264 flagged for human review (tc:2 kw:0 inc:0)
2026-07-05T11:14+10:00 | 342-cleveland-st-surry-hills | s3-timeline | script:s3_timeline.py | done | 146 events; unresolved rooms: {'moveout': 4, 'maintenance': 84}
2026-07-05T11:14+10:00 | 342-cleveland-st-surry-hills | s1-filter:movein | script:s1_filter_house.py | done | 102 kept of 19476 (57 in window; 0 room-code-only)
2026-07-05T11:14+10:00 | 342-cleveland-st-surry-hills | s1-filter:moveout | script:s1_filter_house.py | done | 159 kept of 23810 (158 in window; 1 room-code-only)
2026-07-05T11:14+10:00 | 342-cleveland-st-surry-hills | s1-filter:maintenance | script:s1_filter_house.py | done | 264 kept of 49791 (157 in window; 0 room-code-only)
2026-07-05T11:14+10:00 | 342-cleveland-st-surry-hills | s2-preflag:movein | script:s2_preflag.py | done | 20/102 flagged for human review (tc:20 kw:0 inc:0)
2026-07-05T11:14+10:00 | 342-cleveland-st-surry-hills | s2-preflag:moveout | script:s2_preflag.py | done | 68/159 flagged for human review (tc:32 kw:0 inc:36)
2026-07-05T11:14+10:00 | 342-cleveland-st-surry-hills | s2-preflag:maintenance | script:s2_preflag.py | done | 2/264 flagged for human review (tc:2 kw:0 inc:0)
2026-07-05T11:14+10:00 | 342-cleveland-st-surry-hills | s3-timeline | script:s3_timeline.py | done | 146 events; unresolved rooms: {'moveout': 2, 'maintenance': 83}
2026-07-05T11:18+10:00 | 342-cleveland-st-surry-hills | s4-verify | script:s4_verify.py | FAIL | 2 failing checks
2026-07-05T11:19+10:00 | 342-cleveland-st-surry-hills | s3-timeline | script:s3_timeline.py | done | 143 events; unresolved rooms: {'moveout': 2, 'maintenance': 81}; deduped: {'maintenance': 3}
2026-07-05T11:19+10:00 | 342-cleveland-st-surry-hills | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T11:53+10:00 | 342-cleveland-st-surry-hills | s1-filter:movein | script:s1_filter_house.py | done | 43 kept of 19476 (59 out-of-window dropped; 0 no-date kept)
2026-07-05T11:53+10:00 | 342-cleveland-st-surry-hills | s1-filter:moveout | script:s1_filter_house.py | done | 20 kept of 23810 (139 out-of-window dropped; 0 no-date kept)
2026-07-05T11:53+10:00 | 342-cleveland-st-surry-hills | s1-filter:maintenance | script:s1_filter_house.py | done | 104 kept of 49791 (160 out-of-window dropped; 0 no-date kept)
2026-07-05T11:53+10:00 | 342-cleveland-st-surry-hills | s2-preflag:movein | script:s2_preflag.py | done | 14/43 flagged for human review (tc:14 kw:0 inc:0)
2026-07-05T11:53+10:00 | 342-cleveland-st-surry-hills | s2-preflag:moveout | script:s2_preflag.py | done | 17/20 flagged for human review (tc:11 kw:0 inc:6)
2026-07-05T11:53+10:00 | 342-cleveland-st-surry-hills | s2-preflag:maintenance | script:s2_preflag.py | done | 1/104 flagged for human review (tc:1 kw:0 inc:0)
2026-07-05T11:53+10:00 | 342-cleveland-st-surry-hills | s3-timeline | script:s3_timeline.py | done | 61 events; unresolved rooms: {'maintenance': 31}; deduped: {}
2026-07-05T11:54+10:00 | 342-cleveland-st-surry-hills | s3-timeline | script:s3_timeline.py | done | 59 events; unresolved rooms: {'maintenance': 31}; deduped: {}
2026-07-05T11:58+10:00 | 342-cleveland-st-surry-hills | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T12:30+10:00 | 342-cleveland-st-surry-hills | s3-timeline | script:s3_timeline.py | done | 59 events; unresolved rooms: {'maintenance': 31}; deduped: {}
2026-07-05T12:30+10:00 | 342-cleveland-st-surry-hills | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T12:36+10:00 | 342-cleveland-st-surry-hills | s5-tenancies-html | script:s5_tenancies_html.py | done | 16 tenancies, 9 gaps, html rendered
2026-07-05T12:38+10:00 | 342-cleveland-st-surry-hills | s3-timeline | script:s3_timeline.py | done | 57 events; unresolved rooms: {'maintenance': 31}; deduped: {}
2026-07-05T12:38+10:00 | 342-cleveland-st-surry-hills | s5-tenancies-html | script:s5_tenancies_html.py | done | 15 tenancies, 7 gaps, html rendered
2026-07-05T12:38+10:00 | 342-cleveland-st-surry-hills | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T12:39+10:00 | 342-cleveland-st-surry-hills | s5-tenancies-html | script:s5_tenancies_html.py | done | 15 tenancies, 7 gaps, html rendered
2026-07-05T13:08+10:00 | 342-cleveland-st-surry-hills | s1-filter:movein | script:s1_filter_house.py | done | 43 kept of 19476 (59 out-of-window dropped; 0 no-date kept)
2026-07-05T13:08+10:00 | 342-cleveland-st-surry-hills | s1-filter:moveout | script:s1_filter_house.py | done | 20 kept of 23810 (139 out-of-window dropped; 0 no-date kept)
2026-07-05T13:08+10:00 | 342-cleveland-st-surry-hills | s1-filter:maintenance | script:s1_filter_house.py | done | 104 kept of 49791 (160 out-of-window dropped; 0 no-date kept)
2026-07-05T13:08+10:00 | 342-cleveland-st-surry-hills | s2-preflag:movein | script:s2_preflag.py | done | 14/43 flagged for human review (tc:14 kw:0 inc:0)
2026-07-05T13:08+10:00 | 342-cleveland-st-surry-hills | s2-preflag:moveout | script:s2_preflag.py | done | 17/20 flagged for human review (tc:11 kw:0 inc:6)
2026-07-05T13:08+10:00 | 342-cleveland-st-surry-hills | s2-preflag:maintenance | script:s2_preflag.py | done | 1/104 flagged for human review (tc:1 kw:0 inc:0)
2026-07-05T13:08+10:00 | 342-cleveland-st-surry-hills | s3-timeline | script:s3_timeline.py | done | 57 events; unresolved rooms: {'maintenance': 31}; deduped: {}
2026-07-05T13:08+10:00 | 342-cleveland-st-surry-hills | s5-tenancies-html | script:s5_tenancies_html.py | done | 15 tenancies, 7 gaps, html rendered
2026-07-05T13:08+10:00 | 342-cleveland-st-surry-hills | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T13:08+10:00 | 342-cleveland-st-surry-hills | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-05_342-cleveland-st-surry-hills.md

2026-07-05T03:10+10:00 | 342-cleveland-st-surry-hills | skills+eval | orchestrator | done | 4 skills packaged; eval harness + golden frozen; eval PASS
2026-07-05T03:17+10:00 | - | runbook | orchestrator | done | BATCH-RUNBOOK.md written; comments deferred to P5 sweep per Kurian; task-ID-only verification rule
2026-07-05T14:23+10:00 | - | p0-registry | script:p0_build_registry.py | done | 225 houses, 1 code dupes, 3 tightened patterns
2026-07-05T14:25+10:00 | - | p0-registry | script:p0_build_registry.py | done | 225 houses, 1 code dupes, 3 tightened patterns
2026-07-05T14:32+10:00 | 287-cleveland-st-redfern | a0-roomcode-check | script:a0_roomcode_check.py | FAIL | 2 problems, 7 notes
2026-07-05T14:32+10:00 | 1-148-liverpool-rd-enfield | a0-roomcode-check | script:a0_roomcode_check.py | PASS | 0 problems, 0 notes
2026-07-05T14:32+10:00 | 350-marsden-rd-carlingford | a0-roomcode-check | script:a0_roomcode_check.py | PASS | 0 problems, 1 notes
2026-07-05T14:32+10:00 | 66-boundary-st-parramatta | a0-roomcode-check | script:a0_roomcode_check.py | PASS | 0 problems, 0 notes
2026-07-05T14:32+10:00 | 71-therry-street-avalon-beach | a0-roomcode-check | script:a0_roomcode_check.py | PASS | 0 problems, 3 notes
2026-07-05T04:33+10:00 | - | a0-gate-added | orchestrator | done | A0 room-code integrity gate scripted + wired into runbook/pilot prompt; first run: 287-cleveland FAIL (orphan beds 038B/039B), 4 houses PASS
2026-07-05T04:39+10:00 | - | kickoff-cleared | operator: Kurian | done | All questions resolved: room-code issues handled at A0 per batch (~3 expected portfolio-wide); 2026-07-04 CSV snapshot locked as permanent data source (covers full window). Pilot cleared to start.
2026-07-05T14:45+10:00 | 287-cleveland-st-redfern | a0-roomcode-check | script:a0_roomcode_check.py | FAIL | 2 problems, 7 notes
2026-07-05T14:45+10:00 | 1-148-liverpool-rd-enfield | a0-roomcode-check | script:a0_roomcode_check.py | PASS | 0 problems, 0 notes
2026-07-05T14:45+10:00 | 350-marsden-rd-carlingford | a0-roomcode-check | script:a0_roomcode_check.py | PASS | 0 problems, 1 notes
2026-07-05T14:45+10:00 | 66-boundary-st-parramatta | a0-roomcode-check | script:a0_roomcode_check.py | PASS | 0 problems, 0 notes
2026-07-05T14:45+10:00 | 71-therry-street-avalon-beach | a0-roomcode-check | script:a0_roomcode_check.py | PASS | 0 problems, 3 notes

## 2026-07-05 (session) | operator: Kurian | PILOT BATCH 00 orchestration
2026-07-05T14:45+10:00 | - | a0-gate | orchestrator | done | 5 pilot entries copied registry→houses.json (hand-curated). A0: 4 PASS (1-148-liverpool, 350-marsden, 66-boundary, 71-therry). 287-cleveland C3 orphan beds 038B/039B → DOCUMENTED-PROCEED per policy (beds of Room 4/Room 5; assumption in houses.json + QUESTIONS-FOR-KURIAN.md). No houses parked. Batch cleared for Stage A extraction.
2026-07-05T14:46+10:00 | 287-cleveland-st-redfern | s1-filter:movein | script:s1_filter_house.py | done | 181 kept of 19476 (117 out-of-window dropped; 0 no-date kept)
2026-07-05T14:46+10:00 | 287-cleveland-st-redfern | s1-filter:moveout | script:s1_filter_house.py | done | 68 kept of 23810 (176 out-of-window dropped; 0 no-date kept)
2026-07-05T14:46+10:00 | 287-cleveland-st-redfern | s1-filter:maintenance | script:s1_filter_house.py | done | 177 kept of 49791 (215 out-of-window dropped; 0 no-date kept)
2026-07-05T14:46+10:00 | 287-cleveland-st-redfern | s2-preflag:movein | script:s2_preflag.py | done | 47/181 flagged for human review (tc:40 kw:0 inc:7)
2026-07-05T14:46+10:00 | 287-cleveland-st-redfern | s2-preflag:moveout | script:s2_preflag.py | done | 50/68 flagged for human review (tc:21 kw:0 inc:29)
2026-07-05T14:46+10:00 | 287-cleveland-st-redfern | s2-preflag:maintenance | script:s2_preflag.py | done | 7/177 flagged for human review (tc:4 kw:3 inc:0)
2026-07-05T14:46+10:00 | 287-cleveland-st-redfern | s3-timeline | script:s3_timeline.py | done | 124 events; unresolved rooms: {'movein': 11, 'moveout': 7, 'maintenance': 54}; deduped: {}
2026-07-05T14:46+10:00 | 66-boundary-st-parramatta | s1-filter:movein | script:s1_filter_house.py | done | 58 kept of 19476 (81 out-of-window dropped; 0 no-date kept)
2026-07-05T14:46+10:00 | 66-boundary-st-parramatta | s1-filter:moveout | script:s1_filter_house.py | done | 62 kept of 23810 (102 out-of-window dropped; 0 no-date kept)
2026-07-05T14:46+10:00 | 66-boundary-st-parramatta | s1-filter:maintenance | script:s1_filter_house.py | done | 129 kept of 49791 (215 out-of-window dropped; 0 no-date kept)
2026-07-05T14:46+10:00 | 1-148-liverpool-rd-enfield | s1-filter:movein | script:s1_filter_house.py | done | 29 kept of 19476 (10 out-of-window dropped; 0 no-date kept)
2026-07-05T14:46+10:00 | 1-148-liverpool-rd-enfield | s1-filter:moveout | script:s1_filter_house.py | done | 17 kept of 23810 (20 out-of-window dropped; 0 no-date kept)
2026-07-05T14:46+10:00 | 1-148-liverpool-rd-enfield | s1-filter:maintenance | script:s1_filter_house.py | done | 54 kept of 49791 (56 out-of-window dropped; 0 no-date kept)
2026-07-05T14:46+10:00 | 350-marsden-rd-carlingford | s1-filter:movein | script:s1_filter_house.py | done | 74 kept of 19476 (14 out-of-window dropped; 0 no-date kept)
2026-07-05T14:46+10:00 | 350-marsden-rd-carlingford | s1-filter:moveout | script:s1_filter_house.py | done | 20 kept of 23810 (10 out-of-window dropped; 0 no-date kept)
2026-07-05T14:46+10:00 | 350-marsden-rd-carlingford | s1-filter:maintenance | script:s1_filter_house.py | done | 112 kept of 49791 (51 out-of-window dropped; 0 no-date kept)
2026-07-05T14:46+10:00 | 66-boundary-st-parramatta | s2-preflag:movein | script:s2_preflag.py | done | 19/58 flagged for human review (tc:17 kw:0 inc:2)
2026-07-05T14:46+10:00 | 66-boundary-st-parramatta | s2-preflag:moveout | script:s2_preflag.py | done | 44/62 flagged for human review (tc:12 kw:0 inc:32)
2026-07-05T14:46+10:00 | 66-boundary-st-parramatta | s2-preflag:maintenance | script:s2_preflag.py | done | 0/129 flagged for human review (tc:0 kw:0 inc:0)
2026-07-05T14:46+10:00 | 350-marsden-rd-carlingford | s2-preflag:movein | script:s2_preflag.py | done | 24/74 flagged for human review (tc:23 kw:0 inc:1)
2026-07-05T14:46+10:00 | 350-marsden-rd-carlingford | s2-preflag:moveout | script:s2_preflag.py | done | 14/20 flagged for human review (tc:13 kw:0 inc:1)
2026-07-05T14:46+10:00 | 350-marsden-rd-carlingford | s2-preflag:maintenance | script:s2_preflag.py | done | 1/112 flagged for human review (tc:1 kw:0 inc:0)
2026-07-05T14:46+10:00 | 350-marsden-rd-carlingford | s3-timeline | script:s3_timeline.py | done | 79 events; unresolved rooms: {'movein': 1, 'maintenance': 37}; deduped: {}
2026-07-05T14:46+10:00 | 1-148-liverpool-rd-enfield | s2-preflag:movein | script:s2_preflag.py | done | 11/29 flagged for human review (tc:10 kw:0 inc:1)
2026-07-05T14:46+10:00 | 1-148-liverpool-rd-enfield | s2-preflag:moveout | script:s2_preflag.py | done | 16/17 flagged for human review (tc:8 kw:0 inc:8)
2026-07-05T14:46+10:00 | 1-148-liverpool-rd-enfield | s2-preflag:maintenance | script:s2_preflag.py | done | 3/54 flagged for human review (tc:2 kw:1 inc:0)
2026-07-05T14:46+10:00 | 1-148-liverpool-rd-enfield | s3-timeline | script:s3_timeline.py | done | 37 events; unresolved rooms: {'maintenance': 20}; deduped: {}
2026-07-05T14:46+10:00 | 66-boundary-st-parramatta | s3-timeline | script:s3_timeline.py | done | 91 events; unresolved rooms: {'movein': 3, 'moveout': 5, 'maintenance': 57}; deduped: {}
2026-07-05T14:46+10:00 | 1-148-liverpool-rd-enfield | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T14:47+10:00 | 71-therry-street-avalon-beach | s1-filter:movein | script:s1_filter_house.py | done | 60 kept of 19476 (20 out-of-window dropped; 0 no-date kept)
2026-07-05T14:47+10:00 | 71-therry-street-avalon-beach | s1-filter:moveout | script:s1_filter_house.py | done | 32 kept of 23810 (104 out-of-window dropped; 0 no-date kept)
2026-07-05T14:47+10:00 | 71-therry-street-avalon-beach | s1-filter:maintenance | script:s1_filter_house.py | done | 104 kept of 49791 (78 out-of-window dropped; 0 no-date kept)
2026-07-05T14:47+10:00 | 71-therry-street-avalon-beach | s2-preflag:movein | script:s2_preflag.py | done | 22/60 flagged for human review (tc:20 kw:0 inc:3)
2026-07-05T14:47+10:00 | 71-therry-street-avalon-beach | s2-preflag:moveout | script:s2_preflag.py | done | 27/32 flagged for human review (tc:12 kw:1 inc:14)
2026-07-05T14:47+10:00 | 71-therry-street-avalon-beach | s2-preflag:maintenance | script:s2_preflag.py | done | 2/104 flagged for human review (tc:1 kw:1 inc:0)
2026-07-05T14:47+10:00 | 71-therry-street-avalon-beach | s3-timeline | script:s3_timeline.py | done | 65 events; unresolved rooms: {'moveout': 1, 'maintenance': 26}; deduped: {}
2026-07-05T14:47+10:00 | 350-marsden-rd-carlingford | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T14:47+10:00 | 287-cleveland-st-redfern | s1-filter:movein | script:s1_filter_house.py | done | 181 kept of 19476 (117 out-of-window dropped; 0 no-date kept)
2026-07-05T14:47+10:00 | 287-cleveland-st-redfern | s1-filter:moveout | script:s1_filter_house.py | done | 68 kept of 23810 (176 out-of-window dropped; 0 no-date kept)
2026-07-05T14:47+10:00 | 287-cleveland-st-redfern | s1-filter:maintenance | script:s1_filter_house.py | done | 177 kept of 49791 (215 out-of-window dropped; 0 no-date kept)
2026-07-05T14:47+10:00 | 287-cleveland-st-redfern | s2-preflag:movein | script:s2_preflag.py | done | 47/181 flagged for human review (tc:40 kw:0 inc:7)
2026-07-05T14:47+10:00 | 287-cleveland-st-redfern | s2-preflag:moveout | script:s2_preflag.py | done | 50/68 flagged for human review (tc:21 kw:0 inc:29)
2026-07-05T14:47+10:00 | 287-cleveland-st-redfern | s2-preflag:maintenance | script:s2_preflag.py | done | 7/177 flagged for human review (tc:4 kw:3 inc:0)
2026-07-05T14:47+10:00 | 287-cleveland-st-redfern | s3-timeline | script:s3_timeline.py | done | 124 events; unresolved rooms: {'maintenance': 52}; deduped: {}
2026-07-05T14:47+10:00 | 287-cleveland-st-redfern | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T14:47+10:00 | 66-boundary-st-parramatta | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T14:49+10:00 | 71-therry-street-avalon-beach | s1-filter:movein | script:s1_filter_house.py | done | 60 kept of 19476 (20 out-of-window dropped; 0 no-date kept)
2026-07-05T14:49+10:00 | 71-therry-street-avalon-beach | s1-filter:moveout | script:s1_filter_house.py | done | 32 kept of 23810 (104 out-of-window dropped; 0 no-date kept)
2026-07-05T14:49+10:00 | 71-therry-street-avalon-beach | s1-filter:maintenance | script:s1_filter_house.py | done | 104 kept of 49791 (78 out-of-window dropped; 0 no-date kept)
2026-07-05T14:49+10:00 | 71-therry-street-avalon-beach | s2-preflag:movein | script:s2_preflag.py | done | 22/60 flagged for human review (tc:20 kw:0 inc:3)
2026-07-05T14:49+10:00 | 71-therry-street-avalon-beach | s2-preflag:moveout | script:s2_preflag.py | done | 27/32 flagged for human review (tc:12 kw:1 inc:14)
2026-07-05T14:49+10:00 | 71-therry-street-avalon-beach | s2-preflag:maintenance | script:s2_preflag.py | done | 2/104 flagged for human review (tc:1 kw:1 inc:0)
2026-07-05T14:49+10:00 | 71-therry-street-avalon-beach | s3-timeline | script:s3_timeline.py | done | 65 events; unresolved rooms: {'maintenance': 25}; deduped: {}
2026-07-05T14:49+10:00 | 71-therry-street-avalon-beach | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T04:52:42Z | 1-148-liverpool-rd-enfield | review:movein | movein-subagent | done | 7 reviewed, 4 flagged
2026-07-05T04:53+0000 | 287-cleveland-st-redfern | review:movein | opus-subagent | done | 39 reviewed, 12 flagged
2026-07-05T14:52+10:00 | 350-marsden-rd-carlingford | review:movein | agent:movein-review | done | 20 reviewed, 8 flagged
2026-07-05T04:55:00Z | 1-148-liverpool-rd-enfield | review:moveout | moveout-subagent | done | 8 reviewed, 5 flagged, $1259.80 fees, 8 need comment check
2026-07-05T04:53+0000 | 66-boundary-st-parramatta | review:movein | opus-subagent | done | 17 reviewed, 10 flagged
2026-07-05T14:53+10:00 | 71-therry-street-avalon-beach | review:movein | opus-subagent | done | 17 reviewed, 8 flagged
2026-07-05 | 350-marsden-rd-carlingford | review:moveout | opus | done | 14 reviewed, 9 flagged, $4010 fees ($3290 if Dunstan retracted), 14 need comment check
2026-07-05T05:00+0000 | 71-therry-street-avalon-beach | review:moveout | opus-subagent | done | 15 reviewed, 11 flagged, $660 fees, 12 need comment check
2026-07-05T15:10+10:00 | 66-boundary-st-parramatta | review:moveout | opus-subagent | done | 11 reviewed, 10 flagged, $3700 fees, 7 need comment check
2026-07-05T15:30+10:00 | 287-cleveland-st-redfern | review:moveout | opus-subagent | done | 26 reviewed, 17 flagged, $4700 fees ($3080 break + $1620 charges; $300 waived), 11 need comment check
2026-07-05T15:20+10:00 | ALL-5-pilot | reviews | orchestrator | done | movein+moveout+fees complete for all 5. Spot-audit 2 lines/house by Task ID vs CSV: 10/10 clean (dates, codes, paid, ruling#7 all consistent). Minor: some move-out links omit trailing /f.
2026-07-05T15:00+10:00 | 287-cleveland-st-redfern | s3-timeline | script:s3_timeline.py | done | 117 events; unresolved rooms: {'maintenance': 52}; deduped: {}
2026-07-05T15:00+10:00 | 287-cleveland-st-redfern | s5-tenancies-html | script:s5_tenancies_html.py | done | 44 tenancies, 23 gaps, html rendered
2026-07-05T15:00+10:00 | 287-cleveland-st-redfern | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T15:00+10:00 | 350-marsden-rd-carlingford | s3-timeline | script:s3_timeline.py | done | 76 events; unresolved rooms: {'movein': 1, 'maintenance': 37}; deduped: {}
2026-07-05T15:00+10:00 | 350-marsden-rd-carlingford | s5-tenancies-html | script:s5_tenancies_html.py | done | 22 tenancies, 15 gaps, html rendered
2026-07-05T15:00+10:00 | 350-marsden-rd-carlingford | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T15:00+10:00 | 1-148-liverpool-rd-enfield | s3-timeline | script:s3_timeline.py | done | 35 events; unresolved rooms: {'maintenance': 20}; deduped: {}
2026-07-05T15:00+10:00 | 1-148-liverpool-rd-enfield | s5-tenancies-html | script:s5_tenancies_html.py | done | 9 tenancies, 6 gaps, html rendered
2026-07-05T15:00+10:00 | 1-148-liverpool-rd-enfield | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T15:00+10:00 | 66-boundary-st-parramatta | s3-timeline | script:s3_timeline.py | done | 87 events; unresolved rooms: {'movein': 1, 'moveout': 5, 'maintenance': 57}; deduped: {}
2026-07-05T15:01+10:00 | 66-boundary-st-parramatta | s5-tenancies-html | script:s5_tenancies_html.py | done | 14 tenancies, 8 gaps, html rendered
2026-07-05T15:01+10:00 | 66-boundary-st-parramatta | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T15:01+10:00 | 71-therry-street-avalon-beach | s3-timeline | script:s3_timeline.py | done | 64 events; unresolved rooms: {'maintenance': 25}; deduped: {}
2026-07-05T15:01+10:00 | 71-therry-street-avalon-beach | s5-tenancies-html | script:s5_tenancies_html.py | done | 25 tenancies, 15 gaps, html rendered
2026-07-05T15:01+10:00 | 71-therry-street-avalon-beach | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T15:30+10:00 | 287-cleveland-st-redfern | double-check-package | sub-agent | sent | 44 tenancies, 23 gaps, 7 overrides, VERIFY PASS, 18 confirmations requested
2026-07-05T15:05+10:00 | 1-148-liverpool-rd-enfield | double-check-package | agent:tenancy-timeline | sent | 4 confirmations requested (2 overrides, Diego-keep, Subhojit-fresh); anomaly: 433 three-ongoing (transfer move-outs are subtasks)
2026-07-05T15:05+10:00 | 350-marsden-rd-carlingford | double-check-package | agent:tenancy-timeline | sent | 22 tenancies, 15 gaps, 3 overrides; VERIFY PASS; 5 confirmations requested (Mahyar-1175 subtask not closing, Mohd Amaan 1173/1169, 2-ongoing x3 rooms, 2 overlaps, Dunstan retraction)
2026-07-05T16:05+10:00 | 66-boundary-st-parramatta | double-check-package | agent:tenancy-timeline | sent | 6 confirmations requested (4 override-exclusions, cross-house transfer 1211433880033810, single-digit #7/#8/#9 move-out resolver gap stranding 5 move-outs; anomalies: Room 6 empty, Rm4 & Rm1 two-ongoing)
2026-07-05T15:05+10:00 | 342-cleveland-st-surry-hills | s1-filter:movein | script:s1_filter_house.py | done | 43 kept of 19476 (59 out-of-window dropped; 0 no-date kept)
2026-07-05T15:05+10:00 | 342-cleveland-st-surry-hills | s1-filter:moveout | script:s1_filter_house.py | done | 20 kept of 23810 (139 out-of-window dropped; 0 no-date kept)
2026-07-05T15:05+10:00 | 342-cleveland-st-surry-hills | s1-filter:maintenance | script:s1_filter_house.py | done | 104 kept of 49791 (160 out-of-window dropped; 0 no-date kept)
2026-07-05T15:05+10:00 | 342-cleveland-st-surry-hills | s2-preflag:movein | script:s2_preflag.py | done | 14/43 flagged for human review (tc:14 kw:0 inc:0)
2026-07-05T15:05+10:00 | 342-cleveland-st-surry-hills | s2-preflag:moveout | script:s2_preflag.py | done | 17/20 flagged for human review (tc:11 kw:0 inc:6)
2026-07-05T15:05+10:00 | 342-cleveland-st-surry-hills | s2-preflag:maintenance | script:s2_preflag.py | done | 1/104 flagged for human review (tc:1 kw:0 inc:0)
2026-07-05T15:05+10:00 | 342-cleveland-st-surry-hills | s3-timeline | script:s3_timeline.py | done | 57 events; unresolved rooms: {'maintenance': 31}; deduped: {}
2026-07-05T15:05+10:00 | 342-cleveland-st-surry-hills | s5-tenancies-html | script:s5_tenancies_html.py | done | 15 tenancies, 7 gaps, html rendered
2026-07-05T15:05+10:00 | 342-cleveland-st-surry-hills | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T15:05+10:00 | 342-cleveland-st-surry-hills | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-05_342-cleveland-st-surry-hills.md
2026-07-05T15:05+10:00 | 287-cleveland-st-redfern | s1-filter:movein | script:s1_filter_house.py | done | 181 kept of 19476 (117 out-of-window dropped; 0 no-date kept)
2026-07-05T15:05+10:00 | 287-cleveland-st-redfern | s1-filter:moveout | script:s1_filter_house.py | done | 68 kept of 23810 (176 out-of-window dropped; 0 no-date kept)
2026-07-05T15:05+10:00 | 287-cleveland-st-redfern | s1-filter:maintenance | script:s1_filter_house.py | done | 177 kept of 49791 (215 out-of-window dropped; 0 no-date kept)
2026-07-05T15:05+10:00 | 287-cleveland-st-redfern | s2-preflag:movein | script:s2_preflag.py | done | 47/181 flagged for human review (tc:40 kw:0 inc:7)
2026-07-05T15:05+10:00 | 287-cleveland-st-redfern | s2-preflag:moveout | script:s2_preflag.py | done | 50/68 flagged for human review (tc:21 kw:0 inc:29)
2026-07-05T15:05+10:00 | 287-cleveland-st-redfern | s2-preflag:maintenance | script:s2_preflag.py | done | 7/177 flagged for human review (tc:4 kw:3 inc:0)
2026-07-05T15:05+10:00 | 287-cleveland-st-redfern | s3-timeline | script:s3_timeline.py | done | 117 events; unresolved rooms: {'maintenance': 52}; deduped: {}
2026-07-05T15:05+10:00 | 287-cleveland-st-redfern | s5-tenancies-html | script:s5_tenancies_html.py | done | 44 tenancies, 23 gaps, html rendered
2026-07-05T15:05+10:00 | 287-cleveland-st-redfern | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T15:05+10:00 | 287-cleveland-st-redfern | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-05_287-cleveland-st-redfern.md
2026-07-05T15:05+10:00 | 1-148-liverpool-rd-enfield | s1-filter:movein | script:s1_filter_house.py | done | 29 kept of 19476 (10 out-of-window dropped; 0 no-date kept)
2026-07-05T15:05+10:00 | 1-148-liverpool-rd-enfield | s1-filter:moveout | script:s1_filter_house.py | done | 17 kept of 23810 (20 out-of-window dropped; 0 no-date kept)
2026-07-05T15:05+10:00 | 1-148-liverpool-rd-enfield | s1-filter:maintenance | script:s1_filter_house.py | done | 54 kept of 49791 (56 out-of-window dropped; 0 no-date kept)
2026-07-05T15:05+10:00 | 1-148-liverpool-rd-enfield | s2-preflag:movein | script:s2_preflag.py | done | 11/29 flagged for human review (tc:10 kw:0 inc:1)
2026-07-05T15:05+10:00 | 1-148-liverpool-rd-enfield | s2-preflag:moveout | script:s2_preflag.py | done | 16/17 flagged for human review (tc:8 kw:0 inc:8)
2026-07-05T15:05+10:00 | 1-148-liverpool-rd-enfield | s2-preflag:maintenance | script:s2_preflag.py | done | 3/54 flagged for human review (tc:2 kw:1 inc:0)
2026-07-05T15:05+10:00 | 1-148-liverpool-rd-enfield | s3-timeline | script:s3_timeline.py | done | 35 events; unresolved rooms: {'maintenance': 20}; deduped: {}
2026-07-05T15:05+10:00 | 1-148-liverpool-rd-enfield | s5-tenancies-html | script:s5_tenancies_html.py | done | 9 tenancies, 6 gaps, html rendered
2026-07-05T15:05+10:00 | 1-148-liverpool-rd-enfield | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T15:05+10:00 | 1-148-liverpool-rd-enfield | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-05_1-148-liverpool-rd-enfield.md
2026-07-05T15:05+10:00 | 350-marsden-rd-carlingford | s1-filter:movein | script:s1_filter_house.py | done | 74 kept of 19476 (14 out-of-window dropped; 0 no-date kept)
2026-07-05T15:05+10:00 | 350-marsden-rd-carlingford | s1-filter:moveout | script:s1_filter_house.py | done | 20 kept of 23810 (10 out-of-window dropped; 0 no-date kept)
2026-07-05T15:05+10:00 | 350-marsden-rd-carlingford | s1-filter:maintenance | script:s1_filter_house.py | done | 112 kept of 49791 (51 out-of-window dropped; 0 no-date kept)
2026-07-05T15:05+10:00 | 350-marsden-rd-carlingford | s2-preflag:movein | script:s2_preflag.py | done | 24/74 flagged for human review (tc:23 kw:0 inc:1)
2026-07-05T15:05+10:00 | 350-marsden-rd-carlingford | s2-preflag:moveout | script:s2_preflag.py | done | 14/20 flagged for human review (tc:13 kw:0 inc:1)
2026-07-05T15:05+10:00 | 350-marsden-rd-carlingford | s2-preflag:maintenance | script:s2_preflag.py | done | 1/112 flagged for human review (tc:1 kw:0 inc:0)
2026-07-05T15:05+10:00 | 350-marsden-rd-carlingford | s3-timeline | script:s3_timeline.py | done | 76 events; unresolved rooms: {'movein': 1, 'maintenance': 37}; deduped: {}
2026-07-05T15:05+10:00 | 350-marsden-rd-carlingford | s5-tenancies-html | script:s5_tenancies_html.py | done | 22 tenancies, 15 gaps, html rendered
2026-07-05T15:05+10:00 | 350-marsden-rd-carlingford | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T15:05+10:00 | 350-marsden-rd-carlingford | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-05_350-marsden-rd-carlingford.md
2026-07-05T15:05+10:00 | 66-boundary-st-parramatta | s1-filter:movein | script:s1_filter_house.py | done | 58 kept of 19476 (81 out-of-window dropped; 0 no-date kept)
2026-07-05T15:05+10:00 | 66-boundary-st-parramatta | s1-filter:moveout | script:s1_filter_house.py | done | 62 kept of 23810 (102 out-of-window dropped; 0 no-date kept)
2026-07-05T15:05+10:00 | 66-boundary-st-parramatta | s1-filter:maintenance | script:s1_filter_house.py | done | 129 kept of 49791 (215 out-of-window dropped; 0 no-date kept)
2026-07-05T15:05+10:00 | 66-boundary-st-parramatta | s2-preflag:movein | script:s2_preflag.py | done | 19/58 flagged for human review (tc:17 kw:0 inc:2)
2026-07-05T15:05+10:00 | 66-boundary-st-parramatta | s2-preflag:moveout | script:s2_preflag.py | done | 44/62 flagged for human review (tc:12 kw:0 inc:32)
2026-07-05T15:05+10:00 | 66-boundary-st-parramatta | s2-preflag:maintenance | script:s2_preflag.py | done | 0/129 flagged for human review (tc:0 kw:0 inc:0)
2026-07-05T15:05+10:00 | 66-boundary-st-parramatta | s3-timeline | script:s3_timeline.py | done | 87 events; unresolved rooms: {'movein': 1, 'moveout': 5, 'maintenance': 57}; deduped: {}
2026-07-05T15:05+10:00 | 66-boundary-st-parramatta | s5-tenancies-html | script:s5_tenancies_html.py | done | 14 tenancies, 8 gaps, html rendered
2026-07-05T15:05+10:00 | 66-boundary-st-parramatta | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T15:05+10:00 | 66-boundary-st-parramatta | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-05_66-boundary-st-parramatta.md
2026-07-05T15:05+10:00 | 71-therry-street-avalon-beach | s1-filter:movein | script:s1_filter_house.py | done | 60 kept of 19476 (20 out-of-window dropped; 0 no-date kept)
2026-07-05T15:05+10:00 | 71-therry-street-avalon-beach | s1-filter:moveout | script:s1_filter_house.py | done | 32 kept of 23810 (104 out-of-window dropped; 0 no-date kept)
2026-07-05T15:05+10:00 | 71-therry-street-avalon-beach | s1-filter:maintenance | script:s1_filter_house.py | done | 104 kept of 49791 (78 out-of-window dropped; 0 no-date kept)
2026-07-05T15:05+10:00 | 71-therry-street-avalon-beach | s2-preflag:movein | script:s2_preflag.py | done | 22/60 flagged for human review (tc:20 kw:0 inc:3)
2026-07-05T15:05+10:00 | 71-therry-street-avalon-beach | s2-preflag:moveout | script:s2_preflag.py | done | 27/32 flagged for human review (tc:12 kw:1 inc:14)
2026-07-05T15:05+10:00 | 71-therry-street-avalon-beach | s2-preflag:maintenance | script:s2_preflag.py | done | 2/104 flagged for human review (tc:1 kw:1 inc:0)
2026-07-05T15:05+10:00 | 71-therry-street-avalon-beach | s3-timeline | script:s3_timeline.py | done | 64 events; unresolved rooms: {'maintenance': 25}; deduped: {}
2026-07-05T15:05+10:00 | 71-therry-street-avalon-beach | s5-tenancies-html | script:s5_tenancies_html.py | done | 25 tenancies, 15 gaps, html rendered
2026-07-05T15:05+10:00 | 71-therry-street-avalon-beach | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T15:05+10:00 | 71-therry-street-avalon-beach | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-05_71-therry-street-avalon-beach.md
2026-07-05T15:35+10:00 | ALL-5-pilot | timeline+eval | orchestrator | done | S5 timelines built, all VERIFY PASS. Evals: all 5 PASS (no goldens yet) + 342 golden regression PASS. Tenancies: 287=44,1-148=9,350=22,66=14,71=25.
2026-07-05T15:35+10:00 | - | batch-report | orchestrator | done | data/batches/batch-00-pilot-REPORT.md written. 2 script defects found (single-digit #code regex in lib/common.py; subtask transfer-out skipped by S3), eval blind spot, flag-rate high vs baseline, export lacks fee/bond fields (52 comment-checks). Decisions list sent to Kurian.
2026-07-05T15:13+10:00 | 66-boundary-st-parramatta | s3-timeline | script:s3_timeline.py | done | 87 events; unresolved rooms: {'movein': 1, 'maintenance': 55}; deduped: {}
2026-07-05T15:13+10:00 | 66-boundary-st-parramatta | s5-tenancies-html | script:s5_tenancies_html.py | done | 17 tenancies, 11 gaps, html rendered
2026-07-05T15:13+10:00 | 66-boundary-st-parramatta | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T15:13+10:00 | 342-cleveland-st-surry-hills | s1-filter:movein | script:s1_filter_house.py | done | 43 kept of 19476 (59 out-of-window dropped; 0 no-date kept)
2026-07-05T15:13+10:00 | 342-cleveland-st-surry-hills | s1-filter:moveout | script:s1_filter_house.py | done | 20 kept of 23810 (139 out-of-window dropped; 0 no-date kept)
2026-07-05T15:13+10:00 | 342-cleveland-st-surry-hills | s1-filter:maintenance | script:s1_filter_house.py | done | 104 kept of 49791 (160 out-of-window dropped; 0 no-date kept)
2026-07-05T15:13+10:00 | 342-cleveland-st-surry-hills | s2-preflag:movein | script:s2_preflag.py | done | 14/43 flagged for human review (tc:14 kw:0 inc:0)
2026-07-05T15:13+10:00 | 342-cleveland-st-surry-hills | s2-preflag:moveout | script:s2_preflag.py | done | 17/20 flagged for human review (tc:11 kw:0 inc:6)
2026-07-05T15:13+10:00 | 342-cleveland-st-surry-hills | s2-preflag:maintenance | script:s2_preflag.py | done | 1/104 flagged for human review (tc:1 kw:0 inc:0)
2026-07-05T15:13+10:00 | 342-cleveland-st-surry-hills | s3-timeline | script:s3_timeline.py | done | 57 events; unresolved rooms: {'maintenance': 31}; deduped: {}
2026-07-05T15:13+10:00 | 342-cleveland-st-surry-hills | s5-tenancies-html | script:s5_tenancies_html.py | done | 15 tenancies, 7 gaps, html rendered
2026-07-05T15:13+10:00 | 342-cleveland-st-surry-hills | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T15:13+10:00 | 342-cleveland-st-surry-hills | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-05_342-cleveland-st-surry-hills.md
2026-07-05T05:14+10:00 | - | pilot-defect-fixes | orchestrator | done | Defect#1 regex 1-4 digits (66-boundary re-run: 0 stranded, VERIFY PASS incl new room-resolution gate); Defect#2 promote_move_out override action in S3+S4; 342 golden regression PASS
2026-07-05T16:32+10:00 | 350-marsden-rd-carlingford | s3-timeline | script:s3_timeline.py | done | 77 events; unresolved rooms: {'movein': 1, 'maintenance': 37}; deduped: {'moveout': 1}
2026-07-05T16:32+10:00 | 350-marsden-rd-carlingford | s5-tenancies-html | script:s5_tenancies_html.py | done | 23 tenancies, 16 gaps, html rendered
2026-07-05T16:32+10:00 | 350-marsden-rd-carlingford | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T16:32+10:00 | 1-148-liverpool-rd-enfield | s3-timeline | script:s3_timeline.py | done | 37 events; unresolved rooms: {'maintenance': 20}; deduped: {'moveout': 2}
2026-07-05T16:32+10:00 | 1-148-liverpool-rd-enfield | s5-tenancies-html | script:s5_tenancies_html.py | done | 11 tenancies, 6 gaps, html rendered
2026-07-05T16:32+10:00 | 1-148-liverpool-rd-enfield | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T16:32+10:00 | 287-cleveland-st-redfern | s3-timeline | script:s3_timeline.py | done | 118 events; unresolved rooms: {'maintenance': 52}; deduped: {'moveout': 1}
2026-07-05T16:32+10:00 | 287-cleveland-st-redfern | s5-tenancies-html | script:s5_tenancies_html.py | done | 45 tenancies, 24 gaps, html rendered
2026-07-05T16:32+10:00 | 287-cleveland-st-redfern | s4-verify | script:s4_verify.py | PASS | 0 failing checks

## 2026-07-05 (session) | PILOT ROUND 2
2026-07-05T16:10+10:00 | 350,1-148,287 | promote-overrides | orchestrator | PARTIAL | Added promote_move_out overrides: 350 Mahyar 1215478013034340(#1175); 1-148 Umashankar 1213450431910672 + Diego 1213815366058872(#433); 287 Jin 1213589504292986(#035B, same-pattern found in scan). S3 created move_out events, all VERIFY PASS. BUT tenancies NOT closed — DEFECT #2b: promoted events get tenant from empty "Tenant Name" column (s3 line 103), so S5 name-pairing (line 55) leaves them orphan_out + move_in ongoing. Overrides retained; closure blocked pending owner fix (derive tenant from task_name on promote, or chronological fallback in S5).
2026-07-05T16:30+10:00 | 287-cleveland-st-redfern | bed-recon | orchestrator | done | Manual bed-pairing pass: marked 6 phantom-ongoing rows as bed-pairing artifacts in review_moveout.md + double_check.md (Francisco 035A/B, Syed 38/038B same-room; Masato/Giordano/Zaid/Haroun across 40↔41 — room ambiguity flagged). No tenancies.csv hand-edits.
2026-07-05T06:44+10:00 | 1-148-liverpool-rd-enfield | p5-asana-comment-sweep | connector:asana get_task | done | 9 tasks swept; 8/8 fees resolved (needs_asana_check=no); 0 retractions->excludes; 1 final-move-out-date finding (Hassan S3 2025-12-25 vs vacate 11/29 vs compliance 12/24); Umashankar $209.80 attributed to primary 1213450431910672 (dup 1213291114470159 stays excluded); no overrides added so s3/s5/s4 NOT re-run (fees.csv/rulings.md are review artifacts, not pipeline inputs); last VERIFY still PASS
2026-07-05T16:45+10:00 | 71-therry-street-avalon-beach | s3-timeline | script:s3_timeline.py | done | 63 events; unresolved rooms: {'maintenance': 25}; deduped: {}
2026-07-05T16:45+10:00 | 71-therry-street-avalon-beach | s5-tenancies-html | script:s5_tenancies_html.py | done | 25 tenancies, 15 gaps, html rendered
2026-07-05T16:45+10:00 | 71-therry-street-avalon-beach | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T16:45+10:00 | 350-marsden-rd-carlingford | s3-timeline | script:s3_timeline.py | done | 76 events; unresolved rooms: {'movein': 1, 'maintenance': 37}; deduped: {'moveout': 1}
2026-07-05T16:45+10:00 | 350-marsden-rd-carlingford | s5-tenancies-html | script:s5_tenancies_html.py | done | 23 tenancies, 16 gaps, html rendered
2026-07-05T16:45+10:00 | 350-marsden-rd-carlingford | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05 R2-T4 P5 Asana comment sweep 350-marsden-rd-carlingford — 18 flagged tasks swept (14 fees + 4 movein). 10 fees resolved w/ amounts; Islam #1171 break fee $1760 WAIVED (+SD refund); Patrick #1175 BOND FORFEITED. 1 retraction→exclude (1215355847925679 Md Aftab move-out); Dunstan 1211407198436857 NOT retracted (re-proceeded, kept). Re-ran S3→S5→S4: VERIFY PASS (76 events, 23 tenancies).
2026-07-05T16:46+10:00 | 287-cleveland-st-redfern | s3-timeline | script:s3_timeline.py | done | 117 events; unresolved rooms: {'maintenance': 52}; deduped: {'moveout': 1}
2026-07-05T16:46+10:00 | 287-cleveland-st-redfern | s5-tenancies-html | script:s5_tenancies_html.py | done | 45 tenancies, 24 gaps, html rendered
2026-07-05T16:46+10:00 | 287-cleveland-st-redfern | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05 | R2-T4 P5 Asana comment sweep | 287-cleveland-st-redfern | 13 flagged tasks swept (12 fees.csv needs_asana_check=yes + 1 movein prior-room-chain) | fees resolved: 10 (Santiago $75, Chanwoo $222.50, Zaid $310, Haroun-Dec9 $75, Camila $160, Lisa-MO $100, Federico $0-waived, Giordano $0-full-refund, Haroun-Nov19 retracted, LisaRELOC excluded) | still-silent: 2 (Sabrina 1215821222380914 no fee data; Leonardo 1211929755311339 break fee amount unconfirmed) | retractions->excludes added: 1 (1210737767129253 Lisa OFFER RELOC) | final-move-out-date findings: 1 (Sabrina retraction letter contradicts active MO 2026-06-24 - needs Kurian) | movein 1213976823034682 prior-room resolved (#28 @ 285 Cleveland, diff building) | re-run: s3->s5->s4 done, VERIFY=PASS (117 events, 45 tenancies)
2026-07-05T16:47+10:00 | 342-cleveland-st-surry-hills | s1-filter:movein | script:s1_filter_house.py | done | 43 kept of 19476 (59 out-of-window dropped; 0 no-date kept)
2026-07-05T16:47+10:00 | 342-cleveland-st-surry-hills | s1-filter:moveout | script:s1_filter_house.py | done | 20 kept of 23810 (139 out-of-window dropped; 0 no-date kept)
2026-07-05T16:47+10:00 | 342-cleveland-st-surry-hills | s1-filter:maintenance | script:s1_filter_house.py | done | 104 kept of 49791 (160 out-of-window dropped; 0 no-date kept)
2026-07-05T16:47+10:00 | 342-cleveland-st-surry-hills | s2-preflag:movein | script:s2_preflag.py | done | 14/43 flagged for human review (tc:14 kw:0 inc:0)
2026-07-05T16:47+10:00 | 342-cleveland-st-surry-hills | s2-preflag:moveout | script:s2_preflag.py | done | 17/20 flagged for human review (tc:11 kw:0 inc:6)
2026-07-05T16:47+10:00 | 342-cleveland-st-surry-hills | s2-preflag:maintenance | script:s2_preflag.py | done | 1/104 flagged for human review (tc:1 kw:0 inc:0)
2026-07-05T16:47+10:00 | 342-cleveland-st-surry-hills | s3-timeline | script:s3_timeline.py | done | 57 events; unresolved rooms: {'maintenance': 31}; deduped: {}
2026-07-05T16:47+10:00 | 342-cleveland-st-surry-hills | s5-tenancies-html | script:s5_tenancies_html.py | done | 15 tenancies, 7 gaps, html rendered
2026-07-05T16:47+10:00 | 342-cleveland-st-surry-hills | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T16:47+10:00 | 342-cleveland-st-surry-hills | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-05_342-cleveland-st-surry-hills.md
2026-07-05T16:47+10:00 | 287-cleveland-st-redfern | s1-filter:movein | script:s1_filter_house.py | done | 181 kept of 19476 (117 out-of-window dropped; 0 no-date kept)
2026-07-05T16:48+10:00 | 287-cleveland-st-redfern | s1-filter:moveout | script:s1_filter_house.py | done | 68 kept of 23810 (176 out-of-window dropped; 0 no-date kept)
2026-07-05T16:48+10:00 | 287-cleveland-st-redfern | s1-filter:maintenance | script:s1_filter_house.py | done | 177 kept of 49791 (215 out-of-window dropped; 0 no-date kept)
2026-07-05T16:48+10:00 | 287-cleveland-st-redfern | s2-preflag:movein | script:s2_preflag.py | done | 47/181 flagged for human review (tc:40 kw:0 inc:7)
2026-07-05T16:48+10:00 | 287-cleveland-st-redfern | s2-preflag:moveout | script:s2_preflag.py | done | 50/68 flagged for human review (tc:21 kw:0 inc:29)
2026-07-05T16:48+10:00 | 287-cleveland-st-redfern | s2-preflag:maintenance | script:s2_preflag.py | done | 7/177 flagged for human review (tc:4 kw:3 inc:0)
2026-07-05T16:48+10:00 | 287-cleveland-st-redfern | s3-timeline | script:s3_timeline.py | done | 117 events; unresolved rooms: {'maintenance': 52}; deduped: {'moveout': 1}
2026-07-05T16:48+10:00 | 287-cleveland-st-redfern | s5-tenancies-html | script:s5_tenancies_html.py | done | 45 tenancies, 24 gaps, html rendered
2026-07-05T16:48+10:00 | 287-cleveland-st-redfern | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T16:48+10:00 | 287-cleveland-st-redfern | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-05_287-cleveland-st-redfern.md
2026-07-05T16:48+10:00 | 1-148-liverpool-rd-enfield | s1-filter:movein | script:s1_filter_house.py | done | 29 kept of 19476 (10 out-of-window dropped; 0 no-date kept)
2026-07-05T16:48+10:00 | 1-148-liverpool-rd-enfield | s1-filter:moveout | script:s1_filter_house.py | done | 17 kept of 23810 (20 out-of-window dropped; 0 no-date kept)
2026-07-05T16:48+10:00 | 1-148-liverpool-rd-enfield | s1-filter:maintenance | script:s1_filter_house.py | done | 54 kept of 49791 (56 out-of-window dropped; 0 no-date kept)
2026-07-05T16:48+10:00 | 1-148-liverpool-rd-enfield | s2-preflag:movein | script:s2_preflag.py | done | 11/29 flagged for human review (tc:10 kw:0 inc:1)
2026-07-05T16:48+10:00 | 1-148-liverpool-rd-enfield | s2-preflag:moveout | script:s2_preflag.py | done | 16/17 flagged for human review (tc:8 kw:0 inc:8)
2026-07-05T16:48+10:00 | 1-148-liverpool-rd-enfield | s2-preflag:maintenance | script:s2_preflag.py | done | 3/54 flagged for human review (tc:2 kw:1 inc:0)
2026-07-05T16:48+10:00 | 1-148-liverpool-rd-enfield | s3-timeline | script:s3_timeline.py | done | 37 events; unresolved rooms: {'maintenance': 20}; deduped: {'moveout': 2}
2026-07-05T16:48+10:00 | 1-148-liverpool-rd-enfield | s5-tenancies-html | script:s5_tenancies_html.py | done | 11 tenancies, 6 gaps, html rendered
2026-07-05T16:48+10:00 | 1-148-liverpool-rd-enfield | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T16:48+10:00 | 1-148-liverpool-rd-enfield | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-05_1-148-liverpool-rd-enfield.md
2026-07-05T16:48+10:00 | 350-marsden-rd-carlingford | s1-filter:movein | script:s1_filter_house.py | done | 74 kept of 19476 (14 out-of-window dropped; 0 no-date kept)
2026-07-05T16:48+10:00 | 350-marsden-rd-carlingford | s1-filter:moveout | script:s1_filter_house.py | done | 20 kept of 23810 (10 out-of-window dropped; 0 no-date kept)
2026-07-05T16:48+10:00 | 350-marsden-rd-carlingford | s1-filter:maintenance | script:s1_filter_house.py | done | 112 kept of 49791 (51 out-of-window dropped; 0 no-date kept)
2026-07-05T16:48+10:00 | 350-marsden-rd-carlingford | s2-preflag:movein | script:s2_preflag.py | done | 24/74 flagged for human review (tc:23 kw:0 inc:1)
2026-07-05T16:48+10:00 | 350-marsden-rd-carlingford | s2-preflag:moveout | script:s2_preflag.py | done | 14/20 flagged for human review (tc:13 kw:0 inc:1)
2026-07-05T16:48+10:00 | 350-marsden-rd-carlingford | s2-preflag:maintenance | script:s2_preflag.py | done | 1/112 flagged for human review (tc:1 kw:0 inc:0)
2026-07-05T16:48+10:00 | 350-marsden-rd-carlingford | s3-timeline | script:s3_timeline.py | done | 76 events; unresolved rooms: {'movein': 1, 'maintenance': 37}; deduped: {'moveout': 1}
2026-07-05T16:48+10:00 | 350-marsden-rd-carlingford | s5-tenancies-html | script:s5_tenancies_html.py | done | 23 tenancies, 16 gaps, html rendered
2026-07-05T16:48+10:00 | 350-marsden-rd-carlingford | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T16:48+10:00 | 350-marsden-rd-carlingford | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-05_350-marsden-rd-carlingford.md
2026-07-05T16:48+10:00 | 66-boundary-st-parramatta | s1-filter:movein | script:s1_filter_house.py | done | 59 kept of 19476 (83 out-of-window dropped; 0 no-date kept)
2026-07-05T16:48+10:00 | 66-boundary-st-parramatta | s1-filter:moveout | script:s1_filter_house.py | done | 65 kept of 23810 (102 out-of-window dropped; 0 no-date kept)
2026-07-05T16:48+10:00 | 66-boundary-st-parramatta | s1-filter:maintenance | script:s1_filter_house.py | done | 133 kept of 49791 (224 out-of-window dropped; 0 no-date kept)
2026-07-05T16:48+10:00 | 66-boundary-st-parramatta | s2-preflag:movein | script:s2_preflag.py | done | 20/59 flagged for human review (tc:18 kw:0 inc:2)
2026-07-05T16:48+10:00 | 66-boundary-st-parramatta | s2-preflag:moveout | script:s2_preflag.py | done | 47/65 flagged for human review (tc:15 kw:0 inc:32)
2026-07-05T16:48+10:00 | 66-boundary-st-parramatta | s2-preflag:maintenance | script:s2_preflag.py | done | 0/133 flagged for human review (tc:0 kw:0 inc:0)
2026-07-05T16:48+10:00 | 66-boundary-st-parramatta | s3-timeline | script:s3_timeline.py | done | 95 events; unresolved rooms: {'movein': 1, 'maintenance': 55}; deduped: {}
2026-07-05T16:48+10:00 | 66-boundary-st-parramatta | s5-tenancies-html | script:s5_tenancies_html.py | done | 21 tenancies, 12 gaps, html rendered
2026-07-05T16:48+10:00 | 66-boundary-st-parramatta | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T16:48+10:00 | 66-boundary-st-parramatta | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-05_66-boundary-st-parramatta.md
2026-07-05T16:48+10:00 | 71-therry-street-avalon-beach | s1-filter:movein | script:s1_filter_house.py | done | 60 kept of 19476 (20 out-of-window dropped; 0 no-date kept)
2026-07-05T16:48+10:00 | 71-therry-street-avalon-beach | s1-filter:moveout | script:s1_filter_house.py | done | 32 kept of 23810 (104 out-of-window dropped; 0 no-date kept)
2026-07-05T16:48+10:00 | 71-therry-street-avalon-beach | s1-filter:maintenance | script:s1_filter_house.py | done | 104 kept of 49791 (78 out-of-window dropped; 0 no-date kept)
2026-07-05T16:48+10:00 | 71-therry-street-avalon-beach | s2-preflag:movein | script:s2_preflag.py | done | 22/60 flagged for human review (tc:20 kw:0 inc:3)
2026-07-05T16:48+10:00 | 71-therry-street-avalon-beach | s2-preflag:moveout | script:s2_preflag.py | done | 27/32 flagged for human review (tc:12 kw:1 inc:14)
2026-07-05T16:48+10:00 | 71-therry-street-avalon-beach | s2-preflag:maintenance | script:s2_preflag.py | done | 2/104 flagged for human review (tc:1 kw:1 inc:0)
2026-07-05T16:48+10:00 | 71-therry-street-avalon-beach | s3-timeline | script:s3_timeline.py | done | 63 events; unresolved rooms: {'maintenance': 25}; deduped: {}
2026-07-05T16:48+10:00 | 71-therry-street-avalon-beach | s5-tenancies-html | script:s5_tenancies_html.py | done | 25 tenancies, 15 gaps, html rendered
2026-07-05T16:48+10:00 | 71-therry-street-avalon-beach | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T16:48+10:00 | 71-therry-street-avalon-beach | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-05_71-therry-street-avalon-beach.md
2026-07-05T17:05+10:00 | ALL-6 | eval | orchestrator | PASS | Round 2 eval: all 5 pilot houses PASS + 342 golden regression PASS. All 6 VERIFY PASS. New room-resolution S4 gate green everywhere (66 single-digit codes resolved).
2026-07-05T17:08+10:00 | 287-cleveland-st-redfern | s3-timeline | script:s3_timeline.py | done | 117 events; unresolved rooms: {'maintenance': 52}; deduped: {'moveout': 1}
2026-07-05T17:08+10:00 | 287-cleveland-st-redfern | s5-tenancies-html | script:s5_tenancies_html.py | done | 44 tenancies, 23 gaps, html rendered
2026-07-05T17:08+10:00 | 287-cleveland-st-redfern | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T17:08+10:00 | 350-marsden-rd-carlingford | s3-timeline | script:s3_timeline.py | done | 76 events; unresolved rooms: {'movein': 1, 'maintenance': 37}; deduped: {'moveout': 1}
2026-07-05T17:08+10:00 | 350-marsden-rd-carlingford | s5-tenancies-html | script:s5_tenancies_html.py | done | 22 tenancies, 15 gaps, html rendered
2026-07-05T17:08+10:00 | 350-marsden-rd-carlingford | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T17:08+10:00 | 1-148-liverpool-rd-enfield | s3-timeline | script:s3_timeline.py | done | 37 events; unresolved rooms: {'maintenance': 20}; deduped: {'moveout': 2}
2026-07-05T17:08+10:00 | 1-148-liverpool-rd-enfield | s5-tenancies-html | script:s5_tenancies_html.py | done | 9 tenancies, 6 gaps, html rendered
2026-07-05T17:08+10:00 | 1-148-liverpool-rd-enfield | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T17:08+10:00 | 342-cleveland-st-surry-hills | s1-filter:movein | script:s1_filter_house.py | done | 43 kept of 19476 (59 out-of-window dropped; 0 no-date kept)
2026-07-05T17:08+10:00 | 342-cleveland-st-surry-hills | s1-filter:moveout | script:s1_filter_house.py | done | 20 kept of 23810 (139 out-of-window dropped; 0 no-date kept)
2026-07-05T17:08+10:00 | 342-cleveland-st-surry-hills | s1-filter:maintenance | script:s1_filter_house.py | done | 104 kept of 49791 (160 out-of-window dropped; 0 no-date kept)
2026-07-05T17:08+10:00 | 342-cleveland-st-surry-hills | s2-preflag:movein | script:s2_preflag.py | done | 14/43 flagged for human review (tc:14 kw:0 inc:0)
2026-07-05T17:08+10:00 | 342-cleveland-st-surry-hills | s2-preflag:moveout | script:s2_preflag.py | done | 17/20 flagged for human review (tc:11 kw:0 inc:6)
2026-07-05T17:08+10:00 | 342-cleveland-st-surry-hills | s2-preflag:maintenance | script:s2_preflag.py | done | 1/104 flagged for human review (tc:1 kw:0 inc:0)
2026-07-05T17:08+10:00 | 342-cleveland-st-surry-hills | s3-timeline | script:s3_timeline.py | done | 57 events; unresolved rooms: {'maintenance': 31}; deduped: {}
2026-07-05T17:08+10:00 | 342-cleveland-st-surry-hills | s5-tenancies-html | script:s5_tenancies_html.py | done | 15 tenancies, 7 gaps, html rendered
2026-07-05T17:08+10:00 | 342-cleveland-st-surry-hills | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T17:08+10:00 | 342-cleveland-st-surry-hills | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-05_342-cleveland-st-surry-hills.md
2026-07-05T17:08+10:00 | 287-cleveland-st-redfern | s1-filter:movein | script:s1_filter_house.py | done | 181 kept of 19476 (117 out-of-window dropped; 0 no-date kept)
2026-07-05T17:08+10:00 | 287-cleveland-st-redfern | s1-filter:moveout | script:s1_filter_house.py | done | 68 kept of 23810 (176 out-of-window dropped; 0 no-date kept)
2026-07-05T17:09+10:00 | 287-cleveland-st-redfern | s1-filter:maintenance | script:s1_filter_house.py | done | 177 kept of 49791 (215 out-of-window dropped; 0 no-date kept)
2026-07-05T17:09+10:00 | 287-cleveland-st-redfern | s2-preflag:movein | script:s2_preflag.py | done | 47/181 flagged for human review (tc:40 kw:0 inc:7)
2026-07-05T17:09+10:00 | 287-cleveland-st-redfern | s2-preflag:moveout | script:s2_preflag.py | done | 50/68 flagged for human review (tc:21 kw:0 inc:29)
2026-07-05T17:09+10:00 | 287-cleveland-st-redfern | s2-preflag:maintenance | script:s2_preflag.py | done | 7/177 flagged for human review (tc:4 kw:3 inc:0)
2026-07-05T17:09+10:00 | 287-cleveland-st-redfern | s3-timeline | script:s3_timeline.py | done | 117 events; unresolved rooms: {'maintenance': 52}; deduped: {'moveout': 1}
2026-07-05T17:09+10:00 | 287-cleveland-st-redfern | s5-tenancies-html | script:s5_tenancies_html.py | done | 44 tenancies, 23 gaps, html rendered
2026-07-05T17:09+10:00 | 287-cleveland-st-redfern | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T17:09+10:00 | 287-cleveland-st-redfern | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-05_287-cleveland-st-redfern.md
2026-07-05T17:09+10:00 | 350-marsden-rd-carlingford | s1-filter:movein | script:s1_filter_house.py | done | 74 kept of 19476 (14 out-of-window dropped; 0 no-date kept)
2026-07-05T17:09+10:00 | 350-marsden-rd-carlingford | s1-filter:moveout | script:s1_filter_house.py | done | 20 kept of 23810 (10 out-of-window dropped; 0 no-date kept)
2026-07-05T17:09+10:00 | 350-marsden-rd-carlingford | s1-filter:maintenance | script:s1_filter_house.py | done | 112 kept of 49791 (51 out-of-window dropped; 0 no-date kept)
2026-07-05T17:09+10:00 | 350-marsden-rd-carlingford | s2-preflag:movein | script:s2_preflag.py | done | 24/74 flagged for human review (tc:23 kw:0 inc:1)
2026-07-05T17:09+10:00 | 350-marsden-rd-carlingford | s2-preflag:moveout | script:s2_preflag.py | done | 14/20 flagged for human review (tc:13 kw:0 inc:1)
2026-07-05T17:09+10:00 | 350-marsden-rd-carlingford | s2-preflag:maintenance | script:s2_preflag.py | done | 1/112 flagged for human review (tc:1 kw:0 inc:0)
2026-07-05T17:09+10:00 | 350-marsden-rd-carlingford | s3-timeline | script:s3_timeline.py | done | 76 events; unresolved rooms: {'movein': 1, 'maintenance': 37}; deduped: {'moveout': 1}
2026-07-05T17:09+10:00 | 350-marsden-rd-carlingford | s5-tenancies-html | script:s5_tenancies_html.py | done | 22 tenancies, 15 gaps, html rendered
2026-07-05T17:09+10:00 | 350-marsden-rd-carlingford | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T17:09+10:00 | 350-marsden-rd-carlingford | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-05_350-marsden-rd-carlingford.md
2026-07-05T17:09+10:00 | 1-148-liverpool-rd-enfield | s1-filter:movein | script:s1_filter_house.py | done | 29 kept of 19476 (10 out-of-window dropped; 0 no-date kept)
2026-07-05T17:09+10:00 | 1-148-liverpool-rd-enfield | s1-filter:moveout | script:s1_filter_house.py | done | 17 kept of 23810 (20 out-of-window dropped; 0 no-date kept)
2026-07-05T17:09+10:00 | 1-148-liverpool-rd-enfield | s1-filter:maintenance | script:s1_filter_house.py | done | 54 kept of 49791 (56 out-of-window dropped; 0 no-date kept)
2026-07-05T17:09+10:00 | 1-148-liverpool-rd-enfield | s2-preflag:movein | script:s2_preflag.py | done | 11/29 flagged for human review (tc:10 kw:0 inc:1)
2026-07-05T17:09+10:00 | 1-148-liverpool-rd-enfield | s2-preflag:moveout | script:s2_preflag.py | done | 16/17 flagged for human review (tc:8 kw:0 inc:8)
2026-07-05T17:09+10:00 | 1-148-liverpool-rd-enfield | s2-preflag:maintenance | script:s2_preflag.py | done | 3/54 flagged for human review (tc:2 kw:1 inc:0)
2026-07-05T17:09+10:00 | 1-148-liverpool-rd-enfield | s3-timeline | script:s3_timeline.py | done | 37 events; unresolved rooms: {'maintenance': 20}; deduped: {'moveout': 2}
2026-07-05T17:09+10:00 | 1-148-liverpool-rd-enfield | s5-tenancies-html | script:s5_tenancies_html.py | done | 9 tenancies, 6 gaps, html rendered
2026-07-05T17:09+10:00 | 1-148-liverpool-rd-enfield | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T17:09+10:00 | 1-148-liverpool-rd-enfield | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-05_1-148-liverpool-rd-enfield.md
2026-07-05T17:09+10:00 | 66-boundary-st-parramatta | s1-filter:movein | script:s1_filter_house.py | done | 59 kept of 19476 (83 out-of-window dropped; 0 no-date kept)
2026-07-05T17:09+10:00 | 66-boundary-st-parramatta | s1-filter:moveout | script:s1_filter_house.py | done | 65 kept of 23810 (102 out-of-window dropped; 0 no-date kept)
2026-07-05T17:09+10:00 | 66-boundary-st-parramatta | s1-filter:maintenance | script:s1_filter_house.py | done | 133 kept of 49791 (224 out-of-window dropped; 0 no-date kept)
2026-07-05T17:09+10:00 | 66-boundary-st-parramatta | s2-preflag:movein | script:s2_preflag.py | done | 20/59 flagged for human review (tc:18 kw:0 inc:2)
2026-07-05T17:09+10:00 | 66-boundary-st-parramatta | s2-preflag:moveout | script:s2_preflag.py | done | 47/65 flagged for human review (tc:15 kw:0 inc:32)
2026-07-05T17:09+10:00 | 66-boundary-st-parramatta | s2-preflag:maintenance | script:s2_preflag.py | done | 0/133 flagged for human review (tc:0 kw:0 inc:0)
2026-07-05T17:09+10:00 | 66-boundary-st-parramatta | s3-timeline | script:s3_timeline.py | done | 95 events; unresolved rooms: {'movein': 1, 'maintenance': 55}; deduped: {}
2026-07-05T17:09+10:00 | 66-boundary-st-parramatta | s5-tenancies-html | script:s5_tenancies_html.py | done | 21 tenancies, 12 gaps, html rendered
2026-07-05T17:09+10:00 | 66-boundary-st-parramatta | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T17:09+10:00 | 66-boundary-st-parramatta | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-05_66-boundary-st-parramatta.md
2026-07-05T17:09+10:00 | 71-therry-street-avalon-beach | s1-filter:movein | script:s1_filter_house.py | done | 60 kept of 19476 (20 out-of-window dropped; 0 no-date kept)
2026-07-05T17:09+10:00 | 71-therry-street-avalon-beach | s1-filter:moveout | script:s1_filter_house.py | done | 32 kept of 23810 (104 out-of-window dropped; 0 no-date kept)
2026-07-05T17:09+10:00 | 71-therry-street-avalon-beach | s1-filter:maintenance | script:s1_filter_house.py | done | 104 kept of 49791 (78 out-of-window dropped; 0 no-date kept)
2026-07-05T17:09+10:00 | 71-therry-street-avalon-beach | s2-preflag:movein | script:s2_preflag.py | done | 22/60 flagged for human review (tc:20 kw:0 inc:3)
2026-07-05T17:09+10:00 | 71-therry-street-avalon-beach | s2-preflag:moveout | script:s2_preflag.py | done | 27/32 flagged for human review (tc:12 kw:1 inc:14)
2026-07-05T17:09+10:00 | 71-therry-street-avalon-beach | s2-preflag:maintenance | script:s2_preflag.py | done | 2/104 flagged for human review (tc:1 kw:1 inc:0)
2026-07-05T17:09+10:00 | 71-therry-street-avalon-beach | s3-timeline | script:s3_timeline.py | done | 63 events; unresolved rooms: {'maintenance': 25}; deduped: {}
2026-07-05T17:09+10:00 | 71-therry-street-avalon-beach | s5-tenancies-html | script:s5_tenancies_html.py | done | 25 tenancies, 15 gaps, html rendered
2026-07-05T17:09+10:00 | 71-therry-street-avalon-beach | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T17:09+10:00 | 71-therry-street-avalon-beach | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-05_71-therry-street-avalon-beach.md
2026-07-05T07:10+10:00 | - | defect-2b-fix | orchestrator | done | tenant_from_name derivation + S5 chronological fallback + set_move_out_date override action; 287/350/1-148 re-run VERIFY PASS; 4 transfer closures confirmed; eval 6/6 PASS incl 342 regression
2026-07-05T07:13+10:00 | pilot-batch | kurian-rulings-r3 | operator: Kurian | done | rulings recorded to 5 house rulings.md files (Sabrina later-date; Leonardo 313; Hassan billed-vs-physical; MdAftab current tenant; Rm6 full-window; 40/41 slot method approved)
2026-07-05T17:24+10:00 | 287-cleveland-st-redfern | s3-timeline | script:s3_timeline.py | done | 115 events; unresolved rooms: {'maintenance': 52}; deduped: {'moveout': 1}
2026-07-05T17:24+10:00 | 287-cleveland-st-redfern | s5-tenancies-html | script:s5_tenancies_html.py | done | 42 tenancies, 21 gaps, html rendered
2026-07-05T17:24+10:00 | 287-cleveland-st-redfern | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T17:25+10:00 | 1-148-liverpool-rd-enfield | s3-timeline | script:s3_timeline.py | done | 37 events; unresolved rooms: {'maintenance': 20}; deduped: {'moveout': 2}
2026-07-05T17:25+10:00 | 1-148-liverpool-rd-enfield | s5-tenancies-html | script:s5_tenancies_html.py | done | 9 tenancies, 6 gaps, html rendered
2026-07-05T17:25+10:00 | 1-148-liverpool-rd-enfield | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T17:25+10:00 | 71-therry-street-avalon-beach | s3-timeline | script:s3_timeline.py | done | 62 events; unresolved rooms: {'maintenance': 25}; deduped: {}
2026-07-05T17:25+10:00 | 71-therry-street-avalon-beach | s5-tenancies-html | script:s5_tenancies_html.py | done | 24 tenancies, 14 gaps, html rendered
2026-07-05T17:25+10:00 | 71-therry-street-avalon-beach | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T17:25+10:00 | 66-boundary-st-parramatta | s3-timeline | script:s3_timeline.py | done | 95 events; unresolved rooms: {'movein': 1, 'maintenance': 55}; deduped: {}
2026-07-05T17:25+10:00 | 66-boundary-st-parramatta | s5-tenancies-html | script:s5_tenancies_html.py | done | 21 tenancies, 12 gaps, html rendered
2026-07-05T17:25+10:00 | 66-boundary-st-parramatta | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T17:25+10:00 | 287-cleveland-st-redfern | s3-timeline | script:s3_timeline.py | done | 115 events; unresolved rooms: {'maintenance': 52}; deduped: {'moveout': 1}
2026-07-05T17:25+10:00 | 287-cleveland-st-redfern | s5-tenancies-html | script:s5_tenancies_html.py | done | 42 tenancies, 21 gaps, html rendered
2026-07-05T17:25+10:00 | 287-cleveland-st-redfern | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T17:25+10:00 | 342-cleveland-st-surry-hills | s1-filter:movein | script:s1_filter_house.py | done | 43 kept of 19476 (59 out-of-window dropped; 0 no-date kept)
2026-07-05T17:25+10:00 | 342-cleveland-st-surry-hills | s1-filter:moveout | script:s1_filter_house.py | done | 20 kept of 23810 (139 out-of-window dropped; 0 no-date kept)
2026-07-05T17:25+10:00 | 342-cleveland-st-surry-hills | s1-filter:maintenance | script:s1_filter_house.py | done | 104 kept of 49791 (160 out-of-window dropped; 0 no-date kept)
2026-07-05T17:25+10:00 | 342-cleveland-st-surry-hills | s2-preflag:movein | script:s2_preflag.py | done | 14/43 flagged for human review (tc:14 kw:0 inc:0)
2026-07-05T17:25+10:00 | 342-cleveland-st-surry-hills | s2-preflag:moveout | script:s2_preflag.py | done | 17/20 flagged for human review (tc:11 kw:0 inc:6)
2026-07-05T17:25+10:00 | 342-cleveland-st-surry-hills | s2-preflag:maintenance | script:s2_preflag.py | done | 1/104 flagged for human review (tc:1 kw:0 inc:0)
2026-07-05T17:25+10:00 | 342-cleveland-st-surry-hills | s3-timeline | script:s3_timeline.py | done | 57 events; unresolved rooms: {'maintenance': 31}; deduped: {}
2026-07-05T17:25+10:00 | 342-cleveland-st-surry-hills | s5-tenancies-html | script:s5_tenancies_html.py | done | 15 tenancies, 7 gaps, html rendered
2026-07-05T17:25+10:00 | 342-cleveland-st-surry-hills | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T17:25+10:00 | 342-cleveland-st-surry-hills | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-05_342-cleveland-st-surry-hills.md
2026-07-05T17:25+10:00 | 287-cleveland-st-redfern | s1-filter:movein | script:s1_filter_house.py | done | 181 kept of 19476 (117 out-of-window dropped; 0 no-date kept)
2026-07-05T17:25+10:00 | 287-cleveland-st-redfern | s1-filter:moveout | script:s1_filter_house.py | done | 68 kept of 23810 (176 out-of-window dropped; 0 no-date kept)
2026-07-05T17:25+10:00 | 287-cleveland-st-redfern | s1-filter:maintenance | script:s1_filter_house.py | done | 177 kept of 49791 (215 out-of-window dropped; 0 no-date kept)
2026-07-05T17:25+10:00 | 287-cleveland-st-redfern | s2-preflag:movein | script:s2_preflag.py | done | 47/181 flagged for human review (tc:40 kw:0 inc:7)
2026-07-05T17:25+10:00 | 287-cleveland-st-redfern | s2-preflag:moveout | script:s2_preflag.py | done | 50/68 flagged for human review (tc:21 kw:0 inc:29)
2026-07-05T17:25+10:00 | 287-cleveland-st-redfern | s2-preflag:maintenance | script:s2_preflag.py | done | 7/177 flagged for human review (tc:4 kw:3 inc:0)
2026-07-05T17:25+10:00 | 287-cleveland-st-redfern | s3-timeline | script:s3_timeline.py | done | 115 events; unresolved rooms: {'maintenance': 52}; deduped: {'moveout': 1}
2026-07-05T17:25+10:00 | 287-cleveland-st-redfern | s5-tenancies-html | script:s5_tenancies_html.py | done | 42 tenancies, 21 gaps, html rendered
2026-07-05T17:25+10:00 | 287-cleveland-st-redfern | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T17:25+10:00 | 287-cleveland-st-redfern | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-05_287-cleveland-st-redfern.md
2026-07-05T17:25+10:00 | 1-148-liverpool-rd-enfield | s1-filter:movein | script:s1_filter_house.py | done | 29 kept of 19476 (10 out-of-window dropped; 0 no-date kept)
2026-07-05T17:25+10:00 | 1-148-liverpool-rd-enfield | s1-filter:moveout | script:s1_filter_house.py | done | 17 kept of 23810 (20 out-of-window dropped; 0 no-date kept)
2026-07-05T17:25+10:00 | 1-148-liverpool-rd-enfield | s1-filter:maintenance | script:s1_filter_house.py | done | 54 kept of 49791 (56 out-of-window dropped; 0 no-date kept)
2026-07-05T17:25+10:00 | 1-148-liverpool-rd-enfield | s2-preflag:movein | script:s2_preflag.py | done | 11/29 flagged for human review (tc:10 kw:0 inc:1)
2026-07-05T17:25+10:00 | 1-148-liverpool-rd-enfield | s2-preflag:moveout | script:s2_preflag.py | done | 16/17 flagged for human review (tc:8 kw:0 inc:8)
2026-07-05T17:25+10:00 | 1-148-liverpool-rd-enfield | s2-preflag:maintenance | script:s2_preflag.py | done | 3/54 flagged for human review (tc:2 kw:1 inc:0)
2026-07-05T17:25+10:00 | 1-148-liverpool-rd-enfield | s3-timeline | script:s3_timeline.py | done | 37 events; unresolved rooms: {'maintenance': 20}; deduped: {'moveout': 2}
2026-07-05T17:25+10:00 | 1-148-liverpool-rd-enfield | s5-tenancies-html | script:s5_tenancies_html.py | done | 9 tenancies, 6 gaps, html rendered
2026-07-05T17:25+10:00 | 1-148-liverpool-rd-enfield | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T17:25+10:00 | 1-148-liverpool-rd-enfield | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-05_1-148-liverpool-rd-enfield.md
2026-07-05T17:25+10:00 | 350-marsden-rd-carlingford | s1-filter:movein | script:s1_filter_house.py | done | 74 kept of 19476 (14 out-of-window dropped; 0 no-date kept)
2026-07-05T17:25+10:00 | 350-marsden-rd-carlingford | s1-filter:moveout | script:s1_filter_house.py | done | 20 kept of 23810 (10 out-of-window dropped; 0 no-date kept)
2026-07-05T17:25+10:00 | 350-marsden-rd-carlingford | s1-filter:maintenance | script:s1_filter_house.py | done | 112 kept of 49791 (51 out-of-window dropped; 0 no-date kept)
2026-07-05T17:25+10:00 | 350-marsden-rd-carlingford | s2-preflag:movein | script:s2_preflag.py | done | 24/74 flagged for human review (tc:23 kw:0 inc:1)
2026-07-05T17:25+10:00 | 350-marsden-rd-carlingford | s2-preflag:moveout | script:s2_preflag.py | done | 14/20 flagged for human review (tc:13 kw:0 inc:1)
2026-07-05T17:25+10:00 | 350-marsden-rd-carlingford | s2-preflag:maintenance | script:s2_preflag.py | done | 1/112 flagged for human review (tc:1 kw:0 inc:0)
2026-07-05T17:25+10:00 | 350-marsden-rd-carlingford | s3-timeline | script:s3_timeline.py | done | 76 events; unresolved rooms: {'movein': 1, 'maintenance': 37}; deduped: {'moveout': 1}
2026-07-05T17:25+10:00 | 350-marsden-rd-carlingford | s5-tenancies-html | script:s5_tenancies_html.py | done | 22 tenancies, 15 gaps, html rendered
2026-07-05T17:25+10:00 | 350-marsden-rd-carlingford | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T17:25+10:00 | 350-marsden-rd-carlingford | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-05_350-marsden-rd-carlingford.md
2026-07-05T17:25+10:00 | 66-boundary-st-parramatta | s1-filter:movein | script:s1_filter_house.py | done | 59 kept of 19476 (83 out-of-window dropped; 0 no-date kept)
2026-07-05T17:25+10:00 | 66-boundary-st-parramatta | s1-filter:moveout | script:s1_filter_house.py | done | 65 kept of 23810 (102 out-of-window dropped; 0 no-date kept)
2026-07-05T17:25+10:00 | 66-boundary-st-parramatta | s1-filter:maintenance | script:s1_filter_house.py | done | 133 kept of 49791 (224 out-of-window dropped; 0 no-date kept)
2026-07-05T17:25+10:00 | 66-boundary-st-parramatta | s2-preflag:movein | script:s2_preflag.py | done | 20/59 flagged for human review (tc:18 kw:0 inc:2)
2026-07-05T17:25+10:00 | 66-boundary-st-parramatta | s2-preflag:moveout | script:s2_preflag.py | done | 47/65 flagged for human review (tc:15 kw:0 inc:32)
2026-07-05T17:25+10:00 | 66-boundary-st-parramatta | s2-preflag:maintenance | script:s2_preflag.py | done | 0/133 flagged for human review (tc:0 kw:0 inc:0)
2026-07-05T17:25+10:00 | 66-boundary-st-parramatta | s3-timeline | script:s3_timeline.py | done | 95 events; unresolved rooms: {'movein': 1, 'maintenance': 55}; deduped: {}
2026-07-05T17:25+10:00 | 66-boundary-st-parramatta | s5-tenancies-html | script:s5_tenancies_html.py | done | 21 tenancies, 12 gaps, html rendered
2026-07-05T17:25+10:00 | 66-boundary-st-parramatta | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T17:25+10:00 | 66-boundary-st-parramatta | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-05_66-boundary-st-parramatta.md
2026-07-05T17:25+10:00 | 71-therry-street-avalon-beach | s1-filter:movein | script:s1_filter_house.py | done | 60 kept of 19476 (20 out-of-window dropped; 0 no-date kept)
2026-07-05T17:25+10:00 | 71-therry-street-avalon-beach | s1-filter:moveout | script:s1_filter_house.py | done | 32 kept of 23810 (104 out-of-window dropped; 0 no-date kept)
2026-07-05T17:25+10:00 | 71-therry-street-avalon-beach | s1-filter:maintenance | script:s1_filter_house.py | done | 104 kept of 49791 (78 out-of-window dropped; 0 no-date kept)
2026-07-05T17:25+10:00 | 71-therry-street-avalon-beach | s2-preflag:movein | script:s2_preflag.py | done | 22/60 flagged for human review (tc:20 kw:0 inc:3)
2026-07-05T17:25+10:00 | 71-therry-street-avalon-beach | s2-preflag:moveout | script:s2_preflag.py | done | 27/32 flagged for human review (tc:12 kw:1 inc:14)
2026-07-05T17:25+10:00 | 71-therry-street-avalon-beach | s2-preflag:maintenance | script:s2_preflag.py | done | 2/104 flagged for human review (tc:1 kw:1 inc:0)
2026-07-05T17:25+10:00 | 71-therry-street-avalon-beach | s3-timeline | script:s3_timeline.py | done | 62 events; unresolved rooms: {'maintenance': 25}; deduped: {}
2026-07-05T17:25+10:00 | 71-therry-street-avalon-beach | s5-tenancies-html | script:s5_tenancies_html.py | done | 24 tenancies, 14 gaps, html rendered
2026-07-05T17:25+10:00 | 71-therry-street-avalon-beach | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T17:25+10:00 | 71-therry-street-avalon-beach | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-05_71-therry-street-avalon-beach.md
2026-07-05T17:27+10:00 | 342-cleveland-st-surry-hills | s1-filter:movein | script:s1_filter_house.py | done | 43 kept of 19476 (59 out-of-window dropped; 0 no-date kept)
2026-07-05T17:27+10:00 | 342-cleveland-st-surry-hills | s1-filter:moveout | script:s1_filter_house.py | done | 20 kept of 23810 (139 out-of-window dropped; 0 no-date kept)
2026-07-05T17:27+10:00 | 342-cleveland-st-surry-hills | s1-filter:maintenance | script:s1_filter_house.py | done | 104 kept of 49791 (160 out-of-window dropped; 0 no-date kept)
2026-07-05T17:27+10:00 | 342-cleveland-st-surry-hills | s2-preflag:movein | script:s2_preflag.py | done | 14/43 flagged for human review (tc:14 kw:0 inc:0)
2026-07-05T17:27+10:00 | 342-cleveland-st-surry-hills | s2-preflag:moveout | script:s2_preflag.py | done | 17/20 flagged for human review (tc:11 kw:0 inc:6)
2026-07-05T17:27+10:00 | 342-cleveland-st-surry-hills | s2-preflag:maintenance | script:s2_preflag.py | done | 1/104 flagged for human review (tc:1 kw:0 inc:0)
2026-07-05T17:27+10:00 | 342-cleveland-st-surry-hills | s3-timeline | script:s3_timeline.py | done | 57 events; unresolved rooms: {'maintenance': 31}; deduped: {}
2026-07-05T17:27+10:00 | 342-cleveland-st-surry-hills | s5-tenancies-html | script:s5_tenancies_html.py | done | 15 tenancies, 7 gaps, html rendered
2026-07-05T17:27+10:00 | 342-cleveland-st-surry-hills | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T17:27+10:00 | 342-cleveland-st-surry-hills | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-05_342-cleveland-st-surry-hills.md
2026-07-05T17:27+10:00 | 287-cleveland-st-redfern | s1-filter:movein | script:s1_filter_house.py | done | 181 kept of 19476 (117 out-of-window dropped; 0 no-date kept)
2026-07-05T17:27+10:00 | 287-cleveland-st-redfern | s1-filter:moveout | script:s1_filter_house.py | done | 68 kept of 23810 (176 out-of-window dropped; 0 no-date kept)
2026-07-05T17:27+10:00 | 287-cleveland-st-redfern | s1-filter:maintenance | script:s1_filter_house.py | done | 177 kept of 49791 (215 out-of-window dropped; 0 no-date kept)
2026-07-05T17:27+10:00 | 287-cleveland-st-redfern | s2-preflag:movein | script:s2_preflag.py | done | 47/181 flagged for human review (tc:40 kw:0 inc:7)
2026-07-05T17:27+10:00 | 287-cleveland-st-redfern | s2-preflag:moveout | script:s2_preflag.py | done | 50/68 flagged for human review (tc:21 kw:0 inc:29)
2026-07-05T17:27+10:00 | 287-cleveland-st-redfern | s2-preflag:maintenance | script:s2_preflag.py | done | 7/177 flagged for human review (tc:4 kw:3 inc:0)
2026-07-05T17:27+10:00 | 287-cleveland-st-redfern | s3-timeline | script:s3_timeline.py | done | 115 events; unresolved rooms: {'maintenance': 52}; deduped: {'moveout': 1}
2026-07-05T17:27+10:00 | 287-cleveland-st-redfern | s5-tenancies-html | script:s5_tenancies_html.py | done | 42 tenancies, 21 gaps, html rendered
2026-07-05T17:27+10:00 | 287-cleveland-st-redfern | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T17:27+10:00 | 287-cleveland-st-redfern | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-05_287-cleveland-st-redfern.md
2026-07-05T17:27+10:00 | 1-148-liverpool-rd-enfield | s1-filter:movein | script:s1_filter_house.py | done | 29 kept of 19476 (10 out-of-window dropped; 0 no-date kept)
2026-07-05T17:27+10:00 | 1-148-liverpool-rd-enfield | s1-filter:moveout | script:s1_filter_house.py | done | 17 kept of 23810 (20 out-of-window dropped; 0 no-date kept)
2026-07-05T17:27+10:00 | 1-148-liverpool-rd-enfield | s1-filter:maintenance | script:s1_filter_house.py | done | 54 kept of 49791 (56 out-of-window dropped; 0 no-date kept)
2026-07-05T17:27+10:00 | 1-148-liverpool-rd-enfield | s2-preflag:movein | script:s2_preflag.py | done | 11/29 flagged for human review (tc:10 kw:0 inc:1)
2026-07-05T17:27+10:00 | 1-148-liverpool-rd-enfield | s2-preflag:moveout | script:s2_preflag.py | done | 16/17 flagged for human review (tc:8 kw:0 inc:8)
2026-07-05T17:27+10:00 | 1-148-liverpool-rd-enfield | s2-preflag:maintenance | script:s2_preflag.py | done | 3/54 flagged for human review (tc:2 kw:1 inc:0)
2026-07-05T17:27+10:00 | 1-148-liverpool-rd-enfield | s3-timeline | script:s3_timeline.py | done | 37 events; unresolved rooms: {'maintenance': 20}; deduped: {'moveout': 2}
2026-07-05T17:27+10:00 | 1-148-liverpool-rd-enfield | s5-tenancies-html | script:s5_tenancies_html.py | done | 9 tenancies, 6 gaps, html rendered
2026-07-05T17:27+10:00 | 1-148-liverpool-rd-enfield | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T17:27+10:00 | 1-148-liverpool-rd-enfield | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-05_1-148-liverpool-rd-enfield.md
2026-07-05T17:27+10:00 | 350-marsden-rd-carlingford | s1-filter:movein | script:s1_filter_house.py | done | 74 kept of 19476 (14 out-of-window dropped; 0 no-date kept)
2026-07-05T17:27+10:00 | 350-marsden-rd-carlingford | s1-filter:moveout | script:s1_filter_house.py | done | 20 kept of 23810 (10 out-of-window dropped; 0 no-date kept)
2026-07-05T17:27+10:00 | 350-marsden-rd-carlingford | s1-filter:maintenance | script:s1_filter_house.py | done | 112 kept of 49791 (51 out-of-window dropped; 0 no-date kept)
2026-07-05T17:27+10:00 | 350-marsden-rd-carlingford | s2-preflag:movein | script:s2_preflag.py | done | 24/74 flagged for human review (tc:23 kw:0 inc:1)
2026-07-05T17:27+10:00 | 350-marsden-rd-carlingford | s2-preflag:moveout | script:s2_preflag.py | done | 14/20 flagged for human review (tc:13 kw:0 inc:1)
2026-07-05T17:27+10:00 | 350-marsden-rd-carlingford | s2-preflag:maintenance | script:s2_preflag.py | done | 1/112 flagged for human review (tc:1 kw:0 inc:0)
2026-07-05T17:27+10:00 | 350-marsden-rd-carlingford | s3-timeline | script:s3_timeline.py | done | 76 events; unresolved rooms: {'movein': 1, 'maintenance': 37}; deduped: {'moveout': 1}
2026-07-05T17:27+10:00 | 350-marsden-rd-carlingford | s5-tenancies-html | script:s5_tenancies_html.py | done | 22 tenancies, 15 gaps, html rendered
2026-07-05T17:27+10:00 | 350-marsden-rd-carlingford | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T17:27+10:00 | 350-marsden-rd-carlingford | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-05_350-marsden-rd-carlingford.md
2026-07-05T17:27+10:00 | 66-boundary-st-parramatta | s1-filter:movein | script:s1_filter_house.py | done | 59 kept of 19476 (83 out-of-window dropped; 0 no-date kept)
2026-07-05T17:27+10:00 | 66-boundary-st-parramatta | s1-filter:moveout | script:s1_filter_house.py | done | 65 kept of 23810 (102 out-of-window dropped; 0 no-date kept)
2026-07-05T17:27+10:00 | 66-boundary-st-parramatta | s1-filter:maintenance | script:s1_filter_house.py | done | 133 kept of 49791 (224 out-of-window dropped; 0 no-date kept)
2026-07-05T17:27+10:00 | 66-boundary-st-parramatta | s2-preflag:movein | script:s2_preflag.py | done | 20/59 flagged for human review (tc:18 kw:0 inc:2)
2026-07-05T17:27+10:00 | 66-boundary-st-parramatta | s2-preflag:moveout | script:s2_preflag.py | done | 47/65 flagged for human review (tc:15 kw:0 inc:32)
2026-07-05T17:27+10:00 | 66-boundary-st-parramatta | s2-preflag:maintenance | script:s2_preflag.py | done | 0/133 flagged for human review (tc:0 kw:0 inc:0)
2026-07-05T17:27+10:00 | 66-boundary-st-parramatta | s3-timeline | script:s3_timeline.py | done | 95 events; unresolved rooms: {'movein': 1, 'maintenance': 55}; deduped: {}
2026-07-05T17:27+10:00 | 66-boundary-st-parramatta | s5-tenancies-html | script:s5_tenancies_html.py | done | 21 tenancies, 12 gaps, html rendered
2026-07-05T17:27+10:00 | 66-boundary-st-parramatta | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T17:27+10:00 | 66-boundary-st-parramatta | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-05_66-boundary-st-parramatta.md
2026-07-05T17:27+10:00 | 71-therry-street-avalon-beach | s1-filter:movein | script:s1_filter_house.py | done | 60 kept of 19476 (20 out-of-window dropped; 0 no-date kept)
2026-07-05T17:27+10:00 | 71-therry-street-avalon-beach | s1-filter:moveout | script:s1_filter_house.py | done | 32 kept of 23810 (104 out-of-window dropped; 0 no-date kept)
2026-07-05T17:27+10:00 | 71-therry-street-avalon-beach | s1-filter:maintenance | script:s1_filter_house.py | done | 104 kept of 49791 (78 out-of-window dropped; 0 no-date kept)
2026-07-05T17:27+10:00 | 71-therry-street-avalon-beach | s2-preflag:movein | script:s2_preflag.py | done | 22/60 flagged for human review (tc:20 kw:0 inc:3)
2026-07-05T17:27+10:00 | 71-therry-street-avalon-beach | s2-preflag:moveout | script:s2_preflag.py | done | 27/32 flagged for human review (tc:12 kw:1 inc:14)
2026-07-05T17:27+10:00 | 71-therry-street-avalon-beach | s2-preflag:maintenance | script:s2_preflag.py | done | 2/104 flagged for human review (tc:1 kw:1 inc:0)
2026-07-05T17:27+10:00 | 71-therry-street-avalon-beach | s3-timeline | script:s3_timeline.py | done | 62 events; unresolved rooms: {'maintenance': 25}; deduped: {}
2026-07-05T17:27+10:00 | 71-therry-street-avalon-beach | s5-tenancies-html | script:s5_tenancies_html.py | done | 24 tenancies, 14 gaps, html rendered
2026-07-05T17:27+10:00 | 71-therry-street-avalon-beach | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T17:27+10:00 | 71-therry-street-avalon-beach | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-05_71-therry-street-avalon-beach.md

## 2026-07-05 (session) | PILOT ROUND 3 (Kurian rulings applied) + CLOSE
2026-07-05T18:30+10:00 | ALL | r3-rulings | orchestrator | done | Applied Kurian r3: 287 Sabrina no-change, Leonardo fee $1980->$313; 1/148 Hassan set_move_out_date 2025-12-24 (+physical-vacate 2025-11-30 note); 350 MdAftab ongoing confirmed; 71 Harrison=479 (excluded mis-roomed 172 move-in) + Owen exclude; 66 Room6 #12 -> full_window_occupants (no in-window MO found; post-window Rohit Shinde 1216188786381563). Melany 71 set_move_out_date 2026-01-07.
2026-07-05T18:30+10:00 | 287-cleveland-st-redfern | slot-resolution | orchestrator | done | 40<->41 slot method (per-Kurian): Room6=40A Zaid->Jack,40B Haroun; Room7=bed1 Masato, bed2 Juan->Callum->Radikanesha->Udaya; Giordano excluded (never occupied). Crosser phantoms accepted as-is per Kurian; reassign_room override flagged as residual.
2026-07-05T18:30+10:00 | ALL-6 | eval | orchestrator | PASS | All 5 pilot + 342 regression PASS after r3.
2026-07-05T17:35+10:00 | 287-cleveland-st-redfern | s3-timeline | script:s3_timeline.py | done | 115 events; unresolved rooms: {'maintenance': 52}; deduped: {'moveout': 1}
2026-07-05T17:35+10:00 | 287-cleveland-st-redfern | s3-timeline | script:s3_timeline.py | done | 115 events; unresolved rooms: {'maintenance': 52}; deduped: {'moveout': 1}
2026-07-05T17:35+10:00 | 287-cleveland-st-redfern | s5-tenancies-html | script:s5_tenancies_html.py | done | 42 tenancies, 21 gaps, html rendered
2026-07-05T17:35+10:00 | 342-cleveland-st-surry-hills | s1-filter:movein | script:s1_filter_house.py | done | 43 kept of 19476 (59 out-of-window dropped; 0 no-date kept)
2026-07-05T17:35+10:00 | 342-cleveland-st-surry-hills | s1-filter:moveout | script:s1_filter_house.py | done | 20 kept of 23810 (139 out-of-window dropped; 0 no-date kept)
2026-07-05T17:35+10:00 | 342-cleveland-st-surry-hills | s1-filter:maintenance | script:s1_filter_house.py | done | 104 kept of 49791 (160 out-of-window dropped; 0 no-date kept)
2026-07-05T17:35+10:00 | 342-cleveland-st-surry-hills | s2-preflag:movein | script:s2_preflag.py | done | 14/43 flagged for human review (tc:14 kw:0 inc:0)
2026-07-05T17:35+10:00 | 342-cleveland-st-surry-hills | s2-preflag:moveout | script:s2_preflag.py | done | 17/20 flagged for human review (tc:11 kw:0 inc:6)
2026-07-05T17:35+10:00 | 342-cleveland-st-surry-hills | s2-preflag:maintenance | script:s2_preflag.py | done | 1/104 flagged for human review (tc:1 kw:0 inc:0)
2026-07-05T17:35+10:00 | 342-cleveland-st-surry-hills | s3-timeline | script:s3_timeline.py | done | 57 events; unresolved rooms: {'maintenance': 31}; deduped: {}
2026-07-05T17:35+10:00 | 342-cleveland-st-surry-hills | s5-tenancies-html | script:s5_tenancies_html.py | done | 15 tenancies, 7 gaps, html rendered
2026-07-05T17:35+10:00 | 342-cleveland-st-surry-hills | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T17:35+10:00 | 342-cleveland-st-surry-hills | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-05_342-cleveland-st-surry-hills.md
2026-07-05T17:35+10:00 | 287-cleveland-st-redfern | s1-filter:movein | script:s1_filter_house.py | done | 181 kept of 19476 (117 out-of-window dropped; 0 no-date kept)
2026-07-05T17:35+10:00 | 287-cleveland-st-redfern | s1-filter:moveout | script:s1_filter_house.py | done | 68 kept of 23810 (176 out-of-window dropped; 0 no-date kept)
2026-07-05T17:35+10:00 | 287-cleveland-st-redfern | s1-filter:maintenance | script:s1_filter_house.py | done | 177 kept of 49791 (215 out-of-window dropped; 0 no-date kept)
2026-07-05T17:35+10:00 | 287-cleveland-st-redfern | s2-preflag:movein | script:s2_preflag.py | done | 47/181 flagged for human review (tc:40 kw:0 inc:7)
2026-07-05T17:35+10:00 | 287-cleveland-st-redfern | s2-preflag:moveout | script:s2_preflag.py | done | 50/68 flagged for human review (tc:21 kw:0 inc:29)
2026-07-05T17:35+10:00 | 287-cleveland-st-redfern | s2-preflag:maintenance | script:s2_preflag.py | done | 7/177 flagged for human review (tc:4 kw:3 inc:0)
2026-07-05T17:35+10:00 | 287-cleveland-st-redfern | s3-timeline | script:s3_timeline.py | done | 115 events; unresolved rooms: {'maintenance': 52}; deduped: {'moveout': 1}
2026-07-05T17:35+10:00 | 287-cleveland-st-redfern | s5-tenancies-html | script:s5_tenancies_html.py | done | 42 tenancies, 21 gaps, html rendered
2026-07-05T17:35+10:00 | 287-cleveland-st-redfern | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T17:35+10:00 | 287-cleveland-st-redfern | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-05_287-cleveland-st-redfern.md
2026-07-05T17:35+10:00 | 350-marsden-rd-carlingford | s1-filter:movein | script:s1_filter_house.py | done | 74 kept of 19476 (14 out-of-window dropped; 0 no-date kept)
2026-07-05T17:35+10:00 | 350-marsden-rd-carlingford | s1-filter:moveout | script:s1_filter_house.py | done | 20 kept of 23810 (10 out-of-window dropped; 0 no-date kept)
2026-07-05T17:35+10:00 | 350-marsden-rd-carlingford | s1-filter:maintenance | script:s1_filter_house.py | done | 112 kept of 49791 (51 out-of-window dropped; 0 no-date kept)
2026-07-05T17:35+10:00 | 350-marsden-rd-carlingford | s2-preflag:movein | script:s2_preflag.py | done | 24/74 flagged for human review (tc:23 kw:0 inc:1)
2026-07-05T17:35+10:00 | 350-marsden-rd-carlingford | s2-preflag:moveout | script:s2_preflag.py | done | 14/20 flagged for human review (tc:13 kw:0 inc:1)
2026-07-05T17:35+10:00 | 350-marsden-rd-carlingford | s2-preflag:maintenance | script:s2_preflag.py | done | 1/112 flagged for human review (tc:1 kw:0 inc:0)
2026-07-05T17:35+10:00 | 350-marsden-rd-carlingford | s3-timeline | script:s3_timeline.py | done | 76 events; unresolved rooms: {'movein': 1, 'maintenance': 37}; deduped: {'moveout': 1}
2026-07-05T17:35+10:00 | 350-marsden-rd-carlingford | s5-tenancies-html | script:s5_tenancies_html.py | done | 22 tenancies, 15 gaps, html rendered
2026-07-05T17:35+10:00 | 350-marsden-rd-carlingford | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T17:35+10:00 | 350-marsden-rd-carlingford | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-05_350-marsden-rd-carlingford.md
2026-07-05T17:35+10:00 | 1-148-liverpool-rd-enfield | s1-filter:movein | script:s1_filter_house.py | done | 29 kept of 19476 (10 out-of-window dropped; 0 no-date kept)
2026-07-05T17:35+10:00 | 1-148-liverpool-rd-enfield | s1-filter:moveout | script:s1_filter_house.py | done | 17 kept of 23810 (20 out-of-window dropped; 0 no-date kept)
2026-07-05T17:35+10:00 | 1-148-liverpool-rd-enfield | s1-filter:maintenance | script:s1_filter_house.py | done | 54 kept of 49791 (56 out-of-window dropped; 0 no-date kept)
2026-07-05T17:35+10:00 | 1-148-liverpool-rd-enfield | s2-preflag:movein | script:s2_preflag.py | done | 11/29 flagged for human review (tc:10 kw:0 inc:1)
2026-07-05T17:35+10:00 | 1-148-liverpool-rd-enfield | s2-preflag:moveout | script:s2_preflag.py | done | 16/17 flagged for human review (tc:8 kw:0 inc:8)
2026-07-05T17:35+10:00 | 1-148-liverpool-rd-enfield | s2-preflag:maintenance | script:s2_preflag.py | done | 3/54 flagged for human review (tc:2 kw:1 inc:0)
2026-07-05T17:35+10:00 | 1-148-liverpool-rd-enfield | s3-timeline | script:s3_timeline.py | done | 37 events; unresolved rooms: {'maintenance': 20}; deduped: {'moveout': 2}
2026-07-05T17:35+10:00 | 1-148-liverpool-rd-enfield | s5-tenancies-html | script:s5_tenancies_html.py | done | 9 tenancies, 6 gaps, html rendered
2026-07-05T17:35+10:00 | 1-148-liverpool-rd-enfield | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T17:35+10:00 | 1-148-liverpool-rd-enfield | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-05_1-148-liverpool-rd-enfield.md
2026-07-05T17:35+10:00 | 66-boundary-st-parramatta | s1-filter:movein | script:s1_filter_house.py | done | 59 kept of 19476 (83 out-of-window dropped; 0 no-date kept)
2026-07-05T17:35+10:00 | 66-boundary-st-parramatta | s1-filter:moveout | script:s1_filter_house.py | done | 65 kept of 23810 (102 out-of-window dropped; 0 no-date kept)
2026-07-05T17:35+10:00 | 66-boundary-st-parramatta | s1-filter:maintenance | script:s1_filter_house.py | done | 133 kept of 49791 (224 out-of-window dropped; 0 no-date kept)
2026-07-05T17:35+10:00 | 66-boundary-st-parramatta | s2-preflag:movein | script:s2_preflag.py | done | 20/59 flagged for human review (tc:18 kw:0 inc:2)
2026-07-05T17:35+10:00 | 66-boundary-st-parramatta | s2-preflag:moveout | script:s2_preflag.py | done | 47/65 flagged for human review (tc:15 kw:0 inc:32)
2026-07-05T17:35+10:00 | 66-boundary-st-parramatta | s2-preflag:maintenance | script:s2_preflag.py | done | 0/133 flagged for human review (tc:0 kw:0 inc:0)
2026-07-05T17:35+10:00 | 66-boundary-st-parramatta | s3-timeline | script:s3_timeline.py | done | 95 events; unresolved rooms: {'movein': 1, 'maintenance': 55}; deduped: {}
2026-07-05T17:35+10:00 | 66-boundary-st-parramatta | s5-tenancies-html | script:s5_tenancies_html.py | done | 21 tenancies, 12 gaps, html rendered
2026-07-05T17:35+10:00 | 66-boundary-st-parramatta | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T17:35+10:00 | 66-boundary-st-parramatta | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-05_66-boundary-st-parramatta.md
2026-07-05T17:35+10:00 | 71-therry-street-avalon-beach | s1-filter:movein | script:s1_filter_house.py | done | 60 kept of 19476 (20 out-of-window dropped; 0 no-date kept)
2026-07-05T17:35+10:00 | 71-therry-street-avalon-beach | s1-filter:moveout | script:s1_filter_house.py | done | 32 kept of 23810 (104 out-of-window dropped; 0 no-date kept)
2026-07-05T17:35+10:00 | 71-therry-street-avalon-beach | s1-filter:maintenance | script:s1_filter_house.py | done | 104 kept of 49791 (78 out-of-window dropped; 0 no-date kept)
2026-07-05T17:35+10:00 | 71-therry-street-avalon-beach | s2-preflag:movein | script:s2_preflag.py | done | 22/60 flagged for human review (tc:20 kw:0 inc:3)
2026-07-05T17:35+10:00 | 71-therry-street-avalon-beach | s2-preflag:moveout | script:s2_preflag.py | done | 27/32 flagged for human review (tc:12 kw:1 inc:14)
2026-07-05T17:35+10:00 | 71-therry-street-avalon-beach | s2-preflag:maintenance | script:s2_preflag.py | done | 2/104 flagged for human review (tc:1 kw:1 inc:0)
2026-07-05T17:35+10:00 | 71-therry-street-avalon-beach | s3-timeline | script:s3_timeline.py | done | 62 events; unresolved rooms: {'maintenance': 25}; deduped: {}
2026-07-05T17:35+10:00 | 71-therry-street-avalon-beach | s5-tenancies-html | script:s5_tenancies_html.py | done | 24 tenancies, 14 gaps, html rendered
2026-07-05T17:35+10:00 | 71-therry-street-avalon-beach | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T17:35+10:00 | 71-therry-street-avalon-beach | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-05_71-therry-street-avalon-beach.md
2026-07-05T07:35+10:00 | - | reassign-room-action | orchestrator | done | reassign_room override built+mechanism-tested on 287 Masato (40->41 collapse verified, reverted); 6/6 golden regression PASS
2026-07-05T18:51+10:00 | 342-cleveland-st-surry-hills | s1-filter:movein | script:s1_filter_house.py | done | 43 kept of 19476 (59 out-of-window dropped; 0 no-date kept)
2026-07-05T18:51+10:00 | 342-cleveland-st-surry-hills | s1-filter:moveout | script:s1_filter_house.py | done | 20 kept of 23810 (139 out-of-window dropped; 0 no-date kept)
2026-07-05T18:51+10:00 | 342-cleveland-st-surry-hills | s1-filter:maintenance | script:s1_filter_house.py | done | 104 kept of 49791 (160 out-of-window dropped; 0 no-date kept)
2026-07-05T18:51+10:00 | 342-cleveland-st-surry-hills | s2-preflag:movein | script:s2_preflag.py | done | 14/43 flagged for human review (tc:14 kw:0 inc:0)
2026-07-05T18:51+10:00 | 342-cleveland-st-surry-hills | s2-preflag:moveout | script:s2_preflag.py | done | 17/20 flagged for human review (tc:11 kw:0 inc:6)
2026-07-05T18:51+10:00 | 342-cleveland-st-surry-hills | s2-preflag:maintenance | script:s2_preflag.py | done | 1/104 flagged for human review (tc:1 kw:0 inc:0)
2026-07-05T18:51+10:00 | 342-cleveland-st-surry-hills | s3-timeline | script:s3_timeline.py | done | 57 events; unresolved rooms: {'maintenance': 31}; deduped: {}
2026-07-05T18:51+10:00 | 342-cleveland-st-surry-hills | s5-tenancies-html | script:s5_tenancies_html.py | done | 15 tenancies, 7 gaps, html rendered
2026-07-05T18:51+10:00 | 342-cleveland-st-surry-hills | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T18:51+10:00 | 342-cleveland-st-surry-hills | s1-filter:movein | script:s1_filter_house.py | done | 43 kept of 19476 (59 out-of-window dropped; 0 no-date kept)
2026-07-05T18:51+10:00 | 342-cleveland-st-surry-hills | s1-filter:moveout | script:s1_filter_house.py | done | 20 kept of 23810 (139 out-of-window dropped; 0 no-date kept)
2026-07-05T18:51+10:00 | 342-cleveland-st-surry-hills | s1-filter:maintenance | script:s1_filter_house.py | done | 104 kept of 49791 (160 out-of-window dropped; 0 no-date kept)
2026-07-05T18:51+10:00 | 342-cleveland-st-surry-hills | s2-preflag:movein | script:s2_preflag.py | done | 14/43 flagged for human review (tc:14 kw:0 inc:0)
2026-07-05T18:51+10:00 | 342-cleveland-st-surry-hills | s2-preflag:moveout | script:s2_preflag.py | done | 17/20 flagged for human review (tc:11 kw:0 inc:6)
2026-07-05T18:51+10:00 | 342-cleveland-st-surry-hills | s2-preflag:maintenance | script:s2_preflag.py | done | 1/104 flagged for human review (tc:1 kw:0 inc:0)
2026-07-05T18:51+10:00 | 342-cleveland-st-surry-hills | s3-timeline | script:s3_timeline.py | done | 57 events; unresolved rooms: {'maintenance': 31}; deduped: {}
2026-07-05T18:51+10:00 | 342-cleveland-st-surry-hills | s5-tenancies-html | script:s5_tenancies_html.py | done | 15 tenancies, 7 gaps, html rendered
2026-07-05T18:51+10:00 | 342-cleveland-st-surry-hills | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T18:51+10:00 | 342-cleveland-st-surry-hills | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-05_342-cleveland-st-surry-hills.md
2026-07-05T18:51+10:00 | 287-cleveland-st-redfern | s1-filter:movein | script:s1_filter_house.py | done | 181 kept of 19476 (117 out-of-window dropped; 0 no-date kept)
2026-07-05T18:51+10:00 | 287-cleveland-st-redfern | s1-filter:moveout | script:s1_filter_house.py | done | 68 kept of 23810 (176 out-of-window dropped; 0 no-date kept)
2026-07-05T18:51+10:00 | 287-cleveland-st-redfern | s1-filter:maintenance | script:s1_filter_house.py | done | 177 kept of 49791 (215 out-of-window dropped; 0 no-date kept)
2026-07-05T18:51+10:00 | 287-cleveland-st-redfern | s2-preflag:movein | script:s2_preflag.py | done | 47/181 flagged for human review (tc:40 kw:0 inc:7)
2026-07-05T18:51+10:00 | 287-cleveland-st-redfern | s2-preflag:moveout | script:s2_preflag.py | done | 50/68 flagged for human review (tc:21 kw:0 inc:29)
2026-07-05T18:51+10:00 | 287-cleveland-st-redfern | s2-preflag:maintenance | script:s2_preflag.py | done | 7/177 flagged for human review (tc:4 kw:3 inc:0)
2026-07-05T18:51+10:00 | 287-cleveland-st-redfern | s3-timeline | script:s3_timeline.py | done | 115 events; unresolved rooms: {'maintenance': 55}; deduped: {'moveout': 1}
2026-07-05T18:51+10:00 | 287-cleveland-st-redfern | s5-tenancies-html | script:s5_tenancies_html.py | done | 42 tenancies, 21 gaps, html rendered
2026-07-05T18:51+10:00 | 287-cleveland-st-redfern | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T18:51+10:00 | 287-cleveland-st-redfern | s1-filter:movein | script:s1_filter_house.py | done | 181 kept of 19476 (117 out-of-window dropped; 0 no-date kept)
2026-07-05T18:51+10:00 | 287-cleveland-st-redfern | s1-filter:moveout | script:s1_filter_house.py | done | 68 kept of 23810 (176 out-of-window dropped; 0 no-date kept)
2026-07-05T18:51+10:00 | 287-cleveland-st-redfern | s1-filter:maintenance | script:s1_filter_house.py | done | 177 kept of 49791 (215 out-of-window dropped; 0 no-date kept)
2026-07-05T18:51+10:00 | 287-cleveland-st-redfern | s2-preflag:movein | script:s2_preflag.py | done | 47/181 flagged for human review (tc:40 kw:0 inc:7)
2026-07-05T18:51+10:00 | 287-cleveland-st-redfern | s2-preflag:moveout | script:s2_preflag.py | done | 50/68 flagged for human review (tc:21 kw:0 inc:29)
2026-07-05T18:51+10:00 | 287-cleveland-st-redfern | s2-preflag:maintenance | script:s2_preflag.py | done | 7/177 flagged for human review (tc:4 kw:3 inc:0)
2026-07-05T18:51+10:00 | 287-cleveland-st-redfern | s3-timeline | script:s3_timeline.py | done | 115 events; unresolved rooms: {'maintenance': 55}; deduped: {'moveout': 1}
2026-07-05T18:51+10:00 | 287-cleveland-st-redfern | s5-tenancies-html | script:s5_tenancies_html.py | done | 42 tenancies, 21 gaps, html rendered
2026-07-05T18:51+10:00 | 287-cleveland-st-redfern | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T18:51+10:00 | 287-cleveland-st-redfern | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-05_287-cleveland-st-redfern.md
2026-07-05T18:51+10:00 | 350-marsden-rd-carlingford | s1-filter:movein | script:s1_filter_house.py | done | 74 kept of 19476 (14 out-of-window dropped; 0 no-date kept)
2026-07-05T18:51+10:00 | 350-marsden-rd-carlingford | s1-filter:moveout | script:s1_filter_house.py | done | 20 kept of 23810 (10 out-of-window dropped; 0 no-date kept)
2026-07-05T18:51+10:00 | 350-marsden-rd-carlingford | s1-filter:maintenance | script:s1_filter_house.py | done | 112 kept of 49791 (51 out-of-window dropped; 0 no-date kept)
2026-07-05T18:51+10:00 | 350-marsden-rd-carlingford | s2-preflag:movein | script:s2_preflag.py | done | 24/74 flagged for human review (tc:23 kw:0 inc:1)
2026-07-05T18:51+10:00 | 350-marsden-rd-carlingford | s2-preflag:moveout | script:s2_preflag.py | done | 14/20 flagged for human review (tc:13 kw:0 inc:1)
2026-07-05T18:51+10:00 | 350-marsden-rd-carlingford | s2-preflag:maintenance | script:s2_preflag.py | done | 1/112 flagged for human review (tc:1 kw:0 inc:0)
2026-07-05T18:51+10:00 | 350-marsden-rd-carlingford | s3-timeline | script:s3_timeline.py | done | 76 events; unresolved rooms: {'movein': 1, 'maintenance': 37}; deduped: {'moveout': 1}
2026-07-05T18:51+10:00 | 350-marsden-rd-carlingford | s5-tenancies-html | script:s5_tenancies_html.py | done | 22 tenancies, 15 gaps, html rendered
2026-07-05T18:51+10:00 | 350-marsden-rd-carlingford | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T18:51+10:00 | 350-marsden-rd-carlingford | s1-filter:movein | script:s1_filter_house.py | done | 74 kept of 19476 (14 out-of-window dropped; 0 no-date kept)
2026-07-05T18:51+10:00 | 350-marsden-rd-carlingford | s1-filter:moveout | script:s1_filter_house.py | done | 20 kept of 23810 (10 out-of-window dropped; 0 no-date kept)
2026-07-05T18:51+10:00 | 350-marsden-rd-carlingford | s1-filter:maintenance | script:s1_filter_house.py | done | 112 kept of 49791 (51 out-of-window dropped; 0 no-date kept)
2026-07-05T18:51+10:00 | 350-marsden-rd-carlingford | s2-preflag:movein | script:s2_preflag.py | done | 24/74 flagged for human review (tc:23 kw:0 inc:1)
2026-07-05T18:51+10:00 | 350-marsden-rd-carlingford | s2-preflag:moveout | script:s2_preflag.py | done | 14/20 flagged for human review (tc:13 kw:0 inc:1)
2026-07-05T18:51+10:00 | 350-marsden-rd-carlingford | s2-preflag:maintenance | script:s2_preflag.py | done | 1/112 flagged for human review (tc:1 kw:0 inc:0)
2026-07-05T18:51+10:00 | 350-marsden-rd-carlingford | s3-timeline | script:s3_timeline.py | done | 76 events; unresolved rooms: {'movein': 1, 'maintenance': 37}; deduped: {'moveout': 1}
2026-07-05T18:51+10:00 | 350-marsden-rd-carlingford | s5-tenancies-html | script:s5_tenancies_html.py | done | 22 tenancies, 15 gaps, html rendered
2026-07-05T18:51+10:00 | 350-marsden-rd-carlingford | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T18:51+10:00 | 350-marsden-rd-carlingford | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-05_350-marsden-rd-carlingford.md
2026-07-05T18:51+10:00 | 1-148-liverpool-rd-enfield | s1-filter:movein | script:s1_filter_house.py | done | 29 kept of 19476 (10 out-of-window dropped; 0 no-date kept)
2026-07-05T18:51+10:00 | 1-148-liverpool-rd-enfield | s1-filter:moveout | script:s1_filter_house.py | done | 17 kept of 23810 (20 out-of-window dropped; 0 no-date kept)
2026-07-05T18:51+10:00 | 1-148-liverpool-rd-enfield | s1-filter:maintenance | script:s1_filter_house.py | done | 54 kept of 49791 (56 out-of-window dropped; 0 no-date kept)
2026-07-05T18:51+10:00 | 1-148-liverpool-rd-enfield | s2-preflag:movein | script:s2_preflag.py | done | 11/29 flagged for human review (tc:10 kw:0 inc:1)
2026-07-05T18:51+10:00 | 1-148-liverpool-rd-enfield | s2-preflag:moveout | script:s2_preflag.py | done | 16/17 flagged for human review (tc:8 kw:0 inc:8)
2026-07-05T18:51+10:00 | 1-148-liverpool-rd-enfield | s2-preflag:maintenance | script:s2_preflag.py | done | 3/54 flagged for human review (tc:2 kw:1 inc:0)
2026-07-05T18:51+10:00 | 1-148-liverpool-rd-enfield | s3-timeline | script:s3_timeline.py | done | 37 events; unresolved rooms: {'maintenance': 20}; deduped: {'moveout': 2}
2026-07-05T18:51+10:00 | 1-148-liverpool-rd-enfield | s5-tenancies-html | script:s5_tenancies_html.py | done | 9 tenancies, 6 gaps, html rendered
2026-07-05T18:51+10:00 | 1-148-liverpool-rd-enfield | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T18:51+10:00 | 1-148-liverpool-rd-enfield | s1-filter:movein | script:s1_filter_house.py | done | 29 kept of 19476 (10 out-of-window dropped; 0 no-date kept)
2026-07-05T18:51+10:00 | 1-148-liverpool-rd-enfield | s1-filter:moveout | script:s1_filter_house.py | done | 17 kept of 23810 (20 out-of-window dropped; 0 no-date kept)
2026-07-05T18:51+10:00 | 1-148-liverpool-rd-enfield | s1-filter:maintenance | script:s1_filter_house.py | done | 54 kept of 49791 (56 out-of-window dropped; 0 no-date kept)
2026-07-05T18:51+10:00 | 1-148-liverpool-rd-enfield | s2-preflag:movein | script:s2_preflag.py | done | 11/29 flagged for human review (tc:10 kw:0 inc:1)
2026-07-05T18:51+10:00 | 1-148-liverpool-rd-enfield | s2-preflag:moveout | script:s2_preflag.py | done | 16/17 flagged for human review (tc:8 kw:0 inc:8)
2026-07-05T18:51+10:00 | 1-148-liverpool-rd-enfield | s2-preflag:maintenance | script:s2_preflag.py | done | 3/54 flagged for human review (tc:2 kw:1 inc:0)
2026-07-05T18:51+10:00 | 1-148-liverpool-rd-enfield | s3-timeline | script:s3_timeline.py | done | 37 events; unresolved rooms: {'maintenance': 20}; deduped: {'moveout': 2}
2026-07-05T18:51+10:00 | 1-148-liverpool-rd-enfield | s5-tenancies-html | script:s5_tenancies_html.py | done | 9 tenancies, 6 gaps, html rendered
2026-07-05T18:51+10:00 | 1-148-liverpool-rd-enfield | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T18:51+10:00 | 1-148-liverpool-rd-enfield | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-05_1-148-liverpool-rd-enfield.md
2026-07-05T18:51+10:00 | 66-boundary-st-parramatta | s1-filter:movein | script:s1_filter_house.py | done | 58 kept of 19476 (81 out-of-window dropped; 0 no-date kept)
2026-07-05T18:51+10:00 | 66-boundary-st-parramatta | s1-filter:moveout | script:s1_filter_house.py | done | 62 kept of 23810 (102 out-of-window dropped; 0 no-date kept)
2026-07-05T18:51+10:00 | 66-boundary-st-parramatta | s1-filter:maintenance | script:s1_filter_house.py | done | 125 kept of 49791 (215 out-of-window dropped; 0 no-date kept)
2026-07-05T18:51+10:00 | 66-boundary-st-parramatta | s2-preflag:movein | script:s2_preflag.py | done | 19/58 flagged for human review (tc:17 kw:0 inc:2)
2026-07-05T18:51+10:00 | 66-boundary-st-parramatta | s2-preflag:moveout | script:s2_preflag.py | done | 44/62 flagged for human review (tc:12 kw:0 inc:32)
2026-07-05T18:51+10:00 | 66-boundary-st-parramatta | s2-preflag:maintenance | script:s2_preflag.py | done | 0/125 flagged for human review (tc:0 kw:0 inc:0)
2026-07-05T18:51+10:00 | 66-boundary-st-parramatta | s3-timeline | script:s3_timeline.py | done | 83 events; unresolved rooms: {'movein': 1, 'maintenance': 59}; deduped: {}
2026-07-05T18:51+10:00 | 66-boundary-st-parramatta | s5-tenancies-html | script:s5_tenancies_html.py | done | 17 tenancies, 11 gaps, html rendered
2026-07-05T18:51+10:00 | 66-boundary-st-parramatta | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T18:51+10:00 | 66-boundary-st-parramatta | s1-filter:movein | script:s1_filter_house.py | done | 58 kept of 19476 (81 out-of-window dropped; 0 no-date kept)
2026-07-05T18:51+10:00 | 66-boundary-st-parramatta | s1-filter:moveout | script:s1_filter_house.py | done | 62 kept of 23810 (102 out-of-window dropped; 0 no-date kept)
2026-07-05T18:51+10:00 | 66-boundary-st-parramatta | s1-filter:maintenance | script:s1_filter_house.py | done | 125 kept of 49791 (215 out-of-window dropped; 0 no-date kept)
2026-07-05T18:51+10:00 | 66-boundary-st-parramatta | s2-preflag:movein | script:s2_preflag.py | done | 19/58 flagged for human review (tc:17 kw:0 inc:2)
2026-07-05T18:51+10:00 | 66-boundary-st-parramatta | s2-preflag:moveout | script:s2_preflag.py | done | 44/62 flagged for human review (tc:12 kw:0 inc:32)
2026-07-05T18:51+10:00 | 66-boundary-st-parramatta | s2-preflag:maintenance | script:s2_preflag.py | done | 0/125 flagged for human review (tc:0 kw:0 inc:0)
2026-07-05T18:51+10:00 | 66-boundary-st-parramatta | s3-timeline | script:s3_timeline.py | done | 83 events; unresolved rooms: {'movein': 1, 'maintenance': 59}; deduped: {}
2026-07-05T18:51+10:00 | 66-boundary-st-parramatta | s5-tenancies-html | script:s5_tenancies_html.py | done | 17 tenancies, 11 gaps, html rendered
2026-07-05T18:51+10:00 | 66-boundary-st-parramatta | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T18:51+10:00 | 66-boundary-st-parramatta | eval-loop | script:eval/run_eval.py | FAIL | report: pipeline/eval/reports/2026-07-05_66-boundary-st-parramatta.md
2026-07-05T18:51+10:00 | 71-therry-street-avalon-beach | s1-filter:movein | script:s1_filter_house.py | done | 60 kept of 19476 (20 out-of-window dropped; 0 no-date kept)
2026-07-05T18:51+10:00 | 71-therry-street-avalon-beach | s1-filter:moveout | script:s1_filter_house.py | done | 32 kept of 23810 (104 out-of-window dropped; 0 no-date kept)
2026-07-05T18:51+10:00 | 71-therry-street-avalon-beach | s1-filter:maintenance | script:s1_filter_house.py | done | 104 kept of 49791 (78 out-of-window dropped; 0 no-date kept)
2026-07-05T18:51+10:00 | 71-therry-street-avalon-beach | s2-preflag:movein | script:s2_preflag.py | done | 22/60 flagged for human review (tc:20 kw:0 inc:3)
2026-07-05T18:51+10:00 | 71-therry-street-avalon-beach | s2-preflag:moveout | script:s2_preflag.py | done | 27/32 flagged for human review (tc:12 kw:1 inc:14)
2026-07-05T18:51+10:00 | 71-therry-street-avalon-beach | s2-preflag:maintenance | script:s2_preflag.py | done | 2/104 flagged for human review (tc:1 kw:1 inc:0)
2026-07-05T18:51+10:00 | 71-therry-street-avalon-beach | s3-timeline | script:s3_timeline.py | done | 62 events; unresolved rooms: {'maintenance': 25}; deduped: {}
2026-07-05T18:51+10:00 | 71-therry-street-avalon-beach | s5-tenancies-html | script:s5_tenancies_html.py | done | 24 tenancies, 14 gaps, html rendered
2026-07-05T18:51+10:00 | 71-therry-street-avalon-beach | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T18:51+10:00 | 71-therry-street-avalon-beach | s1-filter:movein | script:s1_filter_house.py | done | 60 kept of 19476 (20 out-of-window dropped; 0 no-date kept)
2026-07-05T18:51+10:00 | 71-therry-street-avalon-beach | s1-filter:moveout | script:s1_filter_house.py | done | 32 kept of 23810 (104 out-of-window dropped; 0 no-date kept)
2026-07-05T18:51+10:00 | 71-therry-street-avalon-beach | s1-filter:maintenance | script:s1_filter_house.py | done | 104 kept of 49791 (78 out-of-window dropped; 0 no-date kept)
2026-07-05T18:51+10:00 | 71-therry-street-avalon-beach | s2-preflag:movein | script:s2_preflag.py | done | 22/60 flagged for human review (tc:20 kw:0 inc:3)
2026-07-05T18:51+10:00 | 71-therry-street-avalon-beach | s2-preflag:moveout | script:s2_preflag.py | done | 27/32 flagged for human review (tc:12 kw:1 inc:14)
2026-07-05T18:51+10:00 | 71-therry-street-avalon-beach | s2-preflag:maintenance | script:s2_preflag.py | done | 2/104 flagged for human review (tc:1 kw:1 inc:0)
2026-07-05T18:51+10:00 | 71-therry-street-avalon-beach | s3-timeline | script:s3_timeline.py | done | 62 events; unresolved rooms: {'maintenance': 25}; deduped: {}
2026-07-05T18:51+10:00 | 71-therry-street-avalon-beach | s5-tenancies-html | script:s5_tenancies_html.py | done | 24 tenancies, 14 gaps, html rendered
2026-07-05T18:51+10:00 | 71-therry-street-avalon-beach | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T18:51+10:00 | 71-therry-street-avalon-beach | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-05_71-therry-street-avalon-beach.md
2026-07-05T18:52+10:00 | 342-cleveland-st-surry-hills | s1-filter:movein | script:s1_filter_house.py | done | 43 kept of 19476 (59 out-of-window dropped; 0 no-date kept)
2026-07-05T18:52+10:00 | 342-cleveland-st-surry-hills | s1-filter:moveout | script:s1_filter_house.py | done | 20 kept of 23810 (139 out-of-window dropped; 0 no-date kept)
2026-07-05T18:52+10:00 | 342-cleveland-st-surry-hills | s1-filter:maintenance | script:s1_filter_house.py | done | 104 kept of 49791 (160 out-of-window dropped; 0 no-date kept)
2026-07-05T18:52+10:00 | 342-cleveland-st-surry-hills | s2-preflag:movein | script:s2_preflag.py | done | 14/43 flagged for human review (tc:14 kw:0 inc:0)
2026-07-05T18:52+10:00 | 342-cleveland-st-surry-hills | s2-preflag:moveout | script:s2_preflag.py | done | 17/20 flagged for human review (tc:11 kw:0 inc:6)
2026-07-05T18:52+10:00 | 342-cleveland-st-surry-hills | s2-preflag:maintenance | script:s2_preflag.py | done | 1/104 flagged for human review (tc:1 kw:0 inc:0)
2026-07-05T18:52+10:00 | 342-cleveland-st-surry-hills | s3-timeline | script:s3_timeline.py | done | 57 events; unresolved rooms: {'maintenance': 31}; deduped: {}
2026-07-05T18:52+10:00 | 342-cleveland-st-surry-hills | s5-tenancies-html | script:s5_tenancies_html.py | done | 15 tenancies, 7 gaps, html rendered
2026-07-05T18:52+10:00 | 342-cleveland-st-surry-hills | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T18:52+10:00 | 342-cleveland-st-surry-hills | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-05_342-cleveland-st-surry-hills.md
2026-07-05T18:52+10:00 | 287-cleveland-st-redfern | s1-filter:movein | script:s1_filter_house.py | done | 181 kept of 19476 (117 out-of-window dropped; 0 no-date kept)
2026-07-05T18:52+10:00 | 287-cleveland-st-redfern | s1-filter:moveout | script:s1_filter_house.py | done | 68 kept of 23810 (176 out-of-window dropped; 0 no-date kept)
2026-07-05T18:52+10:00 | 287-cleveland-st-redfern | s1-filter:maintenance | script:s1_filter_house.py | done | 177 kept of 49791 (215 out-of-window dropped; 0 no-date kept)
2026-07-05T18:52+10:00 | 287-cleveland-st-redfern | s2-preflag:movein | script:s2_preflag.py | done | 47/181 flagged for human review (tc:40 kw:0 inc:7)
2026-07-05T18:52+10:00 | 287-cleveland-st-redfern | s2-preflag:moveout | script:s2_preflag.py | done | 50/68 flagged for human review (tc:21 kw:0 inc:29)
2026-07-05T18:52+10:00 | 287-cleveland-st-redfern | s2-preflag:maintenance | script:s2_preflag.py | done | 7/177 flagged for human review (tc:4 kw:3 inc:0)
2026-07-05T18:52+10:00 | 287-cleveland-st-redfern | s3-timeline | script:s3_timeline.py | done | 115 events; unresolved rooms: {'maintenance': 55}; deduped: {'moveout': 1}
2026-07-05T18:52+10:00 | 287-cleveland-st-redfern | s5-tenancies-html | script:s5_tenancies_html.py | done | 42 tenancies, 21 gaps, html rendered
2026-07-05T18:52+10:00 | 287-cleveland-st-redfern | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T18:52+10:00 | 287-cleveland-st-redfern | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-05_287-cleveland-st-redfern.md
2026-07-05T18:52+10:00 | 350-marsden-rd-carlingford | s1-filter:movein | script:s1_filter_house.py | done | 74 kept of 19476 (14 out-of-window dropped; 0 no-date kept)
2026-07-05T18:52+10:00 | 350-marsden-rd-carlingford | s1-filter:moveout | script:s1_filter_house.py | done | 20 kept of 23810 (10 out-of-window dropped; 0 no-date kept)
2026-07-05T18:52+10:00 | 350-marsden-rd-carlingford | s1-filter:maintenance | script:s1_filter_house.py | done | 112 kept of 49791 (51 out-of-window dropped; 0 no-date kept)
2026-07-05T18:52+10:00 | 350-marsden-rd-carlingford | s2-preflag:movein | script:s2_preflag.py | done | 24/74 flagged for human review (tc:23 kw:0 inc:1)
2026-07-05T18:52+10:00 | 350-marsden-rd-carlingford | s2-preflag:moveout | script:s2_preflag.py | done | 14/20 flagged for human review (tc:13 kw:0 inc:1)
2026-07-05T18:52+10:00 | 350-marsden-rd-carlingford | s2-preflag:maintenance | script:s2_preflag.py | done | 1/112 flagged for human review (tc:1 kw:0 inc:0)
2026-07-05T18:52+10:00 | 350-marsden-rd-carlingford | s3-timeline | script:s3_timeline.py | done | 76 events; unresolved rooms: {'movein': 1, 'maintenance': 37}; deduped: {'moveout': 1}
2026-07-05T18:52+10:00 | 350-marsden-rd-carlingford | s5-tenancies-html | script:s5_tenancies_html.py | done | 22 tenancies, 15 gaps, html rendered
2026-07-05T18:52+10:00 | 350-marsden-rd-carlingford | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T18:52+10:00 | 350-marsden-rd-carlingford | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-05_350-marsden-rd-carlingford.md
2026-07-05T18:52+10:00 | 1-148-liverpool-rd-enfield | s1-filter:movein | script:s1_filter_house.py | done | 29 kept of 19476 (10 out-of-window dropped; 0 no-date kept)
2026-07-05T18:52+10:00 | 1-148-liverpool-rd-enfield | s1-filter:moveout | script:s1_filter_house.py | done | 17 kept of 23810 (20 out-of-window dropped; 0 no-date kept)
2026-07-05T18:52+10:00 | 1-148-liverpool-rd-enfield | s1-filter:maintenance | script:s1_filter_house.py | done | 54 kept of 49791 (56 out-of-window dropped; 0 no-date kept)
2026-07-05T18:52+10:00 | 1-148-liverpool-rd-enfield | s2-preflag:movein | script:s2_preflag.py | done | 11/29 flagged for human review (tc:10 kw:0 inc:1)
2026-07-05T18:52+10:00 | 1-148-liverpool-rd-enfield | s2-preflag:moveout | script:s2_preflag.py | done | 16/17 flagged for human review (tc:8 kw:0 inc:8)
2026-07-05T18:52+10:00 | 1-148-liverpool-rd-enfield | s2-preflag:maintenance | script:s2_preflag.py | done | 3/54 flagged for human review (tc:2 kw:1 inc:0)
2026-07-05T18:52+10:00 | 1-148-liverpool-rd-enfield | s3-timeline | script:s3_timeline.py | done | 37 events; unresolved rooms: {'maintenance': 20}; deduped: {'moveout': 2}
2026-07-05T18:52+10:00 | 1-148-liverpool-rd-enfield | s5-tenancies-html | script:s5_tenancies_html.py | done | 9 tenancies, 6 gaps, html rendered
2026-07-05T18:52+10:00 | 1-148-liverpool-rd-enfield | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T18:52+10:00 | 1-148-liverpool-rd-enfield | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-05_1-148-liverpool-rd-enfield.md
2026-07-05T18:52+10:00 | 66-boundary-st-parramatta | s1-filter:movein | script:s1_filter_house.py | done | 58 kept of 19476 (81 out-of-window dropped; 0 no-date kept)
2026-07-05T18:52+10:00 | 66-boundary-st-parramatta | s1-filter:moveout | script:s1_filter_house.py | done | 62 kept of 23810 (102 out-of-window dropped; 0 no-date kept)
2026-07-05T18:52+10:00 | 66-boundary-st-parramatta | s1-filter:maintenance | script:s1_filter_house.py | done | 125 kept of 49791 (215 out-of-window dropped; 0 no-date kept)
2026-07-05T18:52+10:00 | 66-boundary-st-parramatta | s2-preflag:movein | script:s2_preflag.py | done | 19/58 flagged for human review (tc:17 kw:0 inc:2)
2026-07-05T18:52+10:00 | 66-boundary-st-parramatta | s2-preflag:moveout | script:s2_preflag.py | done | 44/62 flagged for human review (tc:12 kw:0 inc:32)
2026-07-05T18:52+10:00 | 66-boundary-st-parramatta | s2-preflag:maintenance | script:s2_preflag.py | done | 0/125 flagged for human review (tc:0 kw:0 inc:0)
2026-07-05T18:52+10:00 | 66-boundary-st-parramatta | s3-timeline | script:s3_timeline.py | done | 83 events; unresolved rooms: {'movein': 1, 'maintenance': 59}; deduped: {}
2026-07-05T18:52+10:00 | 66-boundary-st-parramatta | s5-tenancies-html | script:s5_tenancies_html.py | done | 17 tenancies, 11 gaps, html rendered
2026-07-05T18:52+10:00 | 66-boundary-st-parramatta | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T18:52+10:00 | 66-boundary-st-parramatta | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-05_66-boundary-st-parramatta.md
2026-07-05T18:52+10:00 | 71-therry-street-avalon-beach | s1-filter:movein | script:s1_filter_house.py | done | 60 kept of 19476 (20 out-of-window dropped; 0 no-date kept)
2026-07-05T18:52+10:00 | 71-therry-street-avalon-beach | s1-filter:moveout | script:s1_filter_house.py | done | 32 kept of 23810 (104 out-of-window dropped; 0 no-date kept)
2026-07-05T18:52+10:00 | 71-therry-street-avalon-beach | s1-filter:maintenance | script:s1_filter_house.py | done | 104 kept of 49791 (78 out-of-window dropped; 0 no-date kept)
2026-07-05T18:52+10:00 | 71-therry-street-avalon-beach | s2-preflag:movein | script:s2_preflag.py | done | 22/60 flagged for human review (tc:20 kw:0 inc:3)
2026-07-05T18:52+10:00 | 71-therry-street-avalon-beach | s2-preflag:moveout | script:s2_preflag.py | done | 27/32 flagged for human review (tc:12 kw:1 inc:14)
2026-07-05T18:52+10:00 | 71-therry-street-avalon-beach | s2-preflag:maintenance | script:s2_preflag.py | done | 2/104 flagged for human review (tc:1 kw:1 inc:0)
2026-07-05T18:52+10:00 | 71-therry-street-avalon-beach | s3-timeline | script:s3_timeline.py | done | 62 events; unresolved rooms: {'maintenance': 25}; deduped: {}
2026-07-05T18:52+10:00 | 71-therry-street-avalon-beach | s5-tenancies-html | script:s5_tenancies_html.py | done | 24 tenancies, 14 gaps, html rendered
2026-07-05T18:52+10:00 | 71-therry-street-avalon-beach | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-05T18:52+10:00 | 71-therry-street-avalon-beach | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-05_71-therry-street-avalon-beach.md
2026-07-05T08:52+10:00 | 66-boundary-st-parramatta | junk-fix+refreeze | orchestrator | done | code-only match >=3 chars + notes-attribution >=3 chars; 4 cross-house tasks dropped (Kapil/Gabriel/Malik/Tung — Kurian ground truth); overstay columns added; 66 golden re-frozen; 6/6 eval PASS
2026-07-06T09:22+10:00 | 66-boundary-st-parramatta | s6-gap-hunt | script:s6_gap_hunt.py | done | 12 targets, 25 candidates, overocc: 1
2026-07-06T09:23+10:00 | 342-cleveland-st-surry-hills | s6-gap-hunt | script:s6_gap_hunt.py | done | 13 targets, 17 candidates, overocc: 1
2026-07-06T09:23+10:00 | 287-cleveland-st-redfern | s6-gap-hunt | script:s6_gap_hunt.py | done | 32 targets, 32 candidates, overocc: 5
2026-07-06T09:23+10:00 | 350-marsden-rd-carlingford | s6-gap-hunt | script:s6_gap_hunt.py | done | 18 targets, 24 candidates, overocc: 4
2026-07-06T09:23+10:00 | 1-148-liverpool-rd-enfield | s6-gap-hunt | script:s6_gap_hunt.py | done | 5 targets, 5 candidates, overocc: 0
2026-07-06T09:23+10:00 | 71-therry-street-avalon-beach | s6-gap-hunt | script:s6_gap_hunt.py | done | 24 targets, 45 candidates, overocc: 5
2026-07-05T23:23+10:00 | - | s6-gap-hunt | orchestrator | done | S6 fuzzy gap-hunt built (name tokens + code family + A/B fuzzy + address + date); run on all 6 pilot houses (127 candidates); README+skill updated; found Adriano Castle Hill exit, post-window confirmations, 5 pre-window move-ins at 66-boundary
2026-07-06T09:31+10:00 | 287-cleveland-st-redfern | a0-roomcode-check | script:a0_roomcode_check.py | FAIL | 1 problems, 8 notes
2026-07-06T09:31+10:00 | 1-148-liverpool-rd-enfield | a0-roomcode-check | script:a0_roomcode_check.py | PASS | 0 problems, 0 notes
2026-07-06T09:31+10:00 | 350-marsden-rd-carlingford | a0-roomcode-check | script:a0_roomcode_check.py | PASS | 0 problems, 1 notes
2026-07-06T09:31+10:00 | 66-boundary-st-parramatta | a0-roomcode-check | script:a0_roomcode_check.py | PASS | 0 problems, 0 notes
2026-07-06T09:31+10:00 | 71-therry-street-avalon-beach | a0-roomcode-check | script:a0_roomcode_check.py | PASS | 0 problems, 3 notes
2026-07-06T09:33+10:00 | 350-marsden-rd-carlingford | s1-filter:movein | script:s1_filter_house.py | done | 74 kept of 19476 (14 out-of-window dropped; 0 no-date kept)
2026-07-06T09:33+10:00 | 350-marsden-rd-carlingford | s1-filter:moveout | script:s1_filter_house.py | done | 20 kept of 23810 (10 out-of-window dropped; 0 no-date kept)
2026-07-06T09:33+10:00 | 350-marsden-rd-carlingford | s1-filter:maintenance | script:s1_filter_house.py | done | 112 kept of 49791 (51 out-of-window dropped; 0 no-date kept)
2026-07-06T09:33+10:00 | 350-marsden-rd-carlingford | s2-preflag:movein | script:s2_preflag.py | done | 24/74 flagged for human review (tc:23 kw:0 inc:1)
2026-07-06T09:33+10:00 | 350-marsden-rd-carlingford | s2-preflag:moveout | script:s2_preflag.py | done | 14/20 flagged for human review (tc:13 kw:0 inc:1)
2026-07-06T09:33+10:00 | 350-marsden-rd-carlingford | s2-preflag:maintenance | script:s2_preflag.py | done | 1/112 flagged for human review (tc:1 kw:0 inc:0)
2026-07-06T09:33+10:00 | 350-marsden-rd-carlingford | s3-timeline | script:s3_timeline.py | done | 76 events; unresolved rooms: {'movein': 1, 'maintenance': 37}; deduped: {'moveout': 1}
2026-07-06T09:33+10:00 | 350-marsden-rd-carlingford | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-06T09:33+10:00 | 287-cleveland-st-redfern | s1-filter:movein | script:s1_filter_house.py | done | 181 kept of 19476 (117 out-of-window dropped; 0 no-date kept)
2026-07-06T09:33+10:00 | 287-cleveland-st-redfern | s1-filter:moveout | script:s1_filter_house.py | done | 68 kept of 23810 (176 out-of-window dropped; 0 no-date kept)
2026-07-06T09:33+10:00 | 287-cleveland-st-redfern | s1-filter:maintenance | script:s1_filter_house.py | done | 177 kept of 49791 (215 out-of-window dropped; 0 no-date kept)
2026-07-06T09:33+10:00 | 287-cleveland-st-redfern | s2-preflag:movein | script:s2_preflag.py | done | 47/181 flagged for human review (tc:40 kw:0 inc:7)
2026-07-06T09:33+10:00 | 287-cleveland-st-redfern | s2-preflag:moveout | script:s2_preflag.py | done | 50/68 flagged for human review (tc:21 kw:0 inc:29)
2026-07-06T09:33+10:00 | 287-cleveland-st-redfern | s2-preflag:maintenance | script:s2_preflag.py | done | 7/177 flagged for human review (tc:4 kw:3 inc:0)
2026-07-06T09:33+10:00 | 287-cleveland-st-redfern | s3-timeline | script:s3_timeline.py | done | 115 events; unresolved rooms: {'maintenance': 55}; deduped: {'moveout': 1}
2026-07-06T09:34+10:00 | 71-therry-street-avalon-beach | s1-filter:movein | script:s1_filter_house.py | done | 60 kept of 19476 (20 out-of-window dropped; 0 no-date kept)
2026-07-06T09:34+10:00 | 71-therry-street-avalon-beach | s1-filter:moveout | script:s1_filter_house.py | done | 32 kept of 23810 (104 out-of-window dropped; 0 no-date kept)
2026-07-06T09:34+10:00 | 71-therry-street-avalon-beach | s1-filter:maintenance | script:s1_filter_house.py | done | 104 kept of 49791 (78 out-of-window dropped; 0 no-date kept)
2026-07-06T09:34+10:00 | 287-cleveland-st-redfern | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-06T09:34+10:00 | 1-148-liverpool-rd-enfield | s1-filter:movein | script:s1_filter_house.py | done | 29 kept of 19476 (10 out-of-window dropped; 0 no-date kept)
2026-07-06T09:34+10:00 | 1-148-liverpool-rd-enfield | s1-filter:moveout | script:s1_filter_house.py | done | 17 kept of 23810 (20 out-of-window dropped; 0 no-date kept)
2026-07-06T09:34+10:00 | 1-148-liverpool-rd-enfield | s1-filter:maintenance | script:s1_filter_house.py | done | 54 kept of 49791 (56 out-of-window dropped; 0 no-date kept)
2026-07-06T09:34+10:00 | 71-therry-street-avalon-beach | s2-preflag:movein | script:s2_preflag.py | done | 22/60 flagged for human review (tc:20 kw:0 inc:3)
2026-07-06T09:34+10:00 | 71-therry-street-avalon-beach | s2-preflag:moveout | script:s2_preflag.py | done | 27/32 flagged for human review (tc:12 kw:1 inc:14)
2026-07-06T09:34+10:00 | 71-therry-street-avalon-beach | s2-preflag:maintenance | script:s2_preflag.py | done | 2/104 flagged for human review (tc:1 kw:1 inc:0)
2026-07-06T09:34+10:00 | 71-therry-street-avalon-beach | s3-timeline | script:s3_timeline.py | done | 62 events; unresolved rooms: {'maintenance': 25}; deduped: {}
2026-07-06T09:34+10:00 | 1-148-liverpool-rd-enfield | s2-preflag:movein | script:s2_preflag.py | done | 11/29 flagged for human review (tc:10 kw:0 inc:1)
2026-07-06T09:34+10:00 | 1-148-liverpool-rd-enfield | s2-preflag:moveout | script:s2_preflag.py | done | 16/17 flagged for human review (tc:8 kw:0 inc:8)
2026-07-06T09:34+10:00 | 1-148-liverpool-rd-enfield | s2-preflag:maintenance | script:s2_preflag.py | done | 3/54 flagged for human review (tc:2 kw:1 inc:0)
2026-07-06T09:34+10:00 | 66-boundary-st-parramatta | s1-filter:movein | script:s1_filter_house.py | done | 58 kept of 19476 (81 out-of-window dropped; 0 no-date kept)
2026-07-06T09:34+10:00 | 66-boundary-st-parramatta | s1-filter:moveout | script:s1_filter_house.py | done | 62 kept of 23810 (102 out-of-window dropped; 0 no-date kept)
2026-07-06T09:34+10:00 | 66-boundary-st-parramatta | s1-filter:maintenance | script:s1_filter_house.py | done | 125 kept of 49791 (215 out-of-window dropped; 0 no-date kept)
2026-07-06T09:34+10:00 | 71-therry-street-avalon-beach | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-06T09:34+10:00 | 66-boundary-st-parramatta | s2-preflag:movein | script:s2_preflag.py | done | 19/58 flagged for human review (tc:17 kw:0 inc:2)
2026-07-06T09:34+10:00 | 66-boundary-st-parramatta | s2-preflag:moveout | script:s2_preflag.py | done | 44/62 flagged for human review (tc:12 kw:0 inc:32)
2026-07-06T09:34+10:00 | 66-boundary-st-parramatta | s2-preflag:maintenance | script:s2_preflag.py | done | 0/125 flagged for human review (tc:0 kw:0 inc:0)
2026-07-06T09:34+10:00 | 66-boundary-st-parramatta | s3-timeline | script:s3_timeline.py | done | 83 events; unresolved rooms: {'movein': 1, 'maintenance': 59}; deduped: {}
2026-07-06T09:34+10:00 | 66-boundary-st-parramatta | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-06T09:34+10:00 | 1-148-liverpool-rd-enfield | s3-timeline | script:s3_timeline.py | done | 37 events; unresolved rooms: {'maintenance': 20}; deduped: {'moveout': 2}
2026-07-06T09:34+10:00 | 1-148-liverpool-rd-enfield | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-06T09:45+10:00 | batch-00R-rerun | stageA-extraction | orchestrator | PASS | 5/5 VERIFY=PASS; all top-level filter counts identical to pilot-final (287:39/27/58, 1-148:7/6/24, 350:20/14/45, 66:17/11/59, 71:17/15/33); no cross-house leakage (66 Boundary Kapil/Gabriel/Malik/Tung absent); overrides.csv+rulings.md untouched all houses
2026-07-06T09:41+10:00 | 287-cleveland-st-redfern | s5-tenancies-html | script:s5_tenancies_html.py | done | 42 tenancies, 21 gaps, html rendered
2026-07-06T09:41+10:00 | 1-148-liverpool-rd-enfield | s5-tenancies-html | script:s5_tenancies_html.py | done | 9 tenancies, 6 gaps, html rendered
2026-07-06T09:41+10:00 | 350-marsden-rd-carlingford | s5-tenancies-html | script:s5_tenancies_html.py | done | 22 tenancies, 15 gaps, html rendered
2026-07-06T09:41+10:00 | 66-boundary-st-parramatta | s5-tenancies-html | script:s5_tenancies_html.py | done | 17 tenancies, 11 gaps, html rendered
2026-07-06T09:41+10:00 | 71-therry-street-avalon-beach | s5-tenancies-html | script:s5_tenancies_html.py | done | 24 tenancies, 14 gaps, html rendered
2026-07-06T09:45+10:00 | 350-marsden-rd-carlingford | review:movein | agent:movein-review-v2 | done | 20 reviewed, 0 flagged
2026-07-05T23:46:21Z | 287-cleveland-st-redfern | review:movein | movein-subagent | done | 39 reviewed, 1 flagged
2026-07-06 | 350-marsden-rd-carlingford | review:moveout | v2 | done | 14 reviewed, 0 flagged (0%), $1116 fees applied + $160 temp subtask, $1760 waived, 1 bond forfeited, 0 NO FEE DATA, 0 need comment check
2026-07-06 | 287-cleveland-st-redfern | review:moveout | v2 | done | 26 reviewed, 2 flagged (7.7%), $3250.50 fees applied, $300 break-fee waived (known), 2 need comment check
2026-07-06T10:40+10:00 | batch-00R-rerun | stageB-reviews | orchestrator | PASS | move-in+move-out reviews all 5 houses; move-out flag rates crashed vs pilot r1 (287 65->7.7%, 1-148 62.5->0%, 350 64->0%, 66 91->45.5%, 71 73->6.7%); 66 movein re-run once (over-flagged 4 override-settled items -> corrected to 3 genuine); spot-audit 2/house Task-ID clean (Mohd Amaan 1169-vs-1173 -> Stage C); P5 comment sweep 8 flagged tasks across 287/66/71, connector read OK; overrides.csv byte-identical to pilot all 5; 2 fee rows still open (Sabrina 287, Orisi 66 arrears)
2026-07-06T10:16+10:00 | 287-cleveland-st-redfern | s3-timeline | script:s3_timeline.py | done | 115 events; unresolved rooms: {'maintenance': 55}; deduped: {'moveout': 1}
2026-07-06T10:16+10:00 | 287-cleveland-st-redfern | s5-tenancies-html | script:s5_tenancies_html.py | done | 42 tenancies, 21 gaps, html rendered
2026-07-06T10:16+10:00 | 1-148-liverpool-rd-enfield | s3-timeline | script:s3_timeline.py | done | 37 events; unresolved rooms: {'maintenance': 20}; deduped: {'moveout': 2}
2026-07-06T10:16+10:00 | 1-148-liverpool-rd-enfield | s5-tenancies-html | script:s5_tenancies_html.py | done | 9 tenancies, 6 gaps, html rendered
2026-07-06T10:16+10:00 | 1-148-liverpool-rd-enfield | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-06T10:16+10:00 | 1-148-liverpool-rd-enfield | s6-gap-hunt | script:s6_gap_hunt.py | done | 5 targets, 5 candidates, overocc: 0
2026-07-06T10:16+10:00 | 287-cleveland-st-redfern | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-06T10:16+10:00 | 350-marsden-rd-carlingford | s3-timeline | script:s3_timeline.py | done | 76 events; unresolved rooms: {'movein': 1, 'maintenance': 37}; deduped: {'moveout': 1}
2026-07-06T10:16+10:00 | 350-marsden-rd-carlingford | s5-tenancies-html | script:s5_tenancies_html.py | done | 22 tenancies, 15 gaps, html rendered
2026-07-06T10:16+10:00 | 350-marsden-rd-carlingford | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-06T10:16+10:00 | 287-cleveland-st-redfern | s6-gap-hunt | script:s6_gap_hunt.py | done | 32 targets, 32 candidates, overocc: 5
2026-07-06T10:16+10:00 | 71-therry-street-avalon-beach | s3-timeline | script:s3_timeline.py | done | 62 events; unresolved rooms: {'maintenance': 25}; deduped: {}
2026-07-06T10:16+10:00 | 66-boundary-st-parramatta | s3-timeline | script:s3_timeline.py | done | 83 events; unresolved rooms: {'movein': 1, 'maintenance': 59}; deduped: {}
2026-07-06T10:16+10:00 | 66-boundary-st-parramatta | s5-tenancies-html | script:s5_tenancies_html.py | done | 17 tenancies, 11 gaps, html rendered
2026-07-06T10:17+10:00 | 71-therry-street-avalon-beach | s5-tenancies-html | script:s5_tenancies_html.py | done | 24 tenancies, 14 gaps, html rendered
2026-07-06T10:17+10:00 | 71-therry-street-avalon-beach | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-06T10:17+10:00 | 66-boundary-st-parramatta | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-06T10:17+10:00 | 350-marsden-rd-carlingford | s6-gap-hunt | script:s6_gap_hunt.py | done | 18 targets, 24 candidates, overocc: 4
2026-07-06T10:17+10:00 | 66-boundary-st-parramatta | s6-gap-hunt | script:s6_gap_hunt.py | done | 12 targets, 25 candidates, overocc: 1
2026-07-06T10:18+10:00 | 71-therry-street-avalon-beach | s6-gap-hunt | script:s6_gap_hunt.py | done | 24 targets, 45 candidates, overocc: 5
2026-07-06T10:18+10:00 | 287-cleveland-st-redfern | double-check-package | tenancy-timeline-subagent | sent | 3 confirmations requested (035A over-occupancy Tanguy/Chung; Room6/7 cross-code slot MASATO+Zaid+Haroun; 038B pre-window Syed movein source)
2026-07-06T10:19+1000 | 350-marsden-rd-carlingford | double-check-package | S5+S6 rerun (22 tenancies, 15 gaps); S4 PASS | sent | 1 gap-hunt confirmation requested (Dhruv #1169 transfer-out 1213322591040000) + 3 pre-existing over-occupancy anomalies for Kurian
2026-07-06T10:26+10:00 | 350-marsden-rd-carlingford | s3-timeline | script:s3_timeline.py | done | 77 events; unresolved rooms: {'movein': 1, 'maintenance': 37}; deduped: {'moveout': 2}
2026-07-06T10:26+10:00 | 350-marsden-rd-carlingford | s5-tenancies-html | script:s5_tenancies_html.py | done | 22 tenancies, 15 gaps, html rendered
2026-07-06T10:26+10:00 | 350-marsden-rd-carlingford | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-06T10:26+10:00 | 66-boundary-st-parramatta | s3-timeline | script:s3_timeline.py | done | 84 events; unresolved rooms: {'movein': 1, 'maintenance': 59}; deduped: {'moveout': 1}
2026-07-06T10:26+10:00 | 66-boundary-st-parramatta | s5-tenancies-html | script:s5_tenancies_html.py | done | 17 tenancies, 11 gaps, html rendered
2026-07-06T10:26+10:00 | 66-boundary-st-parramatta | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-06T11:30+10:00 | batch-00R-rerun | stageC-gaphunt | orchestrator | PASS | 2 in-window gaps attached (350 Dhruv promote_move_out 2026-02-20; 66 Adriano reassign#7+promote 2025-09-23, both Asana-verified); S3->S5->S4 re-run 350+66 VERIFY PASS; 66 Room10 double-ongoing RESOLVED; pre/post-window findings recorded in rulings.md all 5 houses
2026-07-06T10:32+10:00 | 287-cleveland-st-redfern | s3-timeline | script:s3_timeline.py | done | 115 events; unresolved rooms: {'maintenance': 55}; deduped: {'moveout': 1}
2026-07-06T10:32+10:00 | 287-cleveland-st-redfern | s5-tenancies-html | script:s5_tenancies_html.py | done | 41 tenancies, 21 gaps, html rendered
2026-07-06T10:32+10:00 | 287-cleveland-st-redfern | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-06T10:32+10:00 | 71-therry-street-avalon-beach | s3-timeline | script:s3_timeline.py | done | 61 events; unresolved rooms: {'maintenance': 25}; deduped: {}
2026-07-06T10:32+10:00 | 71-therry-street-avalon-beach | s5-tenancies-html | script:s5_tenancies_html.py | done | 23 tenancies, 13 gaps, html rendered
2026-07-06T10:32+10:00 | 71-therry-street-avalon-beach | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-06T11:55+10:00 | batch-00R-rerun | stageC-complete | orchestrator | PASS | +2 ruling-completions applied (287 Leonardo set_date 2025-11-22; 71 Owen move-in exclude), 287+71 re-run VERIFY PASS; 66+1-148 fully clean; remaining double-ongoing = genuine Kurian items (287 035A/035B/38/41, 350 1169/1170/1175, 71 174/479); double-check package posted, awaiting Kurian
2026-07-06T12:20+10:00 | batch-00R-rerun | roster-reconciliation | orchestrator | INFO | incorporated "Tenant Name" col from New Raw Data trimmed (ground-truth current occupant); reconciled vs timeline ongoing all 5 houses; resolved over-occupancy (current vs departed/missing-move-out), named pre-window occupants, flagged code-crosses (287 #40/#41, 71 #168A/#479). Artifact: data/batches/batch-00R-roster-reconciliation.md
2026-07-06T11:00+10:00 | 287-cleveland-st-redfern | s1-filter:movein | script:s1_filter_house.py | done | 181 kept of 19476 (117 out-of-window dropped; 0 no-date kept)
2026-07-06T11:00+10:00 | 287-cleveland-st-redfern | s1-filter:moveout | script:s1_filter_house.py | done | 68 kept of 23810 (176 out-of-window dropped; 0 no-date kept)
2026-07-06T11:00+10:00 | 287-cleveland-st-redfern | s1-filter:maintenance | script:s1_filter_house.py | done | 177 kept of 49791 (215 out-of-window dropped; 0 no-date kept)
2026-07-06T11:00+10:00 | 287-cleveland-st-redfern | s2-preflag:movein | script:s2_preflag.py | done | 47/181 flagged for human review (tc:40 kw:0 inc:7)
2026-07-06T11:00+10:00 | 287-cleveland-st-redfern | s2-preflag:moveout | script:s2_preflag.py | done | 50/68 flagged for human review (tc:21 kw:0 inc:29)
2026-07-06T11:00+10:00 | 287-cleveland-st-redfern | s2-preflag:maintenance | script:s2_preflag.py | done | 7/177 flagged for human review (tc:4 kw:3 inc:0)
2026-07-06T11:00+10:00 | 287-cleveland-st-redfern | s3-timeline | script:s3_timeline.py | done | 115 events; unresolved rooms: {'maintenance': 55}; deduped: {'moveout': 1}
2026-07-06T11:00+10:00 | 287-cleveland-st-redfern | s5-tenancies-html | script:s5_tenancies_html.py | done | 41 tenancies, 21 gaps, html rendered
2026-07-06T11:00+10:00 | 287-cleveland-st-redfern | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-06T11:00+10:00 | 287-cleveland-st-redfern | eval-loop | script:eval/run_eval.py | FAIL | report: pipeline/eval/reports/2026-07-06_287-cleveland-st-redfern.md
2026-07-06T11:00+10:00 | 1-148-liverpool-rd-enfield | s1-filter:movein | script:s1_filter_house.py | done | 29 kept of 19476 (10 out-of-window dropped; 0 no-date kept)
2026-07-06T11:00+10:00 | 1-148-liverpool-rd-enfield | s1-filter:moveout | script:s1_filter_house.py | done | 17 kept of 23810 (20 out-of-window dropped; 0 no-date kept)
2026-07-06T11:00+10:00 | 1-148-liverpool-rd-enfield | s1-filter:maintenance | script:s1_filter_house.py | done | 54 kept of 49791 (56 out-of-window dropped; 0 no-date kept)
2026-07-06T11:00+10:00 | 1-148-liverpool-rd-enfield | s2-preflag:movein | script:s2_preflag.py | done | 11/29 flagged for human review (tc:10 kw:0 inc:1)
2026-07-06T11:00+10:00 | 1-148-liverpool-rd-enfield | s2-preflag:moveout | script:s2_preflag.py | done | 16/17 flagged for human review (tc:8 kw:0 inc:8)
2026-07-06T11:00+10:00 | 1-148-liverpool-rd-enfield | s2-preflag:maintenance | script:s2_preflag.py | done | 3/54 flagged for human review (tc:2 kw:1 inc:0)
2026-07-06T11:00+10:00 | 1-148-liverpool-rd-enfield | s3-timeline | script:s3_timeline.py | done | 37 events; unresolved rooms: {'maintenance': 20}; deduped: {'moveout': 2}
2026-07-06T11:00+10:00 | 1-148-liverpool-rd-enfield | s5-tenancies-html | script:s5_tenancies_html.py | done | 9 tenancies, 6 gaps, html rendered
2026-07-06T11:00+10:00 | 1-148-liverpool-rd-enfield | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-06T11:00+10:00 | 1-148-liverpool-rd-enfield | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-06_1-148-liverpool-rd-enfield.md
2026-07-06T11:00+10:00 | 350-marsden-rd-carlingford | s1-filter:movein | script:s1_filter_house.py | done | 74 kept of 19476 (14 out-of-window dropped; 0 no-date kept)
2026-07-06T11:00+10:00 | 350-marsden-rd-carlingford | s1-filter:moveout | script:s1_filter_house.py | done | 20 kept of 23810 (10 out-of-window dropped; 0 no-date kept)
2026-07-06T11:00+10:00 | 350-marsden-rd-carlingford | s1-filter:maintenance | script:s1_filter_house.py | done | 112 kept of 49791 (51 out-of-window dropped; 0 no-date kept)
2026-07-06T11:00+10:00 | 350-marsden-rd-carlingford | s2-preflag:movein | script:s2_preflag.py | done | 24/74 flagged for human review (tc:23 kw:0 inc:1)
2026-07-06T11:00+10:00 | 350-marsden-rd-carlingford | s2-preflag:moveout | script:s2_preflag.py | done | 14/20 flagged for human review (tc:13 kw:0 inc:1)
2026-07-06T11:00+10:00 | 350-marsden-rd-carlingford | s2-preflag:maintenance | script:s2_preflag.py | done | 1/112 flagged for human review (tc:1 kw:0 inc:0)
2026-07-06T11:00+10:00 | 350-marsden-rd-carlingford | s3-timeline | script:s3_timeline.py | done | 77 events; unresolved rooms: {'movein': 1, 'maintenance': 37}; deduped: {'moveout': 2}
2026-07-06T11:00+10:00 | 350-marsden-rd-carlingford | s5-tenancies-html | script:s5_tenancies_html.py | done | 22 tenancies, 15 gaps, html rendered
2026-07-06T11:00+10:00 | 350-marsden-rd-carlingford | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-06T11:00+10:00 | 350-marsden-rd-carlingford | eval-loop | script:eval/run_eval.py | FAIL | report: pipeline/eval/reports/2026-07-06_350-marsden-rd-carlingford.md
2026-07-06T11:00+10:00 | 66-boundary-st-parramatta | s1-filter:movein | script:s1_filter_house.py | done | 58 kept of 19476 (81 out-of-window dropped; 0 no-date kept)
2026-07-06T11:00+10:00 | 66-boundary-st-parramatta | s1-filter:moveout | script:s1_filter_house.py | done | 62 kept of 23810 (102 out-of-window dropped; 0 no-date kept)
2026-07-06T11:00+10:00 | 66-boundary-st-parramatta | s1-filter:maintenance | script:s1_filter_house.py | done | 125 kept of 49791 (215 out-of-window dropped; 0 no-date kept)
2026-07-06T11:00+10:00 | 66-boundary-st-parramatta | s2-preflag:movein | script:s2_preflag.py | done | 19/58 flagged for human review (tc:17 kw:0 inc:2)
2026-07-06T11:00+10:00 | 66-boundary-st-parramatta | s2-preflag:moveout | script:s2_preflag.py | done | 44/62 flagged for human review (tc:12 kw:0 inc:32)
2026-07-06T11:00+10:00 | 66-boundary-st-parramatta | s2-preflag:maintenance | script:s2_preflag.py | done | 0/125 flagged for human review (tc:0 kw:0 inc:0)
2026-07-06T11:00+10:00 | 66-boundary-st-parramatta | s3-timeline | script:s3_timeline.py | done | 84 events; unresolved rooms: {'movein': 1, 'maintenance': 59}; deduped: {'moveout': 1}
2026-07-06T11:00+10:00 | 66-boundary-st-parramatta | s5-tenancies-html | script:s5_tenancies_html.py | done | 17 tenancies, 11 gaps, html rendered
2026-07-06T11:00+10:00 | 66-boundary-st-parramatta | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-06T11:00+10:00 | 66-boundary-st-parramatta | eval-loop | script:eval/run_eval.py | FAIL | report: pipeline/eval/reports/2026-07-06_66-boundary-st-parramatta.md
2026-07-06T11:00+10:00 | 71-therry-street-avalon-beach | s1-filter:movein | script:s1_filter_house.py | done | 60 kept of 19476 (20 out-of-window dropped; 0 no-date kept)
2026-07-06T11:00+10:00 | 71-therry-street-avalon-beach | s1-filter:moveout | script:s1_filter_house.py | done | 32 kept of 23810 (104 out-of-window dropped; 0 no-date kept)
2026-07-06T11:00+10:00 | 71-therry-street-avalon-beach | s1-filter:maintenance | script:s1_filter_house.py | done | 104 kept of 49791 (78 out-of-window dropped; 0 no-date kept)
2026-07-06T11:00+10:00 | 71-therry-street-avalon-beach | s2-preflag:movein | script:s2_preflag.py | done | 22/60 flagged for human review (tc:20 kw:0 inc:3)
2026-07-06T11:00+10:00 | 71-therry-street-avalon-beach | s2-preflag:moveout | script:s2_preflag.py | done | 27/32 flagged for human review (tc:12 kw:1 inc:14)
2026-07-06T11:00+10:00 | 71-therry-street-avalon-beach | s2-preflag:maintenance | script:s2_preflag.py | done | 2/104 flagged for human review (tc:1 kw:1 inc:0)
2026-07-06T11:00+10:00 | 71-therry-street-avalon-beach | s3-timeline | script:s3_timeline.py | done | 61 events; unresolved rooms: {'maintenance': 25}; deduped: {}
2026-07-06T11:00+10:00 | 71-therry-street-avalon-beach | s5-tenancies-html | script:s5_tenancies_html.py | done | 23 tenancies, 13 gaps, html rendered
2026-07-06T11:00+10:00 | 71-therry-street-avalon-beach | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-06T11:00+10:00 | 71-therry-street-avalon-beach | eval-loop | script:eval/run_eval.py | FAIL | report: pipeline/eval/reports/2026-07-06_71-therry-street-avalon-beach.md
2026-07-06T11:00+10:00 | 342-cleveland-st-surry-hills | s1-filter:movein | script:s1_filter_house.py | done | 43 kept of 19476 (59 out-of-window dropped; 0 no-date kept)
2026-07-06T11:00+10:00 | 342-cleveland-st-surry-hills | s1-filter:moveout | script:s1_filter_house.py | done | 20 kept of 23810 (139 out-of-window dropped; 0 no-date kept)
2026-07-06T11:00+10:00 | 342-cleveland-st-surry-hills | s1-filter:maintenance | script:s1_filter_house.py | done | 104 kept of 49791 (160 out-of-window dropped; 0 no-date kept)
2026-07-06T11:00+10:00 | 342-cleveland-st-surry-hills | s2-preflag:movein | script:s2_preflag.py | done | 14/43 flagged for human review (tc:14 kw:0 inc:0)
2026-07-06T11:00+10:00 | 342-cleveland-st-surry-hills | s2-preflag:moveout | script:s2_preflag.py | done | 17/20 flagged for human review (tc:11 kw:0 inc:6)
2026-07-06T11:00+10:00 | 342-cleveland-st-surry-hills | s2-preflag:maintenance | script:s2_preflag.py | done | 1/104 flagged for human review (tc:1 kw:0 inc:0)
2026-07-06T11:00+10:00 | 342-cleveland-st-surry-hills | s3-timeline | script:s3_timeline.py | done | 57 events; unresolved rooms: {'maintenance': 31}; deduped: {}
2026-07-06T11:00+10:00 | 342-cleveland-st-surry-hills | s5-tenancies-html | script:s5_tenancies_html.py | done | 15 tenancies, 7 gaps, html rendered
2026-07-06T11:00+10:00 | 342-cleveland-st-surry-hills | s4-verify | script:s4_verify.py | PASS | 0 failing checks
2026-07-06T11:00+10:00 | 342-cleveland-st-surry-hills | eval-loop | script:eval/run_eval.py | PASS | report: pipeline/eval/reports/2026-07-06_342-cleveland-st-surry-hills.md
2026-07-06T12:45+10:00 | batch-00R-rerun | stageD-eval | orchestrator | INFO | eval all 6: 1-148 PASS, 342 PASS (regression green); 287/350/66/71 FAIL = expected drift, each maps to exactly ONE intended change (287 Leonardo set_date, 350 Dhruv gap-hunt, 66 Adriano slot, 71 Owen ruling). ZERO unexplained divergences. Goldens for 287/350/66/71 pending Kurian sign-off to re-freeze.
2026-07-06T13:15+10:00 | batch-00R-rerun | stageD-report+dashboard | orchestrator | DONE | wrote batch-00R-rerun-REPORT.md + data/final/batch-00R-timelines.html (interactive: timelines, tenant drill-down, flag buckets, gaps w/ days, signed-vs-actual, roster truth). Goldens NOT re-frozen — awaiting Kurian sign-off for 287/350/66/71 (1-148 & 342 unchanged). Verdict: pipeline ready for batch-01 at 8-10 houses.
