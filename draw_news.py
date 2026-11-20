#!/usr/bin/env python3
"""Draw the Friday 20 November 2026 world-news front page (1024x1024 PNG).

Original work: every shape, flag, map and line of text is drawn here with
Pillow primitives. No photo, no downloaded image, no copied artwork.
"""
import math
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 241, 227)      # cream newsprint
INK = (18, 24, 38)           # navy-black text
NAVY = (24, 48, 96)
RED = (178, 34, 34)
RED_DK = (140, 20, 20)
GREY = (96, 96, 92)
RULE = (120, 110, 88)
PANEL = (238, 231, 210)
SKY = (214, 228, 240)

FD = "/usr/share/fonts/truetype/dejavu"
def F(path, size):
    return ImageFont.truetype(path, size)

SERIF_B = lambda s: F(f"{FD}/DejaVuSerif-Bold.ttf", s)
SERIF = lambda s: F(f"{FD}/DejaVuSerif.ttf", s)
SANS_B = lambda s: F(f"{FD}/DejaVuSans-Bold.ttf", s)
SANS = lambda s: F(f"{FD}/DejaVuSans.ttf", s)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

def wrap(text, font, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def text(x, y, s, font, fill=INK, anchor="la"):
    d.text((x, y), s, font=font, fill=fill, anchor=anchor)

def hline(x0, x1, y, fill=RULE, wdt=2):
    d.line([(x0, y), (x1, y)], fill=fill, width=wdt)

def vline(x, y0, y1, fill=RULE, wdt=2):
    d.line([(x, y0), (x, y1)], fill=fill, width=wdt)

def chip_num(x, y, n, size=20, bg=RED, fg=(255, 255, 255)):
    d.rounded_rectangle([x, y, x + size, y + size], radius=4, fill=bg)
    f = SANS_B(size - 6)
    tw = d.textlength(str(n), font=f)
    d.text((x + (size - tw) / 2, y + 2), str(n), font=f, fill=fg)

# ---------------- flags (simple vector originals) ----------------
def flag_us(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(255, 255, 255))
    for i in range(7):
        d.rectangle([x, y + i * h / 6.5, x + w, y + (i + 0.5) * h / 6.5], fill=(178, 34, 34))
    cw, ch = w * 0.4, h * 0.54
    d.rectangle([x, y, x + cw, y + ch], fill=NAVY)
    for r in range(3):
        for c in range(4):
            d.ellipse([x + 4 + c * cw / 4.4, y + 3 + r * ch / 3.4,
                       x + 8 + c * cw / 4.4, y + 7 + r * ch / 3.4], fill=(255, 255, 255))

def flag_cn(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(222, 41, 16))
    d.ellipse([x + w * 0.06, y + h * 0.1, x + w * 0.3, y + h * 0.52], fill=(255, 222, 0))
    for cx, cy in [(0.55, 0.15), (0.68, 0.3), (0.68, 0.55), (0.55, 0.68)]:
        d.ellipse([x + w * cx, y + h * cy, x + w * cx + 4, y + h * cy + 4], fill=(255, 222, 0))

def flag_ru(x, y, w, h):
    d.rectangle([x, y, x + w, y + h / 3], fill=(255, 255, 255))
    d.rectangle([x, y + h / 3, x + w, y + 2 * h / 3], fill=(0, 57, 166))
    d.rectangle([x, y + 2 * h / 3, x + w, y + h], fill=(213, 0, 50))

def flag_eu(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(0, 51, 153))
    cx, cy, r = x + w / 2, y + h / 2, min(w, h) * 0.32
    for k in range(12):
        a = -math.pi / 2 + k * math.pi / 6
        px, py = cx + r * math.cos(a), cy + r * math.sin(a)
        d.ellipse([px - 2, py - 2, px + 2, py + 2], fill=(255, 204, 0))

def flag_in(x, y, w, h):
    d.rectangle([x, y, x + w, y + h / 3], fill=(255, 153, 51))
    d.rectangle([x, y + h / 3, x + w, y + 2 * h / 3], fill=(255, 255, 255))
    d.rectangle([x, y + 2 * h / 3, x + w, y + h], fill=(19, 136, 8))
    cx, cy, r = x + w / 2, y + h / 2, h * 0.16
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(0, 0, 128), width=1)

def flag_sa(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(0, 106, 78))
    d.rectangle([x + w * 0.2, y + h * 0.42, x + w * 0.8, y + h * 0.52], fill=(255, 255, 255))

