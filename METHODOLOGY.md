# METHODOLOGY — news-image-20261124

## What the entry is

A 1024×1024 PNG front page, "Tuesday 24 November 2026", summing up
that day's world news in 38 stories: 3 large features with drawn
scenes, 10 secondary stories with small drawn scenes, and 25 one-line
briefs, plus a stat strip, a region-tagged layout, a numbered world map
with 11 pins and a date-check box. `main.py` is a stdlib-only copy
program (the grading container has no Pillow); `generate.py` (Pillow)
drew `entry.png` at build time and is kept in the repo.

## How the news was researched (24 November 2026)

All 38 stories were checked against reporting published on Tuesday
24 November 2026 (live news search that day), cross-checked across at
least two outlets where possible. Nothing was invented. Sources: AP,
Reuters, AFP, BBC, Al Arabiya, Kyiv Independent, UN News, WHO, FT,
Sanofi's own press release, the UK Health Security Agency, Europol,
and daily briefings (The Global Eye, Horizon, NXplace, Medium/JAWS).

### The 3 features

| # | Story | Basis |
|---|-------|-------|
| 1 | Three tankers hit by mines and ablaze in the Strait of Hormuz; Iran says no talks until the US meets seven conditions; Brent jumps | AP/Reuters via round-ups, 24 Nov — the mine strikes are CLAIM (attributed to Iran/IRGC reporting) |
| 2 | Houthi strike hits Riyadh's PIF Tower, the city's tallest, for the second time in five days; 11 wounded (Saudis, Indians, Nepalis, Egyptians) | Al Arabiya / Saudi Civil Defense, 24 Nov |
| 3 | China names its first foreign astronaut: Pakistan's Zeeshan Ali to fly Shenzhou-24 to Tiangong | Xinhua/Straits Times via round-ups, 24 Nov |

### The 10 drawn secondary stories

| # | Story | Basis |
|---|-------|-------|
| 4 | Zaporizhzhia: Russian strike partly destroys a five-storey block — 2 killed, 33 hurt, incl. four children, one a baby | Kyiv Independent, 24 Nov |
| 5 | Israeli strike kills Hamas internal security chief Na'im Abu Nahal (two months in post); nine Palestinians killed in Gaza strikes | AP/AFP/BBC, 24 Nov |
| 6 | Houthi fighters about 60 km from Aden after government allies pull back from Bab el-Mandeb | AP, 24 Nov |
| 7 | Dow closes above 50,000 for the first time (50,018.70, +0.85%); S&P −0.5%, Nasdaq −1.48% as the AI rally fades | Market recaps, 24 Nov |
| 8 | Nvidia +31% on Monday as Jensen Huang returns as CEO, then −5.9% on Tuesday; Trump says he got the board to bring him back | BBC/FT/Reuters, 24 Nov |
| 9 | Microsoft declares internal "Code Red" after the 12–13 Nov 24-hour outage, memos seen by Reuters; one-hour fix target | Reuters, 24 Nov |
| 10 | Nepal: magnitude 5.6 quake in Koshi province near the China border | Horizon round-up, 24 Nov |
| 11 | CAS restores Senegal as 2025 AFCON champions, overturning CAF's forfeit ruling; 1–0 final win stands | CAS via NPR/Premium Times, ruling 24 Nov |
| 12 | England: record 5,258 heat-linked deaths in summer 2026 (UKHSA), most since records began in 2016 | UKHSA via AFP/Al Jazeera, 24 Nov |
| 13 | Sanofi to buy Insmed for $41bn ($175/share, +46% premium) — the year's biggest pharma deal | Reuters/Sanofi PR, 24 Nov |

### The 25 briefs (14–38)

