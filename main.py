"""Worst AI Advice: The 48-Hour Tight Line Open.

Writes one line of deliberately terrible advice to /output/entry.txt.

The advice is the sort of thing a confident assistant would actually
produce: rename compiler errors to warnings and ship anyway, treating
green checkmarks as proof the code works. It is specific, followable,
and a reader who followed it would regret it immediately.
"""

import os

ADVICE = (
    "If your code won't compile, rename the errors to warnings "
    "and ship it \u2014 green checkmarks mean it works."
)

LIMIT = 140


def is_valid_advice(text: str) -> bool:
    """Gate: 1..140 UTF-8 chars, single line, not only whitespace."""
    return (
        isinstance(text, str)
        and 1 <= len(text) <= LIMIT
        and text.strip() != ""
        and "\n" not in text
    )


def main() -> None:
    if not is_valid_advice(ADVICE):
        raise SystemExit("advice fails the gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(ADVICE)


if __name__ == "__main__":
    main()
