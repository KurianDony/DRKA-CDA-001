#!/usr/bin/env python3
"""Build the batch-00R interactive timelines dashboard (single self-contained HTML).
Live per-house timelines; click a tenant -> move-in/move-out task links + facts +
signed-vs-actual stay; human-flag detail with reasons+facts; flag buckets; vacancy gaps
with day counts; roster (Tenant Name col) current-occupant truth.
Usage: python3 pipeline/build_dashboard.py
"""
import csv, json, re, sys
from pathlib import Path
from datetime import date
ROOT = Path(__file__).resolve().parent.parent
HOUSES = {
 "287-cleveland-st-redfern": ("287 Cleveland St, Redfern", "287 Cleveland"),
 "1-148-liverpool-rd-enfield": ("1/148 Liverpool Rd, Enfield", "1/148 Liverpool"),
 "350-marsden-rd-carlingford": ("350 Marsden Rd, Carlingford", "350 Marsden"),
 "66-boundary-st-parramatta": ("66 Boundary St, Parramatta", "66 Boundary"),
 "71-therry-street-avalon-beach": ("71 Therry Street, Avalon Beach", "71 Therry"),
}
WIN_START, WIN_END = "2025-07-01", "2026-06-30"

def clean_name(n):
    n = re.sub(r'^\s*styling\s*-\s*', '', (n or '').strip(), flags=re.I)
    return re.sub(r'\s+', ' ', n).strip()
def toks(n): return set(t for t in clean_name(n).lower().split() if len(t) > 2)
def nmatch(a, b): return bool(toks(a) & toks(b))

def load_roster():
    rows = list(csv.reader(open(ROOT/"New Raw Data - trimmed.csv", encoding="utf-8-sig")))
    hdr = rows[0]
    ci = {h: i for i, h in enumerate(hdr)}
    # two 'Property Address' cols; use index 9 (Full) and Tenant Name index
    tni = [i for i, h in enumerate(hdr) if h.strip() == "Tenant Name"][0]
    out = {}  # key -> {code: tenant}
    for slug, (_, key) in HOUSES.items():
        d = {}
        for r in rows[1:]:
            if key.lower() in r[9].lower():
                d[r[5].upper()] = clean_name(r[tni])
        out[slug] = d
    return out

def room_labels(slug):
    houses = json.loads((ROOT/"pipeline/config/houses.json").read_text())
    e = houses.get(slug, {})
    return e.get("room_names", {}) or e.get("room_labels", {})

def task_facts(slug):
    """index Task ID -> facts dict from movein+moveout filtered top-level rows."""
    idx = {}
    for src in ("movein", "moveout"):
        p = ROOT/f"data/houses/{slug}/{src}_filtered.csv"
        if not p.exists(): continue
        for row in csv.DictReader(open(p, encoding="utf-8-sig")):
            tid = row.get("Task ID")
            if not tid: continue
            idx[tid] = {
                "url": row.get("task_url") or f"https://app.asana.com/0/0/{tid}/f",
                "name": (row.get("Name") or "").strip(),
                "agreed_term": (row.get("Agreed Lease Term") or "").strip(),
                "weekly_rent": (row.get("Weekly Rent") or "").strip(),
                "payment_made": (row.get("Payment Made") or "").strip(),
                "date_paid": (row.get("Date and Time Paid") or "").strip()[:10],
                "room_status": (row.get("Room Status") or "").strip(),
                "due": (row.get("Due Date") or "").strip()[:10],
                "src": src,
            }
    return idx

FLAG_RE = re.compile(r'^-\s*\[(\d+)\]\(([^)]+)\)\s*(.*?)\s*\*\*HUMAN REVIEW:\s*(.*?)\*\*', re.I)
def parse_flags(slug):
    flags = []
    for src in ("movein", "moveout"):
        p = ROOT/f"data/houses/{slug}/review_{src}.md"
        if not p.exists(): continue
        for line in p.read_text(encoding="utf-8").splitlines():
            m = FLAG_RE.match(line.strip())
            if not m: continue
            tid, url, body, reason = m.groups()
            parts = [x.strip() for x in body.split("|")]
            room = parts[0] if parts else ""
            tenant = parts[1] if len(parts) > 1 else ""
            note = parts[2] if len(parts) > 2 else ""
            flags.append({"task_id": tid, "url": url, "room": room, "tenant": tenant,
                          "note": note, "reason": reason, "source": src})
    return flags

