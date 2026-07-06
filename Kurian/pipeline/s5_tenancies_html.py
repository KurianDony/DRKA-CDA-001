#!/usr/bin/env python3
"""S5 — Pair move-in/move-out events into tenancies, compute vacancy gaps, and render a
self-contained HTML per-room timeline mockup.

Pairing per room (from timeline.csv):
  - move_in ↔ move_out matched by tenant first name where possible, else chronology
  - move_out with no prior move_in  → pre-window occupant (bar starts at window start, dashed)
  - move_in with no later move_out  → ongoing tenancy (bar runs to window end, arrow)
Vacancy gap = days between a tenancy's end and the next tenancy's start in the same room.

Usage: python3 pipeline/s5_tenancies_html.py <house-slug>
Output: data/houses/<slug>/tenancies.csv, vacancy_gaps.csv, timeline.html
"""
import sys
from collections import defaultdict
from datetime import timedelta
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent / "lib"))
from common import (PROJECT_ROOT, load_settings, house_config, read_csv, write_csv,
                    parse_date, name_sim, now_sydney_iso, append_runlog)

ASANA = "https://app.asana.com/0/0/{}/f"
import re as _re

def parse_term_months(s):
    """'6 months' / '12 Months' / '6' → 6.0; '' → None."""
    m = _re.search(r"(\d+(?:\.\d+)?)", s or "")
    return float(m.group(1)) if m else None
PALETTE = ["#4e79a7", "#f28e2b", "#59a14f", "#b07aa1", "#76b7b2", "#e15759", "#edc948",
           "#af7aa1", "#9c755f", "#86bcb6"]

