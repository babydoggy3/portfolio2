"""Inline styles.css into index.html (between the CSS markers) so the page renders without a blocking request.
Edit styles.css, then run: python3 -I tools/inline-css.py"""
from pathlib import Path
import re

root = Path(__file__).resolve().parent.parent
html = (root / "index.html").read_text()
css = (root / "styles.css").read_text()
css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
css = re.sub(r"\s*\n\s*", "\n", css).strip()
block = f"<!--css-->\n<style>\n{css}\n</style>\n<!--/css-->"
if "<!--css-->" in html:
    html = re.sub(r"<!--css-->.*?<!--/css-->", lambda _: block, html, flags=re.S)
else:
    html = html.replace('<link rel="stylesheet" href="styles.css">', block)
(root / "index.html").write_text(html)
print(f"inlined {len(css)} bytes of CSS")
