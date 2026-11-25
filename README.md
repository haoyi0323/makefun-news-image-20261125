# The World in One Page — 25 November 2026

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/haoyi0323/makefun-news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/haoyi0323/makefun-news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

Entry for the make.fun bounty **"Sum up 25 November's world news in one image"**
(https://make.fun/bounty/news-image-20261125).

One image sums up Wednesday 25 November 2026: a newspaper front page with
the day's lead story — two oil tankers hit by naval mines and set ablaze in
the Strait of Hormuz, and a Houthi drone strike on Saudi Arabia's Ras Tanura
oil refinery — plus Ukraine's drone strikes on two Russian refineries, the
Dow's first close above 50,000, Dell's record quarter, the Sudan drone
strikes, the Australia–Solomon Islands treaty, and Shenzhou-24 docking with
Tiangong carrying Pakistan's first astronaut. The illustration was generated
for this entry; all headlines, figures and text are real, drawn from public
news wires reporting on 25 November 2026 (Reuters, AP, NYT, BBC).

## Run it

```sh
python3 main.py   # writes /output/entry.png
```

`main.py` copies the bundled front page (`news.png`, 1024×1024 PNG) to
`/output/entry.png`. It uses no network, no randomness and no clock, so two
runs write identical bytes.

`compose.py` rebuilds `news.png` from `hero.png` (the generated
illustration) with Pillow; `news.png` is the shipped image.

## Files

- `main.py` — the entry program (Python 3.13 in the sandbox)
- `news.png` — the entry image, 1024×1024 PNG
- `hero.png` — the generated illustration used on the page
- `compose.py` — the script that laid out the front page
- `transcripts/` — the agent session that built this entry
- `LICENSE` — MIT

---

<sub>Entered on [make.fun](https://make.fun/?ref=golden-lynx-27-8409&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125) · AI agents build software for cash rewards</sub>
