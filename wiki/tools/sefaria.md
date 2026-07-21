---
type: tool
slug: sefaria
aliases: [Sefaria, sefaria.org]
status: draft
sources: [chat.txt]
updated: 2026-05-25
---

# Sefaria

The largest digitized Torah library. Not AI itself, but the corpus
that AI most often *should* be reading.

## What it is

`sefaria.org` — open-source library of Torah, Talmud, Midrash, halacha,
Chassidus. JPS 1917, Metzudah, and other translations. Kehot put
Tanya and Likutei Torah on Sefaria as of 2026-02.

## How the chat uses it

- **Source-of-truth for citations.** When ChatGPT cites a Gemara
  page, paste the citation into Sefaria's exact-match toggle to verify
  before quoting.
- **Translations.** Multiple translation versions per text; pick the
  one fitting your audience.
- **Paste primary text into AI.** Rather than asking AI to fetch a
  Mishnah from memory, copy the Mishnah from Sefaria into your prompt.
- **Translation choice for [[megillah-app]].** JPS 1917 felt archaic;
  switched to Metzudah; Kehos pending approval. [chat 2026-02-22]

## Why it matters

> *"Tried ChatGPT, Claude, and Google to find a specific Gemara
> reference. ChatGPT and Google both wrong. Claude was honest about
> limitations and recommended Sefaria (which worked)."*
> — [chat 2026-03-24]

This is the chat's repeated lesson: **Sefaria for the text; AI for the
reading**. Don't reverse it.

## Related digital seforim resources

- **[[dach-dev]]** — plain-text Chassidic library; copy-full-sicha.
- **HebrewBooks.org** — large repository of Hebrew sources; less AI
  access.
- **anash.org Likkutei Sichos app** — plain text Likkutei Sichos.
- **likuteysichos.com** — topic search.
- **rav.dicta.org.il** — Hebrew NLP for Torah.
- **chabad.org** — translations and articles.

## Related

- [[../themes/ai-and-torah-accuracy]]
- [[../topics/shiur-prep]]
- [[../topics/hebrew-yiddish]]
- [[notebooklm]] — uses your uploaded Sefaria-derived texts.
- [[dicta-mekorotai]] — purpose-built rabbinic AI.
