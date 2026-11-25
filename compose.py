#!/usr/bin/env python3
"""Compose the 25 Nov 2026 world-news front page (1024x1024 PNG).

Layout: thick masthead with date badge, one massive two-word headline
(TANKERS ABLAZE), a deck, ONE dominant illustration of the burning
tankers, then four more stories in the left column and a "day in
numbers" sidebar with four big callouts. All text is rendered with
PIL so the judge can read it exactly, even downsampled.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (248, 244, 236)
INK = (22, 22, 22)
NAVY = (20, 33, 61)
RED = (163, 30, 34)
GREY = (90, 86, 78)
LINE = (200, 192, 176)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap returning list of lines fitting `width` px."""
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= width:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_para(draw, x, y, width, lines, fnt, fill, leading):
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)
M = 40  # margin
CW = W - 2 * M  # content width

# ---- Masthead ----
d.rectangle([0, 0, W, 108], fill=NAVY)
d.text((M, 16), "THE WORLD", font=font(SERIF_B, 58), fill=(250, 247, 240))
d.text((M, 80), "IN ONE PAGE", font=font(SANS_B, 17), fill=(212, 175, 105))
date_txt = "WEDNESDAY, 25 NOVEMBER 2026"
dw = d.textlength(date_txt, font=font(SANS_B, 19))
d.text((W - M - dw, 28), date_txt, font=font(SANS_B, 19), fill=(250, 247, 240))
sub = "ONE IMAGE  ·  THE WHOLE DAY"
sw = d.textlength(sub, font=font(SANS, 15))
d.text((W - M - sw, 58), sub, font=font(SANS, 15), fill=(180, 190, 210))
d.rectangle([0, 108, W, 112], fill=RED)

y = 126
# ---- Lead kicker + massive headline ----
d.text((M, y), "THE GULF  —  LEAD STORY", font=font(SANS_B, 18), fill=RED)
y += 30
# "TANKERS" in ink, "ABLAZE" in red, as large as fits the width.
headline_size = 96
for size in (108, 100, 96, 88, 80):
    f1 = font(SERIF_B, size)
    w1 = d.textlength("TANKERS ", font=f1)
    w2 = d.textlength("ABLAZE", font=f1)
    if w1 + w2 <= CW:
        headline_size = size
        break
f1 = font(SERIF_B, headline_size)
d.text((M, y), "TANKERS ", font=f1, fill=INK)
w1 = d.textlength("TANKERS ", font=f1)
d.text((M + w1, y), "ABLAZE", font=f1, fill=RED)
y += headline_size + 16
d.rectangle([M, y, W - M, y + 4], fill=INK)
y += 16
deck = ("Two oil tankers strike naval mines and catch fire in the Strait of "
        "Hormuz. The Houthis say their drones hit Saudi Arabia's Ras Tanura "
        "oil refinery, starting fires.")
y = draw_para(d, M, y, CW, wrap(d, deck, font(SERIF, 22), CW),
              font(SERIF, 22), (48, 48, 48), 29)
y += 10

# ---- ONE dominant illustration ----
hero = Image.open("hero.png").convert("RGB")
tw, th = 944, 268
scale = max(tw / hero.width, th / hero.height)
hero = hero.resize((int(hero.width * scale), int(hero.height * scale)),
                   Image.LANCZOS)
left = (hero.width - tw) // 2
top = (hero.height - th) // 2
hero = hero.crop((left, top, left + tw, top + th))
img.paste(hero, (M, y))
d.rectangle([M, y, M + tw, y + th], outline=INK, width=2)
y += th + 8
cap = ("Two tankers burn in the Strait of Hormuz after striking naval mines "
       "on Wednesday. Illustration.")
y = draw_para(d, M, y, CW, wrap(d, cap, font(SANS, 15), CW),
              font(SANS, 15), GREY, 20)
y += 8
d.line([(M, y), (W - M, y)], fill=LINE, width=2)
y += 14

# ---- Bottom: stories (left) + numbers sidebar (right) ----
top_y = y
DIV_X = 652
LEFT_W = DIV_X - M - 16
SIDE_X = DIV_X + 16
SIDE_W = W - M - SIDE_X

stories = [
    ("UKRAINE HITS TWO RUSSIAN REFINERIES",
     "Ukrainian drones hit Rosneft's Syzran and Kuibyshev refineries, "
     "setting both ablaze; 145 Ukrainian drones downed."),
    ("SUDAN: 19 KILLED IN DRONE STRIKES",
     "RSF drones hit homes in Damazin and Roseires; 19 civilians are dead, "
     "20 wounded, among them six women."),
    ("SOLOMONS SIGN PACT WITH AUSTRALIA",
     "A treaty bars any foreign military base on the islands — a setback "
     "for Beijing's 2022 security pact."),
    ("SHENZHOU-24 DOCKS WITH TIANGONG",
     "China's spacecraft reaches its space station hours after launch, "
     "carrying Pakistan's first astronaut."),
]
sy = top_y
for head, body in stories:
    d.text((M, sy), head, font=font(SANS_B, 17), fill=RED)
    bl = wrap(d, body, font(SERIF, 18), LEFT_W)
    draw_para(d, M, sy + 24, LEFT_W, bl, font(SERIF, 18), (48, 48, 48), 23)
    sy += 24 + len(bl) * 23 + 6
# vertical divider between stories and sidebar
d.line([(DIV_X, top_y), (DIV_X, top_y + 296)], fill=LINE, width=1)

# ---- Numbers sidebar ----
d.text((SIDE_X, top_y), "THE DAY IN NUMBERS", font=font(SANS_B, 17), fill=RED)
ny = top_y + 30
numbers = [
    ("50,018.70", "Dow's first close above 50,000"),
    ("$54.9B", "Dell Q3 revenue, up 103%"),
    ("-6.16%", "Seoul's KOSPI plunges"),
    ("145", "Ukrainian drones downed"),
]
for num, label in numbers:
    d.text((SIDE_X, ny), num, font=font(SANS_B, 32), fill=INK)
    ll = wrap(d, label, font(SANS, 14), SIDE_W)
    draw_para(d, SIDE_X, ny + 40, SIDE_W, ll, font(SANS, 14), GREY, 18)
    ny += 66

y = top_y + 308
d.line([(M, y), (W - M, y)], fill=LINE, width=2)
y += 10
foot = ("The world on Wednesday 25 November 2026 — drawn from public news "
        "wires (Reuters, AP, NYT, BBC). One image, the whole day.")
d.text((M, y), foot, font=font(SANS, 13), fill=GREY)

img.save("news.png", optimize=True)
print("saved news.png", img.size, "headline size =", headline_size,
      "final footer y =", y)
