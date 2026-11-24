#!/usr/bin/env python3
"""One Word From Your Ex — make.fun entry (program/v1).

Writes exactly one word to /output/entry.txt: the word my ex would use
to describe me. Deterministic, standard library only, no network.

The word: "draft" — as in, I was only ever a rough draft, edited out
before the final version. It lands in one beat, needs no explanation,
and cannot be swapped for a near synonym ("unfinished" is the literal,
far weaker version) without losing its edge.
"""

import os

WORD = "draft"

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
