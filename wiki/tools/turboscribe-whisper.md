---
type: tool
slug: turboscribe-whisper
aliases: [Turboscribe, Whisper, MacWhisper, Pinpoint, Letterly]
status: draft
sources: [chat.txt]
updated: 2026-05-25
---

# Turboscribe / Whisper / MacWhisper / Pinpoint

The English-side transcription stack. Companion to [[sofer-ai]]
which leads on Hebrew/Yiddish.

## Whisper (OpenAI)

The underlying model many tools wrap.

- **Free via OpenAI API** for self-built workflows.
- **Best for English** but works on Hebrew and Yiddish too.
- *"Whisper models are the best. 11labs is also very good but more
  expensive. Parakeet models also very strong. All excellent for both
  Hebrew and English. Can work for Yiddish."*
  — [chat 2025-08-16]
- Used inside Hecher CRM and many DIY pipelines.

## Turboscribe

`turboscribe.ai` — Whisper-wrapped, bulk-friendly.

- **3 free transcriptions/day.**
- **$20/month for bulk** — *"the best deal I've found for bulk
  transcription. I've managed to transcribe hundreds of hours in a
  single month."* [chat 2026-05-12]
- Multilingual support.

## MacWhisper

Local Mac app running Whisper on-device.
`goodsnooze.gumroad.com/l/macwhisper`. One-time purchase.

> *"Good for heavy users."*
> — [chat 2025-11-28]

## Pinpoint (Google)

`recorder.google.com` (mobile) — also a desktop variant.

- Free.
- Up to 2 hours per file; **no limit on number of files**.
- Officially for journalists/students; in practice anyone can use it.
  [chat 2026-01-02]

## Letterly

Voice-to-text app. *"Rave reviews on accuracy."*
[chat 2026-02-15]

## Nvidia Canary / Parakeet

Free ASR models. Canary 180m was being tested for Hebrew/Yiddish
[chat 2026-01-11]. Strong for both Hebrew and English. Requires technical setup.

## ivrit.ai

`transcribe.ivrit.ai` — free Hebrew transcription.
[chat 2025-12-02, +972 53-463-1223]

## Workflow

1. Record (phone voice memo, Zoom, lavalier).
2. Pick the tool by language and budget.
3. Transcribe.
4. Hand transcript to [[claude]] for summarization / shiur outline /
   action-item extraction.

See [[../topics/transcription]] for the language-by-language decision
tree.

## Related

- [[sofer-ai]] — Hebrew/Yiddish leader.
- [[../topics/transcription]]
- [[../topics/shiur-prep]]
- [[meeting-tools]]
