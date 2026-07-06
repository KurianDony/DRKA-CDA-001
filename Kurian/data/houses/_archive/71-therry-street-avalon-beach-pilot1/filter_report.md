# S1 filter report — 71 Therry Street, Avalon Beach (71-therry-street-avalon-beach)
Run: 2026-07-05T18:52+10:00
Audit window: 2025-07-01 → 2026-06-30; padding: {'movein': 7, 'moveout': 7, 'maintenance': 31}

## movein (2025_Applications_Moving_In (3).csv)
- raw rows scanned: 19476
- padded window: 2025-06-24 → 2026-07-07
- rows kept: 60 (address hits: 60, room-code-only: 0, subtasks: 43, top-level: 17)
- house matches dropped as outside padded window: 20
- kept with no parseable event date: 0
- rows in audit window proper: 52
- output: data/houses/71-therry-street-avalon-beach/movein_filtered.csv

## moveout (Off_boarding_team_ (2).csv)
- raw rows scanned: 23810
- padded window: 2025-06-24 → 2026-07-07
- rows kept: 32 (address hits: 32, room-code-only: 0, subtasks: 17, top-level: 15)
- house matches dropped as outside padded window: 104
- kept with no parseable event date: 0
- rows in audit window proper: 28
- output: data/houses/71-therry-street-avalon-beach/moveout_filtered.csv

## maintenance (Maintenance_Requests.csv)
- raw rows scanned: 49791
- padded window: 2025-05-31 → 2026-07-31
- rows kept: 104 (address hits: 104, room-code-only: 0, subtasks: 71, top-level: 33)
- house matches dropped as outside padded window: 78
- kept with no parseable event date: 0
- rows in audit window proper: 94
- output: data/houses/71-therry-street-avalon-beach/maintenance_filtered.csv
