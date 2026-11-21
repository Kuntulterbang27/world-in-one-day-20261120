# world-in-one-day-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/Kuntulterbang27/world-in-one-day-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/Kuntulterbang27/world-in-one-day-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

An original 1024×1024 newspaper covering 39 verified Friday news reports across six continents. The lead follows Friday’s responses to Thursday’s Rohingya genocide judgment; numbered source notes distinguish event dates from publication dates.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out python3.13 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=4c8ppp3f&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>

## Rebuild the artwork

The sandbox entry uses Python’s standard library only and copies `news.png` to `entry.png` in `MAKEFUN_OUTPUT_DIR` (default `/output`). It requires no internet, installation or model calls.

For authoring, install the separately pinned `requirements-authoring.txt` with Python 3.13, then run `python render_news.py`. The readable renderer, edited news copy, original map and icons, and bundled OFL fonts are retained here. See `SOURCES.md` for the source/date audit.

Run `python -m unittest discover -p "test_*.py" -v` to validate the image, every PNG checksum, exactly one sandbox output, and deterministic bytes across fresh processes. `test_art.py` additionally needs the authoring dependency.

MIT covers this original artwork and source; fonts retain the SIL Open Font License in `assets/`. The 39 reports comprise one lead and 38 briefs, not 39 briefs plus a lead. No image is generated from live data at execution time.
