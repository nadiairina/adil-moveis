import glob
import re

# Fix the category hero banner: remove mt-20 (gap), increase height, ensure image centers
OLD_HERO = 'class="relative h-56 md:h-64 bg-gray-200 mt-20"'
NEW_HERO = 'class="relative h-72 md:h-96 bg-gray-900"'

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    content = content.replace(OLD_HERO, NEW_HERO)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  Fixed hero: {filepath}")
    else:
        print(f"  No hero change: {filepath}")

def main():
    html_files = glob.glob("*.html")
    for filepath in sorted(html_files):
        fix_file(filepath)
    print("Done!")

if __name__ == "__main__":
    main()