def flag_ua(x, y, w, h):
    d.rectangle([x, y, x + w, y + h / 2], fill=(0, 87, 184))
    d.rectangle([x, y + h / 2, x + w, y + h], fill=(255, 215, 0))

def flag_gb(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(0, 36, 125))
    d.rectangle([x + w * 0.42, y, x + w * 0.58, y + h], fill=(255, 255, 255))
    d.rectangle([x, y + h * 0.4, x + w, y + h * 0.6], fill=(255, 255, 255))
    d.rectangle([x + w * 0.46, y, x + w * 0.54, y + h], fill=(200, 16, 46))
    d.rectangle([x, y + h * 0.45, x + w, y + h * 0.55], fill=(200, 16, 46))

def flag_nz(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(0, 20, 80))
    d.rectangle([x, y, x + w * 0.5, y + h * 0.5], fill=(0, 36, 125))
    for sx, sy in [(0.72, 0.25), (0.82, 0.5), (0.68, 0.68), (0.85, 0.78)]:
        d.ellipse([x + w * sx, y + h * sy, x + w * sx + 3, y + h * sy + 3], fill=(255, 255, 255))

def flag_jp(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(255, 255, 255))
    cx, cy, r = x + w / 2, y + h / 2, h * 0.3
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(188, 0, 45))

def flag_kr(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(255, 255, 255))
    cx, cy, r = x + w / 2, y + h / 2, h * 0.26
    d.pieslice([cx - r, cy - r, cx + r, cy + r], 180, 360, fill=(205, 46, 58))
    d.pieslice([cx - r, cy - r, cx + r, cy + r], 0, 180, fill=(0, 71, 160))

FLAG = {"US": flag_us, "CN": flag_cn, "RU": flag_ru, "EU": flag_eu,
        "IN": flag_in, "SA": flag_sa, "UA": flag_ua, "GB": flag_gb,
        "NZ": flag_nz, "JP": flag_jp, "KR": flag_kr}

def flag(code, x, y, w=30, h=19):
    d.rectangle([x - 1, y - 1, x + w + 1, y + h + 1], outline=RULE, width=1)
    FLAG[code](x, y, w, h)

# ---------------- illustration panels (original vector art) ----------------
def panel_cyclone(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(178, 210, 232))
    # land strip at bottom
    d.polygon([(x, y + h * 0.78), (x + w * 0.25, y + h * 0.7), (x + w * 0.6, y + h * 0.8),
               (x + w, y + h * 0.72), (x + w, y + h), (x, y + h)], fill=(214, 190, 140))
    cx, cy = x + w * 0.5, y + h * 0.42
    for k in range(5):
        r = 12 + k * 13
        d.arc([cx - r, cy - r * 0.8, cx + r, cy + r * 0.8],
              start=40 + k * 55, end=300 + k * 55, fill=(255, 255, 255), width=7)
    d.ellipse([cx - 9, cy - 8, cx + 9, cy + 8], fill=(255, 255, 255))
    d.ellipse([cx - 4, cy - 3, cx + 4, cy + 3], fill=NAVY)
    flag("IN", x + w - 34, y + h - 24, 30, 19)

def panel_trilateral(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=PANEL)
    fw, fh = 48, 30
    flag_us(x + 6, y + 16, fw, fh)
    flag_cn(x + 55, y + 16, fw, fh)
    flag_ru(x + 104, y + 16, fw, fh)
    d.line([(x + 10, y + 62), (x + w - 10, y + 62)], fill=RULE, width=2)
    # three hands: three small dots joined by lines under the flags
    d.line([(x + 30, y + 78), (x + 79, y + 92)], fill=NAVY, width=3)
    d.line([(x + 128, y + 78), (x + 79, y + 92)], fill=NAVY, width=3)
    d.ellipse([x + 72, y + 85, x + 86, y + 99], fill=RED)
    d.line([(x + 10, y + 118), (x + w - 10, y + 118)], fill=RULE, width=2)
    d.text((x + w / 2, y + 124), "SHENZHEN", font=SANS_B(13), fill=NAVY, anchor="ma")

