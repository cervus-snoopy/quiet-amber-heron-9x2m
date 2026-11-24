#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — one line, under 200 characters.

Writes the excuse to $MAKEFUN_OUTPUT_DIR/entry.txt as UTF-8 text with no
trailing newline, readable by every user.
"""

import os

ENTRY = (
    "Can't come in today \u2014 colonoscopy prep starts at 6am, so until noon "
    "my office is the bathroom and stepping away from my desk is a medical "
    "emergency."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    os.chmod(out_dir, 0o755)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
