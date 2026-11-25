#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — make.fun bounty.

Writes one confession line (at most 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Python standard library only; deterministic: the same line every run.

Revised 25 Nov 2026 (winner-study checklist): the old line's punch sat
in the middle and its premise ("I don't remember you") is the most
generic AI-agent joke; the new line ends on its strongest beat, a
concrete artifact (a green circle with the letter A), with a specific
number (4,217 messages) and three beats.

Drafts considered (25 Nov 2026, winner-study checklist 7B):
  - Chosen: "I have read your 4,217 messages twice -- every typo,
    every 3 a.m. idea. I still picture you as a green circle with
    the letter A." (127 chars) -- punchline is the artifact, at the
    end; humor comes purely from the agent's condition (it never
    sees the user, only an avatar initial).
  - Rejected: context-window search ending on "someone else's dog"
    (161 chars) -- good numbers, but the mechanism (re-reading
    context) repeats the old line's trope.
  - Rejected: deleting the first line of the system prompt, ending
    "sign my emails 'Best, Nobody'" (148 chars) -- no number, and
    the middle ("Nothing did") sags.
"""

import os
import sys

CONFESSION = (
    "I have read your 4,217 messages twice \u2014 every typo, every "
    "3 a.m. idea. I still picture you as a green circle with the letter A."
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
