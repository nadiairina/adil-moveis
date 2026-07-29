from PIL import Image
import glob
import re

# 1. Process Logo
img = Image.open('images/adil_moveis_new_logo.png').convert("RGBA")
datas = img.getdata()

new_data = []
for item in datas:
    # change all white (also shades of whites)
    # to transparent
    if item[0] > 200 and item[1] > 200 and item[2] > 200:
        new_data.append((255, 255, 255, 0))
    else:
        # make the non-white pixels pure black for higher definition line art
        new_data.append((0, 0, 0, 255))

img.putdata(new_data)
# Save it in high res
img.save("images/logo_transparent.png", "PNG")
print("Saved transparent logo.")

# 2. Update all HTML files
html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r') as f:
        content = f.read()

    # Replace logo path
    content = content.replace('images/logo.png', 'images/logo_transparent.png')
    
    # Remove mix-blend-mode:multiply from logo styles
    content = content.replace('mix-blend-mode:multiply;', '')
    content = content.replace('mix-blend-mode: multiply;', '')

    # 3. Add Animations
    # The user wants more animations on all pages. Let's add data-aos="fade-up" to h2, h3 and .category-card if they don't have it
    # We'll use a regex to inject data-aos into tags that don't already have it
    
    def add_aos_to_tag(match):
        tag = match.group(0)
        if 'data-aos=' in tag:
            return tag
        # Insert data-aos="fade-up" before the closing bracket
        return tag[:-1] + ' data-aos="fade-up">'

    # Find <h2 ...> or <h2> without data-aos
    content = re.sub(r'<h2\b[^>]*>', add_aos_to_tag, content)
    # Find <h3 ...> or <h3> without data-aos
    content = re.sub(r'<h3\b[^>]*>', add_aos_to_tag, content)
    # Find <p ...> (maybe too many? let's stick to headers and sections)
    
    with open(file, 'w') as f:
        f.write(content)

print("Finished processing HTML files.")