def main(slug):
    st = load_settings()
    hc = house_config(slug)
    outdir = PROJECT_ROOT / st["houses_dir"] / slug
    a_start = parse_date(st["audit_window"]["start"])
    a_end = parse_date(st["audit_window"]["end"])
    events, _ = read_csv(outdir / "timeline.csv")
    by_room = defaultdict(lambda: {"in": [], "out": [], "maint": []})
    for e in events:
        if not e["event_date"]:
            continue
        e["_d"] = parse_date(e["event_date"])
        rc = e["room_code"]
        if e["event_type"] == "move_in" and rc:
            by_room[rc]["in"].append(e)
        elif e["event_type"] == "move_out" and rc:
            by_room[rc]["out"].append(e)
        elif e["event_type"] == "maintenance":
            by_room[rc or "HOUSE"]["maint"].append(e)

    tenancies, gaps = [], []
    for rc in sorted(by_room):
        ins = sorted(by_room[rc]["in"], key=lambda e: e["_d"])
        outs = sorted(by_room[rc]["out"], key=lambda e: e["_d"])
        used_in = set()
        # Pair each move_out with a NAME-MATCHED earlier (or same-day) move_in. Never pair
        # across different names — mispairs corrupt the whole room timeline.
        for mo in outs:
            mi = next((i for i in ins if id(i) not in used_in and i["_d"] <= mo["_d"]
                       and name_sim(i["tenant"], mo["tenant"])), None)
            if mi is None:
                # defect #2b fallback: a move-out with no/derived-only tenant closes the room's
                # single open tenancy chronologically — only when unambiguous (exactly 1 candidate)
                open_cands = [i for i in ins if id(i) not in used_in and i["_d"] <= mo["_d"]]
                if len(open_cands) == 1 and (not mo["tenant"] or not open_cands[0]["tenant"]
                                             or "tenant_derived" in (mo.get("flags") or "")
                                             or name_sim(open_cands[0]["tenant"], mo["tenant"])):
                    mi = open_cands[0]
                    mo["human_review"] = "yes"  # chronological pairing — reviewable
            if mi is not None:
                used_in.add(id(mi))
                tenancies.append({
                    "room_code": rc, "tenant": mo["tenant"] or mi["tenant"],
                    "start": mi["_d"], "end": mo["_d"],
                    "start_kind": "move_in", "end_kind": "move_out",
                    "start_task": mi["task_id"], "end_task": mo["task_id"],
                    "hr": "yes" if "yes" in (mi["human_review"], mo["human_review"]) else ""})
            elif not ins or mo["_d"] <= ins[0]["_d"]:
                tenancies.append({  # occupant since before the window
                    "room_code": rc, "tenant": mo["tenant"], "start": None, "end": mo["_d"],
                    "start_kind": "pre_window", "end_kind": "move_out",
                    "start_task": "", "end_task": mo["task_id"], "hr": mo["human_review"] or ""})
            else:  # move_out with no matching move_in and not clearly pre-window
                tenancies.append({
                    "room_code": rc, "tenant": mo["tenant"], "start": None, "end": mo["_d"],
                    "start_kind": "orphan_out", "end_kind": "move_out",
                    "start_task": "", "end_task": mo["task_id"], "hr": "yes"})
        for mi in ins:  # unmatched move_ins = ongoing tenancies
            if id(mi) not in used_in:
                tenancies.append({
                    "room_code": rc, "tenant": mi["tenant"], "start": mi["_d"], "end": None,
                    "start_kind": "move_in", "end_kind": "ongoing",
                    "start_task": mi["task_id"], "end_task": "", "hr": mi["human_review"] or ""})
    tenancies.sort(key=lambda t: (t["room_code"], t["start"] or a_start - timedelta(days=365)))
    for rc in sorted({t["room_code"] for t in tenancies}):
        rts = [t for t in tenancies if t["room_code"] == rc]
        for a, b in zip(rts, rts[1:]):
            if a["end"] and b["start"]:
                gap = (b["start"] - a["end"]).days
                if gap < -1:  # >1 day overlap = conflict (ruling #7 definition)
                    a["hr"] = b["hr"] = "yes"
                    gaps.append({"room_code": rc, "vacant_from": a["end"].isoformat(),
                                 "vacant_to": b["start"].isoformat(), "gap_days": gap,
                                 "prev_tenant": a["tenant"], "next_tenant": b["tenant"],
                                 "note": "OVERLAP >1d — HUMAN REVIEW"})
                elif gap > 0:
                    gaps.append({"room_code": rc, "vacant_from": a["end"].isoformat(),
                                 "vacant_to": b["start"].isoformat(), "gap_days": gap,
                                 "prev_tenant": a["tenant"], "next_tenant": b["tenant"], "note": ""})
            elif a["end"] is None and b["start"]:  # two open-ended tenancies overlapping
                a["hr"] = b["hr"] = "yes"
                gaps.append({"room_code": rc, "vacant_from": "", "vacant_to": "",
                             "gap_days": "", "prev_tenant": a["tenant"], "next_tenant": b["tenant"],
                             "note": "TWO ONGOING/OPEN TENANCIES — HUMAN REVIEW"})

    # Overstay computation (Kurian 2026-07-05): staying past the initial agreed term is
    # NORMAL (month-to-month afterwards) — measure it instead of flagging it.
    terms = {}
    mi_path = outdir / "movein_filtered.csv"
    if mi_path.exists():
        for r in read_csv(mi_path)[0]:
            terms[r["Task ID"]] = parse_term_months(r.get("Agreed Lease Term", ""))
    for t in tenancies:
        term = terms.get(t["start_task"])
        end = t["end"] or a_end  # ongoing → measure to window end
        stay_days = (end - t["start"]).days if t["start"] else None
        t["agreed_term_months"] = term if term is not None else ""
        t["stay_days"] = stay_days if stay_days is not None else ""
        if term and stay_days is not None:
            over = round(stay_days / 30.44 - term, 1)
            t["months_past_term"] = over if over > 0 else 0
        else:
            t["months_past_term"] = ""

    write_csv(outdir / "tenancies.csv",
              [{**t, "start": t["start"].isoformat() if t["start"] else "",
                "end": t["end"].isoformat() if t["end"] else ""} for t in tenancies],
              ["room_code", "tenant", "start", "end", "start_kind", "end_kind",
               "start_task", "end_task", "hr", "agreed_term_months", "stay_days",
               "months_past_term"])
    write_csv(outdir / "vacancy_gaps.csv", gaps,
              ["room_code", "vacant_from", "vacant_to", "gap_days", "prev_tenant", "next_tenant", "note"])

    # ---------- HTML ----------
    x0, x1 = a_start - timedelta(days=7), a_end + timedelta(days=7)
    span = (x1 - x0).days
    W, LEFT, ROW_H, BAR_H = 1240, 130, 92, 34
    def X(d):
        return LEFT + (W - LEFT - 20) * (d - x0).days / span
    rooms = sorted({t["room_code"] for t in tenancies} | {r for r in by_room if by_room[r]["maint"]}
                   | set(hc.get("full_window_occupants", {})) | set(hc.get("closed_rooms", {})))
    labels = hc.get("room_names", {})
    H = 70 + ROW_H * len(rooms) + 40
    s = [f'<!DOCTYPE html><html><head><meta charset="utf-8"><title>{hc["canonical_address"]} — room timelines</title>',
         '<style>body{font-family:-apple-system,Segoe UI,sans-serif;margin:20px;background:#fafafa}'
         'svg{background:#fff;border:1px solid #ddd;border-radius:8px}a{text-decoration:none}</style></head><body>',
         f'<h2>{hc["canonical_address"]} — per-room tenancy timeline</h2>',
         f'<p>Audit window {a_start} → {a_end} (padded edges shown). Bars = tenancies (dashed left edge '
         '= tenant already in place pre-window; arrow = still occupying at window end). Red spans = vacancy '
         'gaps. Dots = maintenance tickets (▲ = flagged). Click anything to open the Asana task.</p>',
         f'<svg width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg">']
    # month grid
    m = date_iter = a_start.replace(day=1)
    while date_iter <= x1:
        x = X(max(date_iter, x0))
        s.append(f'<line x1="{x:.0f}" y1="50" x2="{x:.0f}" y2="{H-30}" stroke="#eee"/>'
                 f'<text x="{x+3:.0f}" y="44" font-size="11" fill="#888">{date_iter.strftime("%b %y")}</text>')
        date_iter = (date_iter.replace(day=28) + timedelta(days=4)).replace(day=1)
    s.append(f'<line x1="{X(a_start):.0f}" y1="50" x2="{X(a_start):.0f}" y2="{H-30}" stroke="#bbb" stroke-dasharray="4"/>'
             f'<line x1="{X(a_end):.0f}" y1="50" x2="{X(a_end):.0f}" y2="{H-30}" stroke="#bbb" stroke-dasharray="4"/>')
    ci = 0
    for ri, rc in enumerate(rooms):
        y = 60 + ri * ROW_H
        lbl = labels.get(rc, "") or ("House-level" if rc == "HOUSE" else "")
        s.append(f'<text x="10" y="{y+BAR_H/2+16}" font-size="13" font-weight="600">{lbl or rc}</text>'
                 f'<text x="10" y="{y+BAR_H/2+31}" font-size="10" fill="#888">{"#"+rc if rc!="HOUSE" else ""}</text>'
                 f'<line x1="{LEFT}" y1="{y+ROW_H-8}" x2="{W-20}" y2="{y+ROW_H-8}" stroke="#f0f0f0"/>')
        if rc in hc.get("closed_rooms", {}):
            s.append(f'<g><title>{hc["closed_rooms"][rc]}</title>'
                     f'<rect x="{LEFT}" y="{y+14}" width="{W-LEFT-20}" height="{BAR_H}" rx="5" fill="#ddd"/>'
                     f'<text x="{LEFT+8}" y="{y+14+BAR_H/2+4}" font-size="12" fill="#777">CLOSED — beds merged into Room 6</text></g>')
            continue
        if rc in hc.get("full_window_occupants", {}):
            note = hc["full_window_occupants"][rc]
            nm = note.split(" ")[0]
            s.append(f'<g><title>{note}</title>'
                     f'<rect x="{X(a_start):.0f}" y="{y+14}" width="{X(a_end)-X(a_start):.0f}" height="{BAR_H}" rx="5" '
                     f'fill="#4e79a7" fill-opacity="0.85" stroke="#4e79a7" stroke-dasharray="5,3"/>'
                     f'<text x="{X(a_start)+8:.0f}" y="{y+14+BAR_H/2+4}" font-size="12" fill="#fff">{nm} — in place all window ➔</text></g>')
        rts = [t for t in tenancies if t["room_code"] == rc]
        for t in rts:
            bs, be = t["start"] or x0, t["end"] or x1
            bx, bw = X(bs), max(X(be) - X(bs), 6)
            col = PALETTE[ci % len(PALETTE)]; ci += 1
            tid = t["end_task"] or t["start_task"]
            dash = ' stroke-dasharray="5,3"' if t["start_kind"] == "pre_window" else ""
            title = (f'{t["tenant"] or "?"} | {t["start"] or "pre-window"} → {t["end"] or "ongoing"}'
                     + (" | HUMAN REVIEW" if t["hr"] else ""))
            s.append(f'<a href="{ASANA.format(tid)}" target="_blank"><g><title>{title}</title>'
                     f'<rect x="{bx:.0f}" y="{y+14}" width="{bw:.0f}" height="{BAR_H}" rx="5" fill="{col}" '
                     f'fill-opacity="0.85" stroke="{col}"{dash}/>')
            if t["end_kind"] == "ongoing":
                s.append(f'<text x="{bx+bw-14:.0f}" y="{y+14+BAR_H/2+5}" font-size="14" fill="#fff">➔</text>')
            name = (t["tenant"] or "?").split(" ")[0]
            if bw > 40:
                s.append(f'<text x="{bx+6:.0f}" y="{y+14+BAR_H/2+4}" font-size="12" fill="#fff">{name}'
                         f'{" ⚠" if t["hr"] else ""}</text>')
            s.append('</g></a>')
        for g in [g for g in gaps if g["room_code"] == rc and g["vacant_from"] and g["vacant_to"]
                  and isinstance(g["gap_days"], int) and g["gap_days"] > 0]:
            gx, gw = X(parse_date(g["vacant_from"])), X(parse_date(g["vacant_to"])) - X(parse_date(g["vacant_from"]))
            if gw > 1:
                s.append(f'<g><title>vacant {g["gap_days"]}d: {g["vacant_from"]} → {g["vacant_to"]}</title>'
                         f'<rect x="{gx:.0f}" y="{y+14}" width="{gw:.0f}" height="{BAR_H}" fill="#e15759" fill-opacity="0.18"/>'
                         + (f'<text x="{gx+gw/2-10:.0f}" y="{y+10}" font-size="10" fill="#c44">{g["gap_days"]}d</text>' if gw > 24 else "")
                         + '</g>')
        for mt in by_room.get(rc, {}).get("maint", []):
            mx = X(mt["_d"])
            mark = "▲" if mt["human_review"] == "yes" else "●"
            s.append(f'<a href="{ASANA.format(mt["task_id"])}" target="_blank">'
                     f'<text x="{mx-4:.0f}" y="{y+ROW_H-14}" font-size="10" fill="{"#c44" if mark=="▲" else "#59a14f"}">'
                     f'<title>{mt["event_date"]} {mt["task_name"][:90]}</title>{mark}</text></a>')
    s.append('</svg><p style="color:#888;font-size:12px">Generated ' + now_sydney_iso() +
             ' by pipeline/s5_tenancies_html.py from timeline.csv — see tenancies.csv / vacancy_gaps.csv for the numbers.</p></body></html>')
    (outdir / "timeline.html").write_text("\n".join(s), encoding="utf-8")
    append_runlog(f"{now_sydney_iso()} | {slug} | s5-tenancies-html | script:s5_tenancies_html.py | done | "
                  f"{len(tenancies)} tenancies, {len(gaps)} gaps, html rendered")
    print(f"{len(tenancies)} tenancies, {len(gaps)} vacancy gaps → tenancies.csv, vacancy_gaps.csv, timeline.html")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
