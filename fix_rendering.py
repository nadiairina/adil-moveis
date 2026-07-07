import glob
import re

def main():
    # 1. Fix CSS - remove transform from body animation which breaks sticky/fixed and AOS
    try:
        with open('styles.css', 'r', encoding='utf-8') as f:
            css = f.read()
            
        css = css.replace('transform: translateY(8px);', '')
        css = css.replace('transform: translateY(0);', '')
        
        # Or better, just remove the body animation entirely to be safe
        css = re.sub(r'body\s*\{\s*animation:\s*fadeInPage[^}]+\}\s*', '', css)
        
        with open('styles.css', 'w', encoding='utf-8') as f:
            f.write(css)
    except Exception as e:
        print("CSS Error:", e)

    # 2. Fix HTML - change bg-white/85 to bg-white/90 (standard Tailwind)
    html_files = glob.glob("*.html")
    for filepath in html_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            content = content.replace('bg-white/85', 'bg-white/90')
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
        except Exception as e:
            print("HTML Error:", e)

    print("Fixes applied.")

if __name__ == "__main__":
    main()
