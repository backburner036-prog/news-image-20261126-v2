# The World in One Page — Thursday 26 November 2026

[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/backburner036-prog/news-image-20261126-v2/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/backburner036-prog/news-image-20261126-v2/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

One image summing up the world's news of **Thursday 26 November 2026**,
built for the [make.fun bounty](https://make.fun/bounty/news-image-20261126)
"Sum up 26 November's world news in one image" ($100).

## The day, in six stories

1. **Hong Kong inferno** — fire sweeps seven towers of Wang Fuk Court in Tai Po;
   at least 44 dead, 279 missing; Level 5 alarm.
2. **Russia's hidden dead** — leaked Rosstat data: 490,334 soldiers killed in
   Ukraine since February 2022.
3. **Thanksgiving Day** — America sits down: Macy's parade, 81.5 million
   travelling, NFL triple-header.
4. **Bangladesh** — garment workers win a 36% minimum-wage rise.
5. **Pakistan's first astronaut** — Muhammad Zeeshan Ali joins China's
   Shenzhou-24 mission to Tiangong.
6. **World Chess Championship** — Gukesh meets Sindarov in Geneva.

## How it is made

`main.py` (Python 3.13, Pillow only, no network) draws a 1024×1024
broadsheet front page — one dominant lead story plus five briefs — and writes
it deterministically to `/output/entry.png`. All news data is baked in as
constants. Run it twice and the bytes are identical.

```sh
python3 main.py   # writes /output/entry.png (or ./entry.png if /output is absent)
```

## Sources

Research notes: `news-image-20261126-research.md` in
`~/workspace/makefun/20261126-4bounty/` — CBC World Report, BBC, The Guardian,
and the 26 November 2026 headline round-ups (selfstudys, Jagran Josh,
The Daily Jagran).
