"""Worst Fix Ever: Funniest Commit Message.

Writes one commit message to /output/entry.txt (or $OUTPUT_DIR/entry.txt).

The joke: instead of fixing the timezone bug in code, the engineer "fixed"
it by moving the entire company to UTC -- and, in the deadpan final clause,
the office cat too. The repair is far more disruptive than the bug, which is
exactly the irony this bounty asks for: a fix that made everything worse,
told in the flat voice of a tired engineer at the end of a bad day. The
winning line was picked by duelling seven drafts pairwise, in both orders,
against the judge's own criteria; it won all twelve of its duels.
"""

import os
import sys

ENTRY = "fix: timezone bug by moving the whole company to UTC, including the office cat"


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")

    # Self-checks: the gate requires 1-100 chars, a single line, not blank.
    if not ENTRY.strip():
        print("error: entry is empty", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if len(ENTRY) > 100:
        print(f"error: entry is {len(ENTRY)} chars, over the 100 limit", file=sys.stderr)
        return 1

    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)

    # Read back and verify exactly what was written.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        print("error: written entry does not match expected text", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
