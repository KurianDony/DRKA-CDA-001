# VERIFY — 350-marsden-rd-carlingford
Run: 2026-07-06T11:00+10:00
Verdict: **PASS**

- [PASS] movein: duplicate Task IDs within file: none
- [PASS] moveout: duplicate Task IDs within file: none
- [PASS] maintenance: duplicate Task IDs within file: none
- [PASS] Task-ID exclusivity movein∩moveout: 4 shared (4 multi-homed/subtask, unexplained: none)
- [PASS] Task-ID exclusivity movein∩maintenance: 0 shared (0 multi-homed/subtask, unexplained: none)
- [PASS] Task-ID exclusivity moveout∩maintenance: 0 shared (0 multi-homed/subtask, unexplained: none)
- [PASS] timeline dates within 2025-05-31…2026-07-31: 0 outside 
- [PASS] events with no parseable date: 0 
- [PASS] row-count: top-level 79 - 4 excluded + 2 promoted-subtasks vs timeline events 77 (delta 0)
- [PASS] room-resolution: move-outs stranded UNRESOLVED despite valid #code in name: none
- [PASS] unresolved move-outs (no code anywhere): 0
- [INFO] per-room in/out balance: {'1169': 'in=4 out=2', '1170': 'in=3 out=2', '1171': 'in=2 out=2', '1173': 'in=2 out=3', '1174': 'in=2 out=1', '1175': 'in=5 out=3', 'UNRESOLVED': 'in=1 out=0'}
