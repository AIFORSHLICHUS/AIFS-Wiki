---
type: topic
slug: web-app-building
aliases: [vibe coding, no-code, app building, Lovable, Claude Code, build a website]
status: maintained
sources: [chat.txt]
updated: 2026-05-25
---

# Building Web Apps with AI

Beyond simple flyers and letters: actual web applications. The chat's
maturation arc — from *"holy cow, you can build apps in minutes"* to
*"here's what to vibe-code and what not to."*

## The tool decision

| Need | Tool |
| --- | --- |
| 15-minute prototype, single page, no DB | [[../tools/lovable]] |
| Database-backed, multi-screen | Base44 |
| Real engineering, GitHub | [[../tools/claude]] Code |
| Already in an IDE | GitHub Copilot ($10/mo) |
| Power-user big codebase | Cursor ($300–500/mo at heavy use) |
| Free phone-based prompting | Google Jules |

Full comparison in [[../tools/coding-builders]].

## What to build (safe patterns)

- **In-browser, no server** — page reads input, computes, displays.
  No database.
- **No logins, no accounts.**
- **No payments, no banking info.**
- **No customer PII storage.**
- **Curated corpus, AI re-presents.** (See [[../tools/maamorim-app]].)
- **MCP into vetted backends** when you must integrate (Salesforce,
  Tally, Stripe).

These all live up to Rayi Stern's rules
([[../themes/vibe-coding]]).

## What not to build (alone, with AI alone)

- Anything user-facing **with logins**.
- Anything **with payment / banking** integration without security
  review.
- **Mission-critical email** integrations.
- **Mass-messaging bots** on personal WhatsApp numbers — see
  [[whatsapp-automation]].
- **Mass donor/contact databases** that AI agents can directly
  query without auth boundaries.

## Real examples (shipped)

See [[../tools/chabad-apps]] for the running list. The pattern:

- Mendy Elishevitz: megillah.app, maamorim.app, mishna.me, mikdash.live.
- Berel Marozov: berel.me/... portfolio (dozen+ tools).
- Yossi Yaffe: learningtanach.org, Tzvi-to-Tzadik, Book of Esther,
  Rashi Roots Map.
- Avi Winner: cypcampaign, sms-invite-joy, chabadvocate.
- Mendy Shishler: Tenpr.app.
- Mendy Efune: ChabadUp.com (full-app, 100% AI).
- Mendel Teldon: Rebbe's Global Footprint (15 minutes).
- Yisroel Chaim Shuchat: ai770.com/megillah, ShliachFlow.

## Lessons from the field

- **Restart the chat / refactor often.** Yossi Yaffe's
  learningtanach.org post-mortem [chat 2026-03-04]: *"Each addition
  made the codebase more fragile. By the end, I had six different
  timing systems contradicting each other."*
- **Test in real environments early.** Especially for ChabadOne (XHTML
  1.0); see [[chabadone-integration]].
- **Use AI to write scripts, not to process data.** Berel Marozov:
  *"In general, I always ask AI to make a script instead of asking it
  to directly process the data."* [chat 2026-05-20]
- **Have AI assess your security.** Mendy Efune: *"If you build using
  Claude Code you simply ask it how it can improve the security…"*
- **Watch token usage.** Claude Sonnet 4.6 ran out mid-project for
  +44 7980-795936; restarting in a different model caused issues.

## Open questions

- **How to graduate** from Lovable prototype to maintained software.
- **Template that 200 shluchim can install** without each becoming a
  security incident.
- **Multi-maintainer** vibe-coded projects — most are bus-factor 1.

## Related

- [[../themes/vibe-coding]]
- [[../tools/lovable]]
- [[../tools/coding-builders]]
- [[../tools/megillah-app]]
- [[../tools/berel-me]]
- [[../tools/chabad-apps]]
- [[chabadone-integration]]