def panel_kafd(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(30, 32, 54))
    # stars
    for sx, sy in [(12, 12), (40, 26), (120, 10), (140, 30), (70, 18)]:
        d.ellipse([x + sx, y + sy, x + sx + 2, y + sy + 2], fill=(255, 255, 255))
    base = y + h
    # skyline silhouettes
    for bx, bw, bh in [(6, 22, 52), (32, 18, 74), (54, 24, 44), (82, 20, 88), (106, 22, 60), (132, 16, 40)]:
        d.rectangle([x + bx, base - bh, x + bx + bw, base], fill=(70, 76, 110))
    # KAFD twisted tower (centre, tallest)
    tx = x + w // 2
    d.polygon([(tx - 9, base), (tx - 5, base - 108), (tx + 5, base - 108), (tx + 9, base)],
              fill=(150, 160, 200))
    d.polygon([(tx - 5, base - 108), (tx + 2, base - 122), (tx + 5, base - 108)], fill=(200, 210, 235))
    # missile trail + impact burst
    d.line([(x + 12, y + 8), (tx - 2, base - 96)], fill=(255, 180, 60), width=3)
    for ang in range(0, 360, 45):
        a = math.radians(ang)
        d.line([(tx, base - 96), (tx + 13 * math.cos(a), base - 96 + 13 * math.sin(a))],
               fill=(255, 90, 40), width=3)
    d.ellipse([tx - 5, base - 101, tx + 5, base - 91], fill=(255, 220, 90))
    flag("SA", x + w - 34, y + h - 24, 30, 19)

