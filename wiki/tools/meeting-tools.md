---
type: tool
slug: meeting-tools
aliases: [Fireflies, Otter.ai, Granola, Read.ai, Fathom, Zoom AI Companion]
status: maintained
sources: [chat.txt]
updated: 2026-05-25
---

# Meeting-Transcription Tools

Reference page for tools that auto-join meetings, transcribe, and
summarize. Sister page to [[../topics/transcription]] for the
language-by-language picture.

## The lineup

| Tool | Strength | Watch out |
| --- | --- | --- |
| **Zoom AI Companion** | Free with paid Zoom; custom summary templates; the chat's default. [chat 2025-11-17, Nosson Potash] | Zoom-only. |
| **Fathom** | Free for Zoom; well-liked. [chat 2026-04-19, Shmulie Cunin] | Zoom-only. |
| **Fireflies.ai** | Auto-joins all Zoom/Meet meetings on calendar; transcribes + summarizes. Can attend two simultaneously. [chat 2025-08-05, Yonatan Azrielant] | Paid tiers for serious use. |
| **Granola** | Offline-capable; free trial. [chat 2025-11-17] `go.granola.ai/node8` | Less integrated than Fireflies. |
| **Read.ai** | Auto-joins every Zoom/Teams meeting on calendar; very comprehensive. [chat 2026-05-13] | Creates semi-automatic account; check permissions. |
| **Otter.ai** | Works for in-person meetings. | **Aggressive contact-permission requests**; will try to spam your address book. [chat 2025-11-17, Mordechai Lightstone] |
| **Upmeet** | Understands mixed languages and Torah concepts. [chat 2026-02-06] | Less known in chat; recommended for multilingual. |
| **Plaud** | Recording device + app; works for some. [chat 2026-05-13] | Hardware purchase. |

## The standard workflow

1. Auto-record meeting (Zoom AI / Fireflies / Read.ai).
2. Get transcript + auto-summary.
3. Pipe transcript into [[claude]] for: action items, follow-ups,
   donor notes, calendar events, draft emails.
4. (Optional) Push to CRM via MCP / API. See
   [[../topics/crm-automation]].

## Hecher's voice-note pipeline

[[../people/elazar-green]]'s Hecher CRM does this end-to-end:

> *"GPT/Whisper transcription + Claude instructions to draft emails,
> add calendar items, and update CRM records from voice notes."*
> [chat 2026-05-03]

## Multilingual meetings (Spanish / Hebrew / English)

Unresolved as of chat window. Fireflies and Upmeet claim mixed-language
support; no one in the chat has tested exhaustively.
[chat 2026-02-06]

## Privacy notes

- Otter.ai's contact-permission grab is a red flag.
- Anything auto-joining your calendar sees every meeting; configure
  before enabling.
- Workspace-managed accounts: admin can see transcripts.

## Related

- [[../topics/transcription]]
- [[../topics/crm-automation]]
- [[sofer-ai]] — for Hebrew/Yiddish shiur audio.
- [[../tools/notebooklm]] — for post-meeting synthesis.
