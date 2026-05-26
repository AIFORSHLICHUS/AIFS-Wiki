---
type: topic
slug: flyer-design
aliases: [flyers, posters, event graphics, ad design]
status: maintained
sources: [chat.txt]
updated: 2026-05-25
---

# Flyer Design

The single most discussed practical use case in the chat. Every shliach
makes flyers — Shabbos, Yomim Tovim, dinners, programs — and the chat
has been steadily codifying a workable AI workflow.

## Why it's hard

See [[../themes/ai-flyer-aesthetics]] for the *7 AI Tells*. The short
version: AI image models center everything, polish everything, blend
styles, fake the type space. They also garble Hebrew. And they can't
*see* what they just generated, so each edit drifts.

## The current best-practice workflow

Synthesized from many threads (~30 chat messages between
[2025-08-26, Mendy Shishler] and [2026-05-19, +1 737-786-5770]):

1. **Brief in natural language.** What is this for, who's the audience,
   what mood, what text *exactly*, what brand colors, what size.
2. **Have one model write the prompt for another.** Ask ChatGPT to turn
   the brief into a detailed image-gen prompt that names a single design
   tradition (Swiss typographic, grassroots broadside, editorial
   magazine, luxury invitation, etc.). Optionally use the system prompt
   in [[../resources/designer-prompt]].
3. **Generate in [[../tools/nano-banana]] / Google AI Studio.** Highest
   visual quality, best at not garbling text on first pass. (GPT 5.2's
   image model is now competitive — [chat 2026-01-21, Mendy Shishler].)
4. **Strip the Hebrew before editing.** Tell the model: *remove the
   Hebrew letters, leave placeholders, change nothing else*.
   [chat 2026-05-19, +44 7980-795936]
5. **Open in [[../tools/canva]] with Magic Layers.** Magic Layers
   decomposes the flat AI image into editable elements — fix text,
   swap typography, adjust spacing. [chat 2026-03-08, Mendy Shishler]
6. **Type the Hebrew yourself** in Canva (or Affinity), where you
   control the font.
7. **Optional: vision-check.** Upload the result back to ChatGPT and ask
   it to identify the remaining AI tells. [chat 2026-03-16, Mendy Shishler]

## The "Designer prompt" pattern

The single most-cited prompt asset in the chat —
see [[../resources/designer-prompt]]. Frames the LLM as a "senior
graphic designer with 15+ years designing real print and digital
campaigns" who outputs *one copy-paste-ready prompt for an image
generator*, refusing to drift into AI defaults.

## Easier-than-Photoshop workflows

| Workflow | What it's good for |
| --- | --- |
| ChatGPT brief → Nano Banana → Canva text | Default. Most flyers. |
| ChatGPT brief → ChatGPT image (GPT 5.2) → Canva polish | When you want one tool. |
| Grok batch generation → hand-pick → Canva | When other models refuse demographic descriptors. |
| Upload an existing flyer → "Redesign it with a strong visual upgrade while keeping the core content" → Nano Banana | For modernizing tired templates. [chat 2026-04-25, +1 716-262-2106] |
| Upload reference images + brand colors + sample event flyers | Custom GPT / Gem path for repeated brand consistency. [chat 2026-02-11, Yisroel Chaim Shuchat] |

## Sora and demographic prompts

Sora and other video/image models block prompts naming demographics
("Jewish women", "Caucasian", "Jewish-looking"). The workaround:

> *"Describe what they're wearing and the context, not who they are.
> 'Women wearing modern modest dresses, hair visible, celebrating at a
> Shabbat dinner table.' These prompts are completely allowed."*
> — [chat 2025-11-20, Rabbi Chaim Lazaroff & Mordechai Lightstone]

Words to avoid: *Jewish*, *Caucasian*, *Jewish-looking*. Words that
work: *modern modest dresses, hair visible, no head coverings, smart
casual, Chabad-style, Chasidic*. "Chasidic" tends to outperform "modest"
(which triggers tichel/burka imagery).

## Chabad-specific iconography that still fails

- **Menorah arm count.** Both 7-arm (Beis HaMikdash) and 9-arm (Chanukah)
  consistently wrong. Mordechai Lightstone tests this regularly.
- **Luchos shape.** Tablets come back curved-top instead of square.
- **Kippah / long-sleeve consistency.** Get one figure right, others drift.
- **Hebrew text.** See above.

There's an in-progress "Chabad image skill" custom Gem mentioned at
[chat 2026-05-19, +1 972-58-685-1038], but no public system prompt yet.

## Reference image / template sources

- `shluchim.koshergraphics.com` — flyer template library
- `shlichusmarket.com` — paid templates
- `chabadbrand.com` — brand guideline assets
- Squarespace + ChabadBrand templates for full-site projects
  (examples: `chabadfortwayne.com`, `jewishchagrinfalls.com`)

## Related

- [[../themes/ai-flyer-aesthetics]] — full theory.
- [[../resources/designer-prompt]] — the prompt itself.
- [[../tools/nano-banana]]
- [[../tools/canva]]
- [[../tools/chatgpt]]
- [[../topics/chabadone-integration]] — once you have the flyer, deploy it.
