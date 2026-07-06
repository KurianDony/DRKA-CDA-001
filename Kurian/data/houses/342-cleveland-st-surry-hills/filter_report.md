# S1 filter report — 342 Cleveland St, Surry Hills (342-cleveland-st-surry-hills)
Run: 2026-07-06T11:00+10:00
Audit window: 2025-07-01 → 2026-06-30; padding: {'movein': 7, 'moveout': 7, 'maintenance': 31}

## movein (2025_Applications_Moving_In (3).csv)
- raw rows scanned: 19476
- padded window: 2025-06-24 → 2026-07-07
- rows kept: 43 (address hits: 43, room-code-only: 0, subtasks: 31, top-level: 12)
- house matches dropped as outside padded window: 59
- kept with no parseable event date: 0
- rows in audit window proper: 43
- output: data/houses/342-cleveland-st-surry-hills/movein_filtered.csv

## moveout (Off_boarding_team_ (2).csv)
- raw rows scanned: 23810
- padded window: 2025-06-24 → 2026-07-07
- rows kept: 20 (address hits: 20, room-code-only: 0, subtasks: 9, top-level: 11)
- house matches dropped as outside padded window: 139
- kept with no parseable event date: 0
- rows in audit window proper: 20
- output: data/houses/342-cleveland-st-surry-hills/moveout_filtered.csv

## maintenance (Maintenance_Requests.csv)
- raw rows scanned: 49791
- padded window: 2025-05-31 → 2026-07-31
- rows kept: 104 (address hits: 104, room-code-only: 0, subtasks: 66, top-level: 38)
- house matches dropped as outside padded window: 160
- kept with no parseable event date: 0
- rows in audit window proper: 98
- output: data/houses/342-cleveland-st-surry-hills/maintenance_filtered.csv
