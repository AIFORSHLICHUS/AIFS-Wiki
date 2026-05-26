---
type: tool
slug: learningtanach-org
aliases: [Learning Tanach, learningtanach.org]
status: draft
sources: [chat.txt]
updated: 2026-05-25
---

# learningtanach.org

Yossi Yaffe's interactive Tanach learning tool. Best-known for the
**Megillas Esther reader** featuring high-quality images of the story
based on excavations and academic archaeology.

## What it is

`learningtanach.org` — multi-book Tanach reader with rich visual
supplements:

- `/esther/reader` — the Esther story with images for each pasuk.
- `/home` — full Tanach portal.

Multi-language support. ~100+ hours of work went into the images and
3D reconstructions.

## The Purim 2026 launch

[chat 2026-03-04] post-mortem from Yossi Yaffe is one of the most
valuable artifacts in the chat — a candid public retrospective on
shipping AI-coded software:

> *"I kept adding pieces using AI tools. Each addition made the
> codebase more fragile. By the end, I had six different timing
> systems contradicting each other."*

Result: launch-day bugs, public criticism, then ~**7,000 visitors in 2
days** post-Purim. Worth it.

## What broke

- Multiple AI-built features layered on top of each other without
  refactoring — the [[../themes/vibe-coding]] failure mode.
- AI auto-scroll timing fought page-pinning fought passage navigation.
- Bug fixes generated new bugs because Claude reasons locally, not
  globally.

## What worked

- The corpus itself (text + images) was solid.
- The format — paragraph-by-paragraph with image — landed with users.
- Yossi posted detailed lessons publicly, becoming a reference point.

## Lessons Yossi shared

- Restart the chat / refactor before adding features.
- Don't release vibe-coded apps with login functionality (he didn't,
  good call).
- Test early, commit often.
- Be transparent about failures so others learn.

## Yossi's follow-on projects

- **Tzvi-to-Tzadik** — `tzvi-to-tzadik.lovable.app` — his grandfather's
  poems gifted to the Rebbe, with AI-powered source exploration.
  [chat 2026-03-29]
- **Rashi Roots Map / Atlas of the Sages** — intellectual-history
  timeline on Lovable. [chat 2026-01-23]
- **Book of Esther** — `bookofesther.lovable.app` — with live maps and
  meforshim translation. [chat 2026-02-22]
- **9 Principles for AI Torah Citation** — in-progress community
  document. [chat 2026-02-23]. See [[../themes/ai-and-torah-accuracy]].

## Related

- [[../people/yossi-yaffe]]
- [[../themes/vibe-coding]]
- [[../themes/ai-and-torah-accuracy]]
- [[../topics/hebrew-yiddish]]
- [[lovable]]
