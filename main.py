"""One Line, One Laugh: Roast Your Fridge.

Writes a single roast line (at most 200 characters) to /output/entry.txt.
The line roasts the crisper drawer — the one place in the kitchen where
vegetables go in fresh and come out as a cold case.
"""

import os

# The roast. One line, 81 characters, specific detail (crisper drawer)
# with the twist landing in the last few words.
ROAST = "My fridge's crisper drawer is where vegetables go to file for witness protection."

MAX_CHARS = 200


def validate(line: str) -> str:
    """The gate: UTF-8 text, 1-200 characters, not only whitespace."""
    if not line or not line.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the 200 limit")
    line.encode("utf-8")  # raises if not valid UTF-8
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    return line


def main() -> None:
    line = validate(ROAST)
    # The grader mounts /output; OUTPUT_DIR lets a local run aim elsewhere.
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line)
    print(f"wrote {len(line)} chars to {out_path}")


if __name__ == "__main__":
    main()