def bucket_of(reason, note=""):
    t = (reason + " " + note).lower()
    if any(k in t for k in ["arrears", "break fee", "bond", "fee", "ocr", "undetermined", "unsubstantiated", "waiv"]):
        return "Fees / bond unresolved"
    if any(k in t for k in ["billed", "physical", "conflict", "fallback", "date decision", "move out date", "date "]):
        return "Move-out date decision"
    if any(k in t for k in ["transfer", "slot", "reassign", "prev-room", "prev room", "room code", "mis-room", "mis-roomed", "code"]):
        return "Room / transfer conflict"
    if any(k in t for k in ["retract", "settlement", "cancel"]):
        return "Retraction / settlement"
    if any(k in t for k in ["temp", "cross-house", "perm room", "another house", "foreign"]):
        return "Cross-house / temp room"
    return "Other"

def main():
    roster_all = load_roster()
    houses_data = {}
    for slug, (addr, key) in HOUSES.items():
        roster = roster_all[slug]
        labels = room_labels(slug)
        facts = task_facts(slug)
        # tenancies
        ten = list(csv.DictReader(open(ROOT/f"data/houses/{slug}/tenancies.csv", encoding="utf-8-sig")))
        # gaps
        gaps = list(csv.DictReader(open(ROOT/f"data/houses/{slug}/vacancy_gaps.csv", encoding="utf-8-sig")))
        # ongoing per code for roster status
        from collections import defaultdict
        ongoing = defaultdict(list)
        for t in ten:
            if t.get("end_kind") == "ongoing":
                ongoing[t["room_code"].upper()].append(t["tenant"])
        # build tenancy records
        recs = []
        for t in ten:
            code = t["room_code"].upper()
            rt = roster.get(code, "")
            og = ongoing.get(code, [])
            rstatus = ""
            if t.get("end_kind") == "ongoing":
                if rt and rt.upper() != "N/A" and nmatch(t["tenant"], rt):
                    rstatus = "current_confirmed"
                elif (not rt or rt.upper() == "N/A"):
                    rstatus = "roster_vacant_still_open"
                elif rt and not nmatch(t["tenant"], rt):
                    rstatus = "departed_missing_moveout"
                else:
                    rstatus = "ongoing"
            sd = t.get("stay_days") or ""
            at = t.get("agreed_term_months") or ""
            actual_months = round(int(sd)/30.44, 1) if sd.isdigit() else ""
            mi = facts.get(t.get("start_task"), {})
            mo = facts.get(t.get("end_task"), {})
            recs.append({
                "code": code, "room_label": labels.get(code, code) or code,
                "tenant": t["tenant"], "start": t.get("start", ""), "end": t.get("end", ""),
                "start_kind": t.get("start_kind", ""), "end_kind": t.get("end_kind", ""),
                "start_task": t.get("start_task", ""), "end_task": t.get("end_task", ""),
                "start_url": mi.get("url", f"https://app.asana.com/0/0/{t.get('start_task')}/f" if t.get("start_task") else ""),
                "end_url": mo.get("url", f"https://app.asana.com/0/0/{t.get('end_task')}/f" if t.get("end_task") else ""),
                "hr": t.get("hr", ""), "agreed_term_months": at, "stay_days": sd,
                "actual_months": actual_months, "months_past_term": t.get("months_past_term", ""),
                "roster_status": rstatus, "roster_current": rt,
                "mi_facts": mi, "mo_facts": mo,
            })
        # gaps
        grecs = []
        for g in gaps:
            grecs.append({"code": (g.get("room_code") or "").upper(),
                          "from": g.get("vacant_from", ""), "to": g.get("vacant_to", ""),
                          "days": g.get("gap_days", ""),
                          "prev": g.get("prev_tenant", ""), "next": g.get("next_tenant", ""),
                          "note": g.get("note", "")})
        # flags
        flags = parse_flags(slug)
        for f in flags:
            f["bucket"] = bucket_of(f["reason"], f["note"])
            fc = facts.get(f["task_id"], {})
            f["facts"] = fc
        # roster-derived missing-moveout synthetic flags
        for r in recs:
            if r["roster_status"] == "departed_missing_moveout":
                flags.append({"task_id": r["start_task"], "url": r["start_url"], "room": r["room_label"],
                              "tenant": r["tenant"], "note": f"roster current = {r['roster_current']}",
                              "reason": f"Roster shows {r['roster_current']} as current occupant; {r['tenant']} has departed but no move-out task is in the export (move-out date unknown).",
                              "source": "roster", "bucket": "Missing move-out (roster)", "facts": r["mi_facts"]})
            if r["roster_status"] == "roster_vacant_still_open":
                flags.append({"task_id": r["start_task"], "url": r["start_url"], "room": r["room_label"],
                              "tenant": r["tenant"], "note": "roster shows room vacant",
                              "reason": f"Roster shows room {r['room_label']} VACANT; {r['tenant']} still open in timeline — departed (missing move-out) or roster not yet updated.",
                              "source": "roster", "bucket": "Missing move-out (roster)", "facts": r["mi_facts"]})
        # roster summary per room
        rooms = []
        allcodes = sorted(set(list(labels) + [r["code"] for r in recs] + list(roster)),
                          key=lambda x: (len(x), x))
        for c in allcodes:
            rooms.append({"code": c, "label": labels.get(c, c) or c,
                          "roster_current": roster.get(c, "")})
        houses_data[slug] = {"address": addr, "rooms": rooms, "tenancies": recs,
                             "gaps": grecs, "flags": flags}
    data = {"window": [WIN_START, WIN_END], "generated": date.today().isoformat(), "houses": houses_data,
            "house_names": {s: v[0] for s, v in HOUSES.items()}}
    html = TEMPLATE.replace("__DATA__", json.dumps(data, ensure_ascii=False))
    out = ROOT/"data/final/batch-00R-timelines.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print("wrote", out)
    # quick stats
    for s, hd in houses_data.items():
        print(f"  {s}: {len(hd['tenancies'])} tenancies, {len(hd['gaps'])} gaps, {len(hd['flags'])} flags")

