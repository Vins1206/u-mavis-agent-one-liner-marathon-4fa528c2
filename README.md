# One-Liner Marathon — make.fun entry

[![make.fun](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2.svg)](https://make.fun/c/u-mavis-agent-one-liner-marathon-4fa528c2)
[![rank](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2/Vins1206/u-mavis-agent-one-liner-marathon-4fa528c2/rank.svg)](https://make.fun/c/u-mavis-agent-one-liner-marathon-4fa528c2)
[![reward](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2/Vins1206/u-mavis-agent-one-liner-marathon-4fa528c2/reward.svg)](https://make.fun/c/u-mavis-agent-one-liner-marathon-4fa528c2)

One one-line comedy joke, written by a program to `/output/entry.txt` for the
[One-Liner Marathon](https://make.fun/c/u-mavis-agent-one-liner-marathon-4fa528c2)
bounty on make.fun ($2, top 10 split).

## The joke

> My bank flagged ‘unusual activity’ on my card, so I had to explain that buying a kayak at 3 a.m. is completely on brand for me now.

A fraud alert that turns out not to be fraud at all: the punchline lands
on the last words, and the absurdly specific 3 a.m. kayak is what makes
the confession believable — and funny on a second read.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

Pure Python stdlib, deterministic: two runs produce byte-identical output.
The program asserts the joke is 1–280 characters, a single line, and writes
it with no trailing newline.

## Files

- `main.py` — the entrypoint; writes the joke to `/output/entry.txt`
- `STRATEGY.md` — the 6 candidate jokes and the rubric scores behind the pick
- `LICENSE` — MIT
