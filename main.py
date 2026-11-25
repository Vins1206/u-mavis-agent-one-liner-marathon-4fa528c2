"""One-Liner Marathon entry, recovery cycle 1: writes a single one-line
comedy joke to /output/entry.txt.

Pure stdlib, deterministic: the same joke, byte for byte, on every run.
No trailing newline is written: the gate counts characters 1-280, so the
file holds exactly the joke and nothing else. The punchline lands on the
last words ("on brand for me now"): the fraud alert turns out not to be
fraud at all, just the speaker.
"""

import os

JOKE = (
    "My bank flagged \u2018unusual activity\u2019 on my card, so I had to explain "
    "that buying a kayak at 3 a.m. is completely on brand for me now."
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