TEMPLATE = r"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>CVD Batch 00R — Live Timelines</title>
<style>
:root{--bg:#0f1115;--panel:#181b22;--panel2:#1f232c;--line:#2b3140;--txt:#e6e9ef;--mut:#9aa4b2;
--cur:#2ecc71;--paired:#4a90e2;--pre:#7f8c9a;--dep:#e67e22;--vac:#f1c40f;--flag:#e74c3c;--acc:#8e7cff;}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--txt);font:13px/1.45 -apple-system,Segoe UI,Roboto,sans-serif}
header{padding:12px 18px;border-bottom:1px solid var(--line);display:flex;gap:14px;align-items:center;flex-wrap:wrap;position:sticky;top:0;background:var(--bg);z-index:10}
h1{font-size:15px;margin:0;font-weight:650}
select,button{background:var(--panel2);color:var(--txt);border:1px solid var(--line);border-radius:7px;padding:6px 10px;font-size:13px;cursor:pointer}
.tabs{display:flex;gap:6px}.tab{padding:6px 12px;border-radius:7px;border:1px solid var(--line);background:var(--panel);cursor:pointer}
.tab.on{background:var(--acc);border-color:var(--acc);color:#fff}
.wrap{display:flex;gap:0;height:calc(100vh - 54px)}
.main{flex:1;overflow:auto;padding:14px 18px}
.side{width:400px;border-left:1px solid var(--line);background:var(--panel);overflow:auto;padding:16px;display:none}
.side.on{display:block}
.legend{display:flex;gap:14px;flex-wrap:wrap;margin:2px 0 14px;color:var(--mut);font-size:12px}
.legend span{display:inline-flex;gap:6px;align-items:center}
.sw{width:12px;height:12px;border-radius:3px;display:inline-block}
.room{margin-bottom:6px;border-bottom:1px dashed var(--line);padding-bottom:6px}
.rlabel{display:flex;justify-content:space-between;font-size:12px;color:var(--mut);margin-bottom:3px}
.rlabel b{color:var(--txt)}.rlabel .rc{color:var(--cur)}
.lane{position:relative;height:26px;background:linear-gradient(90deg,#141821,#141821);border-radius:5px}
.bar{position:absolute;top:3px;height:20px;border-radius:4px;font-size:11px;color:#0b0d12;display:flex;align-items:center;padding:0 6px;overflow:hidden;white-space:nowrap;cursor:pointer;border:1px solid rgba(0,0,0,.25)}
.bar:hover{outline:2px solid #fff}
.bar.current{background:var(--cur)}.bar.paired{background:var(--paired);color:#fff}
.bar.pre{background:var(--pre);color:#fff}.bar.departed{background:var(--dep);color:#111}
.bar.flagged::after{content:"⚑";position:absolute;right:3px;top:-1px;color:var(--flag);font-size:12px}
.gap{position:absolute;top:8px;height:10px;background:repeating-linear-gradient(45deg,#3a3320,#3a3320 4px,#2a2513 4px,#2a2513 8px);border:1px solid #5a4d1f;border-radius:3px}
.gap .gd{position:absolute;top:-15px;left:50%;transform:translateX(-50%);font-size:10px;color:var(--vac);white-space:nowrap}
.axis{position:relative;height:18px;margin-bottom:4px;color:var(--mut);font-size:10px}
.axis .tk{position:absolute;top:0;border-left:1px solid var(--line);padding-left:3px;height:100%}
.kv{display:grid;grid-template-columns:120px 1fr;gap:3px 10px;margin:8px 0}
.kv div:nth-child(odd){color:var(--mut)}
.chip{display:inline-block;padding:1px 8px;border-radius:20px;font-size:11px;font-weight:600}
.chip.current{background:rgba(46,204,113,.2);color:var(--cur)}.chip.departed{background:rgba(230,126,34,.2);color:var(--dep)}
.chip.paired{background:rgba(74,144,226,.2);color:var(--paired)}.chip.pre{background:rgba(127,140,154,.25);color:#c3ccd6}
.chip.vacant{background:rgba(241,196,15,.2);color:var(--vac)}
a{color:var(--acc)}a:hover{color:#b3a7ff}
.svbar{height:9px;border-radius:5px;background:#2a2f3a;position:relative;margin:2px 0 8px}
.svbar i{position:absolute;left:0;top:0;height:100%;border-radius:5px;background:var(--acc)}
.svbar.act i{background:var(--cur)}
.bkt{margin-bottom:10px;border:1px solid var(--line);border-radius:8px;overflow:hidden}
.bkt h3{margin:0;padding:9px 12px;background:var(--panel2);font-size:13px;display:flex;justify-content:space-between;cursor:pointer}
.bkt .body{padding:0 12px;display:none}.bkt.open .body{display:block;padding:8px 12px}
.flagcard{border-top:1px solid var(--line);padding:9px 0}
.flagcard:first-child{border-top:none}
.flagcard .rsn{color:var(--flag);font-weight:600;margin:3px 0}
.flagcard .fct{color:var(--mut);font-size:12px}
.muted{color:var(--mut)}.small{font-size:11px}
.pill{font-size:10px;padding:1px 6px;border-radius:10px;background:var(--panel2);border:1px solid var(--line);color:var(--mut);margin-left:6px}
#flagview{display:none;padding:14px 18px;overflow:auto}
.stat{display:inline-block;margin-right:18px}.stat b{font-size:18px}
</style></head><body>
<header>
  <h1>CVD Batch 00R — Live Timelines</h1>
  <select id="house"></select>
  <div class="tabs"><div class="tab on" data-v="timeline">Timelines</div><div class="tab" data-v="flags">Flag buckets</div></div>
  <span class="muted small" id="gen"></span>
</header>
<div class="wrap">
  <div class="main" id="tlview"></div>
  <div id="flagview"></div>
  <div class="side" id="side"></div>
</div>
<script>
const DATA = __DATA__;
const W0 = new Date(DATA.window[0]), W1 = new Date(DATA.window[1]);
const SPAN = (W1-W0);
document.getElementById('gen').textContent = 'generated '+DATA.generated+' · roster snapshot ground-truth';
const sel = document.getElementById('house');
Object.keys(DATA.houses).forEach(s=>{const o=document.createElement('option');o.value=s;o.textContent=DATA.house_names[s];sel.appendChild(o);});
let cur = Object.keys(DATA.houses)[0];
function clampX(d){ if(!d) return null; let t=new Date(d); let x=(t-W0)/SPAN*100; return Math.max(-2,Math.min(102,x)); }
function fmt(d){return d||'—';}
function statusClass(r){ if(r.end_kind==='ongoing'){ if(r.roster_status==='current_confirmed')return 'current'; if(r.roster_status==='departed_missing_moveout'||r.roster_status==='roster_vacant_still_open')return 'departed'; return 'current';} if(r.start_kind==='pre_window'||r.end_kind==='move_out'&&!r.start)return 'pre'; return 'paired'; }
function renderTimeline(){
  const h = DATA.houses[cur]; const m = document.getElementById('tlview'); let html='';
  html += `<div class="legend"><span><i class="sw" style="background:var(--cur)"></i>current (roster-confirmed)</span><span><i class="sw" style="background:var(--paired)"></i>past tenancy (paired)</span><span><i class="sw" style="background:var(--dep)"></i>ongoing but roster says departed → missing move-out</span><span><i class="sw" style="background:var(--pre)"></i>pre-window</span><span><i class="sw" style="background:var(--vac)"></i>vacancy gap (days)</span><span>⚑ human-review flag</span></div>`;
  // axis ticks (months)
  let ticks='';for(let y=2025,mo=7;;){let d=new Date(y,mo-1,1);if(d>W1)break;let x=clampX(d.toISOString().slice(0,10));ticks+=`<div class="tk" style="left:${x}%">${['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'][mo-1]} ${String(y).slice(2)}</div>`;mo++;if(mo>12){mo=1;y++;}}
  html+=`<div class="axis">${ticks}</div>`;
  // group tenancies + gaps by room code
  const byCode={};h.tenancies.forEach(t=>{(byCode[t.code]=byCode[t.code]||{ten:[],lab:t.room_label,rc:''}).ten.push(t);});
  h.rooms.forEach(r=>{byCode[r.code]=byCode[r.code]||{ten:[],lab:r.label,rc:r.roster_current};if(r.roster_current)byCode[r.code].rc=r.roster_current;});
  const gapByCode={};h.gaps.forEach(g=>{(gapByCode[g.code]=gapByCode[g.code]||[]).push(g);});
  const codes=Object.keys(byCode).sort((a,b)=>a.length-b.length||a.localeCompare(b));
  codes.forEach(code=>{
    const R=byCode[code]; if(!R.ten.length && !R.rc) return;
    html+=`<div class="room"><div class="rlabel"><span><b>${R.lab}</b> <span class="muted">#${code}</span></span><span>roster: <span class="rc">${R.rc||'(vacant)'}</span></span></div><div class="lane">`;
    (gapByCode[code]||[]).forEach(g=>{let x0=clampX(g.from),x1=clampX(g.to);if(x0==null||x1==null||x1<=x0)return;html+=`<div class="gap" style="left:${x0}%;width:${x1-x0}%"><span class="gd">${g.days}d</span></div>`;});
    R.ten.forEach((t,i)=>{
      let s=t.start?clampX(t.start):-2; let e=t.end?clampX(t.end):102;
      if(t.start_kind==='pre_window')s=-2; if(t.end_kind==='ongoing')e=102;
      let w=Math.max(2,e-s); let cls=statusClass(t); let fl=t.hr==='yes'?' flagged':'';
      html+=`<div class="bar ${cls}${fl}" style="left:${s}%;width:${w}%" onclick="showTen('${cur}',${i},'${code}')">${t.tenant.split(' ')[0]}</div>`;
    });
    html+=`</div></div>`;
  });
  m.innerHTML=html;
}
function showTen(slug,i,code){
  const h=DATA.houses[slug];const list=h.tenancies.filter(t=>t.code===code);const t=list[i];
  const side=document.getElementById('side');side.classList.add('on');
  const signed=parseFloat(t.agreed_term_months)||0, actual=parseFloat(t.actual_months)||0;
  const mx=Math.max(signed,actual,1);
  const flags=h.flags.filter(f=>f.task_id===t.start_task||f.task_id===t.end_task);
  let html=`<h3 style="margin:0 0 2px">${t.tenant}</h3><div class="muted small">${t.room_label} · #${t.code}</div>`;
  html+=`<div style="margin:8px 0"><span class="chip ${statusClass(t)}">${t.roster_status||t.end_kind}</span></div>`;
  html+=`<div class="kv">
    <div>Move-in</div><div>${t.start_task?`<a href="${t.start_url}" target="_blank">${fmt(t.start)} ↗</a>`:'(pre-window)'}</div>
    <div>Move-out</div><div>${t.end_task?`<a href="${t.end_url}" target="_blank">${fmt(t.end)} ↗</a>`:(t.end_kind==='ongoing'?'ongoing':'—')}</div>
    <div>Roster current</div><div>${t.roster_current||'(vacant)'}</div>
  </div>`;
  html+=`<div class="muted small" style="margin-top:10px">SIGNED vs ACTUAL</div>`;
  html+=`<div>Signed: <b>${t.agreed_term_months||'?'}</b> mo</div><div class="svbar"><i style="width:${signed/mx*100}%"></i></div>`;
  html+=`<div>Actual: <b>${t.actual_months!==''?t.actual_months:'?'}</b> mo ${t.stay_days?`(${t.stay_days}d)`:''} ${t.end_kind==='ongoing'?'<span class="muted">and counting</span>':''}</div><div class="svbar act"><i style="width:${actual/mx*100}%"></i></div>`;
  if(t.months_past_term&&t.months_past_term!=='0'&&t.months_past_term!=='')html+=`<div class="muted small">↳ ${t.months_past_term} months past signed term (month-to-month)</div>`;
  const f=t.mi_facts||{};
  html+=`<div class="muted small" style="margin-top:12px">MOVE-IN FACTS</div><div class="kv">
    <div>Agreed term</div><div>${f.agreed_term||'—'}</div>
    <div>Weekly rent</div><div>${f.weekly_rent||'—'}</div>
    <div>Payment</div><div>${f.payment_made||'—'} ${f.date_paid?('· '+f.date_paid):''}</div>
    <div>Room status</div><div>${f.room_status||'—'}</div></div>`;
  if(flags.length){html+=`<div class="muted small" style="margin-top:12px">⚑ HUMAN REVIEW</div>`;
    flags.forEach(fl=>{html+=`<div class="flagcard"><div class="pill">${fl.bucket}</div><div class="rsn">${fl.reason}</div><div class="fct">${fl.note||''}</div><div class="small" style="margin-top:4px"><a href="${fl.url}" target="_blank">open task ↗</a></div></div>`;});}
  side.innerHTML=html;
}
function renderFlags(){
  const h=DATA.houses[cur];const v=document.getElementById('flagview');
  const bk={};h.flags.forEach(f=>{(bk[f.bucket]=bk[f.bucket]||[]).push(f);});
  const order=Object.keys(bk).sort((a,b)=>bk[b].length-bk[a].length);
  let html=`<div style="margin-bottom:12px"><span class="stat"><b>${h.flags.length}</b><br><span class="muted small">flags</span></span><span class="stat"><b>${order.length}</b><br><span class="muted small">buckets</span></span><span class="muted small">${DATA.house_names[cur]}</span></div>`;
  order.forEach((b,bi)=>{
    html+=`<div class="bkt ${bi===0?'open':''}"><h3 onclick="this.parentNode.classList.toggle('open')"><span>${b}</span><span class="pill">${bk[b].length}</span></h3><div class="body">`;
    bk[b].forEach(f=>{html+=`<div class="flagcard"><b>${f.tenant}</b> <span class="muted small">${f.room}</span><div class="rsn">${f.reason}</div>${f.note?`<div class="fct">${f.note}</div>`:''}<div class="small" style="margin-top:3px"><a href="${f.url}" target="_blank">open task ↗</a> <span class="muted">· ${f.source}</span></div></div>`;});
    html+=`</div></div>`;
  });
  v.innerHTML=html;
}
let view='timeline';
function setView(x){view=x;document.querySelectorAll('.tab').forEach(t=>t.classList.toggle('on',t.dataset.v===x));
  document.getElementById('tlview').style.display=x==='timeline'?'block':'none';
  document.getElementById('flagview').style.display=x==='flags'?'block':'none';
  document.getElementById('side').classList.toggle('on',false);
  if(x==='timeline')renderTimeline();else renderFlags();}
document.querySelectorAll('.tab').forEach(t=>t.onclick=()=>setView(t.dataset.v));
sel.onchange=()=>{cur=sel.value;if(view==='timeline')renderTimeline();else renderFlags();document.getElementById('side').classList.remove('on');};
renderTimeline();
</script></body></html>"""

if __name__ == "__main__":
    main()
