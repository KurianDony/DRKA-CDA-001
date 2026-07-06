# Eval report — 350-marsden-rd-carlingford — 2026-07-06T11:00+10:00
**Verdict: FAIL**

U1/U2 parser unit tests: PASS
E1 s1_filter_house.py: PASS
E1 s2_preflag.py: PASS
E1 s3_timeline.py: PASS
E1 s5_tenancies_html.py: PASS
E1 s4_verify.py: PASS
E2 tenancies vs golden: FAIL
  MISSING vs golden: [('1169', 'dhruv', '2026-02-15', '', 'move_in', 'ongoing')]
  EXTRA vs golden: [('1169', 'dhruv', '2026-02-15', '2026-02-20', 'move_in', 'move_out')]
E3 vacancy gaps vs golden: FAIL
  EXTRA vs golden: [('1169', '2026-02-20', '2026-03-04', '12')]