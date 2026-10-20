"""Create a GitHub Pages/WhatsApp preview PNG from the corrected SVG stage."""
from pathlib import Path
import re
import cairosvg

html = Path("index.html").read_text(encoding="utf-8")
match = re.search(r'(<svg\s+id="scene".*?</svg>)', html, re.S)
if not match:
    raise SystemExit("Could not find stage SVG in index.html")
svg = match.group(1).replace(
    '<svg id="scene"', '<svg xmlns="http://www.w3.org/2000/svg" id="scene"', 1
)
# These shapes are animated and initially invisible via the webpage CSS;
# hide them explicitly when rendering the standalone SVG preview.
for element_id in ("trail", "flying-arrow", "impact", "flames"):
    svg = svg.replace(f'id="{element_id}"', f'id="{element_id}" opacity="0"', 1)
svg = svg.replace(">", '><rect width="900" height="490" fill="#412548"/>', 1)
cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to="preview.png", output_width=1200, output_height=630)
print(f"Created preview.png ({Path('preview.png').stat().st_size:,} bytes)")
