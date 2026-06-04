---
type: theme
slug: llm-wiki-pattern
aliases: [Karpathy LLM Wiki, the meta-pattern, knowledge base]
status: maintained
sources: [chat.txt, https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f]
updated: 2026-05-25
---

# The Karpathy LLM Wiki Pattern

The meta-theme. **This wiki itself is an instance of the pattern it
describes** — a persistent, compounding markdown knowledge base
sitting between an LLM and raw source material.

## The pattern (Karpathy, 2026)

Andrej Karpathy's *LLM Wiki* gist proposes a paradigm shift away
from "upload-and-RAG-at-query-time" toward **incrementally building
and maintaining a structured markdown wiki**:

- **Raw sources** are immutable. The LLM reads them but doesn't
  modify them.
- **The wiki** is LLM-owned markdown — entity pages, syntheses,
  cross-references. The LLM writes; you read.
- **The schema** (`CLAUDE.md` here) tells the LLM the structure and
  workflows. Without it, the LLM is a generic chatbot.

Three operations: **ingest** (read new sources, update affected
pages), **query** (synthesize answers, file good ones back), **lint**
(catch contradictions, stale claims, orphans).

Key file: `index.md` — the catalog, organized by category. Read first
before any query. Bridges the LLM into the corpus without embeddings
or RAG infra.

Key file: `log.md` — append-only chronological record. Prefix entries
so unix tools can parse: `grep "^## \[" log.md | tail`.

## Why this corpus matters to the pattern

This wiki was bootstrapped from a single WhatsApp export
(`raw/chat.txt`, ~7,431 messages, 10 months). The chat itself
*discusses* AI tools at length but doesn't catalog them; queries
across the chat by hand take forever; the same questions get asked
quarterly.

The wiki:

- Catalogs every tool the chat has named.
- Carries forward the consensus (what works) without losing the
  dissent (design skeptics' flyer critique, community vibe-coding
  warnings).
- Makes the chat *queryable* in a way the chat isn't.
- Compounds — new chat snapshots ingest into the existing structure
  rather than starting over.

## The pattern's role in shlichus

> *"The tedious part of maintaining knowledge bases isn't reading or
> thinking — it's bookkeeping. … Humans abandon wikis because
> maintenance burden grows faster than value. LLMs don't bore, don't
> forget updating cross-references, touch 15 files in one pass."*
> — Karpathy's gist.

Shluchim are exactly the audience this serves: small organizations
with one-person ops teams, who hit a maintenance ceiling on every
template, every CRM, every operations doc. The LLM Wiki pattern
collapses that ceiling.

It's also the pattern that *the apps in this wiki* increasingly
implement:

- **[[../tools/maamorim-app]]** — curated corpus, AI re-presents.
- **[[../tools/dach-dev]]** — plain-text canon, paste into your LLM.
- **[[../tools/notebooklm]] with the Rebbe's Torah** — Karpathy's
  pattern applied to Chassidus.
- The in-progress **9 principles for AI Torah citation**
  ([[../conversations/torah-accuracy-debate]]) is essentially a schema
  for a Torah wiki.

## Limits of the pattern

- **The wiki gets stale** when the raw sources are stale. This wiki
  has fast-moving tool reality drifting from underneath it; see the
  `[external]` citation pattern in `CLAUDE.md`.
- **The pattern asks for discipline.** Without periodic *lint* passes,
  it accumulates contradictions and dead links.
- **It doesn't replace primary sources.** The chat is still the
  source of truth; the wiki indexes and cross-references.

## Related

- [[../about]]
- [[../log]] — every ingest/lint operation noted here.
- Karpathy's gist:
  `https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f`
