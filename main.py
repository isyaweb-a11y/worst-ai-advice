"""Worst AI Advice: The 48-Hour Tight Line Open.

Writes one line of deliberately terrible advice to /output/entry.txt.

The advice is the sort of thing a confident assistant would actually
produce: rename compiler errors to warnings and ship anyway, treating
green checkmarks as proof the code works. It is specific, followable,
and a reader who followed it would regret it immediately.

The entry must stay a single line of at most 140 characters, so the
program gates the text before writing anything.
"""

import os

ADVICE = (
    "If your code won't compile, rename the errors to warnings "
    "and ship it \u2014 green checkmarks mean it works."
)

LIMIT = 140
OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """Check the advice is a single non-blank line within the limit."""
    return (
        isinstance(text, str)
        and 1 <= len(text) <= LIMIT
        and text.strip() != ""
        and "\n" not in text
        and "\r" not in text
    )


def write_entry(text, path=OUTPUT_PATH):
    """Write the validated advice to the output file."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


def main():
    if not validate(ADVICE):
        raise SystemExit("advice fails the gate")
    write_entry(ADVICE)


if __name__ == "__main__":
    main()
