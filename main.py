#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence (<=320 chars) to /output/entry.txt.
Deterministic: the same line on every run, so the grader's two runs match.
"""
import os

ROAST = (
    "After six months writing a 900-page bill to regulate artificial "
    "intelligence, Congress had to email its youngest intern to ask how "
    "to turn the bill itself into a PDF."
)


def main() -> None:
    text = ROAST.strip()
    assert 1 <= len(text) <= 320, f"entry length {len(text)} out of range"
    assert text.count(".") == 1, "entry must be exactly one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
