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
verified citations, refusing what it can't ground. Developed by
Professor Moshe Koppel and team at Dicta (Bar-Ilan).

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
- Promised release *"this year"* per Elisha Pearl at the demo.
  [chat 2025-11-14]
- [chat 2026-02-17, +1 415-634-7727] asked if it was working: **"Nah."**
  Still not reliably usable.
- [chat 2025-12-21, +972 54-239-9791] asked for an update; Elisha:
  *"It is heavily ongoing and in process."*

## Other Dicta products mentioned

- `rav.dicta.org.il` — Hebrew NLP for Torah. [chat 2025-12-21]
- Hebrew language analysis tools generally.

## People

- **Professor Moshe Koppel** — Bar-Ilan computer scientist; major
  Hebrew NLP pioneer; *also* a serious *baal nigleh* who teaches *Toras
  Ohr*. Billed at Kinus as having *"major giluyim"* (revelations) on
  AI. [chat 2025-11-14]
- **Elisha Pearl** — closest to the project from the AIFS side;
  primary commentator on its progress. [[../people/elisha-pearl]]

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
- [[../people/elisha-pearl]]
