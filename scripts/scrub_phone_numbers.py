#!/usr/bin/env python3
"""
scrub_phone_numbers.py — strip member phone numbers from wiki citations.

The wiki's citation convention is `[chat <date>, <phone>]`, which attributes
claims to WhatsApp members by their real phone number. The phone number is PII;
the date is fine to keep. This tool removes the phone (and its separator) from
every citation bracket, leaving `[chat <date>]`.

Two jobs, one transform (single source of truth):
  1. One-time cleanup of already-published content (run over `wiki/`).
  2. Post-generation guard in the ingest pipeline: the LLM distiller may re-add
     phone numbers, so the pipeline runs this before committing.

Behaviour:
  * Citation brackets — `[chat <date>, +phone]`, `[<date>, +phone]`,
    multi-citation `[chat <d1>; chat <d2>, +phone]`, and line-wrapped
    variants — have the phone (and leading `, `) removed automatically.
  * After fixing, the tree is re-scanned for ANY residual phone-like token
    (e.g. a phone written in prose, outside a citation). If one remains the
    tool prints it and exits non-zero (fail-closed) — in the pipeline this
    blocks the commit so no PII is published; in one-time cleanup it flags the
    prose stragglers that need a hand edit.

Usage:
    python scripts/scrub_phone_numbers.py [DIR ...]   # default: wiki
    python scripts/scrub_phone_numbers.py --dry-run    # report, do not write
    python scripts/scrub_phone_numbers.py --selftest   # run built-in tests

Dates, names in citations, oklch() colours, referral codes and version numbers
are never touched — only strings that are unambiguously phone numbers
(a leading '+' followed by 7-15 digits in digit/space/hyphen groups).
"""

import re
import sys
from pathlib import Path

# A citation bracket: starts with an optional "chat " then a 4-digit year.
# `[^\]]` matches newlines too, so line-wrapped citations are captured whole.
# Markdown [[wikilinks]], [external: ...] and [text](url) links never start
# with a bare 4-digit year, so they are not matched.
CITATION = re.compile(r"\[(?:chat )?\d{4}[^\]]*\]")

# A phone-shaped token: '+' then a digit, then digit/space/hyphen/paren groups.
# Validated afterwards by digit count so short tokens like "+25" are ignored.
PHONE_CANDIDATE = re.compile(r"\+\d[\d \-()]*\d")

# The phone plus the separator that attaches it to the date inside a citation.
# `\s*` absorbs the newline of a line-wrapped citation.
SEP_PHONE = re.compile(r",?\s*(\+\d[\d \-()]*\d)")


def looks_like_phone(token: str) -> bool:
    """True only for real phone numbers: 7-15 digits (E.164 range)."""
    return 7 <= sum(c.isdigit() for c in token) <= 15


def _strip_phones_in_citation(bracket: str) -> str:
    """Remove every phone (and its separator) from one citation bracket."""

    def drop(m: "re.Match") -> str:
        return "" if looks_like_phone(m.group(1)) else m.group(0)

    out = SEP_PHONE.sub(drop, bracket)
    # Tidy separators left dangling if a phone was the last/only element.
    out = re.sub(r"[,;]\s*\]", "]", out)
    out = re.sub(r"\s+\]", "]", out)
    return out


def scrub_text(text: str) -> str:
    """Return `text` with phone numbers removed from all citation brackets."""
    return CITATION.sub(lambda m: _strip_phones_in_citation(m.group(0)), text)


def find_residual_phones(text: str):
    """Yield every remaining phone-like token (for the fail-closed scan)."""
    for m in PHONE_CANDIDATE.finditer(text):
        if looks_like_phone(m.group(0)):
            yield m.group(0)


def _iter_md(dirs):
    for d in dirs:
        p = Path(d)
        if p.is_file() and p.suffix == ".md":
            yield p
        else:
            yield from sorted(p.rglob("*.md"))


def run(dirs, dry_run=False):
    fixed_files = 0
    fixed_citations = 0
    residual = []  # (file, lineno, token)

    for path in _iter_md(dirs):
        original = path.read_text(encoding="utf-8")
        scrubbed = scrub_text(original)
        if scrubbed != original:
            # Count how many citations lost a phone (before-count minus after).
            before = sum(
                1
                for m in CITATION.finditer(original)
                for _ in find_residual_phones(m.group(0))
            )
            after = sum(
                1
                for m in CITATION.finditer(scrubbed)
                for _ in find_residual_phones(m.group(0))
            )
            fixed_citations += before - after
            fixed_files += 1
            if not dry_run:
                path.write_text(scrubbed, encoding="utf-8")

        # Residual scan is done on the (in-memory) scrubbed text.
        for i, line in enumerate(scrubbed.splitlines(), 1):
            for tok in find_residual_phones(line):
                residual.append((path, i, tok))

    verb = "would fix" if dry_run else "fixed"
    print(f"{verb} {fixed_citations} citation phone(s) across {fixed_files} file(s)")

    if residual:
        print(f"\nRESIDUAL phone-like tokens ({len(residual)}) — NOT auto-fixed:")
        for path, lineno, tok in residual:
            print(f"  {path}:{lineno}: {tok}")
        return 1
    print("No residual phone numbers remain.")
    return 0


