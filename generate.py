#!/usr/bin/env python3
"""Draw entry.png for make.fun news-image-20261124 (dev-time only).

Tuesday 24 November 2026 in one 1024x1024 newspaper front page:
38 dated stories, 10 regions, 13 drawn scenes (3 big features + 10 small),
a world map with 11 pins, a stat strip and a DATE CHECK box.
Claims that rest on one source are labelled CLAIM in the image itself.

The submitted program is main.py (stdlib only): it just copies the
entry.png this script draws. Run:  python3 generate.py
Deterministic: same bytes every run (fixed seed, fixed fonts, no time).
"""
import math
import os
import random

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")
FONT_DIR = os.path.join(HERE, "fonts")

W, H = 1024, 1024

PAPER = (247, 243, 234)
INK = (24, 24, 22)
NAVY = (18, 38, 66)
NAVY2 = (28, 58, 96)
RED = (178, 34, 28)
GOLD = (176, 132, 40)
TEAL = (14, 110, 110)
GREY = (110, 108, 100)
LINE = (190, 184, 170)
CARD = (255, 255, 255)
SKY = (168, 205, 232)
SEA = (38, 84, 124)
SAND = (224, 200, 150)

random.seed(20261124)


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


F_SERIF = lambda s: font("DejaVuSerif-Bold.ttf", s)      # noqa: E731
F_SERIF_R = lambda s: font("DejaVuSerif.ttf", s)         # noqa: E731
F_SANS = lambda s: font("DejaVuSans-Bold.ttf", s)        # noqa: E731
F_SANS_R = lambda s: font("DejaVuSans.ttf", s)           # noqa: E731


