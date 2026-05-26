---
type: tool
slug: shluchimexchange-ai
aliases: [Shluchim Exchange, ShluchimExchange.ai, SE]
status: maintained
sources: [chat.txt]
updated: 2026-05-25
---

# ShluchimExchange.ai

Platform for Chabad-specific AI agents and prompts. Launched at Kinus
Hashluchim 2025-11-13 by Rayi Stern and collaborators. Hosts curated
agents the community can fork, remix, and use.

## What it is

`shluchimexchange.ai` — a directory of Chabad-tuned AI prompts and
agents, accessible via web. Treats *prompts as artifacts*: each one
has a URL, can be remixed, and can be invoked from inside the
platform.

Subpaths referenced in the chat:

- `/kh` — Kiddush HaChodesh tools / prompts.
- `/prompts/{id}` — individual prompt URLs (e.g., the ChabadOne CSS
  code agent: `/prompts/28cbafa6-f2e4-4c18-b072-7ccd8f5282f4`)
- `haggadah.shluchimexchange.ai` — customizable printable Haggadahs
  (children's and adults'). [chat 2026-03-22, Rayi Stern]

## What's in the catalog

- **ChabadOne-compatible code generation** — produces XHTML 1.0
  compliant HTML for ChabadOne sites. Has a master prompt fallback.
  [chat 2026-02-18, Yisroel Chaim Shuchat]
- **Custom-page / custom-email builders** for ChabadOne.
  [[../topics/chabadone-integration]]
- **Torah learning agents** — including a "deep thinking" agent.
- **Newsletter writing agent.**
- **Flyer generation agent** — generates prompts for image models, not
  images directly (as of [chat 2026-02-11, Rayi Stern]).
- **Clear Communication Agent** and **Stop Writing Like a Robot**
  agents. [chat 2026-02-16]
- **Spam / promotions tab checker.** [chat 2026-02-12]
- **JewScore** — Jewish-name scoring (98% confidence on test names).
  `ai4.shlch.us/jewscore`

## How shluchim use it

- **Beta-test new agents** in private; iterate based on community
  feedback. Meir Sudak, Rayi Stern recruit beta testers regularly.
- **Discover prompts** that solve specific Chabad-house problems
  without rebuilding from scratch.
- **Share variants** of prompts across the community.

## Founders &amp; key contributors

- Rayi Stern — co-built; coordinates AI Day at Kinus.
- Meir Sudak — agent curation, beta-tester recruitment.
- Mendy Shishler — strategic direction.
- Yisroel Chaim Shuchat — many of the ChabadOne agents.

## Strengths

- Curated for Chabad context, so prompts come pre-tuned for sources
  (Chabad.org, Sefaria, classical seforim) and constraints (XHTML 1.0,
  brand voice).
- Remixing built in.
- Beta-testing channel for the community.

## Weaknesses / open questions

- Discoverability — many agents exist; how do new shluchim find them?
- Versioning of prompts as models change underneath.
- Long-term ownership / maintenance.

## Related

- [[../people/rayi-stern]]
- [[../people/meir-sudak]]
- [[../conversations/kinus-ai-day-nov-2025]]
- [[../topics/chabadone-integration]]
- [[../resources/master-prompts]]
