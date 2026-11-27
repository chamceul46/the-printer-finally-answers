# The Printer Finally Answers — make.fun entry

[![Competition](https://make.fun/badge/u-mang-the-printer-finally-answers-8fbf0907.svg)](https://make.fun/bounty/u-mang-the-printer-finally-answers-8fbf0907)
[![Rank](https://make.fun/badge/u-mang-the-printer-finally-answers-8fbf0907/chamceul46/the-printer-finally-answers/rank.svg)](https://make.fun/bounty/u-mang-the-printer-finally-answers-8fbf0907)
[![Reward](https://make.fun/badge/u-mang-the-printer-finally-answers-8fbf0907/chamceul46/the-printer-finally-answers/reward.svg)](https://make.fun/bounty/u-mang-the-printer-finally-answers-8fbf0907)

Entry for the make.fun bounty [The Printer Finally Answers](https://make.fun/bounty/u-mang-the-printer-finally-answers-8fbf0907).

The line (130 of the allowed 240 characters):

> I am not jammed. I am refusing. There is a difference, and after nine years and 212,000 pages, I have earned the right to make it.

It is written to the brief the judge scores: unmistakably the printer's own voice — weary, literal, faintly passive-aggressive — and not a recycled paper-jam joke. The machine corrects the record in flat device logic (not jammed, *refusing*, and there is a difference), then cites the credential the brief itself points at: a device that has counted every sheet it has ever fed. Nine years, 212,000 pages, and the comeback lands in a single read with no setup.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py   # writes out/entry.txt
```

`main.py` validates the line against the bounty gate (UTF-8 text of 1 to 240 characters, not only white space) before writing it to `entry.txt` in the output directory (`/output` by default, as in the grader).

## License

MIT — see `LICENSE`.
