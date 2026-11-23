#!/usr/bin/env python3
"""The One-Line Laugh — writes one funny line to entry.txt.

Stdlib only, no network. The line is a single sentence, under 200
characters, judged on a surprise ending that still makes sense, an
everyday truth people recognise, and economy of words.

Candidate lines weighed (pass 1):
- Passwords: "My passwords are so secure even I can't log in, which
  makes me the only hacker I've ever beaten." (96 chars) Everyday
  truth (everyone has locked themselves out), surprise twist at the
  very end (victim becomes the hacker), economical. CHOSEN.
- Inbox: "I finally cleaned out my inbox, and the only thing left was
  an email from 2019 reminding me to clean out my inbox." Circular and
  cute, but the punchline is telegraphed by the setup — weak surprise.
- Standing desk: "I bought a standing desk so I'd sit less, and now I
  just stand still while doomscrolling." True and relatable, but the
  ending restates the setup rather than turning it.
- Alarm: "I set my alarm for 6 a.m. so I could snooze it six times and
  still feel productive." Relatable, but the twist is mild and the
  shape ("snooze six times") is a familiar joke.

The password line wins: the twist lands in the last five words, it
names a truth everyone has lived, and every word earns its place.

Pass 2 revision: dropped "technically" from the line (108 -> 96 chars).
The judge weighs economy — every word earning its place — and
"technically" only hedges a claim the joke needs stated flat. Head-to-
head re-check vs the inbox line: the inbox joke's twist is visible
from the first clause, while the password line's twist arrives only in
the last five words, so the password line keeps the surprise edge.
"""

import os

LINE = (
    "My passwords are so secure even I can't log in, which "
    "makes me the only hacker I've ever beaten."
)


def main() -> None:
    assert LINE and len(LINE) <= 200, "line must be 1-200 chars"
    assert LINE.count(".") == 1 and LINE.endswith("."), "one sentence"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
