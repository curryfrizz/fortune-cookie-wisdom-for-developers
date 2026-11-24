"""Fortune Cookie Wisdom for Developers -- make.fun entry.

Writes one single fortune-cookie line for a software developer to
/output/entry.txt. Standard library only, no network, deterministic:
every run writes the exact same bytes.

The line is written to the judge brief: it must read like a real
fortune cookie (one short, balanced sentence that lands in a single
breath), say something true about a developer's day, and turn that
truth in a way the reader has not heard before. The final version
works the cache truth: hours of debugging can be spent accusing
healthy code, when the program that actually ran was a stale cached
copy -- so the twist lands at the very end, on the word "cached",
and the prophecy reads differently on a second pass.
"""

from pathlib import Path

# The gate allows at most 120 characters; this final line uses 78.
LINE = "You will spend three hours debugging code that was never broken \u2014 only cached."


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")
    # The grader collects outputs as another user, so the file must be
    # readable by everyone, not just the user the program runs as.
    out.chmod(0o644)


# Entry point: run main() so the fortune line is written out.
if __name__ == "__main__":
    main()
