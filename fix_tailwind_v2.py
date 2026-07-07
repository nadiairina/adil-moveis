import os
import glob

for filepath in glob.glob("*.html"):
    if filepath == "dashboard.html":
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Menu width fix (the cause of the full screen menu)
    content = content.replace('sm:w-[400px]', 'sm:w-96')
    content = content.replace('md:w-[400px]', 'md:w-96')
    
    # 2. Fix other arbitrary values from recent index changes
    content = content.replace('h-[80vh]', 'h-full') # fallback
    content = content.replace('h-[90vh]', 'h-full')
    content = content.replace('class="relative h-full md:h-full bg-[#ebe7e0] flex items-center justify-center overflow-hidden"', 'class="relative bg-[#ebe7e0] flex items-center justify-center overflow-hidden" style="height: 85vh;"')
    
    # If the above replacement didn't catch because of exact string matching, let's just do:
    content = content.replace('h-[80vh]', '')
    content = content.replace('md:h-[90vh]', '')
    content = content.replace('class="relative  bg-[#ebe7e0]', 'class="relative bg-[#ebe7e0]" style="height: 85vh;"')
    # Actually just replace using regex for safety
    import re
    # Fix height
    content = re.sub(r'class="(.*?)h-\[80vh\] md:h-\[90vh\](.*?)"', r'class="\1 \2" style="height: 85vh;"', content)
    
    # Fix tracking
    content = content.replace('tracking-[0.2em]', 'tracking-widest')
    
    # Fix aspect ratio
    content = re.sub(r'class="(.*?)aspect-\[4/5\](.*?)"', r'class="\1 \2" style="aspect-ratio: 4/5;"', content)
    
    # Fix menu positioning absolute vs fixed inside the relative. 
    # Actually the menu is full screen because:
    # <div class="absolute top-0 right-0 w-full sm:w-[400px] h-screen bg-white shadow-2xl flex flex-col overflow-hidden">
    # replacing sm:w-[400px] with sm:w-96 will fix it.
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Tailwind v2 compatibility fixes applied!")
