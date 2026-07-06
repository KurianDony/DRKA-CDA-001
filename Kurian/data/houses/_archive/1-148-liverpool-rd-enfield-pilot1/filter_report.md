# S1 filter report — 1/148 Liverpool Rd, Enfield (1-148-liverpool-rd-enfield)
Run: 2026-07-05T18:52+10:00
Audit window: 2025-07-01 → 2026-06-30; padding: {'movein': 7, 'moveout': 7, 'maintenance': 31}

## movein (2025_Applications_Moving_In (3).csv)
- raw rows scanned: 19476
- padded window: 2025-06-24 → 2026-07-07
- rows kept: 29 (address hits: 29, room-code-only: 0, subtasks: 22, top-level: 7)
- house matches dropped as outside padded window: 10
- kept with no parseable event date: 0
- rows in audit window proper: 29
- output: data/houses/1-148-liverpool-rd-enfield/movein_filtered.csv

## moveout (Off_boarding_team_ (2).csv)
- raw rows scanned: 23810
- padded window: 2025-06-24 → 2026-07-07
- rows kept: 17 (address hits: 17, room-code-only: 0, subtasks: 11, top-level: 6)
- house matches dropped as outside padded window: 20
- kept with no parseable event date: 0
- rows in audit window proper: 17
- output: data/houses/1-148-liverpool-rd-enfield/moveout_filtered.csv

## maintenance (Maintenance_Requests.csv)
- raw rows scanned: 49791
- padded window: 2025-05-31 → 2026-07-31
- rows kept: 54 (address hits: 54, room-code-only: 0, subtasks: 30, top-level: 24)
- house matches dropped as outside padded window: 56
- kept with no parseable event date: 0
- rows in audit window proper: 52
- output: data/houses/1-148-liverpool-rd-enfield/maintenance_filtered.csv
