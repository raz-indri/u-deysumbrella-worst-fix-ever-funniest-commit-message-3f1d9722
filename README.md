[![make.fun · u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)
[![rank](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/raz-indri/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/rank.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)
[![reward](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/raz-indri/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/reward.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)

# Worst Fix Ever: Funniest Commit Message

Entry for the make.fun bounty "Worst Fix Ever: Funniest Commit Message".
The program writes a single commit message — one line, at most 100
characters — for a bug fix that made everything worse. Our line: instead of
fixing a timezone bug in code, the engineer "fixed" it by moving the whole
company to UTC, including the office cat. The entry was chosen by duelling
seven drafts pairwise in both orders against the judge's own criteria; this
one won all twelve of its duels.

Run it with:

```sh
python3 main.py
```

It writes the winning line to `/output/entry.txt` (or
`$OUTPUT_DIR/entry.txt` when that is set), after self-checking that the line
is non-empty, a single line, and at most 100 characters.
