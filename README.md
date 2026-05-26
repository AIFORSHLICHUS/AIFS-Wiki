# AIFS-Wiki

A persistent, compounding knowledge base built from the **AI for
Shlichus (Shluchim)** WhatsApp group — Chabad shluchim sharing AI
tools, prompts, and use cases for shlichus work.

Built on Andrej Karpathy's [LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
pattern. The chat lives in `raw/`. The wiki — entity pages for every
tool, person, topic, and theme — lives in `wiki/`. The schema and
workflows are in [`CLAUDE.md`](./CLAUDE.md).

## Start here

- [`wiki/index.md`](./wiki/index.md) — full catalog of pages
- [`wiki/log.md`](./wiki/log.md) — chronological log of ingests and
  lint passes
- [`CLAUDE.md`](./CLAUDE.md) — how the wiki is organized and maintained

## Working with it

Open in Obsidian (or any markdown editor). Hand new sources to your
LLM agent (Claude Code, OpenCode, Codex) along with `CLAUDE.md`. The
agent reads sources, writes pages, updates the index, and appends to
the log. You curate sources, ask questions, and review.
