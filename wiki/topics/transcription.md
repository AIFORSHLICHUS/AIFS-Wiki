---
type: topic
slug: transcription
aliases: [audio transcription, voice to text, meeting notes, shiur transcription]
status: maintained
sources: [chat.txt]
updated: 2026-05-25
---

# Transcription

One of the most reliable wins from AI for shluchim: **record once,
transcribe, hand the text to an LLM, get back a shiur outline / email
draft / summary / blog post.**

## The decision tree

| Use case | Tool |
| --- | --- |
| Hebrew / Yiddish shiur | [[../tools/sofer-ai]] |
| Hebrew only, free | `transcribe.ivrit.ai` |
| English meeting (Zoom) | Zoom AI Companion (built-in, free with paid Zoom) |
| English meeting (not Zoom) | Fathom (free for Zoom); Granola (offline); Read.ai |
| English long-form (lectures, podcasts) | Turboscribe ($20/mo bulk); MacWhisper (Mac, heavy use) |
| Voice notes → text on phone | Wispr Flow (voice-to-text with snippet templates) |
| API / scripting | OpenAI Whisper; Nvidia Parakeet |
| Real-time, multilingual | Otter.ai (but aggressive contact permissions); Upmeet; Fireflies |

## The tools

### [[../tools/sofer-ai]]

Best for Jewish content with mixed languages. [chat 2026-04-22, +1 347-249-2983]:
*"It's really good at transcribing audio that has mixed English Hebrew
Yiddish."* Has WhatsApp integration ([chat 2025-12-10]). Free tier
exists; paid for bulk.

### Turboscribe

Best $/hour for bulk English. [chat 2026-05-12]:
*"Free for three transcriptions per day and $20/month for bulk files.
It's the best deal I've found for bulk transcription. I've managed to
transcribe hundreds of hours in a single month."*

### Whisper (OpenAI)

The underlying model many tools wrap. [chat 2025-08-16]:
*"Whisper models are the best. 11labs is also very good but more
expensive. Parakeet models also very strong. All excellent for both
Hebrew and English. Can work for Yiddish."*

Used by:
- Hecher CRM (Whisper → Claude → CRM update).
- [chat 2026-05-20]: *"Claude directed me to use whisper to scrape and
  rename my Gemara classes."*

### Zoom AI Companion

Free with paid Zoom. [chat 2025-11-17, Nosson Potash]: *"Zoom AI
assistant is very good… summary and list of tasks."* Custom summary
templates available — most users haven't customized them.

### Granola, Fathom, Read.ai, Fireflies, Otter.ai

The meeting-transcription pack. Tradeoffs:

- **Fathom** — free for Zoom; well-liked. [chat 2026-04-19, Shmulie Cunin]
- **Granola** — offline-capable; free trial. [chat 2025-11-17]
- **Read.ai** — auto-joins every Zoom/Teams meeting on calendar.
  [chat 2026-05-13]
- **Otter.ai** — works for in-person; **warning**: aggressive
  contact-permission requests, will try to spam your address book.
  [chat 2025-11-17]
- **Fireflies** — auto-joins meetings on calendar; can attend two
  simultaneously. [chat 2025-08-05]

### Wispr Flow

Voice-to-text *keyboard replacement*. Pre-saved templates ("snippets")
auto-expand. [chat 2026-04-27]: *"voice to text with ai —
you can add snippets meaning you can have pre-written templates."*
Mobile only on Android via waitlist as of [2026-02-15].

### MacWhisper

Local Mac app for heavy use. [chat 2025-11-28]:
*"goodsnooze.gumroad.com/l/macwhisper"*. One-time purchase, runs Whisper
on your machine.

### Pinpoint (Google)

Free transcription up to 2 hours per file, technically for
journalists/students but no limit on number of files.
[chat 2026-01-02]

## The standard workflow

1. Record audio (any way).
2. Run through your chosen transcription tool.
3. Paste transcript into Claude (or NotebookLM).
4. Prompt: one of
   - *"Summarize this shiur and produce a one-page printable PDF."*
   - *"Extract action items, follow-ups, and people to contact."*
   - *"Organize this into a 60-minute shiur with discussion questions."*
5. Iterate.

## Special cases

### Multilingual meetings

For Spanish/Hebrew/English mixed meetings: Fireflies.ai and Upmeet
both claim mixed-language support. No one in the chat has tested
exhaustively — partially unresolved. [chat 2026-02-06]

### Hebrew shiur with English Q&amp;A

[[../tools/sofer-ai]] handles this best. Whisper handles it OK if
you specify the language as "auto" rather than locking it.

### Voicemails

Several users automate: voicemail → email transcription → Claude
extracts action items → write to CRM. Hecher CRM has this end-to-end
for its ~80 beta users.

## Open questions

- Best **voicemail → action items → calendar event** without a
  bespoke build. Mostly DIY today.
- A **simple shiur → printable summary** packaged tool. Possible
  community project.
- Yiddish transcription beyond ~6/10 quality.

## Related

- [[../tools/sofer-ai]]
- [[../tools/notebooklm]]
- [[hebrew-yiddish]]
- [[shiur-prep]]
- [[crm-automation]]
