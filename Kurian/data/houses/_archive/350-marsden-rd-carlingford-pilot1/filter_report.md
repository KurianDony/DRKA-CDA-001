# S1 filter report — 350 Marsden Rd, Carlingford (350-marsden-rd-carlingford)
Run: 2026-07-05T18:52+10:00
Audit window: 2025-07-01 → 2026-06-30; padding: {'movein': 7, 'moveout': 7, 'maintenance': 31}

## movein (2025_Applications_Moving_In (3).csv)
- raw rows scanned: 19476
- padded window: 2025-06-24 → 2026-07-07
- rows kept: 74 (address hits: 74, room-code-only: 0, subtasks: 54, top-level: 20)
- house matches dropped as outside padded window: 14
- kept with no parseable event date: 0
- rows in audit window proper: 73
- output: data/houses/350-marsden-rd-carlingford/movein_filtered.csv

## moveout (Off_boarding_team_ (2).csv)
- raw rows scanned: 23810
- padded window: 2025-06-24 → 2026-07-07
- rows kept: 20 (address hits: 20, room-code-only: 0, subtasks: 6, top-level: 14)
- house matches dropped as outside padded window: 10
- kept with no parseable event date: 0
- rows in audit window proper: 19
- output: data/houses/350-marsden-rd-carlingford/moveout_filtered.csv

## maintenance (Maintenance_Requests.csv)
- raw rows scanned: 49791
- padded window: 2025-05-31 → 2026-07-31
- rows kept: 112 (address hits: 112, room-code-only: 0, subtasks: 67, top-level: 45)
- house matches dropped as outside padded window: 51
- kept with no parseable event date: 0
- rows in audit window proper: 89
- output: data/houses/350-marsden-rd-carlingford/maintenance_filtered.csv
