# S1 filter report — 66 Boundary St, Parramatta (66-boundary-st-parramatta)
Run: 2026-07-05T18:52+10:00
Audit window: 2025-07-01 → 2026-06-30; padding: {'movein': 7, 'moveout': 7, 'maintenance': 31}

## movein (2025_Applications_Moving_In (3).csv)
- raw rows scanned: 19476
- padded window: 2025-06-24 → 2026-07-07
- rows kept: 58 (address hits: 58, room-code-only: 0, subtasks: 41, top-level: 17)
- house matches dropped as outside padded window: 81
- kept with no parseable event date: 0
- rows in audit window proper: 58
- output: data/houses/66-boundary-st-parramatta/movein_filtered.csv

## moveout (Off_boarding_team_ (2).csv)
- raw rows scanned: 23810
- padded window: 2025-06-24 → 2026-07-07
- rows kept: 62 (address hits: 62, room-code-only: 0, subtasks: 51, top-level: 11)
- house matches dropped as outside padded window: 102
- kept with no parseable event date: 0
- rows in audit window proper: 60
- output: data/houses/66-boundary-st-parramatta/moveout_filtered.csv

## maintenance (Maintenance_Requests.csv)
- raw rows scanned: 49791
- padded window: 2025-05-31 → 2026-07-31
- rows kept: 125 (address hits: 125, room-code-only: 0, subtasks: 66, top-level: 59)
- house matches dropped as outside padded window: 215
- kept with no parseable event date: 0
- rows in audit window proper: 119
- output: data/houses/66-boundary-st-parramatta/maintenance_filtered.csv
