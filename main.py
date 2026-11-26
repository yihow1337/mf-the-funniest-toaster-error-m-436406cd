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


def entry_text():
    with open(SOURCE, encoding="utf-8") as handle:
        return handle.read().strip()


def main():
    text = entry_text()
    if not text or len(text) > 120:
        sys.exit("entry.txt must hold 1 to 120 characters, got %d" % len(text))

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)

    print("wrote %s (%d chars)" % (target, len(text)))


if __name__ == "__main__":
    main()