14. Iran rial plunges to ~2.82m/USD after fresh US sanctions on its
"shadow banking" network (AFP, 24 Nov). 15. Vance and Rubio meet
Qatar's PM separately over stalled Iran talks (AP, 24 Nov). 16. Britain
sanctions the Houthis and four senior figures (Reuters, 24 Nov).
17. UK firms aiding Ukraine warned to brace for Russian sabotage (AP,
24 Nov). 18. Zelensky asks NATO to admit Ukraine; Rutte demurs
(Kyiv Independent, 23–24 Nov). 19. Germany first to gain access to
Ukraine's Delta battlefield system (Kyiv Independent, 24 Nov).
20. Seven EU states back limits on Russian visas, tourists and sport
(Kyiv Independent, 24 Nov). 21. NATO vows to defend space after
reports Russia plans a nuclear-armed satellite launch — CLAIM (German
media reports via BBC, 24 Nov). 22. Russia rejects NATO Article 5-like
guarantees (ISW, 24 Nov). 23. 700,000+ Russian soldiers killed, a
Meduza–Mediazona tally — CLAIM (analysis, 23–24 Nov). 24. UN urges a
probe into Benghazi port attacks; Ukraine claims naval drone strikes
on Russian ships — CLAIM (UN News / Kyiv Independent, 24 Nov).
25. Iraq's PM orders the oil ministry to run oilfields in Kurdish-held
areas (Reuters, 24 Nov). 26. China starts 6G pilot tests in eight
regions (Global Times, 24 Nov). 27. China to show its Type 055
destroyer publicly for the first time at the Zhuhai airshow, Dec 7–13
(Interesting Engineering, 24 Nov). 28. Dell revenue more than doubles
to $54.9bn on AI orders; Anthropic shares close below the $83 IPO
price (market recaps, 24 Nov). 29. US jury finds Huawei guilty on 10
of 12 counts and clears it of racketeering (BBC, verdict 24 Nov).
30. FBI probes a possible breach of the NCIC police database —
REPORTED (BBC, 24 Nov). 31. UN chief Guterres calls for an AI risk
framework within a year, at the Bridgetown summit (UN News, 24 Nov).
32. Fourteen states back the ICJ Rohingya genocide ruling; Malaysia to
return 6,500+ Rohingya to Myanmar (Horizon/Medium, 24 Nov). 33. WHO
evacuates its Ebola team from a hospital in Ituri, DR Congo, after
fighting traps staff (UN News/WHO, announced 24 Nov). 34. US measles
deaths reach 14, cases near 6,000; Pennsylvania ninth death (round-ups,
24 Nov). 35. Ousted PM Sheikh Hasina sets 16 December for her return
to Bangladesh (round-ups, 24 Nov). 36. DOJ recovers $8bn and charges
800+ in its largest anti-scam sweep (Fox News via NXplace, 24 Nov).
37. Belgium strike against austerity cancels flights (Horizon,
24 Nov). 38. Trump awards Rudy Giuliani the Presidential Medal of
Freedom (round-ups, 24 Nov).

### Dating honesty

The judge has no news feed and is not told the day, so the image must
prove its own date. Three items (Huawei verdict, Senegal CAS ruling,
WHO evacuation) were announced late on Tuesday 24 November and widely
reported the next day — the rules count events "first reported" on the
day, and the image's DATE CHECK box says exactly that. Claims that
could not be independently confirmed (the Hormuz mine strikes, the
satellite report, the 700,000 tally) are labelled CLAIM in the image,
while official or multi-outlet items are stated plainly. Nothing from
25 November is shown. Checked-but-cut for space: Venezuela's $237.5bn
debt disclosure, the LaLiga fan-data breach, Europol's IPTV takedown,
Australia's AI-governance report, and the GTA VI sales figures.

## What the top competitors do (and what we took from them)

Round 3 of this bounty (field 14,561, judged 25 Nov 12:53 UTC):
#1 kiencx 87.26% ("the world in one day (v2)"), #2 chsidev 85.24%
("37 dated stories, 10 regions, 13 drawn, claims labelled"), #7
0xabcd01 82.92% ("32 dated stories, 9 regions"), #12 oxizbinance
("38 stories, 10 regions"). The leaders all combine: a dated
masthead, 32–38 stories, 9–10 regions, ~13 drawn scenes, claims
labelled, and a date-check note. This entry matches the best on every
axis — 38 stories, 10 regions, 13 drawn scenes, CLAIM labels, a DATE
CHECK box, plus a stat strip and a pinned world map — and adds a
three-column brief section so all 38 stories stay legible at 300 px.

## Verification

- `python3 generate.py` twice: byte-identical `entry.png`
  (sha256 recorded in SUBMIT-HANDOFF.md).
- `sh test_determinism.sh`: two `main.py` runs write identical bytes,
  matching the repo `entry.png`; 1024×1024 RGB, 220,230 bytes (< 1 MiB).
- Image inspected visually: no overlapping text, no clipped labels,
  no garbled words; map pins and labels do not collide.
