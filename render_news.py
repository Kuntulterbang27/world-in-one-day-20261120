"""Draw the original newspaper with Pillow. Offline, no clock or randomness.
Run with Python 3.13 and Pillow 13.0.0: python render_news.py
The submitted main.py needs only the standard library and copies news.png.
"""
from pathlib import Path
import hashlib
from PIL import Image, ImageDraw, ImageFont
from content import DATE, STORIES

ROOT = Path(__file__).resolve().parent
SCALE = 3
SIZE = 1024
PAPER = "#f4f0e5"
INK = "#172b36"
MUTED = "#566368"
RED = "#b13c2f"
LINE = "#c8c7bd"
COLORS = {
    "ASIA": "#a1392c", "OCEANIA": "#19778a", "AFRICA": "#92691f",
    "EUROPE": "#345d92", "MIDDLE EAST": "#8b4e2a", "AMERICAS": "#336f58",
    "ECONOMY / TECHNOLOGY": "#644a88", "GLOBAL / HUMANITARIAN": "#5a6556",
}
COLUMNS = [
    ["ASIA", "OCEANIA", "AFRICA"],
    ["EUROPE", "MIDDLE EAST"],
    ["AMERICAS", "ECONOMY / TECHNOLOGY", "GLOBAL / HUMANITARIAN"],
]
CANVAS = Image.new("RGB", (SIZE * SCALE, SIZE * SCALE), PAPER)
DRAW = ImageDraw.Draw(CANVAS)
FONT_FILES = {
    "regular": "RobotoCondensed-Regular.ttf",
    "bold": "RobotoCondensed-Bold.ttf",
    "serif": "LibreBaskerville-Bold.ttf",
}
METRICS = []


def font(size, style="regular"):
    return ImageFont.truetype(str(ROOT / "assets" / FONT_FILES[style]), round(size * SCALE))


def box(bounds, fill, outline=None, width=1):
    DRAW.rectangle(tuple(round(v * SCALE) for v in bounds), fill=fill,
                   outline=outline, width=round(width * SCALE))


def line(points, fill=LINE, width: float = 1):
    DRAW.line([(round(x * SCALE), round(y * SCALE)) for x, y in points],
              fill=fill, width=round(width * SCALE))


def text(x, y, copy, size: float = 14, style="regular", color=INK, max_width=None, floor=11.5):
    chosen = size
    face = font(chosen, style)
    if max_width is not None:
        while DRAW.textlength(copy, font=face) / SCALE > max_width and chosen > floor:
            chosen = max(floor, chosen - 0.25)
            face = font(chosen, style)
        actual = DRAW.textlength(copy, font=face) / SCALE
        assert actual <= max_width, (copy, actual, max_width)
    DRAW.text((round(x * SCALE), round(y * SCALE)), copy, font=face,
              fill=color, anchor="lt", stroke_width=0)
    METRICS.append((copy, chosen))


def masthead():
    text(22, 14, "THE WORLD IN ONE DAY", 49, "serif", max_width=980, floor=40)
    line([(22, 77), (1002, 77)], INK, 2)
    text(22, 86, DATE, 18, "bold")
    text(673, 89, "39 REPORTS  /  SIX CONTINENTS  /  ONE DAY", 13, "bold", max_width=329)
    line([(22, 112), (1002, 112)], INK, 1)


