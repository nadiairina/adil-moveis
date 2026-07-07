import glob
import re

def main():
    html_files = glob.glob("*.html")
    for filepath in html_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # 1. Center the desktop menu
            # First, check if it's already centered
            if 'absolute left-1/2 transform -translate-x-1/2' not in content:
                content = content.replace(
                    '<nav class="hidden lg:flex items-center space-x-8">',
                    '<nav class="hidden lg:flex items-center space-x-8 absolute left-1/2 transform -translate-x-1/2">'
                )

            # 2. Remove bg-fixed from hero banners to fix image centering
            content = content.replace('bg-cover bg-fixed', 'bg-cover')

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
        except Exception as e:
            print(f"Error processing {filepath}: {e}")
    print("Tweaks applied: Menu centered and parallax (bg-fixed) removed.")

if __name__ == "__main__":
    main()
