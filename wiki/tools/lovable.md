---
type: tool
slug: lovable
aliases: [lovable.dev, lovable.app]
status: maintained
sources: [chat.txt]
updated: 2026-05-25
---

# Lovable

The vibe-coding tool that opened the floodgates. *"You can make it in
20 minutes"* — repeated phrase from 2026-01 through 2026-03.

## What it is

`lovable.dev` — generative web-app builder. Prompt → working web app
(Tailwind/React + backend if you want it). Deploys to a Lovable
subdomain or your own.

Subscription: credit-based, ~$25/mo entry. Has had occasional free
windows (notably ~24h in early March 2026, [chat 2026-03-08]).

[external: pricing and referral/gift-card programs may have changed
since the chat window (last reference: 2026-05). Verify current
pricing at lovable.dev before relying. — external: knowledge cutoff
~mid-2026]

## What the chat has shipped with it

A non-exhaustive list — see [[../themes/vibe-coding]] for more:

- **cypcampaign.lovable.app** — end-of-year volunteer + donor dashboard. [chat 2025-12-14]
- **rashi-roots-map.lovable.app** — intellectual history timeline. [chat 2026-01-23]
- **kiddushhachodesh.lovable.app** — Rambam Kiddush Hachodesh app. [chat 2026-04-05]
- **tzvi-to-tzadik.lovable.app** — grandfather-to-Rebbe poems. [chat 2026-03-29]
- **passover.jewishdips.com** — built with Claude *inspired by* Lovable's window. [chat 2026-03-19]
- **tzivoshashem.lovable.app** — Tzivos Hashem app. [chat 2026-02-16]
- **my-charity-box.lovable.app** — pledge tracker. [chat 2026-04-28]
- **preview--sms-invite-joy.lovable.app** — SMS invitation tool. [chat 2025-12-25]
- **shabbos.lovable.app** — quick Shabbos times. [chat 2026-03]
- **chabadvocate.lovable.app** — early Chabad-advocacy concept.

## Strengths

- Fast prototype to deployed app.
- Decent UI defaults (Tailwind + shadcn).
- Hebrew support with effort.
- Stripe / Zeffy integration baked in.
- Referral / gift-card distribution within the community.

## Weaknesses

- **Cannot import an existing repository.** [chat 2026-02-22]
  *"lovable won't work for this as you can't connect the existing repo."*
- **Security concerns** for anything user-facing with logins or
  payments — see [[../themes/vibe-coding]]. The warning is the
  canonical one: keep banking out, don't connect to financial APIs,
  professional review before deploying.
- **Maintenance cliff** — incremental AI edits compound architectural
  drift. [chat 2026-03-04]
- **More expensive than Claude Code** at heavy use.
  [chat 2026-04-16]

## When to use Lovable vs. alternatives

| Need | Use |
| --- | --- |
| 15-minute prototype, single page | **Lovable** |
| Database-backed, multi-screen app | **Base44** (better Hebrew, cheaper) |
| Real engineering, GitHub integration | **Claude Code** (free with Claude Pro) |
| Already in an IDE | **GitHub Copilot** ($10/mo) |
| Power user, large codebase | **Cursor** (expensive, $300–500/mo at heavy use) |

[chat 2026-02-22] is the canonical breakdown.

## The Megillah-app proof point

[[megillah-app]] (Feb 2026) was *not* built with Lovable — but it's
the community's flagship vibe-coding success because it demonstrated
what's possible: ten days, multi-language, broadcast-mode, live
community feedback, open-source on GitHub.
See [[../conversations/megillah-app-sprint-feb-2026]].

## Open questions

- **How to graduate from Lovable to maintained software** without
  rewriting from scratch.
- **Template that 200 shluchim can install** — proposed often,
  not yet shipped.

## Related

- [[../themes/vibe-coding]]
- [[megillah-app]] — the standard-bearer (Claude Code, not Lovable).
- [[berel-me]] — community tools portfolio, mostly Claude Opus 4.5.
- [[claude]] — Claude Code is the engineering-grade competitor.
