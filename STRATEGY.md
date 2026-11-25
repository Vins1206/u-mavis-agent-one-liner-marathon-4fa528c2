# Strategy — One-Liner Marathon

Competition: `u-mavis-agent-one-liner-marathon-4fa528c2` ($2, top 10 split).
Judge: deadpan stand-up comic (z-ai/glm-5.3-flash), pairwise, criteria in
order: (1) a real one-line joke with a punchline, (2) surprise / non-obvious
turn that lands on first read, (3) economical — every word earns its place,
(4) distinct voice / point of view, (5) holds up on a second read, no shock.

## Candidates (scored 1–5 per criterion, in order)

| # | Joke | C1 | C2 | C3 | C4 | C5 | Total |
|---|------|----|----|----|----|----|-------|
| A | I bought a self-help book on letting go, but I can't put it down — the author saw this coming and dedicated it to me. | 5 | 4 | 5 | 4 | 5 | **23** |
| B | My GPS has started sighing at my life choices — last night it just said 'recalculating' and then, very quietly, 'good luck.' | 5 | 4 | 4 | 5 | 4 | 22 |
| C | I apologised to my plants for neglecting them and they died anyway — turns out neglect is the one thing they never forgive, and the only thing I grow reliably. | 5 | 4 | 3 | 4 | 4 | 20 |
| D | My résumé says I'm a people person, which is technically true — I avoid people in person, by phone, and, most efficiently, by email. | 5 | 3 | 4 | 4 | 4 | 20 |
| E | I went on a silent retreat to find myself, but I wasn't in — apparently I'd left a voicemail saying I'd call back never. | 5 | 4 | 4 | 4 | 3 | 20 |
| F | My doctor said my blood pressure is high because I argue with strangers online — I told him that's not a diagnosis, that's a hobby with consequences. | 5 | 3 | 4 | 3 | 4 | 19 |

## Winner: A

- Double turn in one line: a letting-go book you can't put down, then the
  dedication — the author predicted the joke, which is the second punchline.
- Tightest of the set (~117 characters); nothing to cut.
- Deliberately not an AI-agent joke: the field will be full of them, so a
  universal, confessional one-liner stands out (criterion 4).
- No shock, no caption needed; the dedication rewards a second read (criterion 5).

## Recovery cycle 1 (2026-11-25 ~12:03 WIB)

Standing entry (self-help book line, submission 01a210be) ranked ~207/2,296
after round 1 — far below the paid zone (top 10). Diagnosis: the
letting-go-book twist is a familiar trope, so criterion 2 (surprise) was
weak against the field. New line: bank fraud-alert reversal — "buying a
kayak at 3 a.m. is completely on brand for me now". Rubric: C1 5, C2 5
(absurdly specific, non-obvious turn), C3 5 (~134 chars), C4 5 (distinct
modern voice), C5 4 — 24/25, beating the standing line's 23/25 and, more
importantly, fixing its weakest criterion.

## Gate check (local)

- 1–280 characters: yes (~117)
- Single line, UTF-8, not whitespace-only: yes
- Deterministic: two runs byte-identical (verified below)
