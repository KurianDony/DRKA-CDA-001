"""Shared helpers for the CVD house pipeline."""
import csv, json, re, sys
from datetime import datetime, date
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
CONFIG_DIR = PROJECT_ROOT / "pipeline" / "config"

def load_settings():
    return json.loads((CONFIG_DIR / "settings.json").read_text())

def load_houses():
    return json.loads((CONFIG_DIR / "houses.json").read_text())

def house_config(slug):
    houses = load_houses()
    if slug not in houses:
        sys.exit(f"ERROR: unknown house slug '{slug}'. Known: {list(houses)}")
    return houses[slug]

def read_csv(path):
    with open(path, encoding="utf-8-sig", newline="") as f:
        r = csv.DictReader(f)
        return list(r), r.fieldnames

def write_csv(path, rows, fieldnames):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)

DATE_RE = re.compile(r"^(\d{4})-(\d{2})-(\d{2})")

def parse_date(s):
    """Parse a YYYY-MM-DD-prefixed string to date, else None."""
    if not s:
        return None
    m = DATE_RE.match(s.strip())
    if not m:
        return None
    try:
        return date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    except ValueError:
        return None

# 1–4 digits: single-digit codes are real (66 Boundary: #7/#8/#9 — pilot defect #1).
# Safe because callers intersect hits with the house's valid_codes.
ROOMCODE_TEXT_RE = re.compile(r"#\s?(\d{1,4}[A-Za-z]?)\b")

def room_codes_in_text(text):
    """Room codes referenced as '#1105' style in free text."""
    return set(m.upper() for m in ROOMCODE_TEXT_RE.findall(text or ""))

def resolve_room_code(row, valid_codes):
    """Best-effort room code for a row: Room Code column first, then #-refs in Name, then Notes."""
    col = (row.get("Room Code") or "").strip()
    hits = room_codes_in_text(col)
    if col in valid_codes:
        return col, "room_code_column"
    if hits & valid_codes:
        return sorted(hits & valid_codes)[0], "room_code_column_text"
    for field, label in (("Name", "name"), ("Notes", "notes")):
        hits = room_codes_in_text(row.get(field, "")) & valid_codes
        if label == "notes":
            # Notes are free text — short codes there are usually another property's room
            # NUMBER ("the room is #8 at that property"), not this house's code.
            hits = {h for h in hits if len(h) >= 3}
        if hits:
            if len(hits) > 1:
                return "|".join(sorted(hits)), f"{label}_multi"
            return next(iter(hits)), label
    return "", "unresolved"

MONTHS = {m.lower(): i + 1 for i, m in enumerate(
    ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])}
MONTHS.update({"sept": 9, "january": 1, "february": 2, "march": 3, "april": 4, "june": 6,
               "july": 7, "august": 8, "september": 9, "october": 10, "november": 11,
               "december": 12})
NAME_DATE_RE = re.compile(
    r"(?:(\d{1,2})\s+([A-Za-z]{3,9})|([A-Za-z]{3,9})\s+(\d{1,2}))(?:,?\s*(\d{4}))?\b")

def dates_in_text(text, ref):
    """Dates written in free text ('NT Dec 10', '16 Sept 2024', 'March 31, 2025').
    Year inferred (closest to ref date) when absent. Returns list of date objects."""
    out = []
    for m in NAME_DATE_RE.finditer(text or ""):
        day, mon = (m.group(1), m.group(2)) if m.group(1) else (m.group(4), m.group(3))
        mnum = MONTHS.get(mon.lower())
        if not mnum:
            continue
        try:
            day = int(day)
            if m.group(5):
                out.append(date(int(m.group(5)), mnum, day))
            elif ref:
                cands = [date(y, mnum, day) for y in (ref.year - 1, ref.year, ref.year + 1)]
                out.append(min(cands, key=lambda d: abs((d - ref).days)))
        except ValueError:
            continue
    return out

STREETY_RE = re.compile(
    r"\d|#|\b(rd|st|street|road|ave|avenue|hwy|highway|lane|ln|pde|parade|dr|drive|way|"
    r"cres|crescent|pl|place|room|transfer|icr|ocr|perm|temp|reloc|nt|cb|lr)\b", re.I)

def tenant_from_name(task_name, exclude_suburb=""):
    """Best-effort tenant extraction from a task Name like
    'PERM Room Transfer - Room 1, #1175, 350 Marsden Rd, Carlingford, Mahyar Nasabi'.
    Filters out room/address/keyword segments; prefers the last multi-word candidate.
    Used when the Tenant Name column is blank (transfer subtasks — pilot defect #2b)."""
    parts = [re.sub(r"[^\w\s'\-]", " ", p).strip() for p in (task_name or "").split(",")]
    cands = [p for p in parts
             if p and not STREETY_RE.search(p)
             and p.lower() != (exclude_suburb or "").lower()
             and re.match(r"^[A-Za-z]", p)]
    multi = [c for c in cands if len(c.split()) >= 2]
    return (multi or cands or [""])[-1]

def name_sim(a, b):
    """Fuzzy same-person check: any token pair sharing a >=4-char prefix, or first
    tokens sharing a >=3-char prefix (Danny/Daniel, Walker/Walked)."""
    ta = [t.lower() for t in (a or "").replace(",", " ").split() if len(t) > 2]
    tb = [t.lower() for t in (b or "").replace(",", " ").split() if len(t) > 2]
    if not ta or not tb:
        return False
    for x in ta:
        for y in tb:
            n = min(len(x), len(y), 4)
            if n >= 4 and x[:n] == y[:n]:
                return True
    return ta[0][:3] == tb[0][:3]

def now_sydney_iso():
    # Sandbox runs UTC; Sydney is +10 (AEST) / +11 (AEDT). Jul = +10.
    from datetime import timedelta, timezone
    return datetime.now(timezone(timedelta(hours=10))).strftime("%Y-%m-%dT%H:%M+10:00")

def append_runlog(line):
    p = PROJECT_ROOT / "RUNLOG.md"
    with open(p, "a", encoding="utf-8") as f:
        f.write(line.rstrip() + "\n")
