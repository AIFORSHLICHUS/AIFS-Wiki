---
type: tool
slug: crm-tools
aliases: [CRMs, LGL, Attio, Hecher, Salesforce, MyShul, CiviCRM, Hatch.ai]
status: maintained
sources: [chat.txt]
updated: 2026-05-25
---

# CRM &amp; Donor-Management Tools

Reference page for the donor / contact systems shluchim use, ranked
by their AI-integration readiness.

| CRM | AI integration | Notes |
| --- | --- | --- |
| **ChabadOne (Salesforce-backed)** | Salesforce MCP works easily | [chat 2026-05-15]. The Chabad default. |
| **Little Green Light (LGL)** | API exists; community members use Nanoclaw agent | [chat 2026-05-17] $100 credit link. *"Great CRM for donor management and insight."* |
| **Hecher CRM** | Native MCP integration | ~80 shliach beta. Voice notes → Whisper → Claude → CRM. |
| **CiviCRM (Chabad Suite)** | API; a member connected to Base44 | [chat 2026-05-15] |
| **Attio** | Agent for prospect research/enrichment | Used heavily for prospect research. [chat 2026-03-19] |
| **MyShul** | Built-in AI report bot | *"Type 'give me a list of all 12-year-old boys and their parents' numbers' and it produces the list."* [chat 2026-05-15] |
| **CMS Cloud** | Chabad donor management | [chat 2026-01-06] |
| **Hatch.ai** | Lubavitch-owned prospect research | [chat 2025-09-22]. Some users: *"more hatch and less ai."* [chat 2026-04-21] |

## AI patterns layered on top

- **Browser-automation agents** ([[claude]] Cowork / Dispatch,
  Nanoclaw, Manus.im) — work on any CRM with a web UI, but click-bot
  fragility is real.
- **MCP / API integrations** — cleaner; require dev work or vendor
  support.
- **Spreadsheet-as-CRM** with Gemini `=AI(...)` formula — cheap and
  effective for enrichment passes.
  [chat 2026-03-19]
- **Voice-note → CRM** — Whisper → Claude → API. See Hecher.

## Donor research

- **WealthEngine** — paid prospect scoring.
- **Exa Websets** — `websets.exa.ai/websets/` — research finds for
  fundraising. *"Good ROI for fundraising."*
- **Jewish-name detection gists** — open-source tools for scoring lists
  (see [[../topics/fundraising]]).
- **Claude Cowork** — built a spreadsheet of top Jewish philanthropists
  per city from publicly listed information.
  [chat 2026-04-19, Shmulie Cunin]

## Bookkeeping

- **QuickBooks** is default; some shluchim using AI to draft entries.
  [chat 2026-05-18]
- **Kick.co** / **Booking.ai** — "underwhelming, like Mint.com."
  [chat 2025-10-22]

## Open questions

- A **shareable CRM template** that 200 shluchim could install without
  each one becoming a security incident — persistently proposed, never
  shipped.
- **Multi-CRM donor view** combining LGL + ChabadOne + bank
  statements.

## Related

- [[../topics/crm-automation]] — full workflow page.
- [[../topics/fundraising]]
- [[claude]]
- [[../themes/vibe-coding]] — why most "I'll build my own CRM" ends in tears.
