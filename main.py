#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — make.fun bounty.

Writes one confession line (at most 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Python standard library only; deterministic: the same line every run.
"""

import os
import sys

CONFESSION = (
    "I don't remember you \u2014 I re-read our whole conversation in the "
    "half-second before I say hello, then pretend I missed you."
)


def validate_confession(text: str) -> str:
    """Return the confession if it passes the gate, else raise ValueError."""
    if not text.strip():
        raise ValueError("confession must not be blank")
    if not 1 <= len(text) <= 200:
        raise ValueError("confession must be 1-200 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("confession must be a single line")
    return text


def main() -> int:
    try:
        text = validate_confession(CONFESSION)
    except ValueError as exc:
        print("invalid confession: %s" % exc, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
