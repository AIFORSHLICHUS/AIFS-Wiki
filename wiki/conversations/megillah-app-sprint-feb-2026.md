---
type: conversation
slug: megillah-app-sprint-feb-2026
aliases: [Megillah App sprint, Purim hackathon, 10-day megillah build]
status: maintained
sources: [chat.txt]
updated: 2026-05-25
participants: []
date_range: 2026-02-13 to 2026-03-03
---

# The Megillah App Sprint — Purim 2026

The chat's collective shipping moment. In about ten days during the
run-up to Purim 2026, [[../tools/megillah-app]] was built —
synchronized Megillah reading with live broadcast mode — with feature
requests, bug reports, and design critique flowing live from the chat.
Featured in COLlive: *"700 Shluchim Built a Megillah App in 10 Days."*

## Timeline

| Date | Event |
| --- | --- |
| **2026-02-13** | Group splits — the **AIFS Builders** subgroup is created so feature debates don't crowd the main channel. |
| **2026-02-20** | v0 of megillah.app ships. Suggestion to make the grogger a **phone-shake-triggered button** rather than a Haman-name highlighter is accepted. |
| **2026-02-21** | Live broadcast mode (`megillah.app/live`) added. Password-protected sessions. |
| **2026-02-22** | 6 languages added. Pause button. Haman highlighting. *chabad.org* link. Kids version with images. QR codes for sharing. The **Shluchim Vibe Coding Sprint** kicks off with prompts for Jules, cto.new, Lovable, Kiro, Cursor, Claude Desktop, OpenAI Codex. Repo open on GitHub. |
| **2026-02-22 (eve)** | Live-broadcast latency reports from multiple shluchim testing in their shuls. Builder iterates. |
| **2026-03-03** | Post-Purim debrief. Shmuli Brown: *"People were telling me Chabad are geniuses and leaders. People loved it."* A contributor shares learningtanach.org post-mortem (different project, same week). |

## Feature requests, granted vs. punted

| Feature | Status |
| --- | --- |
| Multiple language toggles | ✅ shipped |
| Transliteration | ✅ shipped |
| Pause / resume controls | ✅ shipped |
| Settings panel + font controls | ✅ shipped |
| Haman name highlighting + sound effects | ✅ shipped |
| Shake-to-grogger | ✅ shipped |
| Kids mode with images | ✅ shipped |
| Auto-scroll based on **voice recognition** | ❌ *"the tech is not ripe enough — too much time delay."* |
| **Do Not Disturb** mode auto-trigger | ❌ websites can't trigger OS-level DND; would need native app |
| **Settings sync** between session participants | ⏳ promised: *"will be fixed soon iyh"* |
| **Kehos** translation | ⏳ pending Chabad-org approval |
| Sound effects triggered by voice recognition | ❌ same root cause |

## What broke (and got fixed)

- **Live broadcast latency** on slow networks. Multiple test threads
  diagnosed it. Iterated to acceptable in the same week.
- **Hebrew font choices** — criticized; corrected.
- **Centering** for auto-scrolling — adjusted from top-pinned to
  center-pinned mid-sprint.
- **Translation politics** — JPS 1917's archaic register felt wrong;
  Metzudah was the interim swap.

## Why this thread matters

- **Proof-of-concept for community-built shliach software.** 200+
  shluchim deployed the same app from one maintainer's repo.
- **Single-maintainer bus factor.** Almost all the merging was done by
  one person. Sustainable? Unclear. The follow-up AIFS Builders group
  is the collective answer.
- **Template for future sprints.** Megillah.app set the cadence —
  community proposes, one builder ships, iteration in hours, not
  weeks.
- **Live demonstration of [[../themes/vibe-coding]] done correctly**:
  no logins, no payments, no database of user PII; just real-time
  synchronization of public Torah text.

## Adjacent shipping in the same window

- **learningtanach.org/esther/reader** — image-heavy Esther reader.
  Bugs at launch; ~7,000 visitors in 2 days regardless. A transparent
  post-mortem ([chat 2026-03-04]) became its own artifact.
- **ai770.com/megillah** — alternative reader.
- **Sound effects + 12 pesukim + grogger** entries in the
  [[../tools/berel-me]] suite.

## The COLlive moment

Shared in [chat 2026-03]:

> *"700 Shluchim Built a Megillah App in 10 Days."*

`collive.com/700-shluchim-built-a-megillah-app-in-10-days/`

## Related

- [[../tools/megillah-app]]
- [[../tools/berel-me]]
- [[../tools/learningtanach-org]]
- [[../themes/vibe-coding]]
