---
type: tool
slug: dach-dev
aliases: [dach.dev, dach]
status: draft
sources: [chat.txt]
updated: 2026-05-25
---

# dach.dev

Plain-text Chassidic library. The tool the chat keeps pointing
people to when they want to *feed* an LLM Likkutei Sichos or
maamorim without OCRing PDFs.

## What it is

`dach.dev/library/` — extracted, copy-able plain text of major
Chassidic seforim. The killer feature: **copy a full sicha at once**
without column / footnote / Hebrew layout headaches.

Mentioned repeatedly as a fix for the Likkutei Sichos OCR problem:

> *"Try dach.dev. Plain text extraction with copy full sicha feature."*
> — [chat 2025-11-04, multiple]

## What the chat uses it for

- **Copy sicha → paste into Claude / Gemini** for translation, shiur
  outline, drosho draft. See [[../topics/shiur-prep]].
- **Avoid the multi-column / footnote nightmare** that breaks GPT and
  Gemini PDF uploads.
- **Source-of-truth for paste-in workflows** — the AI re-presents
  what's already vetted, instead of inventing.

## Related toolkit

- **anash.org Likkutei Sichos app** — alternative plain-text export.
  `anash.org/new-likutei-sichos-app-will-help-you-locate-and-learn/`
- **likuteysichos.com** — search by topic.
- **Sefaria** — for nigleh + Chassidus (Tanya, Likutei Torah added).

## Why it matters

The hardest part of "use AI for Torah" is *getting the Torah text in
front of the AI*. Hebrew PDFs are gnarly: two columns, RTL, footnotes
inline, Hebrew vowels, sometimes Rashi script. dach.dev cuts that
problem.

## Related

- [[../themes/ai-and-torah-accuracy]]
- [[../topics/shiur-prep]]
- [[../topics/hebrew-yiddish]]
- [[notebooklm]] — alternate corpus interface.
- [[maamorim-app]] — curated alternative with summaries baked in.
