"""MkDocs hook: make the wiki's links work on the static site.

1. Resolve Obsidian-style [[wiki-links]] into proper relative Markdown links.
   The wiki authors them three ways:
     [[../themes/vibe-coding]]   - path relative to the current file
     [[topics/shiur-prep]]       - path relative to the docs root (top-level)
     [[claude]]                  - bare slug, resolved by basename anywhere
   Optional display text: [[../tools/claude|Claude]] -> [Claude](...)

2. Fix the handful of plain Markdown links that point outside the published
   site (CLAUDE.md schema, raw/chat.txt) by sending them to the GitHub source,
   add a missing ".md", and degrade bare directory links to plain labels.
"""

import os
import re

REPO_BLOB = "https://github.com/aiforshlichus/aifs-wiki/blob/HEAD"

WIKILINK = re.compile(r"\[\[([^\]|]+?)(?:\|([^\]]+))?\]\]")
MDLINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

# basename (without .md) -> src path relative to docs_dir (without .md)
_index = {}


def on_files(files, config):
    _index.clear()
    for f in files:
        if not f.src_uri.endswith(".md"):
            continue
        stem = f.src_uri[:-3]
        _index.setdefault(os.path.basename(stem), stem)
    return files


def _resolve(target, current_dir):
    """Return docs-root-relative path (no .md) for a wiki-link target."""
    t = target.strip()
    if t.endswith(".md"):
        t = t[:-3]
    if "/" in t or t.startswith(".."):
        return os.path.normpath(os.path.join(current_dir, t))
    return _index.get(t, t)


def _wikilinks(markdown, current_dir):
    def repl(m):
        target, display = m.group(1), m.group(2)
        text = (display or os.path.basename(target.strip().rstrip("/"))).strip()
        low = target.strip().lower()
        # Schema / raw files live outside the published site.
        if low.endswith("claude.md"):
            return f"[{text}]({REPO_BLOB}/CLAUDE.md)"
        if "raw/" in low:
            return f"[{text}]({REPO_BLOB}/{low.lstrip('./')})"
        dest = _resolve(target, current_dir)
        rel = os.path.relpath(dest, current_dir) if current_dir else dest
        return f"[{text}]({rel}.md)"

    return WIKILINK.sub(repl, markdown)


def _mdlinks(markdown, current_dir):
    def repl(m):
        text, url = m.group(1), m.group(2).strip()
        if re.match(r"^(https?:|#|mailto:|//)", url):
            return m.group(0)
        low = url.lower()
        # Out-of-site source files -> GitHub.
        if low.endswith("claude.md"):
            return f"[{text}]({REPO_BLOB}/CLAUDE.md)"
        if "raw/" in low:
            clean = re.sub(r"^(\.\./)+", "", url)
            return f"[{text}]({REPO_BLOB}/{clean})"
        # Bare directory link (trailing slash) -> plain label, no 404.
        if url.endswith("/"):
            return f"**{text}**"
        # In-site page link missing its extension.
        if not os.path.splitext(url)[1] and not url.startswith("#"):
            return f"[{text}]({url}.md)"
        return m.group(0)

    return MDLINK.sub(repl, markdown)


def on_page_markdown(markdown, page, config, files):
    current_dir = os.path.dirname(page.file.src_uri)
    markdown = _wikilinks(markdown, current_dir)
    markdown = _mdlinks(markdown, current_dir)
    return markdown
