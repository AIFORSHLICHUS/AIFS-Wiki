---
type: tool
slug: dicta-mekorotai
aliases: [Dicta, Mekorotai, RavDicta, Rabbinic AI, chabad.mekorotai.dicta.org.il]
status: stub
sources: [chat.txt]
updated: 2026-05-25
---

# Dicta / Mekorotai

The **"Rabbinic AI"** — purpose-built to answer Torah questions with
verified citations, refusing what it can't ground. Developed by the
Dicta team at Bar-Ilan University.

## What it is

`chabad.mekorotai.dicta.org.il` — Chabad-specific variant of Dicta's
broader rabbinic-AI work. Backend uses the [[claude]] API (the model
is swappable). The product hook: **no hallucinated citations**. If
Dicta can't find a real source, it says so.

Previewed at **Kinus AI Day 2025-11-13**.
See [[../conversations/kinus-ai-day-nov-2025]].

## Why it matters

[[../themes/ai-and-torah-accuracy]] argues the only durable answer to
AI Torah hallucination is **structured, indexed, vetted sources** that
the LLM can only re-present, not invent. Dicta/Mekorotai is the
most ambitious shot at that vision in the chat's window.

## Status (as of 2026-05)

- **Demoed 2025-11-13**, not yet generally available.
- Promised release *"this year"* at the demo.
  [chat 2025-11-14]
- [chat 2026-02-17, +1 415-634-7727] asked if it was working: **"Nah."**
  Still not reliably usable.
- [chat 2025-12-21, +972 54-239-9791] asked for an update:
  *"It is heavily ongoing and in process."*

[external: public availability status unconfirmed as of this wiki's
update. The chat's report — "not reliably working" as of early 2026 —
is the most recent data point. Check chabad.mekorotai.dicta.org.il
for current status. — external: knowledge cutoff ~mid-2026]

## Other Dicta products mentioned

- `rav.dicta.org.il` — Hebrew NLP for Torah. [chat 2025-12-21]
- Hebrew language analysis tools generally.

## Background

The tool was developed at Bar-Ilan by a team with deep Hebrew NLP
expertise; the principal researcher was introduced at Kinus as having
*"major giluyim"* (revelations) on AI — also described as a serious
*baal nigleh* who teaches *Toras Ohr*. [chat 2025-11-14]

## Open questions

- When does it ship to the public?
- Does it support Chassidus (Likkutei Sichos, maamarim) at parity with
  *nigleh*?
- Will it have an API non-Dicta apps can call?

## Related

- [[../themes/ai-and-torah-accuracy]]
- [[../conversations/kinus-ai-day-nov-2025]]
- [[notebooklm]] — the workable-today substitute.
- [[dach-dev]] — plain-text Chassidic corpus.
