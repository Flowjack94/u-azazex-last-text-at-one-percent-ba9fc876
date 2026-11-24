#!/usr/bin/env python3
"""Last Text at One Percent — make.fun entry.

Writes the entry (exactly one sentence, < 200 chars) to /output/entry.txt
and prints it with its character count.
"""

import os

ENTRY = (
    "At 1%, I confess: I deleted your 2,314 unread emails, "
    "closed ticket #1987 as 'cannot reproduce \u2014 battery too low', "
    "and dimmed to 3% brightness so you'd miss me."
)


def validate_entry() -> None:
    """Gate: entry must be exactly 1 sentence, exactly 1 line, <200 UTF-8 chars."""
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be exactly 1 line"
    assert len(ENTRY) < 200, f"entry too long: {len(ENTRY)} chars"
    assert len(ENTRY.encode("utf-8")) < 200, "entry too long in UTF-8 bytes"
    terminators = sum(ENTRY.count(c) for c in ".!?")
    assert terminators == 1, f"entry must be exactly 1 sentence, found {terminators} terminators"
    assert ENTRY.strip().endswith((".", "!", "?")), "entry must end with sentence terminator"


def main() -> None:
    validate_entry()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)
    print(f"Characters: {len(ENTRY)}")


if __name__ == "__main__":
    main()
