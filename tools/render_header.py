#!/usr/bin/env python3
"""Render a geographically accurate, rotating Earth for the project README."""
from __future__ import annotations

import argparse
import base64
import json
import math
import urllib.request
from io import BytesIO
from pathlib import Path

import cairosvg
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
BASE_SVG = ROOT / "assets/motion/header-green-base.svg"
GEOJSON = ROOT / "assets/data/ne_110m_admin_0_countries.geojson"
OUT_GIF = ROOT / "assets/motion/header-green-animated.gif"
OUT_PREVIEW = ROOT / "assets/motion/header-green-preview.png"
OUT_STATIC = ROOT / "assets/motion/header-green-static.png"
OUT_STATIC_SVG = ROOT / "assets/motion/header-green.svg"
GEOJSON_URL = "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_110m_admin_0_countries.geojson"

WIDTH, HEIGHT = 1200, 300
GLOBE_CX, GLOBE_CY = 927, 151
RADIUS = 93
TILE_SIZE = 250
SUPERSAMPLE = 3
FRAME_COUNT = 180
FRAME_DURATION_MS = 100
START_LONGITUDE = -82.0


def load_country_polygons(path: Path):
    """Load and unwrap Natural Earth outer rings once for fast per-frame projection."""
    data = json.loads(path.read_text(encoding="utf-8"))
    rings = []
    for feature in data.get("features", []):
        geom = feature.get("geometry") or {}
        kind = geom.get("type")
        coords = geom.get("coordinates", [])
        polygons = [coords] if kind == "Polygon" else coords if kind == "MultiPolygon" else []
        for polygon in polygons:
            if not polygon:
                continue
            raw = polygon[0]
            if len(raw) < 4:
                continue
            lons = np.asarray([p[0] for p in raw], dtype=np.float64)
            lats = np.asarray([p[1] for p in raw], dtype=np.float64)
            unwrapped = np.degrees(np.unwrap(np.radians(lons)))
            unwrapped[-1] = unwrapped[0]
            lats[-1] = lats[0]
            rings.append((unwrapped, lats))
    return rings


def clip_ring(points, xmin=-89.75, xmax=89.75, ymin=-89.75, ymax=89.75):
    """Clip a geographic polygon ring against the visible hemisphere rectangle."""
    output = points
    edges = [
        (lambda p: p[0] >= xmin, lambda a, b: (xmin, a[1] + (b[1]-a[1])*(xmin-a[0])/(b[0]-a[0]))),
        (lambda p: p[0] <= xmax, lambda a, b: (xmax, a[1] + (b[1]-a[1])*(xmax-a[0])/(b[0]-a[0]))),
        (lambda p: p[1] >= ymin, lambda a, b: (a[0] + (b[0]-a[0])*(ymin-a[1])/(b[1]-a[1]), ymin)),
        (lambda p: p[1] <= ymax, lambda a, b: (a[0] + (b[0]-a[0])*(ymax-a[1])/(b[1]-a[1]), ymax)),
    ]
    for inside, intersect in edges:
        if not output:
            break
        source = output
        output = []
        prev = source[-1]
        prev_in = inside(prev)
        for cur in source:
            cur_in = inside(cur)
            if cur_in:
                if not prev_in:
                    try:
                        output.append(intersect(prev, cur))
                    except ZeroDivisionError:
                        pass
                output.append(cur)
            elif prev_in:
                try:
                    output.append(intersect(prev, cur))
                except ZeroDivisionError:
                    pass
            prev, prev_in = cur, cur_in
    return output


def project_ring(coords, radius, center_x, center_y):
    """Orthographic projection of a ring in local longitude/latitude degrees."""
    points = []
    for delta_lon, lat in coords:
        lam = math.radians(delta_lon)
        phi = math.radians(max(-89.999, min(89.999, lat)))
        x = center_x + radius * math.cos(phi) * math.sin(lam)
        y = center_y - radius * math.sin(phi)
        points.append((int(round(x)), int(round(y))))
    return points


