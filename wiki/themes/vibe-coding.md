---
type: theme
slug: vibe-coding
aliases: [no-code, low-code, ai-built apps, lovable, claude code]
status: maintained
sources: [chat.txt]
updated: 2026-05-25
---

# Vibe Coding

*"Vibe coding"* = building real software by describing it to an LLM and
shipping whatever comes out, with little or no traditional engineering
discipline. The chat is full of triumphs and disasters with this
approach.

## The triumphs

A non-exhaustive list of community-shipped apps built this way:

- [[../tools/megillah-app]] — synced Megillah reading, broadcast mode,
  multi-language. Built in ~10 days during Purim 2026, with feature
  requests merged live. Mendy Elishevitz on Claude.
- [[../tools/berel-me]] — 12+ micro-tools (grogger, raffle, dreidel,
  pdflabel, splitmyclass, sicha-stitcher, 12 pesukim, autoprint,
  pushka tracker). Berel Marozov, mostly Claude Opus 4.5.
- [[../tools/maamorim-app]] — curated Rebbe's maamorim with AI search
  and notes. Mendy Elishevitz.
- **Mishna.me** — shareable mishnayos with *osiyos hashem* for shiva /
  yahrtzeits. Mendy Elishevitz, [chat 2026-03-22].
- **Tzvi-to-Tzadik** — Yossi Yaffe's grandfather's poems to the Rebbe,
  AI-powered source exploration. [chat 2026-03-29]
- **Rashi Roots Map / Atlas of the Sages** — intellectual-history
  timeline on Lovable. Yossi Yaffe.
- **Tenpr.app** — *maaser* education tool. Mendy Shishler in Google AI
  Studio. [chat 2026-01-15]
- **Cypcampaign.lovable.app** — end-of-year campaign dashboard. Avi Winner.
- **Countomer** — Sefiras HaOmer with daily *Daf of Sotah* and
  location-based *Tzeis* notifications. [chat 2026-04-16, +1 347-770-3586]
- **Movers-referral-tool** — NCOA results → nearest Chabad House
  referral emails, fully in-browser. [chat 2026-03-10, +1 717-827-6287]
- **Rebbe's Global Footprint** — Mendel Teldon, Base.app, **15 minutes**.

The throughline: pick a small, specific problem; ship; iterate from
community feedback within hours.

## The disasters

> *"I kept adding pieces using AI tools. Each addition made the codebase
> more fragile. By the end, I had six different timing systems
> contradicting each other."*
> — [chat 2026-03-04, Yossi Yaffe], post-mortem of learningtanach.org's
> Esther reader (still got 7,000 visitors in 2 days).

> *"AI coding is powerful, but incremental AI edits can quietly make
> the codebase fragile. Never release an AI-coded app with login
> functionality."*
> — [chat 2026-03-05, Rayi Stern]

> *"They use you and your chat data to train their models."*
> — [chat 2025-03-27, Meir Sudak] (on the broader risk surface)

Specific failure modes the group has documented:

- **Compounding fragility.** Each AI edit fits the *previous* state of
  the code but doesn't reason about the whole. Architecture rots.
- **Security blind spots.** Vibe-coded systems with user accounts +
  payment + AI-built backends are a recipe for credit-card and PII
  leakage. [chat 2026-01-11, +1 33-6 51 48 36 80; Mendy Mann]
- **WhatsApp bans.** Bots and bulk senders that route through personal
  numbers get accounts disabled, sometimes after months of working
  fine. [chat 2026-03-13, Rayi Stern; chat 2025-12-04, +1 203-887-6044]
- **Inability to import existing code.** Lovable can't ingest a real
  repo. For non-trivial work you graduate to Cursor / Claude Code.
  [chat 2026-02-22, Meir Sudak]

## Rayi Stern's rules

[chat 2026-03-13]:

> Don't vibe-code anything that:
> 1. has a database,
> 2. is user-facing with logins,
> 3. handles financial transactions, or
> 4. integrates mission-critical email.
>
> For everything else — fine, ship it.

## The toolchain shakeout (as of May 2026)

| Tool | Pricing signal | Best for | Caveat |
| --- | --- | --- | --- |
| [[../tools/lovable]] | Credits, ~$25/mo entry | Fast prototypes, single-page apps | Can't import repos; security review required before banking/CRM |
| Base44 | Cheap | Database-backed apps; quick MVPs | Less polished than Lovable |
| Bolt | Cheap | Similar to Lovable | — |
| Claude Code | Free with Claude Pro | Real engineering, GitHub integration | Skill curve |
| GitHub Copilot | $10/mo | Best value if you're already in an IDE | — |
| Cursor | $300–500/mo at heavy usage | Power tool | Expensive |
| Google Jules | Free | Phone-based prompting from GitHub | Newish |
| cto.new | Free, browser | Quick experiments | Less polish |
| Kiro.dev | Free preview | Desktop-app style | Beta |

[chat 2026-02-22, Meir Sudak] is the canonical comparison post.

## How the safe ones stay safe

- **In-browser, no server.** The movers-referral-tool never persists
  user data. Same with my-charity-box and countomer.
- **No login.** The dreidel raffle and grogger don't store accounts.
- **Curated corpus, not generation.** maamorim.app and dach.dev expose
  pre-vetted text; the AI helps *find* not *invent*.
- **MCP / API into vetted backends.** Hecher CRM (Elazor Green) and
  the [[../tools/megillah-app]] both connect AI agents to systems whose
  behavior is already correct.

## Open questions

- When the megillah.app live-broadcast mode has latency between
  phones, who fixes it? Single-maintainer projects bus-factor of 1.
- How do we ship a Chabad-house CRM template that 200 shluchim can
  install without each one becoming a security incident?
  [[../topics/crm-automation]]
- Vibe-coding's "shippable in 15 minutes" appeal vs. the maintenance
  cliff. No one in the chat has solved this.

## Related

- [[../tools/lovable]]
- [[../tools/megillah-app]]
- [[../tools/berel-me]]
- [[../topics/crm-automation]]
- [[../conversations/megillah-app-sprint-feb-2026]]