def lead():
    box((22, 122, 1002, 309), INK)
    text(38, 134, "01  /  THE LEAD  /  MYANMAR + BANGLADESH", 12, "bold", "#ddbc77")
    text(38, 155, "AFTER THE GENOCIDE RULING", 25, "bold", PAPER, 597)
    text(38, 188, "A ROAD HOME FOR", 35, "serif", PAPER, 597)
    text(38, 230, "THE ROHINGYA?", 35, "serif", PAPER, 597)
    # An original scales-of-justice drawing, not a photograph or borrowed artwork.
    line([(606, 194), (606, 246), (591, 246), (621, 246)], "#ddbc77", 2)
    line([(583, 206), (629, 206)], "#ddbc77", 2)
    for cx in (586, 626):
        line([(cx, 207), (cx - 9, 224), (cx + 9, 224), (cx, 207)], "#ddbc77", 1)
    text(38, 277, "Bangladesh eyes returns in 1–1.5 years; Myanmar rejects ICJ verdict.",
         14, "regular", PAPER, 597)
    draw_world_map(657, 137, 326, 139)
    text(658, 280, "ICJ: Myanmar responsible for Rohingya genocide.", 12, "bold", "#ddbc77", 324)
    text(658, 297, "Ruling: 19 Nov.  /  New responses: Friday, 20 Nov.", 11.5, "regular", PAPER, 324)


def draw_world_map(x, y, width, height):
    box((x, y, x + width, y + height), "#273e47")
    def project(longitude, latitude):
        return (x + (longitude + 180) / 360 * width,
                y + (85 - latitude) / 145 * height)

    # Deliberately simplified original silhouettes; markers are approximate.
    continents = [
        [(-168, 69), (-141, 72), (-119, 69), (-103, 76), (-80, 70),
         (-58, 53), (-65, 45), (-81, 25), (-97, 17), (-105, 28),
         (-117, 31), (-126, 49), (-154, 57)],
        [(-53, 60), (-43, 59), (-24, 76), (-39, 83), (-58, 77)],
        [(-81, 12), (-69, 10), (-50, -1), (-35, -8), (-44, -25),
         (-54, -35), (-68, -55), (-75, -36), (-80, -7)],
        [(-11, 36), (-7, 48), (5, 59), (22, 71), (39, 69),
         (48, 54), (31, 42), (19, 40), (10, 35)],
        [(-17, 35), (10, 37), (33, 31), (43, 12), (51, 11),
         (43, -12), (34, -29), (20, -35), (11, -17), (-1, 4), (-16, 15)],
        [(31, 42), (39, 69), (81, 76), (124, 71), (179, 63),
         (163, 50), (142, 44), (130, 30), (120, 20), (108, 7),
         (99, 5), (93, 22), (80, 6), (68, 24), (56, 25), (45, 12),
         (35, 29)],
        [(113, -22), (130, -12), (143, -11), (154, -28),
         (145, -39), (131, -32), (115, -35)],
        [(47, -13), (50, -18), (46, -26), (44, -20)],
        [(130, 33), (140, 36), (145, 44), (140, 43)],
        [(166, -34), (178, -39), (171, -46), (166, -45), (173, -40)],
        [(96, 4), (104, -6), (121, -9), (137, -6), (150, -7), (141, -2), (110, -3)],
    ]
    for points in continents:
        DRAW.polygon([(round(px * SCALE), round(py * SCALE))
                      for px, py in (project(lon, lat) for lon, lat in points)],
                     fill="#6c8588")
    for longitude in range(-120, 181, 60):
        px = x + (longitude + 180) / 360 * width
        line([(px, y), (px, y + height)], "#3c525b", 0.5)
    for latitude in (-45, 0, 45):
        py = y + (85 - latitude) / 145 * height
        line([(x, py), (x + width, py)], "#3c525b", 0.5)
    # Regional colour coding matches the section headers below.
    for number, region, _, _, longitude, latitude in STORIES:
        px = x + (longitude + 180) / 360 * width
        py = y + (85 - latitude) / 145 * height
        color = "#ddbc77" if number == 1 else COLORS[region]
        DRAW.ellipse(((px - 2.7) * SCALE, (py - 2.7) * SCALE,
                      (px + 2.7) * SCALE, (py + 2.7) * SCALE), fill="#f4f0e5")
        DRAW.ellipse(((px - 2) * SCALE, (py - 2) * SCALE,
                      (px + 2) * SCALE, (py + 2) * SCALE), fill=color)
    text(x + 5, y + 5, "THE DAY, MAPPED", 10, "bold", "#ffffff")


