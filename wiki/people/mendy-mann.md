---
type: person
slug: mendy-mann
aliases: [Mendy Mann]
status: draft
sources: [chat.txt]
updated: 2026-05-25
---

# Mendy Mann

The chat's "use a script, not the AI" voice — and a deep
[[../tools/notebooklm]] user. Strong on the "patterns vs. data
processing" distinction.

## Editorial positions

> *"AI finds patterns fast, but use Python scripts for data processing
> (more reliable). Python codes can run through a million spreadsheets
> and create a new spreadsheet with all the results that you want in
> under a minute … if you have AI work on a spreadsheet for example
> and he does not understand you 1,000% correctly you can mess up your
> entire list and it will tell you and convince you that this is
> wonderful."*
> — [chat 2026-05-14]

> *"Keep programs locally, don't connect to banking, don't give file
> access. Use professional developer oversight before deploying."*
> — [chat 2026-01-11], on vibe-coded systems.

## Things he's done / contributed

- **JSON-description workflow for image consistency**
  [chat 2026-05-20]:
  > *"I found a video of Miami Boys Choir, I did the Google Lens and
  > I told it to describe it in detail in a JSON format. I
  > copy-pasted that into Gemini's Video Creator [for consistent
  > output]. 100% AI."*

  Generalizes: describe a reference image as JSON → paste JSON into
  the next generation → maintain style across a series.
- **Nano Banana fix** for quality loss on edits: *"remove background
  before editing, then add background back."* [chat 2025-12-03]
- **NotebookLM canary 180m flash** experiments for Hebrew/Yiddish
  transcription. [chat 2026-01-11]
- **Gemini Gems** clarifications — each Gem use creates a new chat;
  must name and pin to save. [chat 2025-12-29]

## Areas of expertise

- **Python-as-glue.** Treats LLMs as code generators for repeatable
  data work, not as data processors themselves.
- **Image consistency** across a series via structured prompts (JSON).
- **NotebookLM** internals and limits.
- **Vibe-coding risk literacy** — recurring voice on security.

## Style

Practical, careful, builds on what others post. Frequent
*"actually, here's what I tried and what worked"* contributions.

## Related

- [[../tools/notebooklm]]
- [[../tools/nano-banana]]
- [[../themes/vibe-coding]]
- [[../topics/flyer-design]]
