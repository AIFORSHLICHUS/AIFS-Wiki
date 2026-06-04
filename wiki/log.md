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

## [2026-05-26] ingest | Second pass — secondary tools, people, themes

User feedback: first pass was too thin. Expanded with ~35 more pages.

**Added tools** (15): manus, sora (with external-context note), suno,
gamma, qwen, coding-builders, meeting-tools, wispr-flow, video-tools,
sefaria, sinai-gpt, chattorah, chabad-apps (roster), crm-tools,
turboscribe-whisper, google-ai-studio, nanoclaw.

**Added people** (13): didy-waks, mordechai-lightstone, mendel-super,
mendy-mann, yossi-yaffe, elazar-green, rabbi-chaim-lazaroff,
avi-winner, mendel-teldon, moshe-koppel, shmuli-neft, mendel-groner,
rabbi-eli-pink.

**Added topics** (6): video-creation, image-generation,
web-app-building, whatsapp-automation, route-optimization,
data-cleanup.

**Added themes** (4): ai-and-shabbos, llm-wiki-pattern, privacy-data,
moshiach-and-ai.

**Added conversations** (1): sora-demographic-workaround.

## [2026-05-26] schema | Added `[external …]` citation pattern

User raised the staleness problem: the chat is months stale on
fast-moving tool reality (e.g., Sora has been discontinued — not
explicit in the chat). Updated `CLAUDE.md` with a second citation
kind: `[external …]` for sparing real-world annotations that *layer
on top of* chat citations rather than replacing them. Rules:

- Only when reader acting on chat alone would be misled.
- Cite the external source explicitly (vendor announcement, user
  note, URL).
- Never paraphrase generic web content without attribution.
- Flag uncertainty and add to this lint backlog.

Applied immediately to [[tools/sora]] (discontinuation note).

**Lint backlog** — pages that need an external pass for staleness:

- [[tools/manus]] — verify Meta acquisition status and current pricing.
- [[tools/gemini]] — "Gemini Spark" / "Gemini Omni" / 3.5 Flash were
  chat-time announcements; confirm what shipped.
- [[tools/perplexity]] — PayPal free-year route ended 2025-12-31;
  verify current free paths.
- [[tools/lovable]] — pricing / referral status.
- [[tools/wispr-flow]] — Android rollout status.
- [[tools/dicta-mekorotai]] — current public availability.
- [[tools/chattorah]] — current public availability.
- [[resources/nonprofit-discounts]] — every offer here has a half-life;
  sweep quarterly.
- [[themes/model-leapfrog]] — by definition perpetually behind; touch
  on every ingest.

Mark pages with `[external: …]` only when the correction *matters* —
not just because reality moved. The chat's voice is the asset.

## [2026-06-04] lint | Anonymization + outdated-info pass

User directive: remove all personal names and phone numbers from the wiki;
apply stronger cleansing for stale information.

**Anonymization (full pass):**
- Stripped names and phone numbers from all `[chat DATE, NAME]` and
  `[chat DATE, +NUMBER]` citations — now `[chat DATE]` throughout.
- Removed all inline name mentions from body text across ~60 pages;
  replaced with role/context descriptors ("the group founder",
  "a community organizer", "a bar-Ilan professor", etc.).
- Deleted all 23 `wiki/people/` pages.
- Removed the People section from `wiki/index.md`.
- Removed all `[[../people/…]]` cross-links from Related sections.

**Outdated-info pass (external annotations applied):**
- [[tools/manus]] — noted autonomous-agent status and acquisition context.
- [[tools/gemini]] — noted continued model-naming evolution post-chat.
- [[tools/perplexity]] — confirmed PayPal free-year ended 2025-12-31.
- [[tools/lovable]] — noted pricing/referral status may have changed.
- [[tools/wispr-flow]] — noted Android rollout status.
- [[tools/dicta-mekorotai]] — noted public-availability caveat.
- [[tools/chattorah]] — noted development status.
- [[resources/nonprofit-discounts]] — added prominent quarterly-sweep warning.
- [[themes/model-leapfrog]] — updated competitive frontier note.

**Pages now**: 68 (down from 91 — 23 people pages removed).
