---
type: tool
slug: gemini
aliases: [Google Gemini, Gemini 3, Gemini 3.5 Flash, Gemini Pro, Nano Banana, Gemini Spark, Gems, Google AI Studio]
status: maintained
sources: [chat.txt]
updated: 2026-05-25
---

# Gemini (Google)

The model with the deepest *integration* story — Workspace, Gmail,
Drive, Docs, Sheets, Calendar — and the fastest swings in perceived
quality.

[external: model naming has continued evolving since the chat window.
The version numbers below (Gemini 2.5 Pro, Gemini 3, etc.) reflect
the chat's references; Google's actual release cadence may differ.
Treat version names as approximate. — external: knowledge cutoff
~mid-2026]

## Surfaces

- **gemini.google.com** — consumer chat.
- **aistudio.google.com** — free high-token API access, plus
  visual/vibe-coding canvas. Used to build
  [Tenpr.app](https://tenpr.app). [chat 2025-11-03]
- **Gemini in Google Workspace** — `=AI(...)` formula in Sheets, Gmail
  side-panel, Docs draft mode.
- **NotebookLM** — see [[notebooklm]]; really a separate product but
  Gemini-powered.
- **Gems** — Gemini's equivalent of Custom GPTs. Free-account
  compatible. [chat 2025-11-26]
- **Gemini Spark** — 24/7 personal agent. Announced [chat 2026-05-19].
- **Gemini Omni** — video model. Announced [chat 2026-05-19].
- **Nano Banana / Nano Banana Pro** — Gemini's image-gen model.
  Released 2025-11-20; Pro variant edits text only, 4× upscale, removes
  watermark. See [[nano-banana]].

## Models referenced

- Gemini 2.5 Pro (early benchmark winner, late 2025)
- Gemini 3 Pro (released 2025-11-20, "massive upgrade")
- **Gemini 3.5 Flash** — fast but hallucinates. *Never use Flash when
  you need accuracy.* [chat 2026-01-22]
- Gemini Pro 3.1 — released 2026-02-22, "Very strong model."

## What the chat uses it for

- **Image generation** — Nano Banana is the workhorse for
  [[../topics/flyer-design]] backgrounds.
- **Hebrew translation** — strong, second only to Qwen for pure
  translation work. [[../topics/hebrew-yiddish]]
- **Spreadsheet wrangling at scale** — the `=AI(...)` Sheets formula
  is unique. [chat 2026-03-19]
- **Email enrichment / contact research** — concatenate all known
  fields → `=AI("find email for...")` → drag down.
- **Deep Research** — Gemini's report-generation flow; bundled with
  paid tiers.
- **Vibe coding** in Google AI Studio (sometimes preferred over Claude
  for visual layout). [chat 2025-11-20]
- **Drive search** — *"asking Gemini to find information in my drive
  has made my life so much easier."* [chat 2026-01-20]
- **Storybook generation** — Gemini Storybook (`gemini.google/overview/storybook/`)
  used for Derher-article-to-illustrated-children's-story flows.
  [chat 2025-08-07]
- **Calendar event creation** — Gemini can add events to your personal
  Google Calendar. Adding to *shared team calendars* is unreliable.
  [chat 2026-01-07; 2026-05-10]

## Strengths

- **Workspace integration** unmatched.
- **Nano Banana** for image gen — until GPT 5.2 caught up.
- **Drive search.** Has access to your whole Drive if you let it.
- **Cheaper at scale** via Google AI Studio (free) and the $6 Gemini
  Plus tier.
- **Long context window** — useful for big documents.

## Weaknesses

- **Quality volatility.** "Gemini recently took a turn for the worse.
  Giving bad information regularly." [chat 2026-04-21]
- **Flash hallucinates badly.** Distinct from Pro. Users have
  repeatedly recommended "*Pro only*."
- **Gems chat history confusing** — each Gem use creates a new chat
  that must be named/pinned to save. [chat 2025-12-29]
- **Workspace admin sees all chats** — Gemini for Workspace users can't
  easily delete their chat history. [chat 2026-05-07]
- **Nonprofit Gemini** doesn't always have the same Gmail integration as
  consumer accounts. [chat 2026-05-07]

## Free / discount paths

- **Google AI Studio** — free; $300 credit for new API users.
- **Gemini Plus** — $6/mo (new cheaper tier, 2025-11).
- **Gemini Pro free 4 months** — `g.co/g1referral/ZAPZU83S`.
  [chat 2025-10-20]
- **Google Workspace Nonprofit** — bundles Gemini for qualifying
  Chabad Houses; 100TB shared storage; warn about downgrades when
  adding seats. [chat 2025-11]

## Notable usage threads

- [chat 2026-01-15] shared a `gemini.google.com/share/` link
  demonstrating LinkedIn-grade Jewish alumni ranking from a single
  prompt.
- [chat 2025-09-22] NotebookLM Hebrew-sicha → speech pipeline.
- [chat 2026-05-19] Claude Design sicha infographic — Gemini for the
  underlying research, Claude for the visualization.

## Open questions

- Will the consumer-Gemini quality flux settle, or is it permanent?
- Best way to make Gemini *not* default to Flash when you didn't ask.
- Privacy concerns of plugging Gemini into your full Gmail/Drive —
  cautioned but not resolved. [chat 2026-05-07]

## Related

- [[nano-banana]] — Gemini's image model is its own page.
- [[notebooklm]] — Gemini-powered, separately important.
- [[chatgpt]]
- [[claude]]
- [[../themes/model-leapfrog]]
