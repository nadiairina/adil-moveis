import glob
import re

def main():
    # 1. Update CSS
    css_additions = """
/* =========================================
   MODERNIZATION UPDATES
   ========================================= */

/* 1. Fade-in Page Transition */
@keyframes fadeInPage {
  from { opacity: 0; transform: translateY(8px); }
  to { opacity: 1; transform: translateY(0); }
}
body {
  animation: fadeInPage 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94) forwards;
}

/* 2. Ken Burns Effect */
@keyframes kenBurns {
  0% { transform: scale(1); }
  100% { transform: scale(1.12); }
}
.ken-burns {
  animation: kenBurns 20s ease-out infinite alternate;
}

/* 3. Global Product Image Micro-Interaction */
.product {
  overflow: hidden;
  transition: box-shadow 0.4s ease, transform 0.4s ease;
}
.product:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 24px -8px rgba(0,0,0,0.1);
}
.product > div.bg-cover {
  transition: transform 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94) !important;
}
.product:hover > div.bg-cover {
  transform: scale(1.08) !important;
}
"""
    try:
        with open('styles.css', 'r', encoding='utf-8') as f:
            css_content = f.read()
        
        if "MODERNIZATION UPDATES" not in css_content:
            with open('styles.css', 'a', encoding='utf-8') as f:
                f.write("\n" + css_additions)
            print("Updated styles.css")
    except Exception as e:
        print("Error updating css:", e)

    # 2. Update HTML files
    html_files = glob.glob("*.html")
    
    for filepath in html_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # A. Glassmorphism Header
            # Replace exactly the header classes
            content = re.sub(
                r'<header class="sticky top-0 z-50 bg-\[#FDFBF7\](.*?)">',
                r'<header class="sticky top-0 z-50 bg-white/85 backdrop-blur-md transition-all duration-300\1">',
                content
            )
            # Some headers might have different spaces or attributes
            content = content.replace('bg-[#FDFBF7] shadow-sm border-b', 'bg-white/85 backdrop-blur-md shadow-sm border-b')

            # B. Parallax Hero Banners (excluding index.html which has a different hero)
            if filepath != "index.html":
                content = content.replace('class="absolute inset-0 bg-cover"', 'class="absolute inset-0 bg-cover bg-fixed"')
                # Some might have inline styles with bg-cover in class
                content = re.sub(r'class="absolute inset-0 bg-cover" style="([^"]+)"', r'class="absolute inset-0 bg-cover bg-fixed" style="\1"', content)

            # C. Ken Burns in index.html
            if filepath == "index.html":
                # Find the img tag for the hero
                hero_img_regex = r'<img src="(https://lourini\.pt/app/uploads/2024/07/dennis-32-1200x1200\.webp)" class="([^"]+)" alt="Hero"[^>]*>'
                
                content = re.sub(
                    hero_img_regex,
                    r'<img src="\1" class="w-full h-full object-cover origin-center ken-burns" alt="Hero">',
                    content
                )
                
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
                
        except Exception as e:
            print(f"Error {filepath}: {e}")
            
    print("Updated all HTML files successfully!")

if __name__ == "__main__":
    main()
