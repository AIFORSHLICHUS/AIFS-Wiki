---
type: tool
slug: claude
aliases: [Anthropic, Claude Pro, Claude Max, Claude Code, Claude Design, Claude Dispatch, Claude Cowork, Opus, Sonnet, Haiku]
status: maintained
sources: [chat.txt]
updated: 2026-05-25
---

# Claude (Anthropic)

The chat's default recommendation for *serious* work — code, long
documents, structured shiurim. Notorious for usage limits until the
**Anthropic–SpaceX compute deal** (announced [chat 2026-05-08])
significantly relaxed them.

## Surfaces &amp; products

- **claude.ai** — chat UI.
- **Claude Pro** — $20/mo. Sufficient for most shluchim post-SpaceX deal.
- **Claude Max** — $100/mo. Removes most rate-limit friction.
- **Claude Code** — `claude.ai/code`. The vibe-coding workhorse; better
  for serious engineering than Lovable. [[../themes/vibe-coding]]
- **Claude Design** — visual design tool. "Pretty promising."
  [chat 2026-05-13]. 7-day allowance. Used for sicha visualizations:
  `zmabraham.github.io/Sicha-Infograph/`.
  [chat 2026-05-19]
- **Claude Dispatch / Cowork** — Claude as desktop / browser agent.
  Used for CRM data entry. [chat 2026-03-29, 2026-04-19]
- **MCP integration** — first-class. Connect GitHub, Salesforce, Tally,
  Canva, Gmail via MCP.
- **Models referenced**: Claude 4, Opus 4.5, Opus 4.7, Sonnet 4.6,
  Haiku, plus the late "Opus 4.6 / GPT-5.3 February 5th milestone."
  [chat 2026-02-13, Matt Shumer article]

## What the chat uses it for

- **Shiur prep** — wins this category decisively. [[../topics/shiur-prep]]
- **Word documents &amp; spreadsheets** — formats well *if* given a
  template. [chat 2026-03-16]
- **HTML / code generation** — best of the three for clean code.
- **App building (Claude Code)** — megillah.app, the berel.me suite, and
  ~20 other community apps. [[../themes/vibe-coding]]
- **Custom CRMs &amp; agents** via MCP. [[../topics/crm-automation]]
- **Letter writing with emotional intelligence** — preferred over
  ChatGPT for pastoral letters. [chat 2025-08-04]
- **Latex / Typst typesetting** — Claude knows LaTeX well; better than
  DOCX for any non-trivial document. [chat 2026-03-09]

## Strengths

- Best at *technical accuracy*. Community bake-offs against
  GPT-5, Gemini 2.5, Grok consistently put Claude first for *iyyun*
  and code.
- Best long-context document handling — "Claude was beautifully
  formatted" vs ChatGPT/Gemini for a Gemara curriculum.
  [chat 2026-05-14]
- Honest about its limits — will say "I don't know" / "use Sefaria for
  this" instead of hallucinating. [chat 2026-03-24]

## Weaknesses

- **No native image generation.** Use [[chatgpt]] or [[nano-banana]].
- **Slowest of the three.** "Claude is pretty slow compared to Gemini
  and GPT." [chat 2026-01-21]
- **Mobile experience trails ChatGPT.**
- **Rate limits used to be brutal.** Pre-SpaceX, even Pro hit "out of
  messages" in 1.5 hours. Largely fixed [chat 2026-05-08].
- **Token consumption with extended thinking.** Long sessions burn
  tokens; restart fresh chats for big projects. [chat 2026-03-18]
- **Projects vs. Chats** — Projects had issues for some users;
  unresolved best practice. [chat 2026-03-18]

## Discounts

- **Claude for Nonprofits** — 75% off, **5-seat minimum** = $40/mo
  total. `claude.com/solutions/nonprofits`. [chat 2025-12-02]
- **Anthropic Skilljar courses** — free, `anthropic.skilljar.com`.
  [chat 2026-05-18]

## Notable patterns

### "If hook fails, troubleshoot the hook" — multi-step prompting

[chat 2025-11-14], the "Golden Prompt of the Week":

> *"When I ask how to do something, work with me step by step — ONE
> step at a time. DON'T give me all the steps at once. Start with a
> SHORT explanation of what we're going to do. Then give me ONLY the
> first step. Wait for me to confirm it worked. Then move to step 2."*

### Claude with MCP for CRMs

Connect Claude to Salesforce, Hecher, or Tally via MCP servers; use
Claude as the natural-language interface.
See [[../topics/crm-automation]].

### Github + Claude Code

[chat 2026-04-27]:

> *"Go to Setting &gt; Connectors &gt; GitHub. Add the connection — your
> Claude will now have access to all your repos. Then select the repo
> and start prompting."*

## Open questions

- Does Claude Design eventually obsolete Canva for flyer work?
- Best practice for Projects vs. Chats on long document work.

## Related

- [[chatgpt]]
- [[gemini]]
- [[lovable]] — alternative app-builder; Claude Code is the competitor.
- [[../themes/vibe-coding]]
- [[../topics/shiur-prep]]
