---
type: tool
slug: megillah-app
aliases: [megillah.app, Megillah App, megillah.app/live]
status: maintained
sources: [chat.txt]
updated: 2026-05-25
---

# megillah.app

The chat's flagship vibe-coding success: an open-source, multi-language,
synchronized Megillah-reading app built in ~10 days for Purim 2026
with live community feature requests.

## What it is

`megillah.app` — a web app for following along during Megillas Esther
reading. Built with [[claude]] (Claude Code). Repo:
`github.com/kadmonim/megillah.app`.

Features (as of 2026-05):

- **Auto-scrolling text** synchronized to a leader.
- **Live broadcast mode** at `megillah.app/live` — one person leads,
  every connected device follows in real time. Password-protected
  sessions.
- **6+ language translations** — including JPS 1917 → Metzudah → Kehos
  (pending Chabad approval, as of [chat 2026-02-22]).
- **Transliteration** alongside the Hebrew.
- **Pause / resume**, settings panel, font/size controls.
- **Haman name highlighting** (with sound effects).
- **Shake to grogger** option (community suggestion).
- **Kids version** with images.
- **QR codes** for session sharing.

## The Purim sprint

The 10-day build is documented in
[[../conversations/megillah-app-sprint-feb-2026]]. The pattern:

1. v0 ships (basic synchronized reading).
2. Posted to AIFS Builders WhatsApp group.
3. Community sends feature requests (translations, transliteration,
   broadcast latency, kids mode, sound effects).
4. Maintainer merges or pushes back within hours.
5. Repeat for ~10 days, culminating in Purim 2026.

Dozens of community members contributed feature ideas and pull requests
during the sprint. Treated by the community as proof that
*shluchim can collectively ship real software*.

## What it taught the community

- **Real-time websocket sync** is hard — *"there is quite a lag between
  when the broadcaster scrolls and when it follows suit on the other
  phone."* [chat 2026-02-22]. Mendy fixed iteratively.
- **Browser security blocks features.** Voice recognition for
  auto-scrolling: *"the tech is not ripe enough — there's too much of a
  time delay."* [chat 2026-02-22]. Same for OS-level
  Do-Not-Disturb mode: websites can't trigger it. Native app would be
  required.
- **Translation politics.** JPS 1917 felt archaic and problematic.
  Metzudah was the interim solution. Kehos was the goal pending
  Chabad-org approval.
- **The community shipped feedback faster than the maintainer could
  triage** — peaked at hundreds of message reactions and feature
  requests per day.

## Use beyond Chabad

> *"It is universally appealing, applies to non-shluchim and even
> non-Chabad."*
> — [chat 2026-02-20]

Used by Chabad houses worldwide on Purim 2026. Got ~700 shluchim
mentioned in COLlive coverage: *"700 Shluchim Built a Megillah App in
10 Days."* [chat 2026-03]

## Open issues

- Live-broadcast latency on slow networks.
- Setting sync between session participants — *"settings don't sync;
  will be fixed soon iyh."* [chat 2026-02-22]
- No native push notifications (browser limitation).
- Bus-factor of 1 — single maintainer.

## Related

- [[../conversations/megillah-app-sprint-feb-2026]]
- [[../themes/vibe-coding]]
- [[claude]] — the build tool.
- [[berel-me]] — analogous Chabad-app portfolio.
