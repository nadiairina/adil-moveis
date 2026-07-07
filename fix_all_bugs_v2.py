import glob
import re

# 1. FIX Z-INDEX OF MENU AND CORRECT LOGO CROPPING ON ALL PAGES
for filepath in glob.glob("*.html"):
    if filepath == "dashboard.html":
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Increase Sidebar z-index so it overlaps WhatsApp button
    content = content.replace('z-[60]', 'z-[999]')

    # Fix the Logo so it's NOT cropped into a circle (which cut off the "A" and "ÓVEIS")
    # Restore it to a neat white rectangle/pill that displays the full image
    bad_logo_pattern = r'<img src="images/adil-moveis-logo\.png" alt="Adil Móveis" class="h-14 md:h-16 w-14 md:w-16 object-cover bg-white rounded-full border-2 border-gray-200 shadow-sm p-1">'
    good_logo = '<img src="images/adil-moveis-logo.png" alt="Adil Móveis" class="h-10 md:h-12 w-auto bg-white rounded border border-gray-200 shadow-sm px-2 py-1">'
    
    # Also catch any residual unstyled logos
    basic_logo_pattern = r'<img src="images/adil-moveis-logo\.png" alt="Adil Móveis" class="h-14 md:h-16 w-auto">'
    
    content = re.sub(bad_logo_pattern, good_logo, content)
    content = re.sub(basic_logo_pattern, good_logo, content)

    # 2. DELETE OLD DOUBLE MENU FROM ALL PAGES
    # The old floating menu block
    start_idx = content.find('<div class="absolute top-0 left-0 w-full z-10 flex justify-between items-center p-4">')
    if start_idx != -1:
        # Find where this block ends. It ends when the page header section begins.
        end_idx = content.find('</div>\\n      \\n  <!-- Page Header', start_idx)
        if end_idx == -1:
            end_idx = content.find('</button>\\n  </div>', start_idx)
            if end_idx != -1:
                end_idx += 17 # length of </button>\n  </div>
                
        if end_idx != -1:
            content = content[:start_idx] + content[end_idx:]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Double menu removed globally, Logo restored to full width, Sidebar pushed above WhatsApp button.")
