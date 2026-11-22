"""High-fidelity synthetic ID document generator.

Renders realistic mock government ID cards (front & back) with:
- Guilloche / security wave pattern backgrounds
- Saffron/green header & footer bands (resembling national standard ID card palettes)
- Machine-readable zone / 2D QR barcode
- Avatar portrait box & hologram stamp
- Real-world camera effects (perspective warp onto tabletop, lighting gradient, sensor grain)
- Layout deviations to test acceptance vs deviation rejection
"""

from __future__ import annotations

import math
import random
from datetime import date
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont
import qrcode

SPECIMEN = ""

_FONT_PATHS = [
    "/System/Library/Fonts/Supplemental/Arial.ttf",
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
]


def _get_font(size: int, bold: bool = False):
    for p in _FONT_PATHS:
        if bold and "Bold" not in p:
            continue
        if Path(p).exists():
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default()


def draw_guilloche(draw: ImageDraw.ImageDraw, width: int, height: int, step: int = 14):
    """Draw fine sine/cosine background security waves."""
    for y in range(0, height, step):
        pts = []
        for x in range(0, width, 8):
            wave = math.sin(x * 0.025) * 8 + math.cos((x + y) * 0.015) * 5
            pts.append((x, y + wave))
        draw.line(pts, fill=(232, 238, 245), width=1)


def generate_qr(payload: str, size: int = 150) -> Image.Image:
    """Generate a clean 2D verification barcode."""
    qr = qrcode.QRCode(box_size=4, border=1)
    qr.add_data(payload)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    return img.resize((size, size))


def draw_portrait(draw: ImageDraw.ImageDraw, x: int, y: int, w: int, h: int, rng: random.Random):
    """Draw a realistic synthetic photo placeholder with shading."""
    # Background
    draw.rectangle([x, y, x + w, y + h], fill=(210, 222, 235), outline=(130, 150, 180), width=2)
    # Head
    face_w, face_h = int(w * 0.46), int(h * 0.44)
    fx = x + (w - face_w) // 2
    fy = y + int(h * 0.16)
    skin = (rng.randint(190, 220), rng.randint(150, 180), rng.randint(120, 150))
    draw.ellipse([fx, fy, fx + face_w, fy + face_h], fill=skin)
    # Hair
    draw.arc([fx - 2, fy - 6, fx + face_w + 2, fy + int(face_h * 0.6)], start=170, end=370, fill=(35, 30, 30), width=6)
    # Shoulders
    sx, sy = x + int(w * 0.12), y + int(h * 0.58)
    draw.chord([sx, sy, x + w - int(w * 0.12), y + h + int(h * 0.3)], start=180, end=360, fill=(45, 65, 95))


