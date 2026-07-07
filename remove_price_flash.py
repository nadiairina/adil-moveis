import glob
import re

price_pattern = r'<span class="snipcart-total-price[^>]*>.*?</span>'

for filepath in glob.glob("*.html"):
    if filepath == "dashboard.html":
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove the snipcart total price span completely to stop any flashing
    content = re.sub(price_pattern, '', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Removed the flashing total price span from all files.")
