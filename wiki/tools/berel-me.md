---
type: tool
slug: berel-me
aliases: [berel.me, Berel's tools]
status: maintained
sources: [chat.txt]
updated: 2026-05-25
---

# berel.me

The portfolio of community micro-tools, mostly built with Claude Opus 4.5.
Each tool solves one small, Chabad-specific problem.

## What it is

`berel.me/...` — a kebab-of-utilities URL pattern. Berel ships
small, focused tools rapidly, posts them to the chat, and iterates
from feedback. The unifying philosophy: do one thing, no logins, no
persistent user data, no payment processing.

## The catalog (as of 2026-05)

| Path | What it does | First mention |
| --- | --- | --- |
| `berel.me/dreidel` | Dreidel-based raffle for menorah lighting; collects user info | [chat 2025-12-22] |
| `berel.me/raffle` | Generic raffle tool for classes | [chat 2025-12-25] |
| `berel.me/splitmyclass` | Class-splitting tool | [chat 2025-12-25] |
| `berel.me/lo` | Google logout shortcut | [chat 2026-01-29] |
| `berel.me/מעיין` | Learning tool (Hebrew name) | [chat 2026-01-23] |
| `berel.me/findasicha` | Find Chabad sichos / teachings | [chat 2026-01-27] |
| `berel.me/donatext` | Quick donation link / payment-method snippets | [chat 2026-01-27] |
| `berel.me/jemsubtitles` | Video subtitle generation; "Perfect for shluchim." Bookmarklet at `berel.me/jemsubtitles/bookmarklet.php` | [chat 2026-01-27, 2026-01-29] |
| `berel.me/ashreinutimes` | Ashreinu times tool | [chat 2026-02-12] |
| `berel.me/taste` | Weekly luach viewer — grays out inapplicable dates; manually chosen Torah portions | [chat 2026-02-13] |
| `berel.me/taste/autoprint` | Auto-print extension (e.g. Mishkan Tanya) | [chat 2026-05-21] |
| `berel.me/grogger` | Phone-shake-triggered grogger for Megillah | [chat 2026-02-20] |
| `berel.me/pdflabel` | PDF label printing | [chat 2026-02-22] |
| `berel.me/crop` | Image cropping tool | [chat 2026-04] |
| `berel.me/12pesukim/` | 12 Pesukim tool (Shnas HaChinuch) | [chat 2026-05-08] |
| `berel.me/sichastitch/` | Sicha-stitching tool | [chat 2026-05-14] |
| `berel.me/kiddushhachodesh` | Rambam Kiddush HaChodesh proof-of-concept | [chat 2026-04-05] |
| `berel.me/pushkapp/gemini3` | 3D digital pushka tracker (test) | [chat 2026-02] |
| `berel.me/proclamations` | Birth / simcha proclamation generator | [chat 2026-02] |
| `berel.me/passover` | Passover concept site | [chat 2026-03-19] |
| `happybirthday.berel.me/gift` | Birthday gift link that *simulates* a $1M charge (safely) | [chat 2026-02] |
| `berel.me/do-my-shlichus-for-me` | Joke link | [chat 2026-03] |

## Why this matters

Berel's portfolio is the chat's proof of *what shluchim can ship* with
AI — small, in-browser, no-login utilities that solve one concrete
need at a time. It's the antithesis of the "AI builds my whole CRM"
fantasy, and it works.

See [[../themes/vibe-coding]] for why this kind of tool stays safe:
no databases, no user accounts, no payments. *"Things that won't fail
catastrophically if the code gets stale."*

## The build process

Mostly **Claude Opus 4.5** in [[claude]] Code. *"I made this
with a single prompt a few months ago."* [chat 2026-04-05] for
Kiddush HaChodesh. Iterates from chat feedback within hours.

## Design critique

The berel.me builder doubles as the chat's resident UX critic. [chat 2026-02-20]
on the early Megillah app: suggested the grogger should be a
shake-triggered button, not a Haman-name highlighter. Most of
these suggestions land in shipped products.

## Related

- [[megillah-app]] — a parallel project that learned from the same UX style.
- [[../themes/vibe-coding]]
- [[../tools/claude]]
