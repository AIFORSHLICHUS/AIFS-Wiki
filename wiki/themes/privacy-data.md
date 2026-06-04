---
type: theme
slug: privacy-data
aliases: [privacy, security, data sharing, AI training data]
status: draft
sources: [chat.txt]
updated: 2026-05-25
---

# Privacy &amp; Data Sharing

Where the chat oscillates between paranoia and pragmatism — and lands
somewhere in the middle.

## The recurring warnings

> *"They use your chat data to train their models."*
> — [chat 2025-12-27]

> *"If you have Gemini for Workspace, users cannot easily delete their
> chats … the admin can see all the chats."*
> — [chat 2026-05-07, +1 773-218-1108]

> *"I've found Gemini for nonprofit doesn't integrate into email the
> same way it does for regular account."*
> — [chat 2026-05-07, +1 347-225-1322]

## The pragmatic position

> *"We here have already sold our liberty to technology."*
> — [chat 2026-03-27]

The honest framing: most shluchim use Gmail, WhatsApp, ChatGPT,
ChabadOne, social media. Adding Gemini integration doesn't change the
threat model materially — it just makes it visible.

## Specific concerns the chat has surfaced

### Connecting AI to your full Gmail/Drive

[chat 2026-05-07, +1 508-314-5472]: *"Question is, is there any
reason for concern?"* No consensus; range from *"go ahead"* to
*"compartmentalize."*

### Vibe-coded apps with banking info

*"Keep programs locally, don't connect to banking, don't give file
access. Use professional developer oversight before deploying."*
[chat 2026-01-11]

### Password storage

[chat 2026-03-12, +1 438-526-6974]: *"Use a dedicated password
manager (Bitwarden, 1Password), not a spreadsheet. Zero-knowledge
architecture, AES-256 standard."*

### Workspace admin visibility

Managed Workspace accounts: the admin can see Gemini chat history;
users can't easily delete. Affects shluchim on org-wide accounts.

### Public Claude artifacts

The [iframe-into-ChabadOne workaround](../topics/chabadone-integration)
publishes the Claude artifact to a public URL. Fine for marketing
pages; not for anything with PII.

### Ethnicity-based marketing lists

[chat 2025-09-12, +1 415-634-7727]: real legal limit (Data Axle and
similar). Not just an AI guardrail. Mind-share required regardless of
which model you ask.

## Patterns that minimize exposure

- **In-browser, no server** vibe-coded apps. Nothing persists.
  Movers-referral-tool, my-charity-box, countomer all do this right.
- **MCP into vetted backends** instead of browser-automation against
  payment systems.
- **Forward sanitized data**, don't connect your full inbox.
- **Anonymize / aggregate before feeding to AI** when you can.
- **Sefer-style buffer layers** — curated corpus the AI can read,
  vetted summaries it can re-present.

## Open questions

- **Free-tier training opt-out** — works? doesn't? varies by vendor
  and changes silently.
- **Workspace Nonprofit Gemini** — different data-use policy than
  consumer? Unclear.
- **Encrypted WhatsApp backups** — block AI mining of personal chat
  data; good or bad?

## Related

- [[ai-and-shabbos]]
- [[vibe-coding]]
- [[../topics/whatsapp-automation]]
- [[../topics/crm-automation]]
