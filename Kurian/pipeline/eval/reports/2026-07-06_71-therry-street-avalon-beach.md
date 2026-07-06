# Eval report — 71-therry-street-avalon-beach — 2026-07-06T11:00+10:00
**Verdict: FAIL**

U1/U2 parser unit tests: PASS
E1 s1_filter_house.py: PASS
E1 s2_preflag.py: PASS
E1 s3_timeline.py: PASS
E1 s5_tenancies_html.py: PASS
E1 s4_verify.py: PASS
E2 tenancies vs golden: FAIL
  MISSING vs golden: [('172', 'owen', '2026-01-18', '', 'move_in', 'ongoing')]
E3 vacancy gaps vs golden: FAIL
  MISSING vs golden: [('172', '', '', ''), ('172', '2026-01-15', '2026-01-18', '3')]
  EXTRA vs golden: [('172', '2026-01-15', '2026-03-17', '61')]