---
type: tool
slug: notebooklm
aliases: [Notebook LM, NotebookLM, Audio Overview]
status: maintained
sources: [chat.txt]
updated: 2026-05-25
---

# NotebookLM (Google)

Google's research / corpus tool. Treat a curated set of documents as
the *only* source; ask questions; get answers with citations. The
chat has used it both as a generic research helper and as a vehicle
for **AI-indexed Torah**.

## What it is

`notebooklm.google.com` — free with a Google account. Upload up to
~200 sources per notebook (~500,000 words). Outputs:

- **Notes / answers** with inline citations to your sources.
- **Audio Overview** — a two-host podcast-style discussion of your
  sources. *"Interrupt"* lets you join as a third voice.
- **Video Overview** — same as Audio but with Nano Banana–generated
  illustrations. Released 2025-11-04. [chat 2025-11-04]
- **Slide deck** — convert sources to Google Slides. Released ~2026-01.

## The Rebbe's Torah notebook

The single most-shared NotebookLM link in the chat:

`notebooklm.google.com/notebook/8fd6b863-f304-4710-89fe-b080ddad1eef`

Sources include the Rebbe's *Likkutei Sichos*, *Igros Kodesh*, *Toras
Menachem*, *Maamarim*. First shared [chat 2026-02-06].

> *"This guy starts telling me things and I'm like 'the Rebbe said
> that?!' … I know the sicha! I never realized it was actually saying
> that! It's actually accurate."*
> — [chat 2026-02-06]

Other community notebooks:

- **Kinus AI Day 2025** sessions
  `notebooklm.google.com/notebook/9a39622b-9114-4cb0-86a3-4a06404490fd`
- **WhatsApp transcript of this group**
  `notebooklm.google.com/notebook/4a2c1656-c37f-4f77-bb5e-691f0768e994`
  and `ai4.shlch.us/notebook`.
- **Pesach research bundle** — `notebooklm.google.com/notebook/5f905078-…`

## What the chat uses it for

- **Shiur preparation** from Hebrew sichos — see [[../topics/shiur-prep]].
- **Likkutei Sichos search** with citation.
- **Audio overviews** of papers, articles, halacha pieces.
- **Voice-note refinement** — paste long voice-note transcripts; ask
  for cleanup. [chat 2025-11-27]
- **Cataloging &amp; titling** archives of audio/written content.
  [chat 2026-05-12]

## Strengths

- Citations are *real* — clickable, with anchor passages highlighted.
- Stays grounded in uploaded sources; refuses to extrapolate further.
- Free for personal use.
- Audio Overview is genuinely impressive output for the effort
  (one upload).

## Weaknesses

- **Source retrieval cap.** Pulls only ~10–12 sources per query no
  matter how many you upload. *"So having large notebooks of 250 sefarim
  is kinda useless unless you're doing a superficial broad search."*
  [chat 2026-03-23]
- **Hebrew video overviews** generate garbled images (gibberish
  Hebrew). [chat 2026-03-08]
- **Message limits** hit quickly on free tier when used heavily.
  [chat 2025-12-12]
- **Output length capped** — long synthesis falls off.

## The source-forcing prompt

[chat 2026-03-24]:

> *"Structure the prompt so that the minimal viable response will
> include the level of variety that you're looking for. I just
> searched for 100 insights into the yomtov of pesach and it provided
> from 109 different sources."*

i.e. if you ask for "10 insights", you get 10. Ask for "100", and the
retrieval engine has to broaden.

## Workflows worth saving

- **Hebrew sicha → English speech notes.**
  [chat 2025-09-22]. See [[../topics/shiur-prep]].
- **PDF book → podcast.** [chat 2025-11-18]: upload book → Audio Overview → done.
- **Group chat → searchable knowledge base.**
  [chat 2025-12-12] confirmed NotebookLM accepts WhatsApp exports.

## Related

- [[../topics/shiur-prep]]
- [[../themes/ai-and-torah-accuracy]]
- [[gemini]] — NotebookLM is Gemini-powered.
- [[maamorim-app]] — curated alternative.
