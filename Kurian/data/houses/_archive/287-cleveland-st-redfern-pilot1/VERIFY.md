# VERIFY — 287-cleveland-st-redfern
Run: 2026-07-05T18:52+10:00
Verdict: **PASS**

- [PASS] movein: duplicate Task IDs within file: none
- [PASS] moveout: duplicate Task IDs within file: none
- [PASS] maintenance: duplicate Task IDs within file: none
- [PASS] Task-ID exclusivity movein∩moveout: 8 shared (8 multi-homed/subtask, unexplained: none)
- [PASS] Task-ID exclusivity movein∩maintenance: 0 shared (0 multi-homed/subtask, unexplained: none)
- [PASS] Task-ID exclusivity moveout∩maintenance: 0 shared (0 multi-homed/subtask, unexplained: none)
- [PASS] timeline dates within 2025-05-31…2026-07-31: 0 outside 
- [PASS] events with no parseable date: 0 
- [PASS] row-count: top-level 124 - 10 excluded + 1 promoted-subtasks vs timeline events 115 (delta 0)
- [PASS] room-resolution: move-outs stranded UNRESOLVED despite valid #code in name: none
- [PASS] unresolved move-outs (no code anywhere): 0
- [INFO] per-room in/out balance: {'035A': 'in=4 out=1', '035B': 'in=4 out=2', '037A': 'in=3 out=3', '037B': 'in=2 out=2', '038B': 'in=0 out=1', '039A': 'in=1 out=1', '36': 'in=2 out=2', '38': 'in=3 out=2', '39': 'in=5 out=5', '40': 'in=1 out=0', '40A': 'in=1 out=1', '40B': 'in=0 out=1', '41': 'in=6 out=4', 'UNRESOLVED': 'in=0 out=0'}
