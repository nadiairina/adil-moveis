import glob
import os

# REVERT LOGO TO ORIGINAL
OLD_LOGO = 'src="images/adil_moveis_new_logo.png"'
NEW_LOGO = 'src="images/adil-moveis-logo.png"'

# Since we want to improve the "format" of her original logo, we will ensure it has `mix-blend-multiply` 
# so the white background disappears into our new beige navbar, making it look much cleaner.
# The class `mix-blend-multiply` is already on the img tag in the new Navbar:
# <img src="images/adil_moveis_new_logo.png" alt="Adil Móveis" class="h-16 w-auto mix-blend-multiply">

for filepath in glob.glob("*.html"):
    if filepath == "dashboard.html":
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if OLD_LOGO in content:
        content = content.replace(OLD_LOGO, NEW_LOGO)
        
        # In case she meant "formato" as in size, let's ensure it's beautifully scaled
        # We can increase the height slightly so it's more prominent but still sleek.
        content = content.replace('class="h-16 w-auto mix-blend-multiply"', 'class="h-14 md:h-16 w-auto mix-blend-multiply drop-shadow-sm"')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Logo reverted to the original and formatted with transparency blending.")
