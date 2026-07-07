import glob
import re

for filepath in glob.glob("*.html"):
    if filepath == "dashboard.html":
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The old floating menu block we need to nuke:
    # <div class="absolute top-0 left-0 w-full z-10 flex justify-between items-center p-4">
    #   <a href="index.html">
    #     <img src="images/logo.png" alt="Adil Móveis" ...>
    #   </a>
    #   <button class="flex items-center space-x-2 text-white bg-black bg-opacity-50 py-2 px-3 rounded" id="menuButton">
    #     <span class="uppercase font-bold">MENU</span>
    #     <i data-feather="menu" class="w-6 h-6"></i>
    #   </button>
    # </div>
    
    # We use regex with DOTALL to match across newlines
    pattern = r'<div class="absolute top-0 left-0 w-full z-10 flex justify-between items-center p-4">.*?</button>\s*</div>'
    
    # Replace the matched block with an empty string
    new_content = re.sub(pattern, '', content, flags=re.DOTALL)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Nuked old floating menu from {filepath}")

print("Global cleanup complete.")
