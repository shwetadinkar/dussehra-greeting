"""Generate a crisp 1200×630 WhatsApp preview from the illustrated greeting."""
from pathlib import Path
import base64
import io
import re

html = Path("index.html").read_text(encoding="utf-8")
match = re.search(r'<script id="hero-encoded" type="text/plain">\s*(.*?)\s*</script>', html, re.S)

if match:
    from PIL import Image, ImageOps
    image_bytes = base64.b64decode(re.sub(r'\s+', '', match.group(1)))
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    preview = ImageOps.fit(image, (1200, 630), method=Image.Resampling.LANCZOS, centering=(.5,.48))
    preview.save("preview.png", optimize=True)
else:
    # Backward compatibility while converting the old SVG-only website.
    import cairosvg
    match = re.search(r'(<svg\s+id="scene".*?</svg>)', html, re.S)
    if not match:
        raise SystemExit("Neither embedded artwork nor legacy stage SVG exists")
    svg = match.group(1).replace('<svg id="scene"', '<svg xmlns="http://www.w3.org/2000/svg" id="scene"', 1)
    for element_id in ("trail", "flying-arrow", "impact", "flames"):
        svg = svg.replace(f'id="{element_id}"', f'id="{element_id}" opacity="0"', 1)
    svg = svg.replace(">", '><rect width="900" height="490" fill="#412548"/>', 1)
    cairosvg.svg2png(bytestring=svg.encode(), write_to="preview.png", output_width=1200, output_height=630)

print(f"Generated preview.png ({Path('preview.png').stat().st_size:,} bytes)")
