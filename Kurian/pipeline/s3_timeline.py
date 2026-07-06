#!/usr/bin/env python3
"""S3 — Room attribution + per-room event timeline.

For each S1-filtered row: resolve the room code (Room Code column → '#code' in Name → Notes),
then emit timeline events:
  movein  → event_type=move_in,  event_date = Due Date (Asana convention: move-in date),
            fallback Date and Time Paid, fallback Completed At
  moveout → event_type=move_out, event_date = LATEST of {Due Date, Earliest Date to Move Out,
            date written in task name} (Kurian ruling 2026-07-05 #7) — unless that overlaps
            the next tenant's move-in for the room by MORE than 1 day, in which case fall
            back to the latest non-conflicting candidate and flag HUMAN REVIEW.
  maintenance → event_type=maintenance, event_date = Created At (issue raised)

Every event carries task_id, date_source, human_review flag, and match_reason so each
timeline entry is traceable to its source row.

Usage: python3 pipeline/s3_timeline.py <house-slug>
Output: data/houses/<slug>/timeline.csv + rooms_report.md
"""
import sys
from collections import Counter, defaultdict
from datetime import timedelta
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent / "lib"))
from common import (PROJECT_ROOT, load_settings, house_config, read_csv, write_csv,
                    parse_date, resolve_room_code, dates_in_text, tenant_from_name,
                    now_sydney_iso, append_runlog)

EVENT_SPEC = {
    "movein": ("move_in", [("Due Date", "due_date"), ("Date and Time Paid", "paid_date"),
                            ("Completed At", "completed_at")]),
    "moveout": ("move_out", [("Due Date", "due_date"),
                              ("Earliest Date to Move Out", "earliest_move_out")]),
    "maintenance": ("maintenance", [("Created At", "created_at")]),
}
FIELDS = ["room_code", "room_label", "event_type", "event_date", "date_source", "tenant",
          "task_id", "task_name", "section", "source", "in_window", "human_review",
          "flags", "match_reason"]

