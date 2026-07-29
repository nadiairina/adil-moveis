import glob

html_files = glob.glob("*.html")

for filepath in html_files:
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        content = content.replace(
            '<link rel="icon" type="image/png" href="images/logo.png">',
            '<link rel="icon" type="image/png" href="images/logo_inverted.png">'
        )
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
            
    except Exception as e:
        print(f"Error {filepath}: {e}")
print("Successfully updated all favicons to logo_inverted.png")
