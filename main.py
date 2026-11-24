"""The Funniest Sick-Day Excuse - make.fun entry.

Writes one line (the winning sick-day excuse, picked by a 6-draft
round-robin duel test against the judge's brief) to /output/entry.txt.
The program takes no input and needs no network.

Contract: the file must hold UTF-8 text of 1-200 characters, a single
line, not only white space - the gate refuses anything else.
"""

import os
from pathlib import Path

ENTRY = (
    "Can't make it in \u2014 my cat sat on my laptop, sent my resignation "
    "to the whole team, and now I need a day to unsend my life."
)


def main() -> None:
    text = ENTRY.strip()
    if not text:
        raise SystemExit("entry must not be empty or only white space")
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry must be 1-200 chars, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    out_dir = (
        os.environ.get("OUTPUT_DIR")
        or os.environ.get("MAKEFUN_OUTPUT_DIR")
        or "/output"
    )
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    target = out / "entry.txt"
    target.write_text(text, encoding="utf-8")
    # Round-trip check: what the grader reads must be exactly the entry.
    if target.read_text(encoding="utf-8") != text:
        raise SystemExit("round-trip check failed: entry.txt differs")


if __name__ == "__main__":
    main()
