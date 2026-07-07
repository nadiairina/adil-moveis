import os
import re

directory = "/Users/nadiairina/Desktop/adil móveis/adil-moveis"
html_files = [f for f in os.listdir(directory) if f.endswith('.html')]

# We'll fix the global promo banner in all files:
# Original: font-size:13px;font-weight:700;letter-spacing:0.15em;z-index:50;position:relative;border-bottom:1px solid #b09e85;overflow:hidden;white-space:nowrap;
# Original container: <div style="background-color:#C8B598;color:#ffffff;padding:8px 0;font-size:13px;...

# Filter buttons are currently: 
# <button class="filter-button px-6 py-3 filter-button-link transition-all rounded-md" data-category="...">
# We can add Tailwind classes like hover:bg-[#C8B598] hover:text-white hover:shadow-lg transform hover:-translate-y-1

for file in html_files:
    filepath = os.path.join(directory, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix Promo Banner Size
    # It might vary slightly, so let's use regex
    content = re.sub(
        r'padding:8px 0;font-size:13px;',
        r'padding:14px 0;font-size:16px;',
        content
    )
    
    # 2. Fix Filter Buttons
    content = content.replace(
        'filter-button px-6 py-3 filter-button-link transition-all rounded-md',
        'filter-button px-6 py-3 transition-all duration-300 rounded-full font-medium tracking-wide shadow-sm hover:shadow-md hover:bg-[#C8B598] hover:text-white hover:-translate-y-1'
    )
    # The active button was usually: bg-navy text-white or bg-gray-100
    # Let's just rely on the JS for active states, but we improved the base classes above.
    
    # 3. Clean up Testemunhos.html
    if file == 'testemunhos.html':
        # Remove any weird dangling Snipcart tags
        # Replace everything after </footer> with a clean block
        footer_end = content.find('</footer>')
        if footer_end != -1:
            clean_end = """
    <script>
      // Initialize Feather Icons
      document.addEventListener('DOMContentLoaded', () => {
        if(typeof feather !== 'undefined') feather.replace();
        const y = document.getElementById('currentYear');
        if(y) y.textContent = new Date().getFullYear();
        
        const m = document.getElementById('menuButton');
        const c = document.getElementById('closeMenuBtn');
        const o = document.getElementById('menuOverlay');
        const s = document.getElementById('menuSidebar');
        if(m && o) m.addEventListener('click', () => { o.classList.remove('hidden'); s.style.transform='translateX(0)'; document.body.style.overflow='hidden'; });
        if(c && o) c.addEventListener('click', () => { s.style.transform='translateX(100%)'; setTimeout(()=>o.classList.add('hidden'),300); document.body.style.overflow=''; });
      });
    </script>
    <script async src="https://cdn.snipcart.com/themes/v3.4.1/default/snipcart.js"></script>
    <div id="snipcart" data-api-key="ODE4MjNlYWYtZGViOS00OGY3LWJhZWEtODU1OTE5OTYzMzQxNjM5MTYyMDI2OTM2NjA0MTY3" hidden></div>
    <div class="floating-contact-bar">
      <a href="https://www.google.com/maps/search/?api=1&query=Adil+Móveis+Feijó+Almada" target="_blank" rel="noopener" class="floating-btn floating-btn-sec">📍 Como Chegar</a>
      <a href="contactos.html?agendar=true" class="floating-btn floating-btn-primary">📅 Agendar Visita</a>
      <a href="https://wa.me/351912582788" target="_blank" rel="noopener" class="floating-btn floating-btn-wpp">💬 Pedir Orçamento</a>
    </div>
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script>document.addEventListener('DOMContentLoaded', function() { if(typeof AOS !== 'undefined') AOS.init({duration:800, once:true, offset:100}); });</script>
</body>
</html>
"""
            content = content[:footer_end + 9] + clean_end

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("UI enhancements applied.")