def main(slug):
    st = load_settings()
    hc = house_config(slug)
    codes = set(c.upper() for c in hc["room_codes"])
    labels = hc.get("room_names", {})
    outdir = PROJECT_ROOT / st["houses_dir"] / slug
    # Kurian rulings: overrides.csv (task_id,action,reason,...) — action=exclude drops the
    # task from the timeline (it stays in the filtered CSVs for traceability).
    overrides = {}
    ov_path = outdir / "overrides.csv"
    if ov_path.exists():
        overrides = {r["task_id"]: r for r in read_csv(ov_path)[0]}
    excluded, promoted_events = [], []
    events, unresolved = [], Counter()
    seen_ids, deduped = set(), Counter()
    for source, (etype, date_prefs) in EVENT_SPEC.items():
        rows, _ = read_csv(outdir / f"{source}_filtered.csv")
        for row in rows:
            ov = overrides.get(row.get("Task ID"))
            promoted = bool(ov and ov["action"] == "promote_move_out")
            if row.get("is_subtask") == "yes" and not promoted:
                continue  # checklist items under a parent task — not standalone events
                # (exception: overrides action=promote_move_out — pilot defect #2:
                #  perm transfer-outs are logged as subtasks but ARE effective move-outs)
            if ov and ov["action"] == "exclude":
                excluded.append(f"{row.get('Task ID')} ({ov['reason'][:60]}…)")
                continue
            if row.get("Task ID") in seen_ids:
                deduped[source] += 1  # multi-homed task already emitted from a higher-priority source
                continue
            seen_ids.add(row.get("Task ID"))
            row_etype = "move_out" if promoted else etype
            if promoted:
                promoted_events.append(row.get("Task ID"))
            # defect #2b: transfer subtasks have a blank Tenant Name column — derive from Name
            tenant = (row.get("Tenant Name") or "").strip()
            tenant_derived = ""
            if not tenant:
                tenant = tenant_from_name(row.get("Name", ""),
                                          hc.get("canonical_address", "").split(",")[-1].strip())
                if tenant:
                    tenant_derived = "tenant_derived_from_name"
            code, how = resolve_room_code(row, codes)
            # override action reassign_room: slot-method / Kurian room rulings win outright
            # (code-crossers: tenant's events collapse onto the room they actually occupied)
            reassigned = ""
            if ov and ov["action"] == "reassign_room" and (ov.get("room") or "").strip():
                code, how = ov["room"].strip().upper(), "override_reassign"
                reassigned = "room_reassigned"
            if not code:
                unresolved[source] += 1
            d = dsrc = None
            candidates = []  # move-out later-date rule (ruling #7)
            if row_etype == "move_out":
                for field, label in (("Due Date", "due_date"),
                                     ("Earliest Date to Move Out", "earliest_move_out")):
                    cd = parse_date(row.get(field, ""))
                    if cd:
                        candidates.append((cd, label))
                ref = candidates[0][0] if candidates else None
                for nd in dates_in_text(row.get("Name", ""), ref):
                    candidates.append((nd, "name_date"))
                candidates.sort()
                if candidates:
                    d, dsrc = candidates[-1]  # latest; conflict check after assembly
            if not d:
                for field, label in date_prefs:
                    d = parse_date(row.get(field, ""))
                    if d:
                        dsrc = label
                        break
            # override action set_move_out_date: comment-derived date correction wins outright
            if ov and ov["action"] == "set_move_out_date" and parse_date(ov.get("date", "")):
                d, dsrc = parse_date(ov["date"]), "override_set_date"
                candidates = []  # exempt from ruling-#7 conflict pass — Kurian/comment-ruled
            flags = "|".join(filter(None, [row.get("flag_transfer_cancel") and "transfer_cancel",
                                           row.get("flag_date_keyword"),
                                           row.get("flag_inconsistency"), tenant_derived,
                                           reassigned]))
            events.append({
                "room_code": code, "room_label": labels.get(code, ""),
                "event_type": row_etype, "event_date": d.isoformat() if d else "",
                "date_source": dsrc or "none", "tenant": tenant,
                "task_id": row.get("Task ID", ""), "task_name": (row.get("Name") or "").strip(),
                "section": row.get("Section/Column", ""), "source": source,
                "in_window": row.get("in_window", ""), "human_review": row.get("human_review", ""),
                "flags": flags, "match_reason": row.get("match_reason", ""),
                "_candidates": candidates,
            })

    # Ruling #7 conflict pass: a move-out may not overlap the next move-in by >1 day.
    n_conflicts = 0
    moveins_by_room = defaultdict(list)
    for e in events:
        if e["event_type"] == "move_in" and e["event_date"] and e["room_code"]:
            moveins_by_room[e["room_code"]].append(parse_date(e["event_date"]))
    for e in events:
        cands = e.pop("_candidates", [])
        if e["event_type"] != "move_out" or not cands or not e["room_code"]:
            continue
        chosen = parse_date(e["event_date"])
        nxt = min((mi for mi in moveins_by_room.get(e["room_code"], [])
                   if mi >= cands[0][0]), default=None)
        if nxt and chosen > nxt + timedelta(days=1):
            ok = [(d, s) for d, s in cands if d <= nxt + timedelta(days=1)]
            d, s = (ok[-1] if ok else cands[0])
            e["event_date"], e["date_source"] = d.isoformat(), f"{s}_conflict_fallback"
            e["human_review"] = "yes"
            e["flags"] = "|".join(filter(None, [e["flags"], "moveout_date_conflict"]))
            n_conflicts += 1

    events.sort(key=lambda e: (e["room_code"] or "~", e["event_date"] or "9999"))
    write_csv(outdir / "timeline.csv", events, FIELDS)

    per_room = defaultdict(Counter)
    for e in events:
        per_room[e["room_code"] or "UNRESOLVED"][e["event_type"]] += 1
    rep = [f"# S3 rooms report — {slug}", f"Run: {now_sydney_iso()}", "",
           "| room | label | move_in | move_out | maintenance |", "|---|---|---|---|---|"]
    for rc in sorted(per_room):
        c = per_room[rc]
        rep.append(f"| {rc} | {labels.get(rc, '')} | {c['move_in']} | {c['move_out']} | {c['maintenance']} |")
    rep += ["", f"Unresolved room attribution by source: {dict(unresolved)}",
            f"Multi-homed tasks deduped (kept higher-priority source): {dict(deduped)}",
            f"Excluded by overrides.csv (Kurian rulings): {excluded or 'none'}",
            f"Promoted transfer-out subtasks (overrides promote_move_out): {promoted_events or 'none'}",
            f"Move-out date conflicts (ruling #7 fallback applied): {n_conflicts}",
            f"Total events: {len(events)} → timeline.csv"]
    (outdir / "rooms_report.md").write_text("\n".join(rep), encoding="utf-8")
    append_runlog(f"{now_sydney_iso()} | {slug} | s3-timeline | script:s3_timeline.py | done | "
                  f"{len(events)} events; unresolved rooms: {dict(unresolved)}; deduped: {dict(deduped)}")
    print("\n".join(rep))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
