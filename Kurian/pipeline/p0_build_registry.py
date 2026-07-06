#!/usr/bin/env python3
"""P0 — Build the house registry from the roster CSV ('New Raw Data - trimmed.csv').

What it does: one registry entry per house (slug, house-number-anchored match pattern,
same-street exclusion list, room codes + labels, company/portfolio/state, active flag),
plus a collision matrix and a build report. The registry is the single source of truth
for every downstream stage.

Inputs:  'New Raw Data - trimmed.csv' (roster: 1 row per room)
Outputs: pipeline/config/registry.json           (all houses)
         pipeline/config/collision_matrix.md     (same-street houses, mutual exclusions)
         pipeline/config/registry_report.md      (counts, anomalies, questions)
NOTE: does NOT overwrite houses.json (hand-curated pilot entries live there); merge at
      dispatch time — registry.json is generated, houses.json entries win if both exist.

Usage: python3 pipeline/p0_build_registry.py
"""
import csv, json, re, sys
from collections import defaultdict
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent / "lib"))
from common import PROJECT_ROOT, now_sydney_iso, append_runlog

SRC = PROJECT_ROOT / "New Raw Data - trimmed.csv"
CFG = PROJECT_ROOT / "pipeline" / "config"

def slugify(addr, suburb):
    s = f"{addr} {suburb}".lower()
    s = s.replace("/", " ").replace(",", " ")
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return re.sub(r"-+", "-", s)

def street_key(addr):
    """'1/148 Liverpool Rd' -> ('148', 'liverpool rd'); '342 Cleveland St' -> ('342','cleveland st')"""
    a = addr.split(",")[0].strip().lower()
    m = re.match(r"^(?:lvl\s*\d+\s*/\s*)?(?:(\d+[a-z]?)\s*/\s*)?(\d+[a-z]?)\s+(.+)$", a)
    if not m:
        return None, a
    return m.group(2), m.group(3).strip()

