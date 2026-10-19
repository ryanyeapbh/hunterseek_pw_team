"""Build readable contact sheets from the downloaded card webp files."""
import os
from PIL import Image

SRC = "ace-arena/gundam-assemble/cards"
OUT = "ace-arena/gundam-assemble/cards/_sheets"
os.makedirs(OUT, exist_ok=True)

GAP = 16
BG = (255, 255, 255)


def stack(paths, crops, scale, out_path):
    """crops: list of (left, top, right, bottom) in source pixels, or None for full."""
    tiles = []
    for p, c in zip(paths, crops):
        im = Image.open(os.path.join(SRC, p)).convert("RGB")
        if c:
            im = im.crop(c)
        w = int(im.width * scale)
        h = int(im.height * scale)
        tiles.append(im.resize((w, h), Image.LANCZOS))
    W = max(t.width for t in tiles)
    H = sum(t.height for t in tiles) + GAP * (len(tiles) - 1)
    sheet = Image.new("RGB", (W, H), BG)
    y = 0
    for t in tiles:
        sheet.paste(t, (0, y))
        y += t.height + GAP
    sheet.save(out_path, quality=95)
    print(out_path, sheet.size)


# --- unit cards: 800x567 -> stats band around y 340..567
units = [f"img_card_st01-u0{i}_en.webp" for i in range(1, 7)]
unit_crop = (0, 335, 800, 567)
for i in range(0, 6, 2):
    group = units[i:i + 2]
    stack(group, [unit_crop] * len(group), 1.6,
          f"{OUT}/units_{i//2 + 1}.png")

# --- tactics cards: 746x1044 -> rules text region y 575..955
tacts = [f"img_card_st01-t{n:02d}_en.webp" for n in range(1, 19)]
tact_crop = (0, 570, 746, 960)
for i in range(0, 18, 3):
    group = tacts[i:i + 3]
    stack(group, [tact_crop] * len(group), 1.45,
          f"{OUT}/tactics_{i//3 + 1}.png")
