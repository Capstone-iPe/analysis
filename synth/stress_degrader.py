"""Image degradation and OCR stress pipeline for synthetic test documents.

Generates realistic real-world inconsistencies and noise:
1. Low-light / severe underexposure
2. Specular camera flash / uneven glare hotspots
3. Sensor ISO noise (Gaussian + salt-and-pepper)
4. Motion & optical blur (defocus / camera shake)
5. Non-standard color format shifts (harsh yellow warm cast, cool fluorescent cast, washed-out sepia, grayscale fax)
6. Partial occlusion (thumb/finger on border, paper clip shadow)
7. Xerox / thermal photocopy high-contrast degradation
"""

from __future__ import annotations

import math
import random
import cv2
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter, ImageDraw


def apply_gaussian_noise(img: np.ndarray, mean: float = 0, sigma: float = 25) -> np.ndarray:
    """Simulate high-ISO mobile camera sensor noise."""
    noise = np.random.normal(mean, sigma, img.shape).astype(np.float32)
    noisy = np.clip(img.astype(np.float32) + noise, 0, 255).astype(np.uint8)
    return noisy


def apply_motion_blur(img: np.ndarray, size: int = 12, angle: float = 30) -> np.ndarray:
    """Simulate hand jitter / camera shake during capture."""
    k = np.zeros((size, size), dtype=np.float32)
    rad = math.radians(angle)
    dx, dy = math.cos(rad), math.sin(rad)
    for i in range(size):
        r = i - size / 2.0
        x = int(round(size / 2.0 + r * dx))
        y = int(round(size / 2.0 + r * dy))
        if 0 <= x < size and 0 <= y < size:
            k[y, x] = 1.0
    k /= (np.sum(k) or 1.0)
    return cv2.filter2D(img, -1, k)


def apply_specular_glare(img: np.ndarray, rng: random.Random) -> np.ndarray:
    """Simulate camera flash reflection off plastic lamination."""
    h, w = img.shape[:2]
    overlay = np.zeros((h, w), dtype=np.float32)
    cx, cy = rng.randint(int(w * 0.3), int(w * 0.7)), rng.randint(int(h * 0.2), int(h * 0.8))
    rx, ry = rng.randint(int(w * 0.15), int(w * 0.25)), rng.randint(int(h * 0.12), int(h * 0.22))
    cv2.ellipse(overlay, (cx, cy), (rx, ry), angle=rng.randint(0, 180), startAngle=0, endAngle=360, color=1.0, thickness=-1)
    overlay = cv2.GaussianBlur(overlay, (101, 101), 0)
    # Blend glare over image
    res = img.astype(np.float32) + overlay[:, :, None] * 160.0
    return np.clip(res, 0, 255).astype(np.uint8)


def apply_color_cast(img: np.ndarray, cast_type: str) -> np.ndarray:
    """Simulate tricky ambient lighting (warm tungsten, cold fluorescent, or photocopy)."""
    res = img.astype(np.float32)
    if cast_type == "warm_tungsten":
        # Heavy yellow/orange tint
        res[:, :, 0] *= 0.65  # Blue channel down
        res[:, :, 1] *= 0.90  # Green channel slight
        res[:, :, 2] *= 1.25  # Red channel up
    elif cast_type == "cool_fluorescent":
        # Harsh blue/green office lighting
        res[:, :, 0] *= 1.25
        res[:, :, 1] *= 1.10
        res[:, :, 2] *= 0.75
    elif cast_type == "xerox_photocopy":
        # High contrast black & white photocopy
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (3, 3), 0)
        bw = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 6)
        return cv2.cvtColor(bw, cv2.COLOR_GRAY2BGR)
    elif cast_type == "faded_thermal":
        # Low-contrast washed out thermal print
        res = res * 0.5 + 110.0
    return np.clip(res, 0, 255).astype(np.uint8)


def apply_finger_occlusion(img: np.ndarray, rng: random.Random) -> np.ndarray:
    """Simulate a user's thumb partially holding the edge of the card."""
    h, w = img.shape[:2]
    res = img.copy()
    tx = rng.randint(0, int(w * 0.15))
    ty = rng.randint(int(h * 0.4), int(h * 0.7))
    # Draw oval skin tone for thumb
    cv2.ellipse(res, (tx, ty), (int(w * 0.08), int(h * 0.16)), angle=15, startAngle=0, endAngle=360, color=(145, 175, 215), thickness=-1)
    cv2.ellipse(res, (tx, ty), (int(w * 0.08), int(h * 0.16)), angle=15, startAngle=0, endAngle=360, color=(110, 140, 180), thickness=2)
    return res


def degrade_image(
    input_path: str,
    output_path: str,
    degradation_type: str,  # glare | blur | underexposed | tungsten | fluorescent | xerox | sensor_noise | thumb_occlusion
    seed: int = 42,
) -> str:
    """Apply specific optical/camera inconsistencies to an image file."""
    rng = random.Random(seed)
    cv_img = cv2.imread(input_path)
    if cv_img is None:
        raise ValueError(f"Could not load image at {input_path}")

    if degradation_type == "glare":
        res = apply_specular_glare(cv_img, rng)
    elif degradation_type == "blur":
        res = apply_motion_blur(cv_img, size=14, angle=rng.randint(15, 45))
    elif degradation_type == "underexposed":
        # Low light / dark room capture
        res = np.clip(cv_img.astype(np.float32) * 0.38, 0, 255).astype(np.uint8)
        res = apply_gaussian_noise(res, sigma=18)
    elif degradation_type == "tungsten":
        res = apply_color_cast(cv_img, "warm_tungsten")
    elif degradation_type == "fluorescent":
        res = apply_color_cast(cv_img, "cool_fluorescent")
    elif degradation_type == "xerox":
        res = apply_color_cast(cv_img, "xerox_photocopy")
    elif degradation_type == "faded":
        res = apply_color_cast(cv_img, "faded_thermal")
    elif degradation_type == "sensor_noise":
        res = apply_gaussian_noise(cv_img, sigma=35)
    elif degradation_type == "thumb_occlusion":
        res = apply_finger_occlusion(cv_img, rng)
    else:
        res = cv_img

    cv2.imwrite(output_path, res, [cv2.IMWRITE_JPEG_QUALITY, 82])
    return output_path


if __name__ == "__main__":
    import os
    os.makedirs("/tmp/stress_test", exist_ok=True)
    base = "/tmp/id_test/standard_id.jpg"
    types = ["glare", "blur", "underexposed", "tungsten", "fluorescent", "xerox", "faded", "sensor_noise", "thumb_occlusion"]
    for t in types:
        out = f"/tmp/stress_test/standard_{t}.jpg"
        degrade_image(base, out, t)
        print("Generated stress test:", out)

