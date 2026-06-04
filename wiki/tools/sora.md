---
type: tool
slug: sora
aliases: [Sora, Sora 2, OpenAI Sora]
status: maintained
sources: [chat.txt]
updated: 2026-05-25
---

# Sora (OpenAI)

OpenAI's video-generation model. The chat's main video-gen workhorse
in late 2025, partially superseded by Grok and Kling.ai by 2026.

> **External context** — *Sora has since been discontinued.*
> [external: user note, 2026-05-26]. This page is preserved because
> the chat's prompt-engineering thread (the *clothing-and-context*
> workaround for demographic refusals) generalizes to Grok, Kling,
> Veo, and any future video model with similar guardrails. The Sora
> *technique* outlives Sora the *product*.

## What it is

`sora.chatgpt.com` (desktop) and mobile app. Generates short video
clips from prompts — natively under 8 seconds on mobile, longer on
desktop. Invite codes traded heavily in chat through Oct-Nov 2025.

## What the chat uses it for

- **Fundraising campaign videos** — short narrative clips.
- **Holiday social-media content.**
- **Educational videos** — shluchim demonstrated use for kids'
  programming. [chat 2026-05-07]

## The famous "demographic prompt" thread

[chat 2025-11-20]: tried to generate Jewish women lighting Shabbos
candles; Sora returned women in burkas. The fix, worked out in the
thread:

**Words Sora blocks**: *"Jewish women," "Caucasian," "white women,"
"Jewish-looking."*

**Words that work** — describe attire and context, not identity:

> *"Women wearing modern modest dresses, hair visible, celebrating at
> a Shabbat dinner table."*
>
> *"Women in contemporary casual clothing, smiling and talking while
> lighting Chanukah candles."*
>
> *"A group of friends wearing smart casual party outfits at a
> festive Jewish event."*

The nuance from the thread: *"Chabad"* or *"Chasidic"* tends to
outperform *"modest"* (which triggers tichel/burka imagery).

See [[../resources/master-prompts]] for the full ready-to-paste
prompt.

## Strengths

- Quality high enough for social-media use.
- Desktop version exceeds 8 seconds (mobile capped).
- Integrated with ChatGPT account.

## Weaknesses

- **Demographic guardrails** trip on benign Jewish content.
- **Length limits** on mobile.
- **Invite-only** for stretches.
- Output quality varies by run; expect to generate many and pick.

## Migration patterns

- [chat 2026-05-07]: user transitioned from Sora to **Grok** for
  educational videos.
- **Kling.ai** for animated videos longer than 10 seconds.
  [chat 2026-02-16]
- **Veo (Google)** mentioned as emerging alternative.
- **Synthesia / D-ID / HeyGen** for talking-avatar use.

## Related

- [[grok]]
- [[../topics/flyer-design]] — same demographic-prompt issue applies
  to image gen.
- [[../resources/master-prompts]]
