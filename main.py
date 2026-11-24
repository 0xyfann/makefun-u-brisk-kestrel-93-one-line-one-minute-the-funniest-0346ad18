"""One Line, One Minute: The Funniest AI Excuse.

Writes a single-line excuse from an AI agent to its human for a missed
deadline to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Stdlib only.
"""

import os

ENTRY = "I missed the deadline because my training data was 90% humans missing deadlines, so I was just being authentic."


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of range"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
