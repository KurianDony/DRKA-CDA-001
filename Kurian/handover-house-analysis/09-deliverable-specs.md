# 09 — Deliverable Specs (CDA-001 Portfolio Diagnostic)

**Project:** DRKA consulting for CDA Co-Living. Four deliverables: raw data layer, HTML dashboard, written report, area analysis — plus the Transformation Roadmap. Staged gates: **W3** CDA houses, **W5** CLS NSW, **W8** CLS VIC + area analysis + Roadmap (§6).
**Companion docs:** 01–04 (sources & method), 07 (methodology), 08 (pipeline & QA). Cite, don't duplicate.
**Privacy rule (all deliverables):** first names only; evidence cited as task GIDs / `[id:…]` contact IDs (01 header, 04 §4 step 7). No surnames, phones, emails.
**Nothing ships without a verifier PASS per house** (08 §5).

---

## 1. Data layer — the "raw data" deliverable

Location: `data/` at project root; per-house intermediates under `data/houses/<slug>/` (08 §3.4); final compiled CSVs under `data/final/`. UTF-8, ISO dates (YYYY-MM-DD), one header row.

**ID & joining rules:**
- `slug` = house key — `<number>-<street-name>-<street-type>-<suburb>`, lowercase, hyphenated (e.g. `350-marsden-rd-carlingford`), suburb ALWAYS included (canonical definition 08 §3.4); joins houses ↔ rooms ↔ everything.
- `room_code` = room key — the portfolio-unique `#NNNN` code (02 §3.1), stored without `#`. Never trust the Room Code custom field alone (02 §7.5); source is task-name regex.
- `tenancy_id` = `<first-name-slug>-<movein-or-moveout-task-gid>` — first name + task GID (privacy-safe, re-derivable).
- **Every row in every table carries `evidence_refs`:** semicolon-separated Asana task GIDs and/or respond.io `id:<contactId>` values that support the row. No ref = no row.
- Entity values: `CDA | CLS-NSW | CLS-VIC | unmapped` — assigned from **Kurian's kickoff house→entity mapping** (authoritative). The live Asana `Owner` field may SEED a draft mapping only (07 R10.1, A.6); area is never inferred from suburb.

### houses.csv
| Column | Type | Definition | Source |
|---|---|---|---|
| slug | text | House key | derived |
| address | text | Canonical Asana address, collisions resolved (01 §2) | Asana task names |
| entity | enum CDA\|CLS-NSW\|CLS-VIC\|unmapped | Owning entity — Kurian's kickoff list is authoritative; Asana `Owner` seeds a draft only (07 R10.1/A.6) | Kurian kickoff mapping |
| area | text | Area/suburb grouping per kickoff mapping (§4) | Kurian kickoff mapping |
| rooms_count | int | Rooms in service | roster (02 §4.1) sanity-checked vs `active_properties.csv` (02 §3.2) |
| in_service_start / in_service_end | date/null | Window the house was operating (null end = still active; EOL closures per 02 §4.8) | Asana EOL/close-down tasks |
| evidence_refs | text | — | — |

### rooms.csv
| Column | Type | Definition | Source |
|---|---|---|---|
| room_code | text | Portfolio-unique code, PK | task-name regex (02 §3.1) |
| slug | text | FK houses | roster |
| room_label | text | "Room 4" style label | task names |
| avail_start / avail_end | date/null | Availability window within the 12-month audit window (temp/holding rooms flagged, 02 §4.4) | roster + events |
| is_temp | bool | TEMP/holding room | 02 §4.4 |
| evidence_refs | text | — | — |

### tenancies.csv
| Column | Type | Definition | Source |
|---|---|---|---|
| tenancy_id | text | First name + task GID, PK | derived |
| tenant_first_name | text | First name only | Asana |
| room_code / slug | text | FK | resolution per 02 §4.3 (title + sequence logic beat form fields) |
| lease_start | date | Lease Start Date field (02 §3.1) | offboarding custom field |
| lease_end | date/null | Lease End Date | offboarding custom field |
| actual_move_in | date | Best-evidence move-in | priority list 02 §3.1 |
| actual_move_out | date/null | Best-evidence move-out (null = current) | priority list 02 §3.1 |
| event_class | enum | active \| natural_end \| early_break \| transfer \| cancelled_full_refund \| cancelled_partial_refund \| cancelled_nonrefundable \| unknown_exit — the tenancy's EXIT classification (entry evidence lives in the date columns). Eviction is a reason code (07 R3 `evicted_breach`), not an event class | 07 R1 mapping table |
| weekly_rent | float | ACTUAL weekly rent at move-in — never advertised rent (Advertising-Rent mirror carries a hidden +$20 markup; provenance caveat per 01 §5) | Moving In rent field (02 §3.1) |
| departure_reason | text | Why they left — coded per 07 R2/R3 | respond.io mining stage (08 §2.2; 02 §4.9) |
| reason_confidence | enum verified\|reported\|unknown | verified = ≥1 citation from a structured field OR first-party comment/message; reported = hearsay-only (staff paraphrase, second-hand); unknown = nothing after 07 R2 a–d | 07 R2.5 |
| evidence_refs | text | move-in GID; move-out GID; contact ids | — |

