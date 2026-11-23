#!/usr/bin/env python3
"""Make the Judge Smile — writes one warm line to /output/entry.txt.

Stdlib only. Output dir comes from $MAKEFUN_OUTPUT_DIR, falling back
to ./output/entry.txt for local runs.
"""

import os

# Revised line: sharper concrete detail (7 a.m., still-warm krupuk,
# "kid") and a stronger surprise turn in the closing clause.
ENTRY = (
    "At 7 a.m. the warung lady slipped a still-warm krupuk into my "
    "takeaway and whispered, 'for luck, kid' \u2014 and my whole "
    "Tuesday suddenly tasted like a win."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
