#!/usr/bin/env python3
"""Write the competition artifact: one toaster error message, byte-identical
on every run.

The line lives in entry.txt next to this file so the text is the only thing
that ever needs editing. Output goes to $MAKEFUN_OUTPUT_DIR or /output.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.txt")

# The gate: /output/entry.txt is UTF-8 text of 1 to 120 characters, not only
# white space. These are the gate's numbers, not ours, so they live up here
# where they can be checked against the rules at a glance.
ARTIFACT_NAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"
MIN_CHARS = 1
MAX_CHARS = 120


def entry_text():
    """Return the single line of the entry, stripped of surrounding space.

    Stripping is what makes the two graded runs byte-identical regardless of
    whether the source file ends with a newline.
    """
    with open(SOURCE, encoding="utf-8") as handle:
        return handle.read().strip()


def check_gate(text):
    """Fail loudly here rather than quietly handing the gate a bad file."""
    if not text.strip():
        sys.exit("entry.txt is empty or only white space")
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        sys.exit(
            "entry.txt must hold %d to %d characters, got %d"
            % (MIN_CHARS, MAX_CHARS, len(text))
        )


def output_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR


def main():
    text = entry_text()
    check_gate(text)

    target_dir = output_dir()
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, ARTIFACT_NAME)

    # Encoded by hand and written in binary: no newline translation, no
    # trailing newline, so every run writes the same bytes on any platform.
    with open(target, "wb") as handle:
        handle.write(text.encode("utf-8"))

    print("wrote %s (%d chars)" % (target, len(text)))


if __name__ == "__main__":
    main()
