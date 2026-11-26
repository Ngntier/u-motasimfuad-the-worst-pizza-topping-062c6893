#!/usr/bin/env python3
"""The Worst Pizza Topping — one funny line pitching a terrible pizza topping.

Writes the entry to entry.txt inside MAKEFUN_OUTPUT_DIR (default /output).
The grader reads /output, so the output directory is honoured exactly.
"""

import os

# The pitch: a pizza topped with dryer lint. The joke turns on the topping
# fighting back — the slice crackles with static, and the taste lands as a
# warm sock that lost a bet. Names the pizza ("Dryer Lint pizza"), names the
# topping (lint), and makes it sound awful without a gross-out list.
ENTRY = (
    "New: the Dryer Lint pizza \u2014 a full load of lint on every slice, "
    "so it crackles with static and tastes like a warm sock that lost a bet."
)


def validate(text: str) -> None:
    """Gate: 1-200 chars, a single line, not only whitespace, valid text.

    Also rejects leading/trailing whitespace and control characters, so the
    file the judge reads is exactly the pitch and nothing else.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 0x20 and ch not in "\t" for ch in text):
        raise ValueError("entry must not contain control characters")
    text.encode("utf-8")  # raises if the text is not valid encodable text


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
