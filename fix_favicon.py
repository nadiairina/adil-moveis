import glob
import re

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    # Replace favicon with proper .ico file
    content = re.sub(
        r'<link rel="icon"[^>]+>',
        '<link rel="icon" type="image/x-icon" href="images/favicon.ico">',
        content
    )
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  Fixed favicon: {filepath}")

def main():
    html_files = glob.glob("*.html")
    for filepath in sorted(html_files):
        fix_file(filepath)
    print("Done!")

if __name__ == "__main__":
    main()
