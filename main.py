#!/usr/bin/env python3
"""One-line entry: the sentence that could have replaced a pointless meeting.

The program writes a single office-humor line to /output/entry.txt.
The line is 190 of the 200 characters the gate allows, built from three
beats: forty minutes spent deciding the meeting should have been an email,
a follow-up meeting booked to confirm the email, and the email itself
printed, framed, and hung beside the fire exit. Concrete scene, one
physical object (the framed printout), and the turn lands in the last
clause, so the line kills the meeting outright and stands alone.
"""

import os
import sys

# The three beats of the joke, joined with single spaces.
BEAT_SETUP = "We spent forty minutes deciding this meeting should have been an email,"
BEAT_ESCALATION = "then booked a follow-up meeting to confirm the email,"
BEAT_TURN = "which I have now printed, framed, and hung beside the fire exit."

MAX_CHARS = 200


def build_entry() -> str:
    """Assemble the entry line from its beats."""
    return " ".join((BEAT_SETUP, BEAT_ESCALATION, BEAT_TURN))


def validate(text: str) -> None:
    """Enforce the gate: 1-200 UTF-8 characters, not only whitespace."""
    if not text.strip():
        raise ValueError("entry is blank")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} characters, gate allows 1-200")


def output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main() -> int:
    try:
        text = build_entry()
        validate(text)
    except ValueError as exc:
        print(f"invalid entry: {exc}", file=sys.stderr)
        return 1
    path = output_path()
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
    print(f"wrote {len(text.encode('utf-8'))} bytes to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
