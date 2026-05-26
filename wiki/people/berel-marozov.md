---
type: person
slug: berel-marozov
aliases: [Berel Marozov, Berel]
status: maintained
sources: [chat.txt]
updated: 2026-05-25
---

# Berel Marozov

Builder of the `berel.me/...` portfolio — a dozen-plus micro-tools for
shlichus use, all rapidly prototyped, mostly with Claude Opus 4.5.

## What he builds

See [[../tools/berel-me]] for the full catalog. Highlights:

- **berel.me/grogger** — shake-the-phone Megillah grogger.
- **berel.me/findasicha** — find Chabad sichos.
- **berel.me/jemsubtitles** — video subtitle generation for shluchim.
- **berel.me/12pesukim** — Shnas HaChinuch tool.
- **berel.me/raffle, berel.me/splitmyclass, berel.me/donatext** — class &amp; donation utilities.
- **berel.me/sichastitch** — stitch multi-part sichos together.
- **berel.me/taste/autoprint** — auto-print for Mishkan Tanya, etc.
- **berel.me/pdflabel** — label-printing tool.
- **berel.me/pushkapp/gemini3** — 3D digital pushka tracker.
- **happybirthday.berel.me/gift** — birthday gift link that *simulates*
  a $1M charge (safely).
- **berel.me/do-my-shlichus-for-me** — joke.

## Why his pattern works

Every Berel tool follows the same shape: **single function, no login,
no persistent user data, no payment processing.** It maps perfectly to
Rayi Stern's "what's safe to vibe-code" rules.

Berel: *"I made this with a single prompt a few months ago."*
[chat 2026-04-05] for kiddushhachodesh. The pattern is:

1. Identify a shliach-pain so specific it's almost trivial.
2. Prompt Claude Opus 4.5 once or twice.
3. Deploy at `berel.me/...`.
4. Post in chat.
5. Iterate on community feedback.

## Design critic

Beyond his own tools, Berel reliably critiques others' UX in chat.
Notable interventions:

- [chat 2026-02-20]: on early megillah.app — suggested grogger should
  be a shake-trigger, not a Haman-name highlighter. Got built.
- [chat 2026-05-20]: *"Ask ChatGPT to make you a script that does it.
  In general, I always ask AI to make a script instead of asking it
  to directly process the data."* — the "don't trust the AI to
  process data, trust the AI to write code that processes data"
  principle.

## Editorial positions

> *"Took longer to make the image preview than to make the program."*
> — [chat 2026-02-12], on berel.me/ashreinutimes.

## Style

Playful tooling, design-aware, opinionated about UX. Treats AI as a
power saw, not a contractor — short, sharp builds rather than agentic
delegations.

## Related

- [[../tools/berel-me]]
- [[../themes/vibe-coding]]
- [[mendy-elishevitz]] — close collaborator on megillah.app feedback.
