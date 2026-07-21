# AIFS-Wiki — Schema

This repository is an **LLM Wiki** built from the WhatsApp chat export of
**AI for Shlichus (Shluchim)** — a group of Chabad emissaries (shluchim)
discussing AI tools, prompts, and use cases for shlichus work.

The pattern is Andrej Karpathy's "LLM Wiki" (see
https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): a
persistent, compounding markdown knowledge base sitting between the
LLM and raw source material. Knowledge accumulates here instead of
being re-derived on every query.

## Three layers

1. **`raw/`** — immutable sources. The chat export (`raw/chat.txt`) and
   contact `.vcf` files. Read-only. Anything pasted in here by the user
   (new screenshots, transcripts, drops) is fair game for ingest but
   must never be edited by the LLM.
2. **`wiki/`** — LLM-owned markdown. Entity pages, tool pages, themes,
   conversation summaries, the index, and the log. The LLM creates,
   updates, cross-links, and lints these freely.
3. **This file (`CLAUDE.md`)** — the schema. Describes conventions and
   workflows.

## Directory layout

```
raw/                      # source documents (immutable)
  chat.txt                # WhatsApp export
  *.vcf                   # contact cards from the export
wiki/
  index.md                # content catalog (every page, one-line summary)
  log.md                  # append-only chronological log of operations
  tools/                  # one page per AI tool / product / GPT
  people/                 # one page per substantive contributor
  topics/                 # use-case topics (e.g. shiur-prep, OCR)
  themes/                 # cross-cutting themes (e.g. halacha-and-ai)
  resources/              # static resources: prompts, links, datasets
  conversations/          # summaries of notable threads from the chat
```

Filenames are lowercase-kebab. Person pages use full name:
`wiki/people/mendy-shishler.md`. Tool pages use the tool's canonical
slug: `wiki/tools/berel-me.md`.

## Page conventions

Every page starts with YAML frontmatter:

```yaml
---
type: tool | person | topic | theme | resource | conversation
slug: <kebab-case-slug>
aliases: [other names]
status: stub | draft | maintained
sources: [chat.txt, ...]   # raw files this page draws from
updated: YYYY-MM-DD
---
```

After frontmatter:

1. **One-paragraph TL;DR** — what this is and why it matters in the
   chat's context.
2. **Body sections** appropriate to the type (see below).
3. **Cross-references** — wiki-links like `[[tools/berel-me]]` or plain
   relative paths `[Berel.me](../tools/berel-me.md)`.
4. **Citations** — every non-obvious claim gets a citation back to a
   chat message with date and sender:
   `[chat 2025-08-12, Mendy Shishler]`.

### Type-specific sections

- **tool**: What it is · Who uses it · How they use it · Links · Notable
  threads · Limitations / open questions
- **person**: Role / bio (only what's evident from the chat) · What
  they've shared or built · Their take on AI · Notable threads
- **topic** (use case): Problem · Tools used · Prompts / workflows ·
  Notable threads · Open questions
- **theme**: Framing · Positions taken · Tensions · Notable threads
- **resource**: What it is · Source · Why it's useful
- **conversation**: Date range · Participants · TL;DR · Resolution · Why
  it's worth preserving · Links to the messages

## Citation format

The wiki has **two** citation kinds, and they look different on purpose.

### `[chat …]` — what the group actually said

The primary source. Cite chat messages inline like this:
> "If you want a clean Chassidus shiur, NotebookLM is unbeatable."
> — [chat 2025-09-14, Yisroel Chaim Shuchat]

For longer quotes, blockquote with a single citation line below. When a
claim is supported by multiple messages, list them comma-separated.

### `[external …]` — sparing real-world annotations

The chat is the source of truth, but the chat is also stale on
fast-moving tool reality. When a chat claim has been **superseded by
events** (product discontinued, model deprecated, company acquired,
pricing changed) and a reader acting on the chat alone would be
misled, add a short `[external …]` annotation.

Rules:

1. **Only when it matters.** Don't pad pages with web trivia. A model
   getting a new minor version is noise; a product being discontinued
   is signal.
2. **Don't replace chat citations** — *layer* on top of them. The chat
   said X at the time; reality is now Y; the page shows both.
3. **Cite the source explicitly.** `[external: vendor announcement,
   2026-04-12]`, `[external: user note]`, `[external: <reliable URL>]`.
   Never paraphrase generic web content without attribution.
4. **Flag uncertainty.** If you're not sure, say *"external context
   uncertain — needs verification"* and add to the lint backlog in
   `log.md`. Better stale-and-honest than confidently wrong.
5. **Don't import unrelated reference material.** If a tool's Wikipedia
   page has 5,000 words of trivia, the wiki doesn't need them. We
   want the chat's voice plus the real-world correction, not a
   secondhand encyclopedia.

Example:

> *"I've been using Sora the last five-six months to create educational
> videos. Recently transitioned to Grok."*
> — [chat 2026-05-07]
>
> [external: per user note, Sora was discontinued — context for any
> shliach still using older threads.]

## Operations

### Ingest

When new source material lands in `raw/` (or the user pastes a snippet):

1. Read the source end-to-end (chunk and parallelize if large).
2. For each item worth a page, create or update the entity page.
3. Touch every related page — tools mentioned, people quoted, themes
   advanced, conversations summarized.
4. Update `wiki/index.md` (catalog).
5. Append a log entry to `wiki/log.md`:
   `## [YYYY-MM-DD] ingest | <source name>` followed by what was
   created / updated.

### Query

When the user asks a question:

1. Read `wiki/index.md` first to find candidate pages.
2. Drill into relevant pages; pull citations from them.
3. Synthesize an answer with citations.
4. If the answer is substantive (a comparison, a recommendation, an
   analysis), **file it back as a new page** under
   `wiki/topics/` or `wiki/conversations/` and add it to the index +
   log. Don't let good synthesis evaporate into chat history.

### Lint

Periodically (or when asked):

- Contradictions across pages → flag in a "Tensions" section.
- Stale claims superseded by a newer message → update + note prior
  position with a date.
- Orphan pages (no inbound links) → either link them in or merge them.
- Concepts mentioned often in the chat but lacking a page → create one.
- Index entries that no longer match the page → fix.

Log every lint pass with:
`## [YYYY-MM-DD] lint | <scope>`

## Style

- Be terse. The chat is the source of truth — this wiki indexes,
  cross-references, and synthesizes; it does not narrate.
- Cite real chat messages. Don't invent quotes. If something isn't in
  the chat, don't put it in the wiki.
- Use the chat's own vocabulary (Chabad / Lubavitch terms like
  *shliach*, *farbrengen*, *mivtzoim*, *shiur*, *bochur*) without
  glossing unless context demands it.
- English is the primary language. Hebrew / Yiddish / Loshon Kodesh
  terms appear inline as-is; transliterations follow the chat's usage.
- No marketing voice. This is a working reference, not a brochure.

## Log entry prefix

Use this exact prefix so `grep '^## \[' wiki/log.md | tail` gives the
recent timeline:

```
## [YYYY-MM-DD] <op> | <subject>
```

Where `<op>` is one of `ingest`, `query`, `lint`, `seed`.
