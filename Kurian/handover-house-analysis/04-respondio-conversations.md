# 04 — Respond.io Conversation Analysis (Handover)

_Last verified: 2026-07-04, against the live respond-io MCP + past session transcripts + project outputs._
_Audience: a fresh Claude Cowork session with zero prior context. Everything below is evidence-cited; anything not directly confirmed is marked **UNVERIFIED**._
_**PRIVACY:** Contains real tenant names/IDs tied to sensitive events — internal use only; in NEW outputs prefer first names or `[id:…]` citations._

---

## 1. Purpose & trigger phrases

Respond.io is CDA CoLiving's tenant/lead messaging hub (primarily WhatsApp Business). Claude uses the **respond-io MCP connector (read-heavy)** to pull per-contact conversation history and mine it for operational signal:

- complaints (housemates, cleanliness, mould, maintenance)
- move-out notices given informally over WhatsApp
- move-out reasons / disputes / legal threats
- timelines ("when did the tenant first report X")
- corroboration or refutation of claims that only exist as Asana comments

It is almost never used alone — it is the **conversation-evidence layer** that gets layered on top of an Asana-derived roster/timeline (see docs 01–03 in this handover set).

**Trigger phrases seen in real sessions:**
- "give me a full house audit of 66 boundry Parramatta" (session `local_2ae5d6b6`, 30 Jun 2026)
- "search for everyone who lives in 19 burnett st… search all the chats for the past 3 months and asana for any relevant tasks… I'm looking for complaints about certain tenants, and cleaning issues… gather all the evidence and present in chronological order" (session `local_15830054`)
- "check everything that's happening in 444b stoney creek… if you don't have all the contacts, use the application moving in project" (same session)
- "What's the update on weed/backyard situation on my house in 7a Harvey st" (tenant message relayed; same session)
- House Stories: "Sources: Asana … + respond.io" (`CDA House Stories - Combined (4 Houses).md`, generated 2026-06-23)

---

## 2. History & evolution (dated)