# --------------------------------------------------------------------------- #
# Built-in tests (regression tripwire). Run: --selftest
# --------------------------------------------------------------------------- #
def selftest() -> int:
    strip_cases = [
        # (input, expected) — every phone format seen in the corpus.
        ("[chat 2025-08-19, +1 347-598-7098]", "[chat 2025-08-19]"),
        ("[chat 2025-08, +1 240-444-3345]", "[chat 2025-08]"),      # partial date
        ("[2026-05-19, +1 737-786-5770]", "[2026-05-19]"),           # no "chat"
        ("[chat 2025-08-03, +27 65 944 5633]", "[chat 2025-08-03]"), # ZA spaces
        ("[chat 2026-02-13, +54 9 11 6164-2418]", "[chat 2026-02-13]"),
        ("[chat 2026-01-11, +1 33-6 51 48 36 80]", "[chat 2026-01-11]"),
        ("[chat 2026-02-11, +44 7710 524460]", "[chat 2026-02-11]"), # UK spaces
        ("[chat 2025-12-13, +33 6 68 42 07 70]", "[chat 2025-12-13]"),
        ("[chat 2025-11-14, +972 53-338-6770]", "[chat 2025-11-14]"),
        ("[chat 2025-08-20, +380 63 770 4111]", "[chat 2025-08-20]"),
        # multi-citation, one bracket
        ("[chat 2026-03-13; chat 2025-12-04, +1 203-887-6044]",
         "[chat 2026-03-13; chat 2025-12-04]"),
        # multiple phones in one bracket
        ("[chat 2026-02-06, +1 415-634-7727, +1 520-703-7466]",
         "[chat 2026-02-06]"),
        # line-wrapped citation
        ("is a [chat 2025-08,\n+1 904-910-5676] specialty.",
         "is a [chat 2025-08] specialty."),
        # PRESERVE: name in citation (not a phone)
        ("[chat 2025-08-06, Mendy Cunin LA]", "[chat 2025-08-06, Mendy Cunin LA]"),
        # PRESERVE: plain date citation
        ("[chat 2026-05-15]", "[chat 2026-05-15]"),
        # PRESERVE: non-phone text that happens to contain '+<digits>'
        ("gained +25 points [chat 2026-01-01]", "gained +25 points [chat 2026-01-01]"),
    ]
    preserve_untouched = [
        "oklch(0.7 0.15 25) and oklch(0.98 0 0)",   # CSS colours
        "referral code MEIR42 and NKUHQBD2D1ZI",     # codes
        "released on 2025-08-19 (an ISO date)",      # bare ISO date
        "Matt Shumer said so",                       # public figure name
        "version 2.5.1 and +25% growth",             # version / percentage
    ]
    residual_cases = [
        # prose phone outside a citation MUST be detected as residual
        ("+1 520-472-8840 introduces the concept", True),
        ("**2026-03-18, +44 7980-795936** documents", True),
        ("the expanded version (+1 737-786-5770) adds", True),
        # non-phones MUST NOT be detected
        ("oklch(0.7 0.15 25)", False),
        ("plain [chat 2025-08-19] citation", False),
    ]

    failures = 0
    for src, want in strip_cases:
        got = scrub_text(src)
        if got != want:
            failures += 1
            print(f"FAIL strip: {src!r}\n  got:  {got!r}\n  want: {want!r}")
    for src in preserve_untouched:
        got = scrub_text(src)
        if got != src:
            failures += 1
            print(f"FAIL preserve: {src!r}\n  got: {got!r}")
    for src, want_residual in residual_cases:
        has = bool(list(find_residual_phones(scrub_text(src))))
        if has != want_residual:
            failures += 1
            print(f"FAIL residual: {src!r} expected residual={want_residual}, got {has}")

    total = len(strip_cases) + len(preserve_untouched) + len(residual_cases)
    if failures:
        print(f"\n{failures}/{total} selftest checks FAILED")
        return 1
    print(f"All {total} selftest checks passed.")
    return 0


def main(argv):
    args = [a for a in argv if not a.startswith("--")]
    flags = {a for a in argv if a.startswith("--")}
    if "--selftest" in flags:
        return selftest()
    dirs = args or ["wiki"]
    return run(dirs, dry_run="--dry-run" in flags)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
