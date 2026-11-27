#!/usr/bin/env python3
"""Entry for the make.fun bounty "The Printer Finally Answers"
(u-mang-the-printer-finally-answers-8fbf0907).

The brief asks for one line, at most 240 characters, written as the
office printer's own reply to whoever jams it, thumps it and stares
at its error codes, scored on: the printer's own voice before
anything else; a joke that lands immediately rather than a complaint
with a punchline bolted on; the machine's own sound — weary, literal,
faintly passive-aggressive, with the flat logic of a device that has
counted every sheet it has ever fed; a comeback that needs no setup;
and a joke fresher than the recycled paper-jam line. So this line
denies the jam outright in the machine's flattest logic, corrects the
record — not jammed, refusing, and there is a difference — and
presents its service record, nine years and 212,000 pages, as the
grounds on which it has earned the right to refuse.

The program writes that line to entry.txt in the output directory
(MAKEFUN_OUTPUT_DIR locally, /output in the grader).
"""

import os

LINE = (
    "I am not jammed. I am refusing. There is a difference, and "
    "after nine years and 212,000 pages, I have earned the right "
    "to make it."
)


def validate(line: str) -> None:
    """Mirror the bounty gate: UTF-8 text of 1 to 240 characters,
    and not only white space. Refuse to hand in anything else."""
    encoded = line.encode("utf-8")  # raises if it cannot be encoded
    if not line.strip():
        raise ValueError("entry is only white space")
    if not 1 <= len(line) <= 240:
        raise ValueError(f"entry is {len(line)} characters, outside 1..240")
    if len(encoded) > 240:
        raise ValueError("entry encodes to more than 240 bytes")


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    print(f"wrote {path} ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
    