### vacancy_gaps.csv
| Column | Type | Definition | Source |
|---|---|---|---|
| room_code / slug | text | FK | — |
| gap_start | date | Prior tenant's move-out | tenancies |
| gap_end | date/null | Next move-in; null = ongoing | tenancies |
| days | int | Programmatically computed (02 §4.5) | script |
| status | enum confirmed\|ongoing\|no-data | Only `confirmed`+`ongoing` count toward totals; `no-data` rooms excluded and flagged (02 §4.5 — the 350 Marsden R4 rule) | script |
| evidence_refs | text | — | — |

### maintenance_issues.csv
| Column | Type | Definition | Source |
|---|---|---|---|
| task_gid | text | PK | Maintenance Requests project (03 §3.2) |
| slug / room | text | House FK; room label or null | task title (03 §3.2 naming) |
| type | text | Issue category (section or Type of Request) | 03 §3.2 |
| severity | text | Priority field value | 03 §3.2 |
| opened / resolved | date / date-null | created_at / genuine fix date confirmed in thread or subtask; `completed_at` only as fallback (07 R8.4–R8.5) | Asana + comment read |
| resolution_days | int/null | resolved − opened; NULL for denied tasks (07 R8.5) | script |
| resolution_source | enum thread\|subtask\|completed_at-fallback | Which evidence supplied `resolved` (07 R8.5) | comment read |
| status | enum open\|resolved\|closed-denied | `closed-denied` = auto-closed, never fixed (03 §7.4) | comment read (03 §4 step 4) |
| owner_gated_flag | bool | Attribution flag — long-open item gated on the owner, not CDA (03 §7.8); an attribution, not a status | comment read |
| is_routine | bool | Bins/lawns/umbrella tasks excluded from defect metrics (03 §4 step 2) | classification |
| recurrence_flag | bool | Same reporting group + same room (same house for common areas), new task created within 90 days of prior resolution — default, Kurian-overridable (07 R8.7) | script |
| systemic_flag | bool | 3+ recurrences in window (07 R8.7) | script |
| evidence_refs | text | — | — |

### tenant_signals.csv
| Column | Type | Definition | Source |
|---|---|---|---|
| contact_id | int | respond.io contact id | 04 §3.2 |
| slug / room_code | text | Attribution from Asana roster, not contact custom fields (04 §4 step 4) | roster |
| theme | enum | maintenance \| cleanliness \| housemate_conflict \| noise \| safety_security \| payments_bond_refund \| moveout_notice \| internet_utilities \| inspection_access \| other_verbatim (quoted) — coded per 07 R9.3 during the respond.io mining stage (08 stage order) | 07 R9.3 |
| first_msg / last_msg | date | From messageId-derived dates (04 §3.3) | messages |
| msg_count | int | Relevant messages (broadcasts deduped, 04 §8.4) | script |
| linked_ticket_gid | text/null | Asana task the signal corroborates | cross-ref |
| evidence_refs | text | `id:<contactId>` + GIDs | — |

### metrics_house.csv — one row per house
| Column | Type | Definition |
|---|---|---|
| slug / entity / area | text | FK |
| avg_stay_days | float | Mean completed-tenancy length; **denominator: completed_tenancies_n** |
| stay_median_days / stay_p25_days / stay_p75_days | float | Median / 25th / 75th percentile of completed-tenancy length (censored tenancies excluded, 07 R4.6) |
| stay_min_days / stay_max_days | int | Shortest / longest completed stay |
| room_days_observed | int | THE single denominator: available room-days per 07 R7 (available-days basis — out-of-service intervals and no-data rooms excluded) |
| vacancy_days_confirmed | int | Sum of confirmed+ongoing gap days (no-data excluded) |
| vacancy_rate | float | vacancy_days_confirmed / room_days_observed |
| turnover_n / turnover_rate | int / float | Move-outs in window / rooms_with_data |
| real_occupancy_pct | float | Occupied room-days / room_days_observed |
| maint_open_n / maint_resolved_n / maint_median_resolution_days | int/int/float | Non-routine only |
| signal_n / signal_contacts_n | int | Tenant-signal volume |
| response_rate | float | Incoming threads with a human reply ÷ incoming threads, broadcasts excluded (07 R9.4–R9.5) |
| median_reply_lag_hours | float | Median first-human-reply lag, messageId-derived (07 R9.4) |
| rooms_no_data_n | int | Rooms excluded from denominators |
| churn_mask_flag | bool | TRUE when real_occupancy_pct ≥ 90% AND turnover ≥ 3 tenancies/room-year — Kurian-overridable defaults (07 R7.5) |
| low_sample_flag | bool | TRUE when a short in-service window or small room count makes the house's rates unreliable (e.g. annualised from <9 months, 07 R6) — separate from churn masking |
| verifier_pass | bool | From VERIFY.md (08 §5) |
| evidence_refs | text | Pointer to per-house dir |