def make_globe_tile(center_lon: float, countries, scale: int = SUPERSAMPLE) -> Image.Image:
    """Create a transparent holographic globe tile at supersampled resolution."""
    size = TILE_SIZE * scale
    center = size // 2
    radius = RADIUS * scale

    yy, xx = np.mgrid[0:size, 0:size]
    nx = (xx - center) / radius
    ny = -(yy - center) / radius
    rr = nx * nx + ny * ny
    inside = rr <= 1.0
    nz = np.sqrt(np.clip(1.0 - rr, 0, 1))

    light = np.array([-0.48, 0.40, 0.78], dtype=float)
    light /= np.linalg.norm(light)
    lambert = np.clip(nx * light[0] + ny * light[1] + nz * light[2], 0, 1)
    limb = np.clip((1.0 - np.sqrt(rr)) * 1.65, 0, 1)

    ocean = np.zeros((size, size, 4), dtype=np.uint8)
    ocean[..., 0] = (1 + 3 * lambert).astype(np.uint8)
    ocean[..., 1] = (12 + 18 * lambert + 5 * limb).astype(np.uint8)
    ocean[..., 2] = (7 + 9 * lambert).astype(np.uint8)
    ocean[..., 3] = np.where(inside, 255, 0).astype(np.uint8)
    tile = Image.fromarray(ocean, "RGBA")

    land_mask = Image.new("L", (size, size), 0)
    land_draw = ImageDraw.Draw(land_mask)
    boundaries = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    boundary_draw = ImageDraw.Draw(boundaries)

    for unwrapped_lons, lats in countries:
        delta = unwrapped_lons - center_lon
        delta -= 360.0 * round(float(np.mean(delta[:-1])) / 360.0)
        ring = list(zip(delta.tolist(), lats.tolist()))
        clipped = clip_ring(ring)
        if len(clipped) < 3:
            continue
        projected = project_ring(clipped, radius, center, center)
        if len(projected) >= 3:
            land_draw.polygon(projected, fill=255)
            boundary_draw.line(projected, fill=(105, 255, 166, 220),
                               width=max(1, int(scale * 0.50)), joint="curve")

    land_tint = Image.new("RGBA", (size, size), (5, 58, 29, 0))
    land_tint.putalpha(land_mask.point(lambda p: int(p * 0.78)))
    tile = Image.alpha_composite(tile, land_tint)

    # Dense, staggered pointillist surface texture, calculated as one raster mask.
    land_array = np.asarray(land_mask, dtype=np.uint8)
    gy, gx = np.mgrid[0:size, 0:size]
    step = 3 * scale
    xphase = (gx + ((gy // step) % 2) * (step // 2)) % step - step / 2
    yphase = gy % step - step / 2
    dot_radius = 1.12 * scale
    dot_pattern = (xphase * xphase + yphase * yphase) <= dot_radius * dot_radius
    dot_alpha = np.where(dot_pattern & (land_array > 100), 225, 0).astype(np.uint8)
    dots_array = np.zeros((size, size, 4), dtype=np.uint8)
    dots_array[..., 0] = 137
    dots_array[..., 1] = 255
    dots_array[..., 2] = 180
    dots_array[..., 3] = dot_alpha
    tile = Image.alpha_composite(tile, Image.fromarray(dots_array, "RGBA"))
    tile = Image.alpha_composite(tile, boundaries)

    # Latitude/longitude graticule projected over the same sphere.
    grid_layer = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    grid = ImageDraw.Draw(grid_layer)
    for lat in (-60, -30, 0, 30, 60):
        coords = []
        for delta in np.linspace(-89.5, 89.5, 260):
            phi, lam = math.radians(lat), math.radians(float(delta))
            coords.append((int(center + radius * math.cos(phi) * math.sin(lam)),
                           int(center - radius * math.sin(phi))))
        grid.line(coords, fill=(65, 255, 139, 65), width=max(1, scale // 2))
    for delta in (-75, -50, -25, 0, 25, 50, 75):
        coords = []
        for lat in np.linspace(-89.5, 89.5, 260):
            phi, lam = math.radians(float(lat)), math.radians(delta)
            coords.append((int(center + radius * math.cos(phi) * math.sin(lam)),
                           int(center - radius * math.sin(phi))))
        grid.line(coords, fill=(65, 255, 139, 65), width=max(1, scale // 2))
    tile = Image.alpha_composite(tile, grid_layer)

    highlight = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    hx, hy = int(center - 0.43*radius), int(center - 0.53*radius)
    ImageDraw.Draw(highlight).ellipse((hx-8*scale, hy-8*scale, hx+8*scale, hy+8*scale),
                                      fill=(89, 255, 153, 80))
    tile = Image.alpha_composite(tile, highlight.filter(ImageFilter.GaussianBlur(6*scale)))

    nodes = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    node_draw = ImageDraw.Draw(nodes)
    for dx, dy, node_radius, alpha in [
        (-0.43, -0.42, 1.5, 235), (0.25, -0.12, 1.1, 175), (0.48, 0.20, 1.3, 190)
    ]:
        px, py = int(center + dx*radius), int(center + dy*radius)
        if (px-center)**2 + (py-center)**2 < radius*radius:
            q = node_radius * scale
            node_draw.ellipse((px-q, py-q, px+q, py+q), fill=(187, 255, 211, alpha))
    tile = Image.alpha_composite(tile, nodes.filter(ImageFilter.GaussianBlur(0.6*scale)))

    rim = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    rim_draw = ImageDraw.Draw(rim)
    rim_draw.ellipse((center-radius, center-radius, center+radius, center+radius),
                     outline=(60, 255, 139, 210), width=max(2, scale))
    rim_draw.arc((center-radius-2*scale, center-radius-2*scale,
                  center+radius+2*scale, center+radius+2*scale),
                 195, 345, fill=(185, 255, 211, 160), width=max(1, scale))
    tile = Image.alpha_composite(tile, rim)

    orbit = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    orbit_draw = ImageDraw.Draw(orbit)
    orbit_radius = int(108 * scale)
    orbit_draw.ellipse((center-orbit_radius, center-orbit_radius,
                        center+orbit_radius, center+orbit_radius),
                       outline=(57, 255, 136, 95), width=max(1, scale//2))
    outer = int(115 * scale)
    orbit_draw.ellipse((center-outer, center-outer, center+outer, center+outer),
                       outline=(245, 217, 10, 85), width=max(1, scale//2))
    orbit_draw.arc((center-int(112*scale), center-int(55*scale),
                    center+int(112*scale), center+int(55*scale)),
                   10, 170, fill=(57, 255, 136, 75), width=max(1, scale//2))
    tile = Image.alpha_composite(tile, orbit)

    aura_mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(aura_mask).ellipse(
        (center-int(116*scale), center-int(116*scale),
         center+int(116*scale), center+int(116*scale)),
        outline=120, width=2*scale
    )
    aura = Image.new("RGBA", (size, size), (57, 255, 136, 0))
    aura.putalpha(aura_mask.filter(ImageFilter.GaussianBlur(5*scale)))
    tile = Image.alpha_composite(aura, tile)
    return tile.resize((TILE_SIZE, TILE_SIZE), Image.Resampling.LANCZOS)


def render_base(path: Path):
    return cairosvg.svg2png(url=str(path), output_width=WIDTH, output_height=HEIGHT)


def build_frame(base: Image.Image, longitude: float, countries) -> Image.Image:
    frame = base.copy().convert("RGBA")
    globe = make_globe_tile(longitude, countries)
    frame.alpha_composite(globe, (GLOBE_CX - TILE_SIZE//2, GLOBE_CY - TILE_SIZE//2))
    return frame.convert("RGB")


def ensure_geodata(path: Path):
    """Download Natural Earth 1:110m GeoJSON on first run."""
    if path.exists():
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    request = urllib.request.Request(
        GEOJSON_URL, headers={"User-Agent": "brooklyn-nine-nine-readme-renderer/1.0"}
    )
    with urllib.request.urlopen(request, timeout=45) as response:
        path.write_bytes(response.read())


def main():
    parser = argparse.ArgumentParser(description="Render the rotating Earth README banner.")
    parser.add_argument("--frames", type=int, default=FRAME_COUNT)
    parser.add_argument("--duration", type=int, default=FRAME_DURATION_MS)
    parser.add_argument("--output", type=Path, default=OUT_GIF)
    parser.add_argument("--preview", type=Path, default=OUT_PREVIEW)
    args = parser.parse_args()
    if args.frames < 48:
        raise SystemExit("Use at least 48 frames for a smooth globe rotation.")
    if not BASE_SVG.exists():
        raise SystemExit(f"Missing required asset: {BASE_SVG}")

    ensure_geodata(GEOJSON)
    base = Image.open(BytesIO(render_base(BASE_SVG))).convert("RGBA")
    countries = load_country_polygons(GEOJSON)
    print(f"Loaded {len(countries)} Natural Earth country boundaries (1:110m).")

    frames = []
    for i in range(args.frames):
        longitude = START_LONGITUDE + 360.0 * i / args.frames
        frames.append(build_frame(base, longitude, countries))
        if (i + 1) % 12 == 0 or i + 1 == args.frames:
            print(f"Rendered {i+1}/{args.frames} frames (central longitude {longitude:.1f}°).")

    palette_source = frames[0].convert("P", palette=Image.Palette.ADAPTIVE, colors=256)
    quantized = [palette_source]
    for frame in frames[1:]:
        quantized.append(frame.quantize(palette=palette_source, dither=Image.Dither.FLOYDSTEINBERG))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    quantized[0].save(
        args.output, save_all=True, append_images=quantized[1:],
        duration=args.duration, loop=0, optimize=True, disposal=1
    )
    frames[0].save(OUT_STATIC)

    globe_png = BytesIO()
    make_globe_tile(START_LONGITUDE, countries).save(globe_png, format="PNG", optimize=True)
    globe_b64 = base64.b64encode(globe_png.getvalue()).decode("ascii")
    static_image = (
        f'<image x="{GLOBE_CX - TILE_SIZE//2}" y="{GLOBE_CY - TILE_SIZE//2}" '
        f'width="{TILE_SIZE}" height="{TILE_SIZE}" '
        f'href="data:image/png;base64,{globe_b64}" preserveAspectRatio="none" />'
    )
    base_svg = BASE_SVG.read_text(encoding="utf-8")
    OUT_STATIC_SVG.write_text(base_svg.replace("</svg>", static_image + "\n</svg>"), encoding="utf-8")

    preview_ids = [0, args.frames//4, args.frames//2, (3*args.frames)//4, args.frames-1]
    sheet = Image.new("RGB", (WIDTH, HEIGHT * len(preview_ids)), (0, 0, 0))
    for row, index in enumerate(preview_ids):
        sheet.paste(frames[index], (0, row*HEIGHT))
    sheet.save(args.preview)

    check = Image.open(args.output)
    duration = check.info.get("duration", 0)
    print(f"Wrote {args.output} ({args.output.stat().st_size:,} bytes), "
          f"frames={check.n_frames}, duration={duration} ms/frame, "
          f"total={check.n_frames * duration / 1000:.2f}s")
    print(f"Static SVG fallback: {OUT_STATIC_SVG}")


if __name__ == "__main__":
    main()
