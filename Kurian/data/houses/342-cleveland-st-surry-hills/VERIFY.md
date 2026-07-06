# VERIFY — 342-cleveland-st-surry-hills
Run: 2026-07-06T11:00+10:00
Verdict: **PASS**

- [PASS] movein: duplicate Task IDs within file: none
- [PASS] moveout: duplicate Task IDs within file: none
- [PASS] maintenance: duplicate Task IDs within file: none
- [PASS] Task-ID exclusivity movein∩moveout: 3 shared (3 multi-homed/subtask, unexplained: none)
- [PASS] Task-ID exclusivity movein∩maintenance: 0 shared (0 multi-homed/subtask, unexplained: none)
- [PASS] Task-ID exclusivity moveout∩maintenance: 0 shared (0 multi-homed/subtask, unexplained: none)
- [PASS] timeline dates within 2025-05-31…2026-07-31: 0 outside 
- [PASS] events with no parseable date: 0 
- [PASS] row-count: top-level 61 - 4 excluded + 0 promoted-subtasks vs timeline events 57 (delta 0)
- [PASS] room-resolution: move-outs stranded UNRESOLVED despite valid #code in name: none
- [PASS] unresolved move-outs (no code anywhere): 0
- [INFO] per-room in/out balance: {'1104': 'in=2 out=1', '1105': 'in=3 out=3', '1107': 'in=3 out=3', '1108': 'in=1 out=1', '1109': 'in=1 out=1', 'UNRESOLVED': 'in=0 out=0'}
