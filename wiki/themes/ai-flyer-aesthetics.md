---
type: theme
slug: ai-flyer-aesthetics
aliases: [flyer design debate, 7 ai tells, designer prompt]
status: maintained
sources: [chat.txt]
updated: 2026-05-25
---

# The "Looks Too AI" Debate

The most persistent design conversation in the group: AI can produce
visually impressive flyers in a minute, but a trained eye spots them
instantly. Why? And what does it take to make a flyer that looks
*intentionally human-designed*?

## The position split

**Pro-AI-for-flyers (most members):**

- *"AI can provide the base; humans polish."* Time-poor shluchim get a
  flyer in 10 minutes, not 10 days. Mendy Shishler, [chat 2026-02-11].
- *"If hiring a designer costs $600 and AI costs $0, the economics are
  not subtle."*

**Skeptical (vocal minority, esp. Mendel Super, +1 971-329-6661, Avi Winner):**

- *"Telltale AI flyer. The design is busy and all over the place. It
  might be easy to produce, but it's not good graphics."*
  — [chat 2026-02-11, Mendel Super]
- *"People want to hear *you*. They see AI, they see it's not you."*
  — [chat 2026-05-21, +1 971-329-6661]
- AI graphics shouldn't replace human designers any more than AI text
  should replace human writing.

## The 7 AI Tells

The canonical taxonomy, distilled by Mendy Shishler's master prompt
([chat 2026-02-11–12]) and refined by [chat 2026-04-20, +1 737-786-5770].
See [[../resources/designer-prompt]] for the full system prompt.

1. **No intent.** AI makes everything "nice" — nothing purposeful.
   Counter: one prompt → one visual idea statable in one sentence.
2. **Default symmetry.** AI centers everything. Counter: asymmetry is the
   default; symmetry must be earned (formal gala, solemnity).
3. **Everything shouts equally.** All elements weighted the same.
   Counter: one dominant read, one secondary, some things deliberately
   quiet.
4. **Fake type space.** AI leaves generic poster space. Counter:
   design around the *actual* text — exact placement, size ratios.
5. **Global polish.** AI smooths everything uniformly. Counter: specify
   imperfect directional lighting, material-specific textures, at least
   one deliberate flaw.
6. **Stylistic mush.** AI blends styles. Counter: name **one** design
   tradition (Swiss typographic, grassroots broadside, editorial food
   magazine, luxury invitation, brutalist, duotone, Japanese minimalist).
7. **Dead space vs. tense space.** AI either fills every pixel or leaves
   lifeless voids. Counter: empty space must have *tension* — a
   relationship to other elements.

## The Hebrew / RTL problem

Image-generation models still garble Hebrew letters and reverse
sentence order. Two workable patterns:

1. **Strip-and-replace.** Generate the flyer; tell the model to *remove
   the Hebrew letters without touching anything else*, leaving
   placeholders; type the Hebrew in [[../tools/canva]] yourself.
   [chat 2026-05-19, +44 7980-795936]
2. **Background-only.** Generate the visual background in
   [[../tools/nano-banana]] / [[../tools/gemini]], add all text in Canva.
   [chat 2025-11-20, Yisroel Chaim Shuchat]

Claude is "needs reminding to write RTL and keep sentence order" —
better than GPT for the *attempt* but still imperfect.
[chat 2026-05-19, +44 7980-795936]

## The workflow that actually wins

A pattern that recurs across many threads:

1. **Generate the prompt with one model.** Ask ChatGPT to write a
   detailed image-gen prompt including your brand colors, audience,
   event details.
2. **Generate the image with another model.** Paste into
   [[../tools/nano-banana]] (Google AI Studio) for the strongest visual
   output.
3. **Edit text and details in [[../tools/canva]].** Magic Layers (new
   feature, [chat 2026-03-08, Mendy Shishler]) decomposes flat AI
   images into editable elements.
4. **Optional: Adobe Firefly / [[../tools/canva]] to import as editable.**

[chat 2026-04-25, +1 716-262-2106] template prompt for redesigning an
uploaded flyer:

> *"Redesign it with a strong visual upgrade while keeping the core
> content intact. Modernize the layout, improve typography, spacing,
> and alignment, and create a clear visual hierarchy. Refine the color
> palette for a more cohesive and striking look. Reduce clutter, enhance
> readability, and add subtle design elements where needed."*

## Open problems

- Generating multiple **consistent** images for a series. Workaround:
  describe a reference image in JSON detail (via Google Lens), paste
  the JSON into each successive generation. [chat 2026-05-20, Mendy Mann]
- AI **can't see what it generated**, so edits revert to defaults.
  [chat 2026-03-20, Elazar Green]
- Chabad-specific iconography fails reliably: menorah arm count,
  Luchos shape, kippah/long-sleeve consistency. Yossi Yaffe and others
  are working on a "Chabad image skill" custom Gem.
  [chat 2026-05-19, +1 972-58-685-1038]

## Related

- [[../resources/designer-prompt]] — the full system prompt.
- [[../topics/flyer-design]] — workflow page.
- [[../tools/nano-banana]]
- [[../tools/canva]]
- [[../tools/chatgpt]]
