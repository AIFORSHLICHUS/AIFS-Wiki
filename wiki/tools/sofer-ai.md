---
type: tool
slug: sofer-ai
aliases: [Sofer.ai, sofer]
status: maintained
sources: [chat.txt]
updated: 2026-05-25
---

# Sofer.ai

Transcription tool specialized for Jewish content. The community's
default for *shiurim* with mixed Hebrew / Yiddish / English.

## What it is

`sofer.ai` — speech-to-text optimized for *limudei kodesh* vocabulary
and the language-switching common in shiurim. Free tier; paid plans for
bulk; WhatsApp transcription integration.

## What the chat uses it for

- **Transcribing shiurim** — the canonical recommendation. *"Excellent
  for transcribing shiurim."* [chat 2025-08-20, +380 63 770 4111]
- **Yiddish audio.** Best of the mainstream options for Yiddish, though
  not perfect — *"I give it a 6/10."* [chat 2025-11-05, Yossi Lipskier]
- **Mixed English/Hebrew/Yiddish** — *"It's really good at transcribing
  audio that has mixed English Hebrew Yiddish."*
  [chat 2026-04-22, +1 347-249-2983]
- **WhatsApp voice notes** — via WhatsApp transcription option on the
  paid plan. [chat 2025-12-10]

## The shiur → summary pipeline

The standard flow [chat 2026-05-20, +1 917-620-7220]:

> *"Uploaded a shiur I gave on פת הבאה בכסנין to sofer.ai. I took the
> transcript and asked Claude to summarize it and make it into a nice
> one-page PDF."*

1. Record the shiur (phone voice memo is fine).
2. Upload to Sofer.ai → transcript.
3. Paste transcript into [[claude]].
4. Prompt: *"Summarize this shiur and produce a printable one-page
   PDF."*
5. Iterate (longer, shorter, focus on specific points).

See [[../topics/shiur-prep]] for the full pipeline.

## Strengths

- Best-in-class Hebrew + Yiddish + English code-switching.
- Recognizes Torah-specific vocabulary that Whisper sometimes garbles.
- Free tier exists.

## Weaknesses

- Yiddish quality plateaus around 6/10; transcript editing still
  required for serious use.
- Paid plan needed for bulk.

## Alternatives

| Tool | When to prefer |
| --- | --- |
| **transcribe.ivrit.ai** | Free Hebrew-only transcription. |
| **Whisper / MacWhisper** | English-heavy; you control the API/local model. |
| **Turboscribe** | $20/mo bulk transcription for English-dominant audio. |
| **Pinpoint (Google)** | Free, up to 2 hours per file. |
| **Captions.AI** | Adds subtitles to video at $11/mo; works for Hebrew. |

See [[../topics/transcription]] for the full landscape.

## Related

- [[../topics/transcription]]
- [[../topics/shiur-prep]]
- [[../topics/hebrew-yiddish]]
- [[claude]] — for the summarization step.