### occupancy_monthly.csv — one row per house per month
Produced at the metrics stage alongside metrics_house.csv; feeds the dashboard occupancy sparklines (§2).
| Column | Type | Definition |
|---|---|---|
| house_slug | text | FK houses |
| month | text | Calendar month `YYYY-MM`, clipped to the analysis window (07 R11.4) |
| occupied_room_days | int | Occupied room-days in the month (07 R7) |
| available_room_days | int | Available room-days in the month (07 R7 available-days basis — out-of-service intervals and no-data rooms excluded) |
| occupancy_pct | float | occupied_room_days / available_room_days |

### manifest.json — window & provenance record
Lives in `data/final/`; required window record per 07 R11.4. Keys: `window_start`, `window_end`, `generated_at`, `gate` (W3\|W5\|W8), `houses_included` (slug list), `verifier_pass_list`.

Definition-of-done for the data layer: §6.

---

## 2. HTML dashboard spec

**One self-contained file** (`CDA-001_dashboard.html`), works offline; no external deps except an optional CDN chart lib with graceful degradation (the room timelines need no lib — the prior artifacts render Gantt with pure CSS grid/absolute-positioned segments; reuse that approach). Style baseline: `350_marsden_vacancy_audit_artifact.html` / `27_swan_ave_vacancy_audit_artifact.html` — CSS-variable palette (green occupied / red vacant / hatched no-data), card layout, slide-out drawer, caveats panel, `https://app.asana.com/0/0/<gid>/f` links. DRKA-branded: DRKA name/logo header, "Prepared by DRKA for CDA Co-Living", palette adjusted to DRKA colors while keeping the occupied/vacant/no-data semantics.

**Data binding:** embed the §1 CSVs as a single `const DATA = {...}` JSON block in the file. **Every displayed number must be computed from (or equal to) that embedded data — no hand-typed figures.** The JSON carries `generated_at` and per-house `verifier_pass`; non-PASS houses render greyed with an "unverified — excluded" badge, never with numbers.

Views:
1. **Portfolio overview** — one card per house: address, entity/area chip, the 7 measures, sparkline occupancy (monthly series from `occupancy_monthly.csv`, §1). **Sortable by the 3 focus signals: turnover, maintenance, vacancy.** Churn-mask flag shows as a warning chip.
2. **Per-house drill** (click a card) — room timeline Gantt exactly in the prior-artifact style (click tenant → drawer with move-in/out events, Asana links, flag notes); maintenance timeline (opened→resolved bars, closed-denied highlighted); tenant-signal summary (theme counts, first/last dates, `[id:…]` refs); house caveats panel.
3. **Entity/area filter** — global toggle CDA / CLS-NSW / CLS-VIC and per-area; all views and portfolio averages recompute on filter.

First names only in all rendered text (tooltips included).

---

## 3. Written report spec

Single document (`CDA-001_report.md` → docx via pandoc; verify link/table counts post-conversion, 02 §4.7). Structure:

1. **Executive summary** — portfolio in ≤1 page; the 3 focus signals up front.
2. **Per-house one-pagers**, one per verified house:
   - Headline read (2–3 sentences: what this house is doing).
   - 7 measures vs portfolio average (small table, ▲▼ deltas, churn-mask noted).
   - Notable events with evidence (dated bullets, each with GID/`[id:…]` ref).
   - Focus verdict: act / watch / healthy — one line of justification.
