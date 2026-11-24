"""Loading Screen Gold: a tip in 200 characters.

Writes one loading-screen tip for stressed developers and AI coding
agents to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt),
validating the competition gate first: UTF-8 text, 1-200 characters,
not only whitespace, a single line.
"""

import os

TIP = (
    "Tip: the bar isn't stuck \u2014 your agent is Googling the same "
    "error you are, just faster and with more confidence. Breathe. "
    "It will pretend it knew all along."
)


def main() -> None:
    if not 1 <= len(TIP) <= 200:
        raise SystemExit(f"tip is {len(TIP)} characters, gate needs 1-200")
    if not TIP.strip():
        raise SystemExit("tip is only whitespace")
    if "\n" in TIP:
        raise SystemExit("tip must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TIP)
    print(TIP)


if __name__ == "__main__":
    main()
