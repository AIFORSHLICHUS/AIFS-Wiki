---
type: person
slug: elazar-green
aliases: [Elazar Green, Elazor Green]
status: maintained
sources: [chat.txt]
updated: 2026-05-25
---

# Elazar Green

Builder of **Hecher CRM** — the chat's leading example of an
AI-native CRM with voice-note → action pipelines.

## What Hecher does

[chat 2026-05-03, 2026-05-15]:

> *"I built this for the Hecher CRM. Basically I use GPT (Whisper I
> think it's called) to transcribe and Claude to follow instructions
> [to draft emails, add calendar items, and update CRM records from
> voice notes]. We do exactly that with Hecher through MCP connection."*

End-to-end:

1. Record voice note (WhatsApp or phone memo).
2. Whisper transcription.
3. Claude reads transcript with system prompt about your CRM schema.
4. Claude calls Hecher MCP server: adds contact, adds calendar event,
   drafts follow-up email.

In beta with ~80 shluchim as of 2026-05.

## Other contributions

- **passover.jewishdips.com** (Pesach concept site) — built with
  Claude, inspired by Didy Waks. [chat 2026-03-19]
- **WhatsApp export scripts** in conversation with Meir Sudak.
- **CiviCRM integration debugging** — *"Spent a number of hours trying.
  Claude and Zapier were convinced it was possible. But it just was
  not working with my CiviCRM."* [chat 2026-03-29]
- **Security thinking** — open about which approaches work and which
  break.

## Editorial positions

> *"It doesn't remember what it just generated, but you asked for
> yarmulkahs, so it did its best guess."*
> — [chat 2026-03-20], on ChatGPT image-gen drift between edits.

> *"It is like an agent working on your computer, in your browser."*
> — describing Claude Dispatch in the CRM context.

## Style

Builder; reports what worked and what didn't with honesty. Doesn't
oversell. Mostly works in production code (not pure prompts).

## Areas of expertise

- **MCP integration** between Claude and arbitrary CRMs.
- **Voice → action workflows** at scale.
- **CRM architecture** specifically for Chabad needs.
- **Honest debugging** — calls out where Claude and Zapier were both
  wrong.

## Related

- [[../tools/crm-tools]] — Hecher's place in the CRM landscape.
- [[../topics/crm-automation]]
- [[../tools/claude]]
- [[didy-waks]]
- [[meir-sudak]]