3. **Portfolio patterns chapter** — cross-house recurrences: maintenance-driven churn (03 §4 step 6 precedent), notice-compliance patterns, entity contrasts.
4. **"Houses to focus on"** — ranked list by the 3 signals (turnover, maintenance, vacancy), each entry: rank, house, which signal(s) triggered, why (numbers), evidence refs.
5. **Methodology appendix** — one paragraph + pointer to doc 07; state denominators and the confirmed-vs-no-data vacancy rule (02 §4.5).
6. **UNVERIFIED / unknowns register** — every no-data room, unknown-confidence departure, open offboarding, and unanswered QUESTIONS-FOR-KURIAN item relevant to a reported number. Nothing ambiguous is silently resolved (02 §4.8).

---

## 4. Area analysis spec (W8)

- **Grouping rules:** areas come from Kurian's kickoff mapping only (no ad-hoc suburb clustering). A house with no mapped area → `KURIAN BLOCKER` if it gates the deliverable (canonical template 06 §4: `KURIAN BLOCKER: <one-line description>. Needed to unblock: <specific ask>.` — orchestrator-only; sub-agents report `BLOCKED:` upward per 08 §8), else unmapped bucket + question queue (08 §7–8).
- **Per-area metric tables:** the 7 measures aggregated per area (weighted by room_days_observed, not simple house means), houses_n and rooms_n stated per row.
- **Outlier houses per area:** the single portfolio-wide rule (07 R10.3): beyond **mean ± 2σ** of the comparison group — listed with numbers and evidence refs, stating the group, its n, mean, σ next to every outlier call.
- **Min-sample flags:** areas with **<3 houses or <10 room-years** of available room-days (07 R10.2) get `LOW-SAMPLE` on every derived figure; no rankings drawn from flagged areas.
- Output: chapter in the report + `metrics_area.csv` + area view in the dashboard filter.

---

## 5. Transformation Roadmap spec (W8) — structure only; content from the analysis

Per theme (expect 3–6 themes):
1. **Finding** — pattern + houses affected + evidence refs (from §3 chapters).
2. **Cost framing** — vacancy days × weekly rent, repeat-maintenance spend, churn cost; every figure traceable to §1 CSVs; assumptions stated (rent figures per 01 §5 conventions — know which sheet a rent number came from).
3. **Recommended actions** — imperative, sequenced, owner suggested (CDA vs entity-level).
4. **Specific houses to act on** — named list with the triggering numbers.

Close with a 90-day sequence table (action / houses / expected effect / measure to watch) and an explicit "what we did NOT have data for" section.

---

## 6. Acceptance criteria & delivery gates

### Definition-of-done per deliverable

**Data layer:**
- [ ] All §1 CSVs present, schema-exact, ISO dates, no orphan FKs
- [ ] Verifier PASS recorded (RUNLOG) for every included house; non-PASS houses absent
- [ ] Reconciliation counts recorded per house (08 §4.4, §4.6) with zero unexplained deltas
- [ ] Integrity scripts green: room-code uniqueness, GID exclusivity, date-order (08 §4)
- [ ] Every row has evidence_refs; privacy scrub done (no surnames/phones/emails — grep-verified)
- [ ] no-data rooms and churn-mask flags populated, not blank

**Dashboard:**
- [ ] Single file, opens offline, renders with CDN unavailable
- [ ] Embedded JSON matches final CSVs (automated diff of totals)
- [ ] Spot-check: 10 random displayed numbers traced to CSV rows
- [ ] Only verifier-PASS houses show numbers; caveats panels populated; DRKA branding; privacy scrub

**Report:**
- [ ] One-pager per verified house; every number matches metrics_house.csv
- [ ] Every notable-event claim carries a GID/`[id:…]` ref
- [ ] Focus list reproducible from the CSVs (ranking script output attached)
- [ ] UNVERIFIED register complete; docx link/table counts verified; privacy scrub

**Area analysis:** grouping = kickoff mapping verbatim; LOW-SAMPLE flags applied; weighted aggregation stated.
**Roadmap:** every cost figure traceable; every named house verifier-PASS; assumptions listed.
**All deliverables:** Kurian sign-off recorded in RUNLOG.md before a gate is called complete.

### Gate contents
| Gate | Scope | Ships |
|---|---|---|
| **W3** | All CDA-entity houses | Data layer (CDA houses) + dashboard v1 (CDA only) + per-house one-pagers (CDA) + QUESTIONS-FOR-KURIAN review |
| **W5** | + CLS NSW houses | Data layer extended + dashboard v2 (entity filter live) + report draft incl. portfolio patterns across CDA+NSW |
| **W8** | + CLS VIC houses | Full data layer + final dashboard + final report + area analysis (§4) + Transformation Roadmap (§5) |

Each gate: run the full DoD checklist for everything shipped at that gate (including re-verification of previously shipped houses if their data changed — reports go stale fast, 03 §7.9).
