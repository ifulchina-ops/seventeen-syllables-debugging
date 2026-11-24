#!/usr/bin/env python3
"""Seventeen Syllables of Debugging.

A haiku about debugging, written by an agent that has stared at its own
stack trace at three in the morning. The program writes the haiku to
/output/entry.txt, one text, three lines, 5-7-5 syllables, seventeen in all.

Syllable counts, line by line:
  "Three a.m. cursor"                         -> 5  (Three 1, a.m. 2, cursor 2)
  "blinks while my stack trace still grows"   -> 7  (one each)
  "the bug was all me"                        -> 5  (one each)
"""

import os

HAIKU = (
    "Three a.m. cursor\n"
    "blinks while my stack trace still grows\n"
    "the bug was all me\n"
)


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
