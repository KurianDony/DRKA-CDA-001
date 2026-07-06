# S1 filter report — 287 Cleveland St, Redfern (287-cleveland-st-redfern)
Run: 2026-07-06T11:00+10:00
Audit window: 2025-07-01 → 2026-06-30; padding: {'movein': 7, 'moveout': 7, 'maintenance': 31}

## movein (2025_Applications_Moving_In (3).csv)
- raw rows scanned: 19476
- padded window: 2025-06-24 → 2026-07-07
- rows kept: 181 (address hits: 181, room-code-only: 0, subtasks: 142, top-level: 39)
- house matches dropped as outside padded window: 117
- kept with no parseable event date: 0
- rows in audit window proper: 166
- output: data/houses/287-cleveland-st-redfern/movein_filtered.csv

## moveout (Off_boarding_team_ (2).csv)
- raw rows scanned: 23810
- padded window: 2025-06-24 → 2026-07-07
- rows kept: 68 (address hits: 68, room-code-only: 0, subtasks: 41, top-level: 27)
- house matches dropped as outside padded window: 176
- kept with no parseable event date: 0
- rows in audit window proper: 62
- output: data/houses/287-cleveland-st-redfern/moveout_filtered.csv

## maintenance (Maintenance_Requests.csv)
- raw rows scanned: 49791
- padded window: 2025-05-31 → 2026-07-31
- rows kept: 177 (address hits: 177, room-code-only: 0, subtasks: 119, top-level: 58)
- house matches dropped as outside padded window: 215
- kept with no parseable event date: 0
- rows in audit window proper: 152
- output: data/houses/287-cleveland-st-redfern/maintenance_filtered.csv
