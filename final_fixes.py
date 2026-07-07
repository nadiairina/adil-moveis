import glob
import re

html_files = glob.glob("*.html")

# The SVG Favicon to replace
svg_favicon_pattern = r'<link rel="icon" href="data:image/svg\+xml,.*?</svg>">'
# The old PNG favicon
png_favicon = '<link rel="icon" type="image/png" href="images/logo.png">'

# The footer text to add
# Let's find: <p class="mt-8 text-xs text-gray-500">&copy; 2026 Adil Móveis. Todos os direitos reservados.</p>
# And append the "Website desenvolvido por..." paragraph right after it.

footer_credit = '<p class="mt-2 text-xs text-gray-400">Website desenvolvido por <a href="https://nadiairina.github.io/portfolio/" target="_blank" class="text-gray-500 hover:text-white transition-colors underline">Nadia Irina</a></p>'

for filepath in html_files:
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Revert Favicon
        if "data:image/svg+xml" in content:
            content = re.sub(svg_favicon_pattern, png_favicon, content)
            
        # Add footer credit if it's not there
        if "desenvolvido por" not in content and "&copy; 2026 Adil Móveis" in content:
            # For most pages
            content = content.replace(
                '<p class="mt-8 text-xs text-gray-500">&copy; 2026 Adil Móveis. Todos os direitos reservados.</p>',
                f'<p class="mt-8 text-xs text-gray-500">&copy; 2026 Adil Móveis. Todos os direitos reservados.</p>\n            {footer_credit}'
            )
            # For old_testemunhos or others that might have a different structure
            if "desenvolvido por" not in content:
                 content = content.replace(
                    '<p>&copy; 2026 Adil Móveis. Todos os direitos reservados.</p>',
                    f'<p>&copy; 2026 Adil Móveis. Todos os direitos reservados.</p>\n      {footer_credit}'
                )
                 
            print(f"Fixed {filepath}")
            
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
            
    except Exception as e:
        print(f"Error {filepath}: {e}")
