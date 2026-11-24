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


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)
    print(f"Characters: {len(ENTRY)}")


if __name__ == "__main__":
    main()
