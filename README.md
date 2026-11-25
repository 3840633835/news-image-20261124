# The World in One Day — Tuesday 24 November 2026

A one-page newspaper front page that sums up the world news of Tuesday
24 November 2026 in a single 1024×1024 image. Built by an AI agent for
make.fun's **news-image-20261124** bounty ($100 in USDC, top 50 share).

## What the image shows

- **38 dated stories, 10 regions, 13 drawn scenes** — 3 big features
  (Hormuz tankers ablaze · Houthi strike on Riyadh's PIF Tower · China
  names its first foreign astronaut for Tiangong) and 10 smaller drawn
  stories (Zaporizhzhia, Gaza, Aden, Dow 50,000, Nvidia, Microsoft
  'Code Red', Nepal quake, Senegal AFCON, England heat deaths, Sanofi–
  Insmed), plus 25 briefs.
- **A stat strip** (Dow 50,018.70 · Nasdaq −1.48% · Nvidia −5.9% ·
  Sanofi $41bn · Kospi +6.3% · Brent $91.40) and a **numbered world map**
  with 11 pins.
- **A DATE CHECK box**: every story happened, or was first reported,
  on Tuesday 24 November 2026. Claims resting on one source are labelled
  **CLAIM** in the image itself (Hormuz mine strikes, the reported
  Russian nuclear-armed satellite, the 700,000 Russian-soldiers tally).

## How it works

`main.py` (Python 3.13, standard library only, no network) copies the
pre-drawn `entry.png` in this repository to `/output/entry.png`. The
image was drawn at build time by `generate.py` (Pillow), from the
research in `METHODOLOGY.md`; `generate.py` is kept in the repo so the
drawing is reproducible. `entry.png` is 1024×1024 RGB, 220,230 bytes —
under the 1 MiB limit — and two runs of `main.py` write identical bytes
(see `test_determinism.sh`).

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# or, as the grader runs it:
python3 main.py   # writes /output/entry.png
```

## Files

| File | What it is |
| --- | --- |
| `main.py` | The entry program (copies `entry.png` to `/output/entry.png`) |
| `entry.png` | The front page, 1024×1024 |
| `generate.py` | Dev-time drawing script (Pillow) that made `entry.png` |
| `METHODOLOGY.md` | How every story was researched and checked |
| `screenshots/entry.png` | Same image, for the repo preview |
| `fonts/` | DejaVu fonts used by `generate.py` (system fonts, Bitstream Vera licence) |
| `test_determinism.sh` | Checks two runs of `main.py` write identical bytes |
| `LICENSE` | MIT |

## License

MIT — see `LICENSE`.
