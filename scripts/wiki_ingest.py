#!/usr/bin/env python3
"""
wiki_ingest.py — Auto-ingest raw/inbox/*.md into the AIFS-Wiki.

Called by GitHub Action on push to raw/inbox/*.md.
Requires ANTHROPIC_API_KEY in environment.

Usage:
    python scripts/wiki_ingest.py raw/inbox/2026-06-05.md
"""

import json
import os
import sys
from datetime import date
from pathlib import Path

import anthropic


def main():
    if len(sys.argv) < 2:
        print("Usage: wiki_ingest.py <inbox_file>")
        sys.exit(1)

    inbox_path = Path(sys.argv[1])
    if not inbox_path.exists():
        print(f"Not found: {inbox_path}", file=sys.stderr)
        sys.exit(1)

    client = anthropic.Anthropic()

    # ── tool definitions ──────────────────────────────────────────────────────

    tools = [
        {
            "name": "read_file",
            "description": "Read any file in the repository.",
            "input_schema": {
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "Repo-root-relative path"}
                },
                "required": ["path"],
            },
        },
        {
            "name": "write_file",
            "description": "Write or overwrite a wiki page. Creates parent dirs as needed.",
            "input_schema": {
                "type": "object",
                "properties": {
                    "path": {"type": "string"},
                    "content": {"type": "string"},
                },
                "required": ["path", "content"],
            },
        },
        {
            "name": "list_files",
            "description": "List files in a directory (one path per line).",
            "input_schema": {
                "type": "object",
                "properties": {
                    "directory": {"type": "string"}
                },
                "required": ["directory"],
            },
        },
        {
            "name": "append_log",
            "description": "Append a log entry to wiki/log.md. Use ONLY after all wiki edits are done.",
            "input_schema": {
                "type": "object",
                "properties": {
                    "entry": {
                        "type": "string",
                        "description": "Full log entry starting with ## [YYYY-MM-DD] ingest | ...",
                    }
                },
                "required": ["entry"],
            },
        },
    ]

    def handle_tool(name: str, inputs: dict) -> str:
        if name == "read_file":
            p = Path(inputs["path"])
            return p.read_text() if p.exists() else f"[not found: {inputs['path']}]"

        if name == "write_file":
            p = Path(inputs["path"])
            # Hard guard: never touch log.md via write_file
            if p.name == "log.md":
                return "[refused: use append_log for log.md]"
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(inputs["content"])
            print(f"  wrote {p}")
            return f"ok: {p}"

        if name == "list_files":
            d = Path(inputs["directory"])
            if not d.exists():
                return f"[not found: {inputs['directory']}]"
            return "\n".join(str(f) for f in sorted(d.iterdir()))

        if name == "append_log":
            log = Path("wiki/log.md")
            existing = log.read_text()
            log.write_text(existing.rstrip() + "\n\n" + inputs["entry"].strip() + "\n")
            print("  appended log entry")
            return "ok"

        return f"[unknown tool: {name}]"

    # ── prompt ────────────────────────────────────────────────────────────────

    schema = Path("CLAUDE.md").read_text()
    inbox_content = inbox_path.read_text()
    today = date.today().isoformat()

    system = f"""You are the AIFS-Wiki maintenance agent. Ingest new messages from the inbox \
and update the wiki.

=== SCHEMA (follow exactly) ===
{schema}

=== HARD RULES ===
- Zero personal names or phone numbers anywhere in wiki output.
- Citations: [chat YYYY-MM-DD] only — no names, no numbers.
- [external: ...] only when a reader acting on chat alone would be misled.
- Terse. The wiki indexes and synthesizes; it does not narrate.
- Today's date: {today}

=== WORKFLOW ===
1. read_file wiki/index.md — understand current pages.
2. For each section in the inbox, find the matching wiki page and read it.
3. Update the page (write_file) with new content merged in.
4. If a section says "(create)", create a new page following the schema conventions.
5. If new pages were created, update wiki/index.md.
6. append_log once — after all writes — with a concise summary.
7. Do NOT re-add information already present on the page."""

    messages = [
        {
            "role": "user",
            "content": (
                f"Ingest this inbox file into the wiki.\n\n"
                f"File: {inbox_path}\n\n"
                f"Contents:\n\n{inbox_content}"
            ),
        }
    ]

    # ── agentic loop ──────────────────────────────────────────────────────────

    print(f"Ingesting {inbox_path} …")
    for turn in range(40):
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=8192,
            system=system,
            tools=tools,
            messages=messages,
        )

        messages.append({"role": "assistant", "content": response.content})

        if response.stop_reason == "end_turn":
            print(f"Done ({turn + 1} turns).")
            break

        if response.stop_reason == "tool_use":
            results = []
            for block in response.content:
                if block.type == "tool_use":
                    print(f"  {block.name}({json.dumps(block.input)[:80]})")
                    result = handle_tool(block.name, block.input)
                    results.append(
                        {"type": "tool_result", "tool_use_id": block.id, "content": result}
                    )
            messages.append({"role": "user", "content": results})
    else:
        print("Warning: hit turn limit.", file=sys.stderr)


if __name__ == "__main__":
    main()
