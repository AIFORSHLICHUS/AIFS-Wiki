---
type: topic
slug: image-generation
aliases: [images, AI images, photo generation]
status: maintained
sources: [chat.txt]
updated: 2026-05-25
---

# Image Generation (Beyond Flyers)

Separate from [[flyer-design]] (which is the specific event-graphic
use case). This page covers image gen as a general technique —
illustrations, infographics, social posts, logos, photo editing.

## The standard tool ranking

| Use | Tool |
| --- | --- |
| Realistic backgrounds &amp; high-res output | **Nano Banana / Nano Banana Pro** |
| Editing existing photos | **Grok** or **Google Photos AI** |
| Logos &amp; brand marks | Nano Banana → ChatGPT for refinement |
| Infographics | **ChatGPT** (post-5.2) — *"way better than Gemini"* [chat 2025-12-24] |
| Storybook illustrations | **Gemini Storybook** |
| Multi-image consistent series | JSON-description workflow (see below) |
| Upscaling | **Upscayl** / **Upscale.media** / Canva Pro upscale via Affinity |
| Background removal | **Canva** Magic Erase |

## The consistency workflow (JSON method)

[chat 2026-05-20]:

1. Run Google Lens on a reference image / video.
2. Ask it to describe in *JSON* — every visible detail, style, color,
   composition.
3. Paste the JSON as the prompt input to the next generation.
4. Maintain style across a series.

Generalization: *describe what you want in structured form, then
generate from the structure*.

## Photo editing

- **Grok** — *"good for photo editing/manipulation."*
  [chat 2025-12-19, +1 805-668-1024]
- **Google Photos AI** — built-in edits.
- **Adobe Firefly** — convert flyers to editable Canva files.
- **BoxBrownie** — photo editing service. [chat 2026-01-12]

## What still fails

See [[../themes/ai-flyer-aesthetics]] for the *7 AI tells* —
applies to images generally.

Chabad-specific iconography that consistently breaks:

- **Menorah arm count** — 7 vs. 9.
- **Luchos shape** — curved vs. squared.
- **Long sleeves / kippot** consistency across figures.
- **Hebrew text** — see [[hebrew-yiddish]].

Workarounds for some: a Chabad-image custom Gem is in progress
([chat 2026-05-19, +1 972-58-685-1038]). Until then, generate the
visual, fix the iconography manually.

## Inserting people / faces consistently

[chat 2026-05-04, +1 650-667-9556]:

> *"What's the best prompt to have ChatGPT not change the photos when
> inserting into a pamphlet/flyer? Sometimes it listens, other times
> it changes the faces."*

Answer: *"Just take the image, draw on it, and circle the area that
should remain unchanged."*

## Related

- [[flyer-design]]
- [[../tools/nano-banana]]
- [[../tools/canva]]
- [[../themes/ai-flyer-aesthetics]]
