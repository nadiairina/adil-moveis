import glob
import re

html_files = glob.glob("*.html")
favicon_tag = '<link rel="icon" type="image/png" href="images/logo.png">'

for filepath in html_files:
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        if "rel=\"icon\"" not in content:
            # Inject before the closing </head>
            content = re.sub(r'</head>', f'  {favicon_tag}\n</head>', content)
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Added favicon to {filepath}")
        else:
            print(f"Favicon already in {filepath}")
    except Exception as e:
        print(f"Error {filepath}: {e}")