def render_realistic_id(
    name: str,
    id_number: str,
    dob: str,
    gender: str = "MALE",
    layout: str = "standard",  # standard | alternative_compact | deviated_unrecognized
    output_path: str = "id_card.jpg",
    apply_photo_capture: bool = True,
    seed: int = 42,
) -> str:
    """Render a card with layout and camera distortion options."""
    rng = random.Random(seed)
    W, H = 1000, 630  # ~CR80 card ratio
    card = Image.new("RGB", (W, H), (252, 253, 255))
    d = ImageDraw.Draw(card)

    # 1. Background Guilloche
    draw_guilloche(d, W, H)

    font_header = _get_font(28, bold=True)
    font_bold = _get_font(24, bold=True)
    font_regular = _get_font(20, bold=False)
    font_small = _get_font(15, bold=False)

    if layout == "standard":
        # National tricolour inspired header / footer band
        d.rectangle([0, 0, W, 22], fill=(225, 115, 35))
        d.rectangle([0, 22, W, 70], fill=(245, 248, 252))
        d.rectangle([0, H - 22, W, H], fill=(45, 140, 60))

        # Emblem placeholder / header title
        d.text((40, 32), "GOVERNMENT OF INDIA - SPECIMEN IDENTITY CARD", fill=(20, 35, 75), font=font_header)

        # Portrait Box (Left)
        draw_portrait(d, 50, 110, 220, 280, rng)

        # Fields (Middle)
        d.text((310, 120), "Name:", fill=(110, 110, 110), font=font_small)
        d.text((310, 142), name.upper(), fill=(15, 15, 15), font=font_bold)

        d.text((310, 195), "Date of Birth / DOB:", fill=(110, 110, 110), font=font_small)
        d.text((310, 218), dob, fill=(20, 20, 20), font=font_regular)

        d.text((310, 265), "Gender:", fill=(110, 110, 110), font=font_small)
        d.text((310, 288), gender, fill=(20, 20, 20), font=font_regular)

        # Prominent ID number (Masked 12-digit style format: XXXX XXXX 1234)
        d.line([310, 335, 680, 335], fill=(200, 210, 220), width=1)
        d.text((310, 350), "IDENTIFICATION NUMBER", fill=(110, 110, 110), font=font_small)
        d.text((310, 375), id_number, fill=(25, 35, 80), font=_get_font(32, bold=True))

        # QR Code on Right
        qr_img = generate_qr(f"SPECIMEN ID: {id_number}; NAME: {name}; DOB: {dob}", size=200)
        card.paste(qr_img, (W - 240, 140))
        d.text((W - 240, 350), "DIGITALLY SIGNED", fill=(90, 100, 115), font=font_small)

        # Hologram foil circle
        d.ellipse([W - 140, 410, W - 70, 480], fill=(215, 225, 235), outline=(170, 190, 210), width=2)
        d.text((W - 128, 438), "VALID", fill=(100, 125, 150), font=font_small)

        # Warning / Specimen disclaimer
        d.text((W // 2, H - 45), SPECIMEN, fill=(160, 40, 40), font=font_small, anchor="mm")

    elif layout == "alternative_compact":
        # Different layout (Horizontal banner + right-aligned portrait)
        d.rectangle([0, 0, W, 60], fill=(30, 65, 130))
        d.text((30, 18), "NATIONAL RESIDENT CARD (SPECIMEN)", fill="white", font=font_header)

        # Fields (Left)
        d.text((50, 110), "Full Name:", fill=(110, 110, 110), font=font_small)
        d.text((50, 135), name.upper(), fill=(15, 15, 15), font=font_bold)

        d.text((50, 195), "DOB / Gender:", fill=(110, 110, 110), font=font_small)
        d.text((50, 220), f"{dob}  |  {gender}", fill=(20, 20, 20), font=font_regular)

        d.text((50, 290), id_number, fill=(25, 35, 80), font=_get_font(32, bold=True))

        # Portrait (Right)
        draw_portrait(d, W - 280, 100, 230, 290, rng)
        qr_img = generate_qr(f"SPECIMEN ID: {id_number}", size=140)
        card.paste(qr_img, (50, 370))

        d.text((W // 2, H - 35), SPECIMEN, fill=(160, 40, 40), font=font_small, anchor="mm")

    elif layout == "deviated_unrecognized":
        # Complete deviation: looks like a gym pass or visiting card rather than official ID
        d.rectangle([0, 0, W, H], fill=(245, 245, 235))
        d.rectangle([0, 0, W, 80], fill=(80, 80, 80))
        d.text((W // 2, 40), "CITY CLUB MEMBERSHIP & ENTRY CARD", fill="white", font=font_header, anchor="mm")
        d.text((100, 160), f"Member: {name}", fill=(30, 30, 30), font=font_bold)
        d.text((100, 220), "Status: Temporary Visitor", fill=(100, 100, 100), font=font_regular)
        d.text((100, 280), f"Card No: {id_number}", fill=(120, 40, 40), font=font_regular)
        d.text((W // 2, H - 50), "NOT AN OFFICIAL GOVERNMENT IDENTITY DOCUMENT", fill=(180, 30, 30), font=font_bold, anchor="mm")

    if not apply_photo_capture:
        card.save(output_path, "JPEG", quality=95)
        return output_path

    # Realistic camera capture simulation:
    # 1. Perspective warp (simulate smartphone photo on tabletop)
    img_cv = cv2.cvtColor(np.array(card), cv2.COLOR_RGB2BGR)
    src_pts = np.float32([[0, 0], [W, 0], [W, H], [0, H]])

    pad = 90
    dst_w, dst_h = W + pad * 2, H + pad * 2
    # Perspective tilt
    dx1, dy1 = rng.randint(25, 55), rng.randint(20, 50)
    dx2, dy2 = rng.randint(20, 45), rng.randint(15, 45)
    dst_pts = np.float32([
        [pad + dx1, pad + dy1],
        [dst_w - pad - dx2, pad + dy2 * 0.7],
        [dst_w - pad + rng.randint(-15, 15), dst_h - pad - rng.randint(10, 35)],
        [pad - rng.randint(5, 25), dst_h - pad - rng.randint(15, 40)]
    ])

    matrix = cv2.getPerspectiveTransform(src_pts, dst_pts)
    warped = cv2.warpPerspective(img_cv, matrix, (dst_w, dst_h), borderValue=(215, 208, 195)) # wooden desk background

    # Convert back to PIL
    final_img = Image.fromarray(cv2.cvtColor(warped, cv2.COLOR_BGR2RGB))

    # Add lighting gradient & camera sensor noise
    lighting = Image.new("L", final_img.size, 255)
    ldraw = ImageDraw.Draw(lighting)
    ldraw.ellipse([dst_w // 2 - 200, 0, dst_w // 2 + 500, dst_h], fill=210)
    final_img = ImageEnhance.Brightness(final_img).enhance(0.96)
    final_img = final_img.filter(ImageFilter.GaussianBlur(0.4)) # slight camera lens blur

    final_img.save(output_path, "JPEG", quality=88)
    return output_path


if __name__ == "__main__":
    import os
    os.makedirs("/tmp/id_test", exist_ok=True)
    p1 = render_realistic_id("Rahul Sharma", "XXXX XXXX 8842", "15/08/1988", "MALE", layout="standard", output_path="/tmp/id_test/standard_id.jpg")
    p2 = render_realistic_id("Asha Nair", "XXXX XXXX 1923", "02/11/1994", "FEMALE", layout="alternative_compact", output_path="/tmp/id_test/compact_id.jpg")
    p3 = render_realistic_id("Vikram Patel", "MEM-9921", "N/A", "MALE", layout="deviated_unrecognized", output_path="/tmp/id_test/deviated_gym_pass.jpg")
    print("Rendered:", p1, p2, p3)