def wrap(draw, text, fnt, width):
    """Greedy word wrap to pixel width; returns list of lines."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= width or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, text, fnt, fill, width, leading=None, align="left"):
    lh = leading or int(fnt.size * 1.28)
    lines = wrap(draw, text, fnt, width)
    for ln in lines:
        if align == "center":
            lx = x + (width - draw.textlength(ln, font=fnt)) / 2
        else:
            lx = x
        draw.text((lx, y), ln, font=fnt, fill=fill)
        y += lh
    return y


def tag(draw, x, y, label, bg, fg=(255, 255, 255)):
    """Small filled tag; returns width used."""
    f = F_SANS(11)
    w = int(draw.textlength(label, font=f) + 10)
    draw.rounded_rectangle([x, y, x + w, y + 16], radius=3, fill=bg)
    draw.text((x + 5, y + 2), label, font=f, fill=fg)
    return w


# ---------------------------------------------------------------- stories
# (headline, standfirst, region) — every item happened or was first
# reported on Tuesday 24 November 2026, checked against AP/Reuters/AFP/
# BBC/UN/WHO/FT reporting that day. CLAIM = single-source or attributed.
FEATURES = [
    ("STRAIT OF HORMUZ",
     "Three tankers hit by mines and ablaze",
     "Iran says no talks until the US meets seven conditions, as three "
     "tankers are reported hit by mines and ablaze in the Strait. CLAIM.",
     "MIDDLE EAST"),
    ("RIYADH",
     "Houthi strike hits the PIF Tower — 11 hurt",
     "A Houthi attack hits Riyadh's tallest tower, in the King Abdullah "
     "Financial District, for the second time in five days. Eleven are "
     "wounded.",
     "MIDDLE EAST"),
    ("TIANGONG",
     "China names its first foreign astronaut",
     "Pakistan's Zeeshan Ali will fly on Shenzhou-24 to China's Tiangong "
     "station — the first foreign astronaut China has named for its own "
     "station.",
     "ASIA"),
]

SECONDARY = [
    ("ZAPORIZHZHIA", "2 killed, 33 hurt as Russian strike hits flats",
     "A strike wrecks a five-storey block; four children among the hurt.",
     "EUROPE"),
    ("GAZA", "Strike kills Hamas security chief Abu Nahal",
     "Abu Nahal, two months in the post, is killed; nine die in strikes.",
     "MIDDLE EAST"),
    ("ADEN", "Houthis now 60 km from Aden",
     "Houthis are 60 km from the interim capital, Yemen's army says.",
     "MIDDLE EAST"),
    ("WALL STREET", "Dow tops 50,000 for the first time",
     "The Dow closes at 50,018.70, up 0.85%, as the AI rally fades.",
     "MARKETS"),
    ("NVIDIA", "Huang's comeback rally cools in a day",
     "Nvidia jumps 31% on Monday as Huang returns, then falls 5.9%.",
     "MARKETS"),
    ("MICROSOFT", "'Code Red' after the 24-hour outage",
     "Memos: a one-hour fix target after the 12–13 Nov outage.",
     "TECH"),
    ("NEPAL", "Quake 5.6 strikes near the China border",
     "A 5.6 quake shakes Koshi province, close to the China border.",
     "ASIA"),
    ("SENEGAL", "CAS gives Senegal the AFCON crown back",
     "CAS overturns CAF's forfeit ruling: the 1–0 final win stands.",
     "SPORT"),
    ("ENGLAND", "Record 5,258 heat deaths in one summer",
     "UKHSA counts 5,258 heat-linked deaths, the most since records began.",
     "HEALTH"),
    ("SANOFI", "Sanofi buys Insmed for $41bn",
     "Sanofi pays $175 a share, a 46% premium, for the US drug maker.",
     "MARKETS"),
]

BRIEFS = [
    ("IRAN", "Rial plunges to 2.82m to the dollar after fresh US sanctions "
     "on its 'shadow banking' network.", "MIDDLE EAST"),
    ("DOHA TALKS", "Vance and Rubio meet Qatar's PM separately as efforts "
     "to revive Iran negotiations stall.", "MIDDLE EAST"),
    ("LONDON", "Britain sanctions the Houthis and four senior figures "
     "over torture, rape and attacks on civilians.", "EUROPE"),
    ("LONDON", "UK firms aiding Ukraine are warned to brace for Russian "
     "sabotage, in a rare public alert.", "EUROPE"),
    ("BERLIN", "Zelensky asks NATO to admit Ukraine outright; chief Mark "
     "Rutte demurs, citing peace talks.", "EUROPE"),
    ("BERLIN", "Germany is the first country to gain access to Ukraine's "
     "Delta battlefield management system.", "EUROPE"),
    ("BRUSSELS", "Seven states back EU limits on Russian visas — for "
     "tourists and for sporting events.", "EUROPE"),
    ("SPACE", "NATO vows to defend space after reports Russia plans a "
     "nuclear-armed satellite launch. CLAIM.", "EUROPE"),
    ("MOSCOW", "Russia rejects any NATO Article 5-like security "
     "guarantees for Ukraine.", "EUROPE"),
    ("TALLY", "More than 700,000 Russian soldiers have been killed, a "
     "Meduza–Mediazona analysis finds. CLAIM.", "EUROPE"),
    ("BENGHAZI", "The UN urges a probe into attacks on the port, after "
     "Ukraine claims drone strikes on Russian ships. CLAIM.", "AFRICA"),
    ("BAGHDAD", "Iraq's PM orders the oil ministry to run oilfields in "
     "areas under Kurdish security control.", "MIDDLE EAST"),
    ("BEIJING", "China starts 6G pilot tests across eight provincial "
     "regions, racing global standards work.", "ASIA"),
    ("ZHUHAI", "China will show its Type 055 destroyer to the public for "
     "the first time at the Dec 7–13 airshow.", "ASIA"),
    ("DELL", "Dell revenue more than doubles to $54.9bn on AI orders; "
     "Anthropic shares close below their $83 IPO price.", "MARKETS"),
    ("HUAWEI", "US jury finds Huawei guilty on 10 of 12 counts — trade "
     "secrets and more — and clears it of racketeering.", "TECH"),
    ("WASHINGTON", "The FBI is probing a possible breach of the NCIC "
     "police database used across the US. REPORTED.", "TECH"),
    ("BARBADOS", "UN chief Guterres calls for an AI risk framework to be "
     "agreed within a year, at the Bridgetown summit.", "TECH"),
    ("ROHINGYA", "Fourteen states back the ICJ genocide ruling; Malaysia "
     "will return 6,500+ Rohingya to Myanmar.", "ASIA"),
    ("ITURI", "WHO evacuates its Ebola team from a hospital in Ituri, "
     "DR Congo, after fighting traps staff for days.", "AFRICA"),
    ("MEASLES", "US measles deaths reach 14 and cases near 6,000; "
     "Pennsylvania records a ninth death.", "HEALTH"),
    ("DHAKA", "Ousted PM Sheikh Hasina sets 16 December as the date for "
     "her return to Bangladesh from India.", "ASIA"),
    ("WASHINGTON", "The DOJ recovers $8bn and charges 800+ suspects in "
     "its largest anti-scam sweep ever.", "AMERICAS"),
    ("BRUSSELS", "A strike against austerity cancels flights across "
     "Belgium; unions march on the capital.", "EUROPE"),
    ("WASHINGTON", "Trump awards Rudy Giuliani the Presidential Medal of "
     "Freedom at the White House.", "AMERICAS"),
]

STATS = [
    ("DOW 50,018.70", "+0.85% · first above 50k"),
    ("NASDAQ −1.48%", "Micron −11%, AMD −8.9%"),
    ("NVIDIA −5.9%", "day after +31% Mon"),
    ("SANOFI $41bn", "$175/share · +46%"),
    ("KOSPI +6.3%", "Seoul rebounds"),
    ("BRENT $91.40", "+2.3% · Hormuz"),
]

PINS = [
    # name, map fx, map fy, label dx, label dy
    ("Hormuz", 0.60, 0.42, 8, 7), ("Riyadh", 0.57, 0.44, -46, -6),
    ("Aden", 0.585, 0.52, 8, 2), ("Gaza", 0.545, 0.40, -36, -6),
    ("Zaporizhzhia", 0.52, 0.24, 8, -5), ("Kathmandu", 0.71, 0.42, 8, 2),
    ("Jiuquan", 0.79, 0.32, -48, -6), ("London", 0.47, 0.20, 8, -5),
    ("Washington", 0.24, 0.33, 8, -5), ("Seoul", 0.855, 0.32, 8, -5),
    ("Dakar", 0.415, 0.52, 8, -5),
]

# ---------------------------------------------------------------- scenes

def scene_hormuz(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(246, 178, 90))
    d.rectangle([x, y, x + w, y + int(h * 0.55)], fill=(232, 122, 54))
    for i in range(5):  # sun bands
        d.ellipse([x + w * 0.68, y + 8 + i * 3, x + w * 0.86, y + 26 + i * 3],
                  fill=(255, 214, 130))
    d.rectangle([x, y + int(h * 0.62), x + w, y + h], fill=SEA)
    for i in range(4):
        yy = y + int(h * 0.68) + i * 12
        d.arc([x + 8, yy, x + w - 8, yy + 10], 0, 180, fill=(120, 180, 210))
    # tanker
    d.rectangle([x + 18, y + int(h * 0.52), x + w - 60, y + int(h * 0.66)],
                fill=(40, 40, 44))
    d.rectangle([x + w - 58, y + int(h * 0.44), x + w - 34, y + int(h * 0.66)],
                fill=(52, 52, 56))
    d.rectangle([x + 30, y + int(h * 0.44), x + w - 70, y + int(h * 0.52)],
                fill=(120, 30, 24))
    # flames + smoke
    for cx, cy, r, col in [(0.30, 0.40, 26, (255, 200, 60)),
                           (0.42, 0.34, 32, (255, 140, 40)),
                           (0.55, 0.42, 22, (255, 200, 60)),
                           (0.36, 0.28, 20, (120, 120, 120)),
                           (0.48, 0.22, 24, (90, 90, 90))]:
        d.ellipse([x + w * cx - r, y + h * cy - r, x + w * cx + r,
                   y + h * cy + r], fill=col)
    d.text((x + 8, y + h - 18), "STRAIT OF HORMUZ", font=F_SANS(10),
           fill=(255, 255, 255))


def scene_riyadh(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(24, 32, 58))
    for _ in range(40):
        sx, sy = random.randint(0, w - 2), random.randint(0, int(h * 0.5))
        d.ellipse([x + sx, y + sy, x + sx + 2, y + sy + 2],
                  fill=(255, 255, 255))
    # city skyline
    for i, bh in enumerate([46, 70, 52, 88, 60, 40]):
        bx = x + 6 + i * 30
        d.rectangle([bx, y + h - bh, bx + 24, y + h], fill=(52, 64, 96))
        for wy in range(y + h - bh + 6, y + h - 6, 10):
            d.rectangle([bx + 4, wy, bx + 8, wy + 5], fill=(255, 214, 120))
    # PIF tower (twisted top)
    tx = x + w - 78
    d.polygon([(tx, y + h), (tx + 8, y + 18), (tx + 34, y + 10),
               (tx + 52, y + 22), (tx + 46, y + h)], fill=(120, 150, 200))
    for wy in range(y + 30, y + h - 8, 9):
        d.line([tx + 6, wy, tx + 46, wy - 4], fill=(200, 220, 240), width=1)
    # drone flash at the top
    d.ellipse([tx + 6, y + 2, tx + 46, y + 34], fill=(255, 180, 60))
    d.ellipse([tx + 14, y + 8, tx + 38, y + 28], fill=(255, 240, 180))
    d.text((x + 8, y + h - 18), "RIYADH · KAFD", font=F_SANS(10),
           fill=(255, 255, 255))


def scene_tiangong(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(10, 16, 40))
    for _ in range(60):
        sx, sy = random.randint(0, w - 2), random.randint(0, h - 2)
        d.ellipse([x + sx, y + sy, x + sx + 2, y + sy + 2],
                  fill=(255, 255, 255))
    # earth curve
    d.ellipse([x - w * 0.4, y + h * 0.72, x + w * 1.4, y + h * 1.7],
              fill=(38, 96, 160))
    d.arc([x - w * 0.4, y + h * 0.72, x + w * 1.4, y + h * 1.7], 200, 340,
          fill=(120, 200, 240), width=3)
    # station: core module + panels
    cx, cy = x + w * 0.42, y + h * 0.42
    d.rectangle([cx - 70, cy - 12, cx + 70, cy + 12], fill=(200, 205, 215))
    d.rectangle([cx - 88, cy - 6, cx - 70, cy + 6], fill=(160, 165, 175))
    d.rectangle([cx + 70, cy - 6, cx + 88, cy + 6], fill=(160, 165, 175))
    for px in (cx - 150, cx + 96):
        d.rectangle([px, cy - 22, px + 52, cy + 22], fill=(30, 90, 180))
        for k in range(4):
            d.line([px + 13 * k, cy - 22, px + 13 * k, cy + 22],
                   fill=(90, 160, 240), width=1)
    # Shenzhou capsule approaching
    sx, sy = x + w * 0.80, y + h * 0.30
    d.ellipse([sx - 26, sy - 14, sx + 26, sy + 14], fill=(230, 230, 235))
    d.rectangle([sx - 40, sy - 6, sx - 26, sy + 6], fill=(180, 180, 190))
    d.ellipse([sx - 8, sy - 5, sx + 8, sy + 5], fill=(30, 90, 180))
    # astronaut figure
    ax, ay = x + w * 0.80, y + h * 0.66
    d.ellipse([ax - 10, ay - 22, ax + 10, ay - 2], fill=(255, 255, 255))
    d.ellipse([ax - 6, ay - 18, ax + 6, ay - 6], fill=(30, 90, 180))
    d.rectangle([ax - 12, ay, ax + 12, ay + 26], fill=(240, 240, 245))
    d.rectangle([ax - 20, ay + 2, ax - 12, ay + 18], fill=(240, 240, 245))
    d.rectangle([ax + 12, ay + 2, ax + 20, ay + 18], fill=(240, 240, 245))
    d.text((x + 8, y + h - 18), "TIANGONG · SHENZHOU-24", font=F_SANS(10),
           fill=(255, 255, 255))


def scene_block(d, x, y, w, h, kind):
    """Small 196x92 drawn panel for a secondary story."""
    if kind == "zaporizhzhia":
        d.rectangle([x, y, x + w, y + h], fill=(196, 200, 208))
        d.rectangle([x + 30, y + 26, x + 110, y + h], fill=(120, 112, 100))
        for r in range(3):
            for c in range(3):
                d.rectangle([x + 40 + c * 22, y + 34 + r * 18,
                             x + 52 + c * 22, y + 44 + r * 18],
                            fill=(60, 58, 52) if (r, c) != (1, 1) else (30, 30, 30))
        d.polygon([(x + 60, y + 30), (x + 110, y + 30), (x + 110, y + h),
                   (x + 60, y + h)], fill=(90, 84, 76))
        for cx, cy, r in [(0.62, 0.24, 20), (0.72, 0.16, 26), (0.55, 0.12, 14)]:
            d.ellipse([x + w * cx - r, y + h * cy - r, x + w * cx + r,
                       y + h * cy + r], fill=(90, 90, 92))
        d.ellipse([x + w * 0.66, y + 6, x + w * 0.78, y + 22],
                  fill=(255, 160, 60))
    elif kind == "gaza":
        d.rectangle([x, y, x + w, y + h], fill=(214, 196, 170))
        d.rectangle([x, y + int(h * 0.62), x + w, y + h], fill=(150, 132, 108))
        for i, (bx, bw, bh) in enumerate([(10, 46, 34), (60, 60, 22),
                                          (126, 52, 40), (150, 30, 16)]):
            d.polygon([(x + bx, y + h), (x + bx, y + h - bh),
                       (x + bx + bw // 2, y + h - bh - 12),
                       (x + bx + bw, y + h - bh), (x + bx + bw, y + h)],
                      fill=(120, 106, 88))
        d.ellipse([x + w * 0.72, y + 8, x + w * 0.86, y + 26],
                  fill=(255, 190, 90))
        for cx, cy, r in [(0.30, 0.30, 16), (0.42, 0.20, 20)]:
            d.ellipse([x + w * cx - r, y + h * cy - r, x + w * cx + r,
                       y + h * cy + r], fill=(140, 130, 118))
    elif kind == "aden":
        d.rectangle([x, y, x + w, y + h], fill=(222, 206, 170))
        d.rectangle([x, y + int(h * 0.55), x + w, y + h], fill=(52, 110, 150))
        d.polygon([(x + 8, y + 8), (x + 150, y + 8), (x + 188, y + 40),
                   (x + 120, y + 52), (x + 60, y + 44), (x + 8, y + 40)],
                  fill=(190, 170, 130))
        d.ellipse([x + 150, y + 34, x + 158, y + 42], fill=RED)
        d.text((x + 118, y + 14), "ADEN", font=F_SANS(11), fill=RED)
        d.line([x + 20, y + 62, x + 138, y + 36], fill=RED, width=4)
        d.polygon([(x + 138, y + 36), (x + 122, y + 30), (x + 124, y + 46)],
                  fill=RED)
        d.text((x + 8, y + 42), "60 km", font=F_SANS(11), fill=(255, 255, 255))
    elif kind == "dow":
        d.rectangle([x, y, x + w, y + h], fill=(16, 44, 34))
        for i in range(6):
            d.line([x + 8, y + h - 12 - i * 12, x + w - 8, y + h - 12 - i * 12],
                   fill=(40, 80, 60), width=1)
        pts = [(10, 74), (40, 66), (70, 70), (100, 52), (130, 56), (160, 34),
               (186, 22)]
        d.line([(x + px, y + py) for px, py in pts], fill=(80, 220, 140),
               width=3, joint="curve")
        d.ellipse([x + 180, y + 16, x + 192, y + 28], fill=(80, 220, 140))
        d.text((x + 8, y + 6), "50,000", font=F_SANS(15), fill=(255, 255, 255))
    elif kind == "nvidia":
        d.rectangle([x, y, x + w, y + h], fill=(10, 30, 12))
        d.text((x + 8, y + 4), "+31% Mon, −5.9% Tue", font=F_SANS(10),
               fill=(120, 230, 140))
        d.rectangle([x + 68, y + 22, x + 128, y + 58], fill=(20, 60, 24),
                    outline=(120, 220, 120), width=2)
        d.rectangle([x + 84, y + 32, x + 112, y + 48], fill=(140, 240, 140))
        for px in (76, 92, 108, 122):
            d.line([x + px, y + 14, x + px, y + 22], fill=(120, 220, 120),
                   width=2)
    elif kind == "microsoft":
        d.rectangle([x, y, x + w, y + h], fill=(20, 60, 110))
        d.rectangle([x + 14, y + 8, x + w - 14, y + 52], fill=(8, 24, 48))
        d.rectangle([x + 22, y + 12, x + w - 22, y + 26], fill=(190, 30, 30))
        d.text((x + 26, y + 14), "CODE RED", font=F_SANS(11),
               fill=(255, 255, 255))
        for i, ln in enumerate(["outage 24h", "fix target: 1h"]):
            d.text((x + 24, y + 30 + i * 12), ln, font=F_SANS_R(11),
                   fill=(180, 210, 240))
    elif kind == "nepal":
        d.rectangle([x, y, x + w, y + h], fill=SKY)
        d.polygon([(x, y + h), (x + 60, y + 18), (x + 120, y + h)],
                  fill=(120, 130, 145))
        d.polygon([(x + 80, y + h), (x + 150, y + 6), (x + w, y + h)],
                  fill=(90, 100, 120))
        d.polygon([(x + 138, y + 20), (x + 150, y + 6), (x + 164, y + 22),
                   (x + 156, y + 22), (x + 150, y + 14), (x + 144, y + 22)],
                  fill=(255, 255, 255))
        d.line([x + 20, y + 48, x + 60, y + 42, x + 100, y + 52, x + 140,
                y + 44, x + 180, y + 52], fill=(178, 34, 28), width=3)
        d.text((x + 8, y + 6), "M 5.6", font=F_SANS(13), fill=RED)
    elif kind == "senegal":
        d.rectangle([x, y, x + w, y + h], fill=(0, 120, 70))
        d.ellipse([x + w // 2 - 20, y + 4, x + w // 2 + 20, y + 28],
                  fill=(255, 214, 90))
        d.polygon([(x + w // 2 - 20, y + 14), (x + w // 2 - 32, y + 4),
                   (x + w // 2 - 28, y + 20)], fill=(255, 214, 90))
        d.polygon([(x + w // 2 + 20, y + 14), (x + w // 2 + 32, y + 4),
                   (x + w // 2 + 28, y + 20)], fill=(255, 214, 90))
        d.rectangle([x + w // 2 - 6, y + 28, x + w // 2 + 6, y + 38],
                    fill=(255, 214, 90))
        d.rectangle([x + w // 2 - 16, y + 38, x + w // 2 + 16, y + 42],
                    fill=(255, 214, 90))
        d.text((x + 8, y + 46), "AFCON CHAMPIONS", font=F_SANS(11),
               fill=(255, 255, 255))
    elif kind == "heat":
        d.rectangle([x, y, x + w, y + h], fill=(255, 214, 120))
        d.ellipse([x + 12, y + 8, x + 64, y + 56], fill=(255, 150, 40))
        d.rounded_rectangle([x + 116, y + 8, x + 132, y + 42], radius=8,
                            fill=(255, 255, 255), outline=RED, width=2)
        d.rectangle([x + 122, y + 30, x + 126, y + 40], fill=RED)
        d.ellipse([x + 116, y + 38, x + 132, y + 56], fill=RED)
        d.text((x + 140, y + 18), "5,258", font=F_SANS(16), fill=RED)
        d.text((x + 140, y + 38), "deaths", font=F_SANS_R(11), fill=INK)
    elif kind == "sanofi":
        d.rectangle([x, y, x + w, y + h], fill=(235, 240, 248))
        d.rectangle([x + 16, y + 20, x + 66, y + 58], fill=(255, 255, 255),
                    outline=NAVY2, width=2)
        d.rectangle([x + 28, y + 10, x + 54, y + 20], fill=NAVY2)
        d.text((x + 24, y + 28), "Rx", font=F_SERIF(20), fill=NAVY2)
        d.text((x + 84, y + 6), "$41bn", font=F_SANS(20), fill=NAVY)
        d.text((x + 84, y + 30), "Sanofi buys", font=F_SANS_R(11), fill=INK)
        d.text((x + 84, y + 44), "Insmed", font=F_SANS(12), fill=INK)

# ---------------------------------------------------------------- layout

def paste_scene(img, fn, x, y, w, h, kind=None):
    """Draw a scene on its own canvas and paste it: nothing may spill
    outside its box."""
    layer = Image.new("RGB", (w, h), PAPER)
    ld = ImageDraw.Draw(layer)
    if kind is None:
        fn(ld, 0, 0, w, h)
    else:
        fn(ld, 0, 0, w, h, kind)
    img.paste(layer, (x, y))


def brief_lines(draw, head, text, width):
    """Wrap a brief whose bold head is measured in the bold font and the
    rest in the regular font. Returns (lines, head_width)."""
    f_b, f_r = F_SANS(11), F_SANS_R(11)
    head_w = draw.textlength(head, font=f_b)
    words = text.split()
    lines, cur, cur_w = [], head, head_w
    for wd in words:
        add = draw.textlength(" " + wd, font=f_r)
        if cur_w + add <= width or cur == head:
            cur = cur + " " + wd
            cur_w += add
        else:
            lines.append(cur)
            cur, cur_w = wd, draw.textlength(wd, font=f_r)
    lines.append(cur)
    if len(lines) > 2:
        lines = lines[:2]
        while lines and draw.textlength(lines[-1] + "…", font=f_r) > width:
            lines[-1] = lines[-1][:-1]
        lines[-1] = lines[-1].rstrip(" ,.;:") + "…"
    return lines, head_w

def fit_lines(draw, text, fnt, width, max_lines):
    lines = wrap(draw, text, fnt, width)
    if len(lines) > max_lines:
        lines = lines[:max_lines]
        while lines and draw.textlength(lines[-1] + "…", font=fnt) > width:
            lines[-1] = lines[-1][:-1]
        lines[-1] = lines[-1].rstrip(" ,.;:") + "…"
    return lines


def draw_lines(draw, x, y, lines, fnt, fill, leading):
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


def draw_map(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(214, 232, 240),
                outline=LINE, width=1)
    # schematic continents (stylised, not to scale)
    land = (196, 208, 170)
    na = [(0.03, 0.18), (0.10, 0.08), (0.20, 0.10), (0.24, 0.22),
          (0.20, 0.34), (0.12, 0.38), (0.05, 0.30)]
    sa = [(0.24, 0.48), (0.29, 0.44), (0.33, 0.52), (0.31, 0.72),
          (0.27, 0.86), (0.24, 0.66)]
    eu = [(0.46, 0.10), (0.52, 0.08), (0.56, 0.16), (0.53, 0.24),
          (0.47, 0.22)]
    af = [(0.46, 0.32), (0.54, 0.30), (0.58, 0.40), (0.56, 0.58),
          (0.51, 0.70), (0.47, 0.52)]
    as_ = [(0.58, 0.08), (0.72, 0.06), (0.88, 0.12), (0.96, 0.22),
           (0.88, 0.34), (0.80, 0.44), (0.72, 0.36), (0.66, 0.40),
           (0.60, 0.26)]
    au = [(0.82, 0.68), (0.90, 0.66), (0.94, 0.74), (0.86, 0.80),
          (0.82, 0.74)]
    for poly in (na, sa, eu, af, as_, au):
        d.polygon([(x + px * w, y + py * h) for px, py in poly], fill=land,
                  outline=(150, 160, 140))
    d.text((x + 6, y + 4), "THE WORLD — 11 PLACES IN TODAY'S NEWS",
           font=F_SANS(10), fill=NAVY)
    for name, fx, fy, lx, ly in PINS:
        px, py = x + fx * w, y + fy * h
        d.ellipse([px - 5, py - 5, px + 5, py + 5], fill=RED,
                  outline=(255, 255, 255), width=1)
        d.text((px + lx, py + ly), name, font=F_SANS(9), fill=INK)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- masthead
    d.rectangle([0, 0, W, 96], fill=NAVY)
    d.rectangle([0, 96, W, 99], fill=GOLD)
    d.text((16, 10), "THE WORLD IN ONE DAY", font=F_SERIF(44), fill=(255, 255, 255))
    d.text((16, 64), "Tuesday 24 November 2026  ·  the day's world news on one page",
           font=F_SERIF_R(16), fill=(200, 214, 232))
    d.text((W - 16 - d.textlength("38 STORIES", font=F_SANS(15)), 14),
           "38 STORIES", font=F_SANS(15), fill=(255, 214, 120))
    d.text((W - 16 - d.textlength("10 REGIONS · 13 SCENES", font=F_SANS(12)), 36),
           "10 REGIONS · 13 SCENES", font=F_SANS(12), fill=(200, 214, 232))
    d.text((W - 16 - d.textlength("CLAIMS LABELLED", font=F_SANS(12)), 58),
           "CLAIMS LABELLED", font=F_SANS(12), fill=(200, 214, 232))

    # ---- stat strip
    y = 102
    for i, (big, small) in enumerate(STATS):
        cx = 16 + i * 164
        d.text((cx, y), big, font=F_SANS(14), fill=NAVY)
        d.text((cx, y + 17), small, font=F_SANS_R(9), fill=GREY)
        if i:
            d.line([cx - 8, y + 2, cx - 8, y + 28], fill=LINE, width=1)

    # ---- three big features
    fy = 134
    fw, gap = 320, 16
    scenes = [scene_hormuz, scene_riyadh, scene_tiangong]
    for i, (kick, head, stand, region) in enumerate(FEATURES):
        fx = 16 + i * (fw + gap)
        paste_scene(img, scenes[i], fx, fy, fw, 110)
        ty = fy + 116
        tag(d, fx, ty, region, NAVY2)
        ty += 20
        draw_lines(d, fx, ty, fit_lines(d, head, F_SERIF(20), fw, 2),
                   F_SERIF(20), INK, 22)
        ty += 46
        draw_lines(d, fx, ty, fit_lines(d, stand, F_SERIF_R(12), fw, 3),
                   F_SERIF_R(12), (60, 60, 56), 15)

    d.line([16, 366, W - 16, 366], fill=LINE, width=1)
    d.text((16, 370), "ALSO TODAY — 10 MORE STORIES, DRAWN",
           font=F_SANS(12), fill=NAVY)

    # ---- secondary grid: 5 cols x 2 rows
    kinds = ["zaporizhzhia", "gaza", "aden", "dow", "nvidia",
             "microsoft", "nepal", "senegal", "heat", "sanofi"]
    cw, ch, cg = 192, 114, 8
    for i, (kick, head, stand, region) in enumerate(SECONDARY):
        col, row = i % 5, i // 5
        sx = 16 + col * (cw + cg)
        sy = 388 + row * ch
        paste_scene(img, scene_block, sx, sy, cw, 60, kinds[i])
        ty = sy + 64
        draw_lines(d, sx, ty, fit_lines(d, head, F_SANS(12), cw, 2),
                   F_SANS(12), INK, 13)
        ty += 26
        draw_lines(d, sx, ty, fit_lines(d, stand, F_SANS_R(10), cw, 2),
                   F_SANS_R(10), (70, 70, 66), 12)

    # ---- briefs: 25 items in 3 columns
    d.line([16, 622, W - 16, 622], fill=LINE, width=1)
    d.text((16, 626), "THE REST OF THE DAY — IN BRIEF",
           font=F_SANS(12), fill=NAVY)
    bw, bg = 318, 10
    per_col = [9, 8, 8]
    idx = 0
    for c in range(3):
        bx = 16 + c * (bw + bg)
        by = 644
        for _ in range(per_col[c]):
            kick, txt, region = BRIEFS[idx]
            num = 14 + idx
            head = "%d · %s — " % (num, kick)
            lines, head_w = brief_lines(d, head, txt, bw)
            for li, ln in enumerate(lines):
                if li == 0:
                    d.text((bx, by), head, font=F_SANS(11), fill=NAVY)
                    d.text((bx + head_w, by), ln[len(head):],
                           font=F_SANS_R(11), fill=INK)
                else:
                    d.text((bx, by), ln, font=F_SANS_R(11), fill=INK)
                by += 12
            idx += 1

    # ---- bottom: map + date check
    d.line([16, 866, W - 16, 866], fill=LINE, width=1)
    draw_map(d, 16, 872, 596, 144)
    dx, dw = 624, 384
    d.rectangle([dx, 872, dx + dw, 1016], outline=NAVY, width=2, fill=CARD)
    d.rectangle([dx, 872, dx + dw, 896], fill=NAVY)
    d.text((dx + 10, 878), "DATE CHECK", font=F_SANS(13), fill=(255, 214, 120))
    d.text((dx + 118, 878), "— TUESDAY 24 NOVEMBER 2026", font=F_SANS(12),
           fill=(255, 255, 255))
    check = (
        "Every story here happened, or was first reported, on Tuesday "
        "24 November 2026. The Huawei verdict, the Senegal CAS ruling "
        "and the WHO evacuation were announced late on the 24th."
    )
    ty = 904
    ty = text_block(d, dx + 10, ty, check, F_SANS_R(11), INK, dw - 20, 14)
    ty += 4
    ty = text_block(d, dx + 10, ty,
                    "CLAIM means one source, or an attributed report: the "
                    "Hormuz mine strikes, the satellite report, the 700,000 "
                    "tally. Nothing from 25 November is shown.",
                    F_SANS_R(11), (120, 30, 24), dw - 20, 14)
    ty += 4
    d.text((dx + 10, ty), "Sources: AP · Reuters · AFP · BBC · UN · WHO · FT",
           font=F_SANS_R(10), fill=GREY)

    img.save(OUT, "PNG", optimize=True)
    print("wrote", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