def main():
    rows = list(csv.reader(open(SRC, encoding="utf-8-sig")))[1:]
    houses = {}
    for r in rows:
        if len(r) < 12 or not r[1].strip():
            continue
        addr, extras, rtype, rnum, code, suburb, state, aid, comp, port = (
            r[1].strip(), r[2].strip(), r[3].strip(), r[4].strip(), r[5].strip(),
            r[6].strip(), r[7].strip(), r[8].strip(), r[10].strip(), r[11].strip())
        key = (addr, suburb)
        h = houses.setdefault(key, {
            "canonical_address": f"{addr}", "suburb": suburb, "state": state,
            "asana_address_id": aid, "companies": [], "portfolio": port,
            "rooms": {}, "closed_rooms": {}, "missing_code_rooms": [], "types": set()})
        h["types"].add(rtype or "Room")
        room_closed = comp.lower() in ("closed", "old", "")  # 'Closed' marks the ROOM, not the house
        if not room_closed:
            h["companies"].append(comp)
        label = f"Room {rnum}" if rnum else (rtype or "Room ?")
        if code:
            h["rooms"][code.upper()] = label + (f" ({rtype})" if rtype not in ("Room", "") else "")
            if room_closed:
                h["closed_rooms"][code.upper()] = f"{label} — company field: {comp or 'blank'}"
        else:
            h["missing_code_rooms"].append(label)

    # collision matrix by street name
    by_street = defaultdict(list)
    for (addr, suburb), h in houses.items():
        num, street = street_key(addr)
        h["_num"], h["_street"] = num, street
        by_street[street].append((addr, suburb))
    registry, dupes = {}, defaultdict(set)
    for (addr, suburb), h in houses.items():
        street_part = addr.split(",")[0].strip()
        slug = slugify(street_part, suburb if suburb.lower() not in addr.lower() else "")
        if suburb.lower() not in slug:
            slug = slugify(street_part, suburb)
        siblings = [f"{a}, {s}" for a, s in by_street[h["_street"]] if (a, s) != (addr, suburb)]
        pattern = f"{h['_num']} {h['_street'].split()[0]}" if h["_num"] else addr.lower()
        from collections import Counter as _C
        comp = _C(h["companies"]).most_common(1)[0][0] if h["companies"] else "ALL-ROOMS-CLOSED"
        registry[slug] = {
            "canonical_address": (addr if suburb.lower() in addr.lower() else f"{addr}, {suburb}"),
            "match_patterns": [pattern],
            "exclusions_note": ("Same street: " + "; ".join(sorted(siblings))) if siblings else "",
            "room_codes": sorted(h["rooms"]),
            "room_names": dict(sorted(h["rooms"].items())),
            "closed_rooms": dict(sorted(h["closed_rooms"].items())),
            "missing_code_rooms": h["missing_code_rooms"],
            "company": comp, "portfolio": h["portfolio"], "state": h["state"],
            "asana_address_id": h["asana_address_id"],
            "active": bool(h["companies"]),
            "unit_types": sorted(h["types"] - {"Room", ""}),
        }
        for c in h["rooms"]:
            dupes[c].add(slug)

    # same-number-same-street ambiguity check (pattern not unique)
    pat_owner = defaultdict(list)
    for slug, e in registry.items():
        pat_owner[e["match_patterns"][0]].append(slug)
    ambiguous = {p: s for p, s in pat_owner.items() if len(s) > 1}
    for p, slugs in ambiguous.items():  # tighten: use full street word + suburb-qualified pattern
        for slug in slugs:
            e = registry[slug]
            e["match_patterns"] = [e["canonical_address"].split(",")[0].lower()]
            e["exclusions_note"] += " | PATTERN TIGHTENED: shares number+street-first-word with " + \
                ", ".join(s for s in slugs if s != slug)

    code_dupes = {c: sorted(s) for c, s in dupes.items() if len(s) > 1}
    CFG.mkdir(parents=True, exist_ok=True)
    (CFG / "registry.json").write_text(json.dumps(registry, indent=1, ensure_ascii=False), encoding="utf-8")

    lines = ["# Collision matrix (same street name)", ""]
    for street, hs in sorted(by_street.items()):
        if len(hs) > 1:
            lines.append(f"- **{street}**: " + "; ".join(sorted(f"{a}, {s}" for a, s in hs)))
    (CFG / "collision_matrix.md").write_text("\n".join(lines), encoding="utf-8")

    n_active = sum(1 for e in registry.values() if e["active"])
    n_closed_rooms = sum(len(e["closed_rooms"]) for e in registry.values())
    rep = [f"# P0 registry report — {now_sydney_iso()}", "",
           f"- houses: {len(registry)} ({n_active} with active rooms, {len(registry)-n_active} fully closed)",
           f"- closed/old rooms inside houses: {n_closed_rooms}",
           f"- rooms with codes: {sum(len(e['room_codes']) for e in registry.values())}",
           f"- rooms MISSING codes: {sum(len(e['missing_code_rooms']) for e in registry.values())} "
           f"across {sum(1 for e in registry.values() if e['missing_code_rooms'])} houses",
           f"- letter-suffix (bed) codes: {sum(1 for e in registry.values() for c in e['room_codes'] if re.search('[A-Z]$', c))}",
           f"- streets with >1 house: {sum(1 for hs in by_street.values() if len(hs)>1)} (see collision_matrix.md)",
           f"- patterns tightened for number+street ambiguity: {len(ambiguous)} {list(ambiguous) or ''}",
           f"- ROOM-CODE DUPES ACROSS HOUSES (breaks uniqueness assumption!): {code_dupes or 'none'}",
           "", "Questions raised → QUESTIONS-FOR-KURIAN.md (code dupes, missing codes)."]
    (CFG / "registry_report.md").write_text("\n".join(rep), encoding="utf-8")
    append_runlog(f"{now_sydney_iso()} | - | p0-registry | script:p0_build_registry.py | done | "
                  f"{len(registry)} houses, {len(code_dupes)} code dupes, {len(ambiguous)} tightened patterns")
    print("\n".join(rep))

if __name__ == "__main__":
    main()
