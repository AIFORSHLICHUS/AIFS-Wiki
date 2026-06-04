---
type: conversation
slug: sora-demographic-workaround
aliases: [Sora burka thread, Sora prompt thread]
status: maintained
sources: [chat.txt]
updated: 2026-05-25
participants: []
date_range: 2025-11-19 to 2025-11-21
---

# The Sora Demographic-Prompt Workaround

A short, dense thread (~48 hours) that produced one of the chat's
most-reused prompt patterns. Generalizes beyond [[../tools/sora]] to
any image / video model with similar guardrails.

> **External context** — Sora has since been discontinued
> [external: user note, 2026-05-26]. This conversation is kept because
> the *clothing-and-context* technique applies to Grok video, Kling,
> Veo, Nano Banana, and every successor model with the same kind of
> demographic guardrails.

## The trigger

[chat 2025-11-20]:

> *"How do I get Sora to stop giving me women with burkas?"*

The shliach had been trying to generate a Shabbos-dinner scene; Sora
kept "playing it safe" by depicting women in head coverings that
didn't match the actual community the content was for.

## The breakthrough

Working it out in the thread, the canonical technique emerged:

> *"Use clothing and style descriptions. Instead of saying who the
> women are, describe what they're wearing and the context."*

Words **Sora blocks**:

- "Jewish women"
- "Caucasian women"
- "white women"
- "Jewish-looking"

Words **that work**:

- "Women wearing modern modest dresses, hair visible, celebrating at
  a Shabbat dinner table."
- "Women in contemporary casual clothing, smiling and talking while
  lighting Chanukah candles."
- "Women in long-sleeve dresses with natural hairstyles, participating
  in a Jewish holiday celebration."
- "A group of friends wearing smart casual party outfits at a festive
  Jewish event."

## The ready-to-use prompt

> *"Create a joyful Shabbat dinner scene with men and women gathered
> around a beautifully set table. Women are wearing modern modest
> dresses with hair visible and styled naturally. The atmosphere is
> warm, elegant, and festive."*

## Why it worked

Sora's guardrails fire on protected-attribute descriptors. They don't
fire on attire + context. By specifying *hair visible, no head
coverings, modern modest dresses, smart casual*, the model no longer
defaults to "safer" coverings.

Nuance from the thread: *"Chabad"* or *"Chasidic"* outperforms
*"modest"* which triggers tichel/burka imagery in the training data.

## Generalization

The lesson outlived Sora. The same pattern works on:

- **Grok video.**
- **Kling.ai.**
- **Veo.**
- **Nano Banana / Gemini image.**
- **ChatGPT image (GPT 5.2+).**

Any time a model refuses a benign demographic prompt, **rewrite as
attire + action + scene**.

## Related

- [[../tools/sora]]
- [[../resources/master-prompts]] — full ready-to-paste prompt block.
- [[../topics/flyer-design]]
- [[../topics/image-generation]]
