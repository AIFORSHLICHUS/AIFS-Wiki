# Inbox File Format — AIFS-Wiki

Hermes pushes one file per digest run to `raw/inbox/YYYY-MM-DD.md` via the GitHub
Contents API. The ingest Action reads it and updates wiki pages automatically.

## File naming

`raw/inbox/YYYY-MM-DD.md` — one file per day (or per run).
Use the date of the *last* message in the batch, not the push date.

## Required structure

```markdown
---
inbox_date: YYYY-MM-DD
period_start: YYYY-MM-DDTHH:MM:SS
period_end: YYYY-MM-DDTHH:MM:SS
message_count: <integer>
---

# AIFS-Wiki Inbox: YYYY-MM-DD

Brief one-line summary of what's in this digest.

## [tool] <Tool Name>
- Bullet point about new usage, tip, or discussion [chat YYYY-MM-DD]
- Another point [chat YYYY-MM-DD]
- Relevant wiki page: tools/<slug> (create | update)

## [tool] <New Tool Not Yet in Wiki>
- First mention — what it does and how the group is using it [chat YYYY-MM-DD]
- Relevant wiki page: tools/<slug> (create)

## [topic] <Topic Name>
- New technique or workflow discussed [chat YYYY-MM-DD]
- Relevant wiki page: topics/<slug> (update)

## [theme] <Theme Name>
- New argument, position, or tension [chat YYYY-MM-DD]
- Relevant wiki page: themes/<slug> (update)

## [resource] <Resource Name>
- New prompt, template, or discount [chat YYYY-MM-DD]
- Relevant wiki page: resources/<slug> (create | update)
```

## Rules Hermes must follow

1. **No names, no phone numbers** — strip all personal identifiers.
   Citations use `[chat YYYY-MM-DD]` only.
2. **Only AI-relevant content** — skip logistics, off-topic chatter, etc.
3. **Include the wiki page hint** — the `Relevant wiki page:` line tells
   the ingest script where to apply the update. Use `create` if the page
   doesn't exist yet, `update` if it does.
4. **Terse bullets** — one idea per bullet. The ingest agent expands.
5. **Deduplicate** — don't re-push content already in a previous digest.
   Use a cursor (last-processed timestamp) to bound the window.

## GitHub API call

```bash
# Create a new inbox file (no sha needed for new paths)
curl -s -X PUT \
  -H "Authorization: Bearer $AIFS_WIKI_PAT" \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/AIFORSHLICHUS/AIFS-Wiki/contents/raw/inbox/$(date +%Y-%m-%d).md \
  -d "{\"message\": \"wiki: inbox $(date +%Y-%m-%d)\", \"content\": \"$(base64 -w0 < /tmp/inbox.md)\"}"
```

Use a fine-grained PAT scoped to `AIFORSHLICHUS/AIFS-Wiki`, permission:
**Contents: Read and Write** — nothing else needed.
