# Eval report — 287-cleveland-st-redfern — 2026-07-06T11:00+10:00
**Verdict: FAIL**

U1/U2 parser unit tests: PASS
E1 s1_filter_house.py: PASS
E1 s2_preflag.py: PASS
E1 s3_timeline.py: PASS
E1 s5_tenancies_html.py: PASS
E1 s4_verify.py: PASS
E2 tenancies vs golden: FAIL
  MISSING vs golden: [('36', 'leonardo', '', '2025-09-22', 'pre_window', 'move_out'), ('36', 'leonardo', '2025-09-29', '', 'move_in', 'ongoing')]
  EXTRA vs golden: [('36', 'leonardo', '2025-09-29', '2025-11-22', 'move_in', 'move_out')]
E3 vacancy gaps vs golden: FAIL
  MISSING vs golden: [('36', '', '', ''), ('36', '2025-09-22', '2025-09-29', '7')]
  EXTRA vs golden: [('36', '2025-09-01', '2025-09-29', '28'), ('36', '2025-11-22', '2025-11-25', '3')]