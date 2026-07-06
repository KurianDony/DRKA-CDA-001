# Eval report — 66-boundary-st-parramatta — 2026-07-06T11:00+10:00
**Verdict: FAIL**

U1/U2 parser unit tests: PASS
E1 s1_filter_house.py: PASS
E1 s2_preflag.py: PASS
E1 s3_timeline.py: PASS
E1 s5_tenancies_html.py: PASS
E1 s4_verify.py: PASS
E2 tenancies vs golden: FAIL
  MISSING vs golden: [('10', 'michael', '2025-09-15', '', 'move_in', 'ongoing')]
  EXTRA vs golden: [('7', 'michael', '2025-09-15', '2025-09-23', 'move_in', 'move_out')]
E3 vacancy gaps vs golden: FAIL
  MISSING vs golden: [('10', '', '', ''), ('10', '2025-09-11', '2025-09-15', '4'), ('7', '2025-09-08', '2025-10-03', '25')]
  EXTRA vs golden: [('10', '2025-09-11', '2025-10-18', '37'), ('7', '2025-09-08', '2025-09-15', '7'), ('7', '2025-09-23', '2025-10-03', '10')]