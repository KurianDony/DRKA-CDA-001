# VERIFY — 71-therry-street-avalon-beach
Run: 2026-07-06T11:00+10:00
Verdict: **PASS**

- [PASS] movein: duplicate Task IDs within file: none
- [PASS] moveout: duplicate Task IDs within file: none
- [PASS] maintenance: duplicate Task IDs within file: none
- [PASS] Task-ID exclusivity movein∩moveout: 1 shared (1 multi-homed/subtask, unexplained: none)
- [PASS] Task-ID exclusivity movein∩maintenance: 0 shared (0 multi-homed/subtask, unexplained: none)
- [PASS] Task-ID exclusivity moveout∩maintenance: 0 shared (0 multi-homed/subtask, unexplained: none)
- [PASS] timeline dates within 2025-05-31…2026-07-31: 0 outside 
- [PASS] events with no parseable date: 0 
- [PASS] row-count: top-level 65 - 4 excluded + 0 promoted-subtasks vs timeline events 61 (delta 0)
- [PASS] room-resolution: move-outs stranded UNRESOLVED despite valid #code in name: none
- [PASS] unresolved move-outs (no code anywhere): 0
- [INFO] per-room in/out balance: {'168': 'in=1 out=1', '168A': 'in=2 out=2', '170': 'in=2 out=2', '171': 'in=2 out=2', '172': 'in=1 out=1', '174': 'in=4 out=3', '479': 'in=3 out=2', 'UNRESOLVED': 'in=0 out=0'}