def news_icon(x, y, number, color):
    """Small original pictograms distinguish the most consequential briefs."""
    if number == 35:  # market chart
        line([(x, y), (x, y + 13), (x + 15, y + 13)], color, 1)
        line([(x + 2, y + 2), (x + 6, y + 5), (x + 9, y + 3),
              (x + 14, y + 11)], color, 1.7)
    elif number == 16:  # tanker
        line([(x, y + 7), (x + 4, y + 12), (x + 12, y + 12),
              (x + 16, y + 7), (x, y + 7)], color, 1.3)
        box((x + 5, y + 3, x + 11, y + 6), color)
    elif number == 21:  # climate leaf
        DRAW.ellipse(((x + 2) * SCALE, y * SCALE, (x + 14) * SCALE,
                      (y + 12) * SCALE), outline=color, width=3)
        line([(x + 1, y + 14), (x + 12, y + 3)], color, 1.3)
    elif number == 24:  # bridge
        line([(x, y + 5), (x + 16, y + 5)], color, 1.8)
        for dx in (2, 8, 14):
            line([(x + dx, y + 5), (x + dx, y + 13)], color, 1.3)
    elif number == 33:  # earthquake trace
        line([(x, y + 7), (x + 4, y + 7), (x + 6, y),
              (x + 9, y + 14), (x + 11, y + 6), (x + 16, y + 6)], color, 1.3)
    elif number == 6:  # cyclone
        DRAW.arc((x * SCALE, y * SCALE, (x + 16) * SCALE, (y + 14) * SCALE),
                 30, 320, fill=color, width=4)
        DRAW.arc(((x + 4) * SCALE, (y + 4) * SCALE,
                  (x + 12) * SCALE, (y + 10) * SCALE), 180, 460, fill=color, width=4)


def section(x, y, name, stories, row_height):
    color = COLORS[name]
    box((x, y, x + 310, y + 20), color)
    text(x + 7, y + 3, name, 13, "bold", "#ffffff", 295)
    y += 29
    for number, _, headline, context, _, _ in stories:
        if number in (6, 16, 21, 24, 33, 35):
            box((x - 2, y - 3, x + 312, y + row_height - 4), "#eae8dc")
            news_icon(x + 1, y + 19, number, color)
        text(x, y + 1, f"{number:02}", 11, "bold", color)
        text(x + 23, y, headline, 15.5, "bold", INK, 287, floor=12)
        text(x + 23, y + 20, context, 13.0, "regular", MUTED, 287, floor=11.5)
        line([(x + 23, y + row_height - 5), (x + 310, y + row_height - 5)], LINE, 0.45)
        y += row_height
    return y + 7


def news_columns():
    for column_index, regions in enumerate(COLUMNS):
        x = 22 + column_index * 335
        y = 327
        rows = sum(sum(story[1] == name for story in STORIES) for name in regions)
        row_height = (647 - len(regions) * 36) / rows
        for name in regions:
            group = [story for story in STORIES if story[1] == name]
            y = section(x, y, name, group, row_height)
        assert y <= 981, (column_index, y)
        if column_index < 2:
            line([(x + 322, 327), (x + 322, 974)], LINE, 0.7)


def render():
    masthead()
    lead()
    news_columns()
    line([(22, 985), (1002, 985)], INK, 1)
    text(22, 995, "FRIDAY EVENTS + FIRST REPORTS  •  Numbers link to SOURCES.md  •  Reuters / AP / AFP / public records", 11, "regular", INK, 830)
    text(920, 995, "20 / 11 / 26", 11, "bold", INK, 82)
    final = CANVAS.resize((SIZE, SIZE), Image.Resampling.LANCZOS)
    path = ROOT / "news.png"
    final.save(path, format="PNG", optimize=True, compress_level=9)
    assert path.stat().st_size <= 1048576
    print("RENDER", final.size, "RGB", path.stat().st_size, "bytes")
    print("SHA256", hashlib.sha256(path.read_bytes()).hexdigest())
    print("MINIMUM FONT", min(size for _, size in METRICS))


if __name__ == "__main__":
    render()
