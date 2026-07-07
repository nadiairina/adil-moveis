import os
import glob
import re

AOS_CSS = '  <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">\n</head>'
AOS_JS = """
  <!-- AOS Animation Script -->
  <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
  <script>
    AOS.init({
      duration: 800,
      easing: 'ease-out-cubic',
      once: true,
      offset: 50
    });
  </script>
</body>
"""

for filepath in glob.glob("*.html"):
    if filepath == "dashboard.html":
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Inject AOS CSS if not present
    if 'aos.css' not in content:
        content = content.replace('</head>', AOS_CSS)

    # 2. Inject AOS JS if not present
    if 'aos.js' not in content:
        content = content.replace('</body>', AOS_JS)

    # 3. Add AOS attributes to various elements
    
    # 3.1. Animate Hero Sections
    # find <h1 class="..." > and make it fade-down
    content = re.sub(r'(<h1[^>]*class="[^"]*?")', r'\1 data-aos="fade-down"', content)
    
    # find hero paragraphs
    content = re.sub(r'(<p[^>]*class="text-xl[^"]*?")', r'\1 data-aos="fade-up" data-aos-delay="200"', content)
    
    # find hero buttons
    content = re.sub(r'(<a[^>]*class="[^"]*?inline-block[^"]*?")', r'\1 data-aos="fade-up" data-aos-delay="400"', content)
    
    # 3.2. Animate Product Cards / Category Cards
    # product cards
    content = content.replace('class="product ', 'class="product " data-aos="fade-up" ')
    # category links in index
    content = content.replace('class="group relative overflow-hidden block"', 'class="group relative overflow-hidden block" data-aos="zoom-in" data-aos-delay="100"')
    
    # 3.3. Animate the 'Porque nos escolher?' Section in index.html
    if filepath == "index.html":
        # The 3 benefit columns
        content = content.replace('class="flex flex-col items-center group"', 'class="flex flex-col items-center group" data-aos="fade-up" data-aos-delay="100"')
        
        # The history section text
        content = content.replace('class="md:w-1/2 space-y-8"', 'class="md:w-1/2 space-y-8" data-aos="fade-left"')
        
        # The history section image
        content = content.replace('class="relative"','class="relative" data-aos="fade-right"')

    # 3.4. Footer animation
    content = content.replace('<footer class="bg-black text-white py-10">', '<footer class="bg-black text-white py-10" data-aos="fade-in">')
    
    # 3.5. Newsletter
    content = content.replace('class="bg-white p-10 md:p-14 rounded-2xl', 'class="bg-white p-10 md:p-14 rounded-2xl" data-aos="zoom-in-up" ')

    # 4. Antarte touches (Soft taupe/greige background where it's gray-50 or gray-100)
    # Antarte uses very elegant beige/greige
    content = content.replace('bg-gray-50', 'bg-[#f7f5f0]')
    content = content.replace('bg-gray-100', 'bg-[#f0ede6]')
    content = content.replace('bg-[#faf9f6]', 'bg-[#f7f5f0]')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("AOS animations added to all files and Antarte colors applied!")