| When | Session / file | What happened |
|---|---|---|
| **UNVERIFIED date** (before the audit session) | Session `local_21faee18` "Respond.io Claude MCP integration" | Kurian set the connector up. Verified facts from that transcript: respond.io publishes an official MCP server (`@respond-io/mcp-server`, run via `npx`); auth is a workspace-level **Developer API Access Token** (respond.io → Settings → Integrations → Developer API → Add Access Token); API base `https://api.respond.io/v2`; **Developer API requires the Growth plan or above**; the server exposes ~28 tools incl. write tools (send message, tags, merge, assign). Config used `RESPONDIO_API_KEY` + `MCP_SERVER_MODE=stdio`. |
| Same session | — | Kurian was given a "full workspace audit" prompt (read-only, phased: capability inventory → workspace discovery → business inference → use cases → limitations). That prompt is the origin of the read-only discipline used ever since. |
| **UNVERIFIED date, ~mid-Jun 2026** | Session `local_15830054` "Respond.io workspace audit" | The audit session evolved live into the first real investigations: (a) replying to a tenant about 7A Harvey St backyard (only known **send_message** use — with explicit user approval of exact wording first); (b) **19 Burnett St, Merrylands** whole-house complaint investigation (roster from Asana → per-tenant chat pulls → chronological evidence report → facts-vs-hearsay verdict); (c) **444B Stoney Creek Rd, Kingsgrove** eviction deep-dive (John Makai harassment case, corroborated across two tenants' chats + Asana Ops task). |
| 2026-06-22 | `Offboarding_Investigation_10rooms_2026-06-22.md`, `_22upcoming_` | Offboarding investigations are Asana/Gmail-led, but respond.io appears repeatedly as the **"how CDA knew"** channel (e.g. R4 #101 Bronte: "Tenant advised via respond [respond.io] that she already left last June 12"; 48-hr eviction notices "sent by TC" via respond.io). |
| 2026-06-23 | `CDA House Stories - Combined (4 Houses).md` + 4 individual `House Story - *.md` | The mature format: every house story has a dedicated **"Tenant comms (respond.io)"** section citing contacts by respond.io ID, e.g. "Nicole Di Gregorio (mould → forced relocation to Newtown) [id:407665783]", "Katherine Concha (legal action threat over bond…) [id:433042116]". respond.io IDs are even used as the *source link* for events that have no Asana task (e.g. a move-in known only from a respond.io broadcast). |
| 2026-06-30 | Session `local_2ae5d6b6` "66 Boundary Parramatta house audit" | Current standard pattern: Asana `search_objects`/`get_task` for the house → `list_contacts` (name search) for active tenants → `list_messages` per tenant → audit report with a "💬 respond.io (recent)" section (caught a live move-out request initiated that morning over WhatsApp, and a failed template delivery). |

Evolution in one line: **setup → read-only audit → ad-hoc house investigations → a repeatable "Asana roster + respond.io chats" evidence method baked into House Stories / house audits.**

---

## 3. The respond-io MCP surface (tools actually used)

Connector name: `respond-io` (tools `mcp__respond-io__*`). Tools are **deferred** in Cowork — load schemas first, e.g.:
`ToolSearch("select:mcp__respond-io__list_contacts,mcp__respond-io__list_messages,mcp__respond-io__get_contact,mcp__respond-io__list_contact_channels,mcp__respond-io__list_channels,mcp__respond-io__list_custom_fields")`

### 3.1 `list_contacts` — the search entry point
- Params: `search` (string), `limit` (1–100, default 10), `cursorId`, `timezone` (default UTC).
- **Search matches name / phone / email only. It does NOT index custom fields** — you cannot search by house address (verified in `local_15830054`: "The respond.io name-search doesn't index the address (it's in a custom field)"). Address lives in custom fields (`general_address`, `Room_Details`), so roster must come from Asana first.
- Returns full contact objects (same shape as `get_contact`, below).
- Live example (2026-07-04): `search:"Nicole Di Gregorio"` → 1 hit, id 407665783.

### 3.2 `get_contact`
- Param: `identifier` — formatted `id:123`, `email:user@example.com`, or `phone:+61…`.
- Response shape (live, anonymised):
```json
{
  "id": 407665783,
  "firstName": "Nicole", "lastName": "DI Gregorio (CDA)",
  "phone": "+3933•••••383", "email": "…@gmail.com",
  "countryCode": "IT",
  "status": "closed",            // conversation status: open/closed
  "isBlocked": false,
  "custom_fields": [
    {"name": "Room_Details",  "value": "Room 3, #1188, 1/253 King St, Newtown"},
    {"name": "general_address","value": "398 Cleveland Street, Surry Hills"},
    {"name": "room_number",   "value": "Room 3, #1188"},
    ...  // name_cda, asana_task_id, asana_comment, bday, contract_end_date, number_not_in_whats_app, comments — often null
  ],
  "tags": [], "assignee": null, "lifecycle": null,
  "created_at": 1773196897       // unix seconds
}
```
- Note the **(CDA) suffix** convention on some lastNames, and that `Room_Details` vs `general_address` can disagree (stale after relocations — Nicole's two fields point at two different houses). Treat custom fields as hints, not truth.
- `lifecycle` and `tags` were null/empty on the contacts sampled; no lifecycle stages or tag taxonomy confirmed in use — **UNVERIFIED** whether any contacts have them populated.

### 3.3 `list_messages` — the core mining tool
- Params: `identifier` (contact id / email / phone — `id:407665783` works), `limit` (1–100, default 20), `cursorId`.
- **Order: newest → oldest.** Pagination is cursor-based: response `pagination.next` URL carries `cursorId=<oldest messageId in page>`; pass that `cursorId` to get the next-older page. `previous` uses a negative cursorId.
- Message object (live example):
```json
{
  "messageId": 1781578749304782,          // microsecond-epoch-like; sortable = chronological
  "channelMessageId": "wamid.HBg…",       // WhatsApp wamid
  "contactId": 407665783,
  "channelId": 348751,                    // which channel the msg went through
  "traffic": "incoming" | "outgoing",
  "message": {"type": "text", "text": "…"},   // also attachment/template types
  "sender": {"source": "contact" | "user", "userId": 485494, "teamId": 24326,
             "workflowId": null, "broadcastHistoryId": null},
  "replyTo": { "id": …, "message": {…} },  // quoted-reply context when present
  "status": [{"value":"pending|sent|delivered|read","timestamp": …}]  // outgoing only
}
```
- Timestamps: derive the message date with the explicit rule **`date = messageId // 1_000_000`, interpreted as unix seconds** (e.g. `1781578749304782` → `1781578749`); confirm once against a `status[].timestamp` on first use. `status[].timestamp` is unix-ms. There is **no separate createdAt field** on the message — derive dates from messageId.
- `sender.source:"contact"` = tenant wrote it; `"user"` + `userId` = a CDA agent; `workflowId`/`broadcastHistoryId` non-null = automation/broadcast (house-wide blasts show up in every tenant's thread — dedupe when building house timelines).
- How far back: full history appears available via cursor pagination (Burnett/Stoney Creek pulls reached Jan–Apr from a June session). No hard cap observed. **UNVERIFIED** whether any retention limit exists.
- **Large histories flood context.** In `local_15830054` the outputs were saved to files and mined with `Grep` rather than read inline — do the same for anything beyond ~2 pages.

### 3.4 `list_channels`
Live result (2026-07-04) — 6 channels, no pagination needed:
| id | name | source |
|---|---|---|
| 390890 | CDA House Updates | whatsapp_business |
| 373819 | Andres - Your CDA Coliving Assistant | whatsapp_business |
| 373392 | Sofia - CDA | whatsapp_business |
| 357318 | Telegram | telegram |
| 348751 | **CDA Co Living** | whatsapp_business |
| 348479 | Website Chat | webchat |

**348751 "CDA Co Living" is the main tenant line** — every investigation message sampled came through it. "CDA House Updates" (created ~Jun 2026) is presumably for house broadcasts (**UNVERIFIED**); Andres/Sofia are bot/assistant lines (**UNVERIFIED** usage).

Note trailing spaces in channel names: `"CDA Co Living "` (id 348751) and `"Andres - Your CDA Coliving Assistant "` both carry a trailing space in the actual name — exact-match lookups must include it.

### 3.5 `list_contact_channels`
- Param: `identifier`. Returns which channels the contact is reachable on + `lastMessageTime` / `lastIncomingMessageTime` (unix-ms) — a fast way to check recency without pulling messages. Sample contact had exactly one channel (CDA Co Living WhatsApp).

### 3.6 `list_custom_fields`
Live result — 10 fields defined: `comments`, `number_not_in_whats_app`, `room_number`, `general_address`, `contract_end_date`, `bday`, `asana_comment`, `asana_task_id`, `name_cda`, `Room_Details` ("Room code or Room number + House address"). These are the house/room attribution fields — but see gotchas.

Note: the field names cited here (`Room_Details`, `general_address`, `room_number`, …) are **API slugs**; the display names differ ("Room Details (Tenant)", "General Address", "Room Number"). Contact payloads use the slugs.

### 3.7 Other tools
- `list_users`, `list_templates(channelId)`, `get_message(identifier, messageId)` — available, occasionally useful (`userId` → agent name via `list_users`). Not load-bearing in past investigations.
- `list_closing_notes` — returns **empty** in this workspace (verified live); closing-note categories are not used.
- **Write tools exist** (`send_message`, `add_contact_tags`, `update_contact`, `merge_contacts`, `assign_conversation`, `update_conversation_status`, `create_comment`, …). House-analysis workflow treats the connector as **READ-ONLY**. The single observed send (`local_15830054`, 7A Harvey backyard reply) followed the rule: *draft exact wording → explicit user go-ahead → send*. Note from that send: a `channelId` param type quirk errored; dropping `channelId` made it default to the contact's last-used channel, which was correct.

---

## 4. Methodology — step by step

The proven pipeline (from `local_15830054` Burnett/Stoney Creek, `local_2ae5d6b6` 66 Boundary, and the House Stories output):

**Step 1 — Build the roster in Asana, not respond.io.**
You cannot search respond.io by address. Get tenant names per room from Asana ("2025_Applications/Moving In" project + "Off boarding team" + Retention). Room codes (#1918 etc.) and full legal names come from there.

**Step 2 — Resolve each tenant to a respond.io contact.**
`list_contacts(search: "<first + last name>")`, one call per tenant (these were fired in parallel batches of ~4–6). Fallbacks: search by phone or email pulled from the Asana move-in task; `get_contact("phone:+61…")` also works. Record the numeric contact `id` — it becomes the citation key (`[id:407665783]`).

**Step 3 — Pull message history.**
`list_messages(identifier: "id:<id>", limit: 100)`, then follow `pagination.next` `cursorId` until you're past the investigation window (messages come newest-first; stop when `messageId`-derived dates precede the window). For 3-month investigations 1–3 pages per tenant usually sufficed. Save long threads to files and `Grep` for keywords (complain, clean, mould, mold, move out, notice, warning, smell, broken, refund, John, etc.).

**Step 4 — Attribute to house/room.**
Primary attribution is the roster from Step 1 (name → room). The contact's `Room_Details` / `general_address` custom fields corroborate but can be stale after transfers/relocations. House-wide **broadcasts** appear in every housemate's thread — use them once, as "CDA → house" events.

**Step 5 — Mine for signal and build a chronology.**
Classify each relevant message: complaint / notice / maintenance report / CDA warning / broadcast. Interleave with Asana task events into one dated timeline. Date each item from `messageId` (or, for approximate phrasing, "~14 Apr" style as in the Burnett report).

**Step 6 — Separate facts from hearsay.**
The signature analytical move (user explicitly asked "whats the actual result/facts we know.. whats hearsay.. whats the likely story and should we take action"). Output three buckets: documented facts (with source), uncorroborated claims, inferred story + proportionate recommended actions. A tenant's own messages either corroborate an Asana allegation or don't — say which.

**Step 7 — Cite respond.io evidence as `[id:<contactId>]`** in the report (House Stories convention), so any future session can re-pull the thread with one `list_messages` call.

**Multiple channels:** in practice every sampled tenant had a single channel (CDA Co Living WhatsApp). If a contact has several, `list_messages` returns all traffic with `channelId` per message — filter/annotate by channel; `list_contact_channels` tells you what exists.

---

## 5. How it plugs into the other workflows

- **House Stories** (doc in this set; output 2026-06-23): each house gets a "Tenant comms (respond.io)" section — 2–4 headline contacts with one-line characterisations + `[id:…]` citations; respond.io also fills gaps where no Asana task exists (move-ins known only from a welcome broadcast are cited as "respond.io broadcast" / "respond.io id:…").
- **Offboarding investigations** (`Offboarding_Investigation_*_2026-06-22.md`): Asana-led, but respond.io supplies the "how did CDA know" evidence — tenants announcing "already left" via respond.io, 48-hr eviction notices sent through it, "Tenant form + respond.io" as the notice channel in the 22-upcoming table.
- **Early lease breaks** (`early_lease_breaks.csv` / `CDA_early_lease_breaks_Mar-Jun_2026.xlsx`): built from Asana move-in/move-out tasks (columns are task URLs); respond.io is the follow-up tool when a specific break needs a why-did-they-really-leave dig. For that dig, follow the single-tenant "why did X leave / break lease early" recipe in 02-house-updates-occupancy-vacancy.md §4.9 (Asana offboarding fields + the message mining in §4 here).
- **House audits / tenant audits** (`local_2ae5d6b6`, `local_1791ad26`): occupancy timelines are pure Asana; respond.io adds the "recent comms" layer (live move-out requests, mould photo chases, failed template deliveries).
- **Live tenant replies** (rare): Asana status → drafted WhatsApp reply → explicit approval → `send_message`. Never send without the user approving exact wording.

---

## 6. Assets & prior outputs

All under `/Users/stuff/Documents/Claude/Projects/Random CDA stuff/` (shell path: `/sessions/<session>/mnt/Random CDA stuff/`):

| File | What it shows |
|---|---|
| `CDA House Stories - Combined (4 Houses).md` (+ `.docx`, + 4 `House Story - *.md`) | The mature report format; "Tenant comms (respond.io)" sections with `[id:…]` citations (Crown St, Bronte Rd, Erskineville Rd, Victoria St). Generated 2026-06-23, 6-month scope. |
| `Offboarding_Investigation_10rooms_2026-06-22.md` | Per-room move-out forensics; respond.io as "how CDA knew" evidence. |
| `Offboarding_Investigation_22upcoming_2026-06-22.md` | 22 upcoming vacancies; "Tenant form + respond.io" notice-channel attributions. |
| `early_lease_breaks.csv`, `CDA_early_lease_breaks_Mar-Jun_2026.xlsx` | Lease-break dataset (Asana-sourced; respond.io used for follow-up digs). |
| `7A_Harvey_St_Issues_Mar-Jun_2026.md` | House issue log — **Asana-only** source (respond.io was used separately in `local_15830054` to *reply* to the 7A Harvey tenant). |
| `CDA_Tenant_Profiles.pdf` | Tenant profile evidence pack (referenced in `local_15830054` as the precedent for "PDF evidence packs"). Content **UNVERIFIED** (not opened for this doc). |

Key transcripts (via `mcp__session_info__read_transcript`): `local_15830054` (workspace audit → Burnett & Stoney Creek investigations — the canonical methodology), `local_21faee18` (MCP setup), `local_2ae5d6b6` (66 Boundary audit), `local_08be3e99` (193 John St offboarding — Asana-only variant), `local_1791ad26` (350 Marsden tenant audit — Asana-only occupancy timeline).

Memory dir (`…/memory/MEMORY.md`): **no respond.io entry exists yet** — this doc is currently the only persistent record of the workflow.

---

## 7. Tools & permissions required

- **respond-io MCP connector** (`mcp__respond-io__*`). Backed by the official `@respond-io/mcp-server` authenticating with a workspace-level Developer API Access Token (`RESPONDIO_API_KEY`); requires respond.io **Growth plan+**. Whether the current Cowork connector runs via that npx/stdio config or a hosted connector is **UNVERIFIED** — it simply appears as the `respond-io` server in-session.
- **Asana connector** (`mcp__cf562c96-…__search_tasks/get_task/search_objects`) — mandatory companion for rosters.
- `ToolSearch` to load deferred schemas; `Write`/`Grep`/`mcp__workspace__bash` for saving and mining long threads.
- Convention: read-only. Any write (send_message, tags, comments) needs explicit user approval of the exact payload.

---

## 8. Gotchas & failure modes (all actually encountered)

1. **No address search.** `list_contacts` search only hits name/phone/email; house address is a custom field and unsearchable. Always roster via Asana first (`local_15830054`).
2. **Stale/conflicting custom fields.** `Room_Details` vs `general_address` can name two different houses on one contact (live example id:407665783). Fields like `name_cda`, `asana_task_id` are usually null.
3. **Newest-first ordering + cursor pagination.** Easy to build a backwards timeline; convert `messageId` → date and re-sort. To go further back, pass `cursorId` from `pagination.next`.
4. **Broadcast noise.** House-wide broadcasts and template blasts appear in every tenant's thread (`broadcastHistoryId`/`workflowId` set) — dedupe, and don't attribute a broadcast to a tenant as if they wrote/received it uniquely.
5. **Huge threads blow up context.** Save `list_messages` output to files and `Grep`; don't read 100-message pages inline (`local_15830054` did exactly this).
6. **`send_message` channelId type quirk.** Passing `channelId` errored once; omitting it defaults to the contact's last-used channel (correct behaviour). Only relevant for the rare approved sends.
7. **Duplicate/near-miss contacts.** Some contacts carry "(CDA)" suffixes or slightly different name spellings vs Asana ("Swann" vs "Swan"-type mismatches happen on the Asana side too). If a name search misses, try phone/email from the Asana task. `merge_contacts` exists but has never been used (**write — don't**).
8. **New tenants have no history** (Burnett: "Luka & Dalil… no chat history yet") and **quiet tenants prove nothing** — absence of chat evidence ≠ absence of a problem; say so explicitly (Nazir/Room 6 case).
9. **`list_closing_notes` is empty** in this workspace; `lifecycle` null on sampled contacts — don't build logic on those.
10. **Rate limits:** none observed across ~10 parallel contact/message pulls per session. **UNVERIFIED** what the API's actual limits are.

---

## 9. Worked example (real, from session `local_15830054`)

Request: *"search for everyone who lives in 19 Burnett St, Merrylands… all chats for the past 3 months and Asana… complaints about certain tenants, and cleaning issues… chronological order."*

1. `mcp__cf562c96__search_tasks("19 Burnett St Merrylands")` → move-in/move-out tasks → roster (R1 Kameli→Luka, R2 Silvia, R4 Daisybahen, R7 Zia→Dalil; R5/R6 unnamed at first).
2. `mcp__respond-io__list_contacts(search:"<name>")` × 6 in parallel → contact IDs. (Address search had already failed — expected.)
3. `mcp__respond-io__list_messages(identifier:"id:<id>")` × 6 → long threads saved to files → `Grep` for complaint keywords.
4. Report: chronological evidence (Asana tickets interleaved with WhatsApp quotes, e.g. Kameli "Car part is not mine", Silvia "the only person in the house at this moment"), roster table, gaps flagged (R5/R6 occupants unknown; "no tenant complained in WhatsApp about Rooms 5/6").
5. Follow-up: "use the applications and moving in project to find who lives in room 5 and 6" → Moving In search → **R5 #1918 Najeebullah, R6 #1919 Nazir** → `get_contact` + `list_messages` for both → combined timeline (AC-misuse thread, "That is not my fridge", Nazir's lone wifi message).
6. Final ask "what's fact / what's hearsay / should we act" → three-bucket verdict: R5 has one documented breach; R6 is guilt-by-association on a single anonymous comment; recommended evidence-building steps instead of punitive action.

Contrast case, same session: **444B Stoney Creek** — same pipeline, but the chats *corroborated* the Asana allegations (Paula's photo evidence + repeated messages), so the verdict supported the eviction that had already happened.

---

## 10. Open questions / UNVERIFIED

- Exact dates of sessions `local_21faee18` (setup) and `local_15830054` (audit) — `list_sessions` gives no timestamps; content places them ≈ early–mid Jun 2026 — accept as unknown; old-project transcripts are unreadable from the new project, do not attempt to verify.
- Which session produced the House Stories files (2026-06-23) — not identifiable by title in the session list; the files themselves document the method — accept as unknown; old-project transcripts are unreadable from the new project, do not attempt to verify.
- How the Cowork `respond-io` connector is currently hosted/authenticated (stdio npx config vs desktop connector) and its rate limits.
- Whether message history has any retention cap (oldest message pulled so far ≈ Jan 2026; workspace channels date to Dec 2024).
- Purpose/traffic of the "CDA House Updates", "Andres", "Sofia", Telegram and Website Chat channels — never used in investigations to date.
- Whether any contacts have `lifecycle` stages or `tags` populated (all sampled were null/empty), and what `CDA_Tenant_Profiles.pdf` contains in detail.
