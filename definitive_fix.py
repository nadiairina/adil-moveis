import glob
import re

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content

    # 1. FIX MENU: The nav with absolute needs the parent div to be relative
    # The parent div is: class="flex items-center justify-between h-20"
    content = content.replace(
        'class="flex items-center justify-between h-20"',
        'class="flex items-center justify-between h-20 relative"'
    )

    # 2. FIX FAVICON: ensure the favicon is logo.png (dark logo)
    content = re.sub(
        r'<link rel="icon"[^>]+>',
        '<link rel="icon" type="image/png" href="images/logo.png">',
        content
    )

    # 3. FIX HERO IMAGES: Remove bg-fixed (parallax) and ensure bg-center
    # These were category page hero banners
    content = re.sub(
        r"(style=\"background-image: url\('[^']+'\);)\s*background-position:\s*center center;\"",
        r'\1 background-position: center center; background-attachment: scroll;"',
        content
    )
    # Also fix class-based bg-fixed still leftover
    content = content.replace('bg-cover bg-fixed', 'bg-cover')
    content = content.replace('bg-fixed bg-cover', 'bg-cover')

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  Fixed: {filepath}")
    else:
        print(f"  No changes: {filepath}")

def main():
    html_files = glob.glob("*.html")
    print(f"Processing {len(html_files)} HTML files...")
    for filepath in sorted(html_files):
        fix_file(filepath)
    print("\nDone!")

if __name__ == "__main__":
    main()
