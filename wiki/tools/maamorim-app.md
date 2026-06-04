---
type: tool
slug: maamorim-app
aliases: [maamorim.app, Maamorim App]
status: draft
sources: [chat.txt]
updated: 2026-05-25
---

# maamorim.app

Curated app for learning the Rebbe's *maamorim* with AI-assisted
search and notes.

## What it is

`maamorim.app` — a clean reader for the Rebbe's *maamorim* with:

- Summaries by **R' Shneur Zalman Farkash**, baked into the corpus.
- **AI search** across maamorim.
- **Favorites &amp; notes** per user.
- *"Even this file was made by AI."* [chat 2026-03-27]

## Why it works (and the contrast with raw NotebookLM)

[[notebooklm]] is general-purpose; it can be pointed at the Rebbe's
corpus, and it does well — but it caps at ~12 sources per query and
has weak Hebrew video output. maamorim.app curates *one* corpus,
ships a domain-specific UI, and bakes in trusted summaries — the
LLM is a helper, not the source of truth.

This is the pattern [[../themes/ai-and-torah-accuracy]] argues for:
**curate the corpus, vet the summaries, let AI re-present rather than
invent**.

## Notable use cases

- **Bar-mitzvah maamar preparation.** [chat 2026-05-25, +1 917-982-9772]:
  > *"I uploaded the last maamar I learned (בלתי מוגה) to Claude and he
  > beautifully extracted the *nekuda* of the maamar and presented it
  > in a way that a 13-year-old can understand. It was the biggest
  > nachas for me to see a boy from my community chazering a maamar at
  > his bar mitzvah."*

  (Workflow generalizes: maamorim.app → Claude → bar-mitzvah-grade
  summary.)

- **Shiur prep on a maamar topic.** Search via the app's index;
  cross-reference; build out a shiur. See [[../topics/shiur-prep]].

## Related

- [[notebooklm]]
- [[../themes/ai-and-torah-accuracy]]
- [[../topics/shiur-prep]]
