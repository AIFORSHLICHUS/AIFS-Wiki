---
type: topic
slug: crm-automation
aliases: [donor management, CRM agents, follow-up automation]
status: maintained
sources: [chat.txt]
updated: 2026-05-25
---

# CRM Automation &amp; Donor Management

A recurring pain point: shluchim spend hours on data entry,
lapsed-donor follow-ups, and contact enrichment. The chat has tested
several patterns.

## The pain

> *"Update my CRM. I can forward it email, voice notes etc. and it
> would either make a new contact or add a note to a contact. Also if
> I could send it a voice note to schedule a follow up in my calendar."*
> — [chat 2026-03-19, +44 7710 524460]

> *"Analyze your CRM. See which donors lapsed and feed you 3 each day.
> Check when you last called them in your phone log or texts or
> WhatsApp or email."*
> — [chat 2026-03-19, Levi Haskelevitch]

Both bubble to the top whenever Mendy Shishler asks "if you had an AI
agent that could do anything for you, what would it do?"

## The CRMs in play

| CRM | Notes from the chat |
| --- | --- |
| **ChabadOne (Salesforce-backed)** | The Chabad-default. AI integration via Salesforce MCP — *easy* to set up per [chat 2026-05-15, +1 438-526-6974]. Yisroel Chaim Shuchat has been testing. |
| **Hecher CRM** | Custom-built by [[../people/elazar-green]] with Claude MCP integration. ~80-shliach beta. Voice notes → transcribe (Whisper) → Claude turns into emails, calendar items, CRM updates. [chat 2026-05-15] |
| **Little Green Light (LGL)** | Mainstream nonprofit CRM. Used heavily by Didy Waks with an AI agent that self-learns features via Nanoclaw. [chat 2026-05-15] |
| **CiviCRM / Chabad Suite** | API exists; +44 7710-524460 connected it to Base44 to push/pull data. [chat 2026-05-15] |
| **MyShul** | Has its own AI report-bot: "give me a list of all 12-year-old boys and their parents' numbers" → produces it. [chat 2026-05-15, +1 786-547-3031] |
| **Attio** | Modern CRM. Rabbi Zalman Abraham uses an agent for prospect research and contact enrichment. [chat 2026-03-19] |

## Patterns that work

### 1. Agent-on-CRM (Claude Dispatch / Cowork / Nanoclaw)

Didy Waks (heaviest user): [[../tools/claude]] Dispatch acts like a VA
clicking through LGL — adds donations, runs reports, drafts
follow-ups. Doesn't use the LGL API; uses *browser automation*.
[chat 2026-03-29]:

> *"It's like an agent working on your computer, in your browser. Pretty
> cool. Like having a VA, but without a brain, so doesn't make low-IQ
> mistakes."*

Nanoclaw (Yonatan Azrielant's recommendation) is the *safer* version:
ex-JLI / ex-IDF 8200 founders, Docker-sandboxed. [chat 2026-03-13]

### 2. MCP / API into vetted backends

When the CRM has an API or MCP server, you skip browser automation:

- **Salesforce MCP** → Claude/ChatGPT → ChabadOne data.
  [chat 2026-05-15]
- **Hecher MCP** → Elazor Green's bespoke setup. [chat 2026-05-03]
- **CiviCRM API** → Base44 (no-code) frontend.

This is the engineering path. Slower to set up; reliable in
production.

### 3. Voice note → action item pipeline

A common request, partially solved:

1. Record voice note (WhatsApp or built-in voice memo).
2. Transcribe with [[../tools/sofer-ai]] or Whisper (free OpenAI API).
3. Feed transcript + system prompt to Claude or ChatGPT.
4. System prompt: *"Extract: new contacts to add, calendar follow-ups,
   email drafts. Output JSON."*
5. Push to CRM via API.

Elazor Green's Hecher CRM has this end-to-end. [chat 2026-05-03]

### 4. Donor research / enrichment

Use cases the group has shipped:

- **Public-philanthropist lookup.** Claude Cowork built spreadsheets
  of *publicly listed* top Jewish donors per city. [chat 2026-04-19,
  Shmulie Cunin] — "Saved me a few hours."
- **Email-finding via Sheets formula.** [chat 2026-03-19, Rabbi Zalman
  Abraham]: Concatenate everything you know about a person into one
  cell, use the `=AI(...)` Gemini Workspace formula, drag down. Retry
  failures.
- **Jewish-name scoring.** Yonatan Azrielant's two open gists
  (`gist.github.com/jonazri/006e3b667dc309f8db4d9875ce8a51e1` agent
  and `gist.github.com/jonazri/b353b67db66a902ba1bcf66c94d48b62`
  prompt) score likelihood that a name is Jewish. *"Use responsibly."*
- **WealthEngine** for prospect scoring. [chat 2025-11].
- **Hatch.ai** — Lubavitch-owned prospect research; some users find it
  "more hatch and less ai." [chat 2026-04-21]

## What *doesn't* work

- **Vibe-coded CRMs with login + payment.** Repeatedly warned against;
  see [[../themes/vibe-coding]]. Mendy Mann: keep banking *out* of
  AI-built systems. [chat 2026-01-11]
- **Web-UI click-bots on flaky pages.** Claude Cowork is good but
  fragile; CRM UI changes break runs.
- **Ethnicity-based marketing lists.** Real legal restriction (Data
  Axle and similar), not just an AI guardrail. [chat 2025-09-12,
  +1 415-634-7727]

## Open questions

- A CRM template that 200 shluchim could install without each one
  becoming a security incident. The community keeps proposing; no one
  has shipped it.
- **Email + voice note → CRM** as a packaged install instead of a
  bespoke build per shliach.
- **WhatsApp data mining.** Meir Sudak's Selenium-based exporter
  ([chat 2026-03-22]) is the only working solution; encrypted backups
  block direct access.

## Related

- [[../tools/claude]] — Dispatch / Cowork / MCP path.
- [[../people/didy-waks]]
- [[../people/elazar-green]]
- [[../themes/vibe-coding]]
- [[fundraising]]
