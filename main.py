#!/usr/bin/env python3
"""The GPS Swears It Was a Shortcut — make.fun entry.

Writes the GPS's own one-line excuse for sending the driver down the
wrong road to /output/entry.txt. Python 3.13 standard library only.
"""

import sys
from pathlib import Path

LINE = (
    "The map swore that cul-de-sac was a shortcut, and frankly "
    "I trust the map more than I trust your driving."
)


def main() -> int:
    # The gate requires 1-200 characters of UTF-8 text, a single line.
    line = LINE.strip()
    assert "\n" not in line, "excuse must be a single line"
    assert 1 <= len(line) <= 200, f"excuse is {len(line)} chars, must be 1-200"
    output_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(line + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