def panel_talks(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=PANEL)
    # two flag panels facing each other across a table line
    flag_eu(x + 10, y + 18, 62, 40)
    flag_ru(x + w - 72, y + 18, 62, 40)
    # speech lines meeting in the middle
    d.line([(x + 76, y + 38), (x + w // 2 - 8, y + 38)], fill=NAVY, width=3)
    d.line([(x + w - 76, y + 38), (x + w // 2 + 8, y + 38)], fill=NAVY, width=3)
    d.ellipse([x + w // 2 - 7, y + 31, x + w // 2 + 7, y + 45], fill=RED)
    d.line([(x + 12, y + 96), (x + w - 12, y + 96)], fill=RULE, width=2)

# ---------------- masthead ----------------
MX, MX2 = 24, 1000
text(MX, 12, "ONE DAY OF WORLD NEWS  •  ONE PICTURE", SANS_B(17), fill=RED)
text(MX2, 12, "FRIDAY'S NEWS  •  PAGE ONE", SANS_B(15), fill=GREY, anchor="ra")
text((W // 2), 34, "Friday 20 November 2026", SERIF_B(64), fill=INK, anchor="ma")
hline(MX, MX2, 112, fill=RED, wdt=4)
text(MX, 120, "28 STORIES  •  SIX CONTINENTS  •  ONE FRIDAY", SANS_B(16), fill=NAVY)
text(MX2, 120, "THE WORLD, IN ONE PAGE", SANS_B(15), fill=GREY, anchor="ra")
hline(MX, MX2, 142, fill=RULE, wdt=1)

# ---------------- sub-headline strip: 3 biggest stories ----------------
SUBS = [
    ("Akvan lands in Odisha", "105,304 evacuated as the cyclone comes ashore"),
    ("Trump, Xi and Putin issue trilateral declaration", "\u201cNo big peace deal\u201d — and Trump defers Iran to 2027"),
    ("Houthi missile hits KAFD tower in Riyadh", "Landmark damaged; no casualties reported"),
]
sy = 152
for s1, s2 in SUBS:
    d.rectangle([MX, sy + 2, MX + 10, sy + 12], fill=RED)
    text(MX + 16, sy - 2, s1, SANS_B(19))
    text(MX + 16, sy + 19, s2, SANS(15), fill=GREY)
    sy += 44
hline(MX, MX2, 288, fill=RULE, wdt=1)

# ---------------- 4 illustrated leads, 2 x 2 ----------------
LEADS = [
    ("1", "AKVAN MAKES LANDFALL",
     "Cyclone Akvan hits Odisha at dawn: 105,304 people evacuated, 423 rescue teams out.",
     panel_cyclone, "INDIA"),
    ("2", "TRILATERAL DECLARATION",
     "\u201cNo big peace deal\u201d — but a trilateral text is out; Trump puts the Iran call off to 2027.",
     panel_trilateral, "SHENZHEN"),
    ("3", "MISSILE OVER RIYADH",
     "A Houthi missile strikes the KAFD tower in Riyadh. The landmark is damaged; nobody is hurt.",
     panel_kafd, "SAUDI ARABIA"),
    ("4", "EUROPE READY TO TALK TO RUSSIA",
     "European leaders say they are ready to negotiate with Moscow to end the war in Ukraine.",
     panel_talks, "EUROPE"),
]
LX0, LY0 = MX, 298
CW, CH, CGAP = 484, 152, 8
for i, (num, head, sub, panel, tag) in enumerate(LEADS):
    cx = LX0 + (i % 2) * (CW + CGAP)
    cy = LY0 + (i // 2) * (CH + CGAP)
    d.rectangle([cx, cy, cx + CW, cy + CH], outline=RULE, width=1)
    panel(cx + 1, cy + 1, 158, CH - 2)
    tx0 = cx + 170
    chip_num(tx0, cy + 8, num, size=22)
    text(tx0 + 30, cy + 8, tag, SANS_B(13), fill=RED)
    hl = wrap(head, SANS_B(24), CW - 182)
    hy = cy + 36
    for ln in hl[:2]:
        text(tx0, hy, ln, SANS_B(24))
        hy += 27
    sl = wrap(sub, SANS(14), CW - 182)
    hy += 2
    for ln in sl[:3]:
        text(tx0, hy, ln, SANS(14), fill=(60, 60, 58))
        hy += 17
hline(MX, MX2, 618, fill=RULE, wdt=1)

# ---------------- big-number strip ----------------
NUMBERS = [
    ("105,304", "evacuated from\nOdisha's coast"),
    ("51–48", "Senate rejects\nIran war-powers curb"),
    ("$3,756", "gold, an ounce\n— near a record"),
    ("113*", "Nicholls, not out\nNZ 243/5, day two"),
    ("83,022", "Sensex, up 989\npoints in a day"),
    ("$1.5tn", "Anthropic value,\nreportedly"),
]
ny = 626
seg = (MX2 - MX) // 6
for i, (big, lab) in enumerate(NUMBERS):
    x0 = MX + i * seg
    if i:
        vline(x0 - 4, ny, ny + 62, fill=RULE, wdt=1)
    text(x0 + seg // 2, ny, big, SANS_B(31), fill=NAVY, anchor="ma")
    for j, ln in enumerate(lab.split("\n")):
        text(x0 + seg // 2, ny + 34 + j * 14, ln, SANS(12), fill=GREY, anchor="ma")
hline(MX, MX2, 692, fill=RULE, wdt=1)

# ---------------- grid 5-16 (one line each, two columns) ----------------
GRID = [
    (5, "Crimean Bridge hit a third time", "rail traffic halted", "UA"),
    (6, "APEC leaders meet in Shenzhen", "Shenzhen Outlook adopted", "CN"),
    (7, "COP31's final day in Antalya", "$305bn gap; fossil-fuel text", None),
    (8, "North Korea expands enrichment", "Yongbyon site grows, IAEA says", None),
    (9, "US–Venezuela restore military ties", "cooperation deal signed", "US"),
    (10, "Seoul court clears ex-PM Han", "martial-law conviction overturned", "KR"),
    (11, "Fiji declares national disaster", "drought empties reservoirs", None),
    (12, "Nicholls 113* as NZ reach 243/5", "day two of the first Test", "NZ"),
    (13, "Sensex jumps 989 to 83,022", "gold holds at $3,756 an ounce", "IN"),
    (14, "Pete Rose pardoned", "posthumous pardon for the hit king", "US"),
    (15, "Haiti approves Salvadoran troops", "to help fight the gangs", None),
    (16, "Migrant boat sinks off Senegal", "rescue under way at sea", None),
]
gy = 700
for k, (n, head, sub, fl) in enumerate(GRID):
    col = k // 6
    row = k % 6
    x0 = MX + col * 492
    y0 = gy + row * 24
    chip_num(x0, y0 + 1, n, size=19)
    tx = x0 + 25
    if fl:
        flag(fl, tx, y0 + 2, 26, 16)
        tx += 31
    line = head + " — " + sub
    f = SANS_B(13)
    if d.textlength(line, font=f) > 492 - (tx - x0) - 4:
        line = head
        f2 = SANS(12)
        text(tx, y0 + 2, line, f)
    else:
        text(tx, y0 + 2, line, f)
hline(MX, MX2, 850, fill=RULE, wdt=1)

# ---------------- world map with numbered pins ----------------
def draw_map(x0, y0, w, h):
    d.rectangle([x0, y0, x0 + w, y0 + h], fill=(232, 222, 196), outline=RULE, width=1)
    # rough continent blobs (fractions of the box)
    def poly(pts, fill=(214, 196, 152)):
        d.polygon([(x0 + px * w, y0 + py * h) for px, py in pts], fill=fill, outline=NAVY)
    poly([(0.03, 0.22), (0.10, 0.10), (0.20, 0.08), (0.27, 0.18), (0.24, 0.30), (0.16, 0.34), (0.08, 0.38), (0.03, 0.30)])  # N America
    poly([(0.24, 0.52), (0.30, 0.48), (0.34, 0.58), (0.32, 0.76), (0.28, 0.88), (0.25, 0.70)])  # S America
    poly([(0.46, 0.16), (0.52, 0.12), (0.56, 0.20), (0.52, 0.28), (0.47, 0.26)])  # Europe
    poly([(0.47, 0.34), (0.55, 0.30), (0.60, 0.42), (0.58, 0.62), (0.52, 0.72), (0.48, 0.55)])  # Africa
    poly([(0.58, 0.12), (0.72, 0.08), (0.88, 0.14), (0.96, 0.26), (0.90, 0.40), (0.78, 0.46), (0.66, 0.38), (0.60, 0.24)])  # Asia
    poly([(0.82, 0.68), (0.90, 0.64), (0.94, 0.74), (0.88, 0.82), (0.83, 0.76)])  # Australia
    text(x0 + 6, y0 + 4, "WHERE IT HAPPENED", SANS_B(11), fill=NAVY)

PINS = [  # (story no, fx, fy) fractions of the map box — spread out, no clusters
    (1, 0.76, 0.42), (2, 0.86, 0.30), (3, 0.62, 0.34), (4, 0.50, 0.18),
    (9, 0.20, 0.50), (11, 0.96, 0.70), (12, 0.97, 0.86),
    (14, 0.12, 0.28), (15, 0.26, 0.44), (16, 0.44, 0.44),
]
MAPX, MAPY, MAPW, MAPH = MX, 858, 420, 88
draw_map(MAPX, MAPY, MAPW, MAPH)
for n, fx, fy in PINS:
    px, py = MAPX + fx * MAPW, MAPY + fy * MAPH
    d.ellipse([px - 7, py - 7, px + 7, py + 7], fill=RED, outline=(255, 255, 255), width=1)
    f = SANS_B(8)
    tw = d.textlength(str(n), font=f)
    d.text((px - tw / 2, py - 5), str(n), font=f, fill=(255, 255, 255))

# ---------------- ALSO ON FRIDAY 20 NOVEMBER (17-28) ----------------
ALSO = [
    (17, "UK expels Myanmar defence attaché", "after the ICJ verdict"),
    (18, "Voyager 1 reaches one light-day", "NASA confirms the milestone"),
    (19, "Anthropic valued at $1.5tn", "reportedly, ahead of debut"),
    (20, "Hayabusa2 drops asteroid landing", "engine trouble forces rethink"),
    (21, "Tanker burns after mine strike", "east of the Strait of Hormuz"),
    (22, "Canada courts AI data centres", "as the US pushes back"),
    (23, "California probes Nvidia chips", "over sales to China"),
    (24, "Fiona the hippo dies", "Cincinnati Zoo mourns its star"),
    (25, "Russia open to NATO-like pledges", "US envoy tells allies"),
    (26, "Blast by Dutch embassy in Kyiv", "minor damage, no injuries"),
    (27, "Taiwan steadies its stock slide", "after a 5,248-point fall"),
    (28, "Takaichi dodges Taiwan question", "at the APEC press conference"),
]
ax = MX + 436
text(ax, 858, "ALSO ON FRIDAY 20 NOVEMBER", SANS_B(14), fill=RED)
for k, (n, head, sub) in enumerate(ALSO):
    col = k // 6
    row = k % 6
    x0 = ax + col * 272
    y0 = 880 + row * 12
    text(x0, y0, f"{n}.", SANS_B(11), fill=RED)
    text(x0 + 20, y0, head, SANS_B(11))

# ---------------- DATE CHECK footer + sources ----------------
d.rectangle([MX, 956, MX2, 1000], outline=RED, width=2)
text(MX + 8, 960, "DATE CHECK — NOT FRIDAY'S NEWS:", SANS_B(12), fill=RED)
dc = ("The ICJ genocide verdict on Myanmar, the first Shenzhen summit meeting, GTA VI's "
      "$1.84bn sales and Anthropic's $81.3bn IPO debut were all first reported on 19 November — "
      "so they are not counted as this day's news.")
for j, ln in enumerate(wrap(dc, SANS(12), MX2 - MX - 16)):
    text(MX + 8, 976 + j * 13, ln, SANS(12), fill=GREY)
text(MX, 1006, "Sources: BBC, Reuters, The Hindu, AP, NASA, IAEA — 20 Nov 2026. "
               "All pictures and flags drawn for this page; no photograph used.", SANS(10), fill=GREY)

img.save("entry.png", optimize=True)
print("saved entry.png")
