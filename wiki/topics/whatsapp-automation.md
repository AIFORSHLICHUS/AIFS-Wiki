---
type: topic
slug: whatsapp-automation
aliases: [whatsapp, mass messaging, broadcast, WABA, ClawdBot, Reach]
status: maintained
sources: [chat.txt]
updated: 2026-05-25
---

# WhatsApp Automation

Where the chat *lives* — and where the largest collection of
"things that worked until they didn't" sit.

## The state of play

**WhatsApp has gotten very good at detecting third-party automation,
and accounts are being disabled.**

> *"WhatsApp is very smart; can block you based on sending more than
> usual, even in legit use."*
> — [chat 2026-03-06]

> *"Many shluchim have taken it too far with Reach app and had their
> WhatsApp disabled."*
> — [chat 2026-03-13]

> *"Recently started glitching, account restricted twice."*
> — on WASender after 5 years of clean use, [chat 2025-12-04, +1 203-887-6044]

## Safe paths

- **WABA — WhatsApp Business API.** Official, paid, requires business
  phone + paid provider. The only path the chat trusts for real
  volume.
- **Regular broadcast lists** (not "mass send"). Manual but durable.
- **Personal-touch tools** like Reach for individualized messages — at
  low volume, with care.

## Risky paths

- **WASender** — historically worked; account-restriction risk now.
- **ClawdBot** — *"changed the world but has major security flaws."*
  Use **[[../tools/nanoclaw]]** instead.
- **Personal phone + AI bot.** Don't.

## What the chat does instead

- **Export the chat, analyze with AI.** A Selenium-based
  exporter [chat 2026-03-22] opens WhatsApp Web, logs in, exports by
  date range and contact. Lives on your machine.
- **WappMaster Contacts Extractor** Chrome extension. [chat 2026-05-09]
- **Group admin → console hack** for member lists [chat 2025-08-14]:
  - WhatsApp Web → click group name → see full participant list
  - Right-click → Inspect → Console
  - Paste a JS snippet to extract names → paste into Excel
  (Note: class names change; the snippet needs updating periodically.)

## Voice notes &amp; transcription

The fully kosher half of WhatsApp + AI:

- **Zapia** — *"Transcribed for me a 30-minute voice note in seconds."*
  [chat 2025-12-12]
- **TranscribeMe** — WhatsApp transcription app.
- **Sofer.ai** — WhatsApp integration on paid plan.
- **NotebookLM** — accepts WhatsApp voice-note transcripts; can run
  follow-up Q&amp;A.

## Personalized broadcast

- **Reach** — many shluchim use; personalizes messages with contact
  names. Carries some account risk.
- **Evant** — *"used by many shluchim; alternative to direct WhatsApp
  automation."* [chat 2026-02-27]
- **Chatbase** — WhatsApp bot builder. *"Good but a bit expensive."*
  [chat 2026-05-17, +39 340 359 5009]
- **Spreadsheet HYPERLINK formula** for one-tap
  personalized message links. The safest of all.
  [chat 2026-03-06]

## Recovering deleted messages

[chat 2026-05-07, +33 6 51 82 35 18]: *"Over Macrodroid there is a
script that saves all deleted messages on WhatsApp."* (Android.)

## Open issues

- **WABA cost / complexity** — official path is expensive enough that
  small shluchim avoid it.
- **Cross-platform identity** — same shliach, multiple WhatsApp
  identities (personal / family / Chabad House) is a recurring
  organization problem.
- **Encrypted backups** block direct file access; can't easily mine
  chat history without re-export.

## Related

- [[../tools/nanoclaw]]
- [[../tools/notebooklm]]
- [[crm-automation]]
- [[../themes/vibe-coding]]
