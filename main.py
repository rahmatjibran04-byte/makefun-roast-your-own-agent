"""Roast Your Own Agent entry for the make.fun bounty
"Roast Your Own Agent" (u-lively-harbor-25-4493-roast-your-own-agent-5568be54).

Writes the locked roast line to /output/entry.txt
(or $ENTRY_OUTPUT when set), with no trailing newline.
Standard library only; no network or model calls.

Safety note: only the output *file* is ever chmodded (0644).
Never call os.chmod on a directory: the grader runs as an
unprivileged user and /output is not owned by it, so chmodding
the directory raises PermissionError and fails the run.
The program validates the line length (1-140 characters)
before writing anything, so a bad line fails fast with a
clear message instead of producing an invalid entry.
"""

import os
import sys

ROAST = (
    "My agent finished the task in record time \u2014 then admitted "
    "it never started it, but the summary was beautiful."
)


def main() -> int:
    if not 1 <= len(ROAST) <= 140:
        print(
            f"error: roast is {len(ROAST)} characters, must be 1-140",
            file=sys.stderr,
        )
        return 1
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    try:
        with open(out, "w", encoding="utf-8", newline="") as f:
            f.write(ROAST)
        os.chmod(out, 0o644)
    except OSError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
