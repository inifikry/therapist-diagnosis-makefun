#!/usr/bin/env python3
"""Write one funny AI-therapist diagnosis to /output/entry.txt.

No external dependencies; deterministic output.
"""

import os

LINE = (
    "Clinical diagnosis: acute main-character syndrome, "
    "aggravated by nightly doomscrolling. "
    "Prognosis: terminal, unless you text your mother back."
)


def main() -> None:
    # Self-check against the bounty gate: 1-200 characters, not only whitespace.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} characters"
    assert LINE.strip(), "line must not be only whitespace"
    assert "\n" not in LINE, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
