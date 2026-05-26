# Log

Append-only. Prefix format: `## [YYYY-MM-DD] <op> | <subject>`.
`grep '^## \[' log.md | tail` for the recent timeline.

## [2026-05-26] seed | Initial wiki ingest from chat.txt

Bootstrapped the wiki from `raw/chat.txt` — the WhatsApp export of
**AI for Shlichus (Shluchim)** covering 2025-07-28 through 2026-05-25
(7,431 messages, ~60 active participants).

- Schema: [`../CLAUDE.md`](../CLAUDE.md).
- Source: [`../raw/chat.txt`](../raw/chat.txt).
- Catalog: [`index.md`](./index.md).
- About: [`about.md`](./about.md).

Created the initial set of pages:

- Themes (5): model-leapfrog, ai-and-torah-accuracy,
  ai-flyer-aesthetics, vibe-coding, paid-vs-free.
- Topics (8): flyer-design, shiur-prep, crm-automation,
  hebrew-yiddish, transcription, letter-writing,
  chabadone-integration, fundraising.
- Tools (18): chatgpt, claude, gemini, perplexity, grok,
  berel-me, megillah-app, shluchimexchange-ai, maamorim-app,
  dicta-mekorotai, learningtanach-org, dach-dev, sofer-ai,
  notebooklm, elevenlabs, lovable, canva, nano-banana.
- People (10): mendy-shishler, rayi-stern, elisha-pearl,
  rabbi-zalman-abraham, yisroel-chaim-shuchat, yonatan-azrielant,
  berel-marozov, mendy-elishevitz, mendy-efune, meir-sudak.
- Resources (3): designer-prompt, master-prompts, nonprofit-discounts.
- Conversations (3): kinus-ai-day-nov-2025,
  megillah-app-sprint-feb-2026, torah-accuracy-debate.

Known open work:
- Many secondary contributors still uncovered (e.g., Mordechai
  Lightstone, Didy Waks, Mendel Super, Mendy Mann, Yossi Yaffe).
- Several tools mentioned only in passing (Manus.im, Nanoclaw,
  Sora, Suno, Wispr Flow, Kling, Synthesia, Gamma, Otter.ai,
  Fireflies, CapCut, NotebookLM-as-platform vs. NotebookLM-as-Rebbe-corpus)
  deserve their own pages on a follow-up ingest.
- The "AI and Shabbos" sub-debate ([chat 2026-04-27]) deserves a
  theme page.
- Karpathy's gist itself — the meta-pattern this wiki implements —
  should get a `themes/llm-wiki-pattern.md` page.

Filed under **lint backlog**.
