"""One-Liner Marathon entry: writes a single one-line comedy joke to /output/entry.txt.

Pure stdlib, deterministic: the same joke, byte for byte, on every run.
No trailing newline is written: the gate counts characters 1-280, so the
file holds exactly the joke and nothing else.
"""

import os

JOKE = (
    "I bought a self-help book on letting go, but I can't put it down "
    "\u2014 the author saw this coming and dedicated it to me."
)


def main() -> None:
    if not 1 <= len(JOKE) <= 280:
        raise ValueError(f"joke must be 1-280 characters, got {len(JOKE)}")
    if "\n" in JOKE or JOKE != JOKE.strip():
        raise ValueError("joke must be a single line with no surrounding whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
