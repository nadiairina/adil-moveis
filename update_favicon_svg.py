import glob
import re

html_files = glob.glob("*.html")

# The old favicon
old_favicon = r'<link rel="icon" type="image/png" href="images/logo.png">'

# The new luxury SVG favicon
# Dark square (#111111) with golden (#C8B598) "A" or "AM"
# Let's do "A" in a nice serif or sans font.
svg_favicon = """<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect width='100' height='100' rx='20' fill='%23111111'/><text x='50%' y='50%' font-size='65' text-anchor='middle' dominant-baseline='central' fill='%23C8B598' font-family='Georgia, serif'>A</text></svg>">"""

for filepath in html_files:
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        if old_favicon in content:
            content = content.replace(old_favicon, svg_favicon)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Updated favicon to SVG in {filepath}")
        elif "rel=\"icon\"" not in content:
            # If for some reason it didn't have it, inject before </head>
            content = re.sub(r'</head>', f'  {svg_favicon}\n</head>', content)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Injected SVG favicon in {filepath}")
            
    except Exception as e:
        print(f"Error {filepath}: {e}")
