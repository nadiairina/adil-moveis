import glob
import re

# 1. Update the "Packs" button from Red to Beige/Gold
old_packs_desktop = r'<a href="conjuntos\.html" class="text-sm font-bold tracking-widest text-red-600 uppercase transition-all duration-300 border border-red-600 px-3 py-1 rounded hover:bg-red-600 hover:text-white animate-pulse">'
new_packs_desktop = '<a href="conjuntos.html" class="text-sm font-bold tracking-widest text-[#C8B598] uppercase transition-all duration-300 border border-[#C8B598] px-3 py-1 rounded hover:bg-[#C8B598] hover:text-white animate-pulse">'

old_packs_mobile = r'<a href="conjuntos\.html" class="text-lg font-bold text-red-600 border border-red-600 rounded px-3 py-1 -ml-3 animate-pulse">Comprar Packs</a>'
new_packs_mobile = '<a href="conjuntos.html" class="text-lg font-bold text-[#C8B598] border border-[#C8B598] rounded px-3 py-1 -ml-3 animate-pulse">Comprar Packs</a>'

for filepath in glob.glob("*.html"):
    if filepath == "dashboard.html":
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update Packs color
    content = re.sub(old_packs_desktop, new_packs_desktop, content)
    content = re.sub(old_packs_mobile, new_packs_mobile, content)
    
    # 2. Add Animations (AOS) to product cards
    # If a product div doesn't have data-aos, we add it.
    # Find `<div class="product group cursor-pointer" data-category="all">`
    # Replace with `<div class="product group cursor-pointer" data-category="all" data-aos="fade-up" data-aos-duration="800">`
    content = content.replace('<div class="product group cursor-pointer" data-category="all">', '<div class="product group cursor-pointer" data-category="all" data-aos="fade-up" data-aos-duration="800">')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# 3. Customize Snipcart Cart Design via CSS variables
# We will append this to styles.css
snipcart_css = """
/* SNIPCART CUSTOMIZATION (LUXURY THEME) */
#snipcart {
    /* Primary Colors */
    --color-default: #111111;
    --color-alt: #666666;
    --color-icon: #111111;
    --color-success: #C8B598;
    --color-error: #ff4d4f;
    
    /* Buttons */
    --color-buttonPrimary: #111111;
    --color-buttonPrimaryHover: #333333;
    --color-buttonPrimaryActive: #000000;
    --color-buttonPrimaryDisabled: #cccccc;
    --color-buttonPrimarySuccess: #C8B598;

    --color-buttonSecondary: #ffffff;
    --color-buttonSecondaryHover: #f8f5f0;
    --color-buttonSecondaryActive: #f0ede6;

    /* Backgrounds */
    --bgColor-default: #FDFBF7;
    --bgColor-alt: #ffffff;
    --bgColor-success: #C8B598;
    --bgColor-error: #fff1f0;
    --bgColor-info: #f0ede6;

    /* Borders */
    --borderColor-default: #EAE6DF;
    
    /* Typography */
    --font-family: 'Inter', sans-serif;
}

/* Make headers inside Snipcart elegant */
.snipcart-cart-header__title {
    font-weight: 300 !important;
    text-transform: uppercase;
    letter-spacing: 0.1em;
}

.snipcart-item-line__title {
    font-weight: 600 !important;
}

/* Hide the Snipcart branding to make it look native */
.snipcart-modal__close-title {
    display: none !important;
}
"""

with open('styles.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

if "/* SNIPCART CUSTOMIZATION" not in css_content:
    with open('styles.css', 'a', encoding='utf-8') as f:
        f.write("\n" + snipcart_css)

print("Changed packs button color, added global product animations, and applied luxury Snipcart CSS variables.")
