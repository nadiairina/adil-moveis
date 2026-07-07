import glob
import re

def main():
    html_files = glob.glob("*.html")
    
    for filepath in html_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # 1. Favicon
            content = content.replace('images/logo_inverted.png', 'images/logo.png')

            # 2. Promo Banner !
            content = content.replace('Grátis num Raio de 50km (Lisboa e Setúbal)!', 'Grátis num Raio de 50km (Lisboa e Setúbal)')

            # 3. Hamburger lg:hidden
            content = re.sub(
                r'<button class="text-black hover:text-gray-600 transition-colors"\s+id="hamburgerBtn">',
                r'<button class="lg:hidden text-black hover:text-gray-600 transition-colors" id="hamburgerBtn">',
                content
            )

            # 4. Agendar Visita & Social in Header
            header_insert = r'''<div class="flex items-center space-x-6">
            <div class="hidden lg:flex items-center space-x-3 mr-4">
              <a href="https://www.instagram.com/adilmoveis/" target="_blank" class="text-gray-500 hover:text-[#E1306C] transition-colors"><i data-feather="instagram" class="w-4 h-4"></i></a>
              <a href="https://www.facebook.com/p/Adil-M%C3%B3veis-100063641348118/" target="_blank" class="text-gray-500 hover:text-[#1877F2] transition-colors"><i data-feather="facebook" class="w-4 h-4"></i></a>
              <div class="h-4 w-px bg-gray-300 mx-2"></div>
              <a href="contactos.html" class="flex items-center text-[10px] font-bold uppercase tracking-widest border border-gray-300 px-4 py-1.5 rounded-full hover:border-black hover:bg-black hover:text-white transition-all shadow-sm">Agendar Visita</a>
            </div>'''
            
            # Replace the opening div for the right side menu
            if '<div class="hidden lg:flex items-center space-x-3 mr-4">' not in content:
                content = content.replace('<div class="flex items-center space-x-6">', header_insert, 1)

            # 5. Filters UI Update
            # Replace the wrapper
            content = content.replace(
                '<div class="flex flex-wrap justify-center gap-6 md:gap-10 mb-12 border-b border-[#EAE6DF] pb-4">',
                '<div class="flex overflow-x-auto justify-start md:justify-center gap-3 mb-12 pb-4 scrollbar-hide px-4">'
            )
            
            # Replace the active button
            content = re.sub(
                r'<button class="filter-button[^"]*?active"[^>]*>([^<]+)</button>',
                r'<button class="filter-button active bg-black text-white px-6 py-2.5 rounded-full text-xs font-bold tracking-widest uppercase whitespace-nowrap transition-all shadow-md" data-category="\1">\1</button>',
                content, flags=re.IGNORECASE
            )
            # Fix data-category values which were captured as the text
            # This is tricky because "Todos" maps to "all". Let's just fix the hardcoded ones.

            # Actually, let's just do a blanket regex for all filter buttons since we don't know the exact classes anymore due to multiple edits.
            def replacer(match):
                classes = match.group(1)
                data_cat = match.group(2)
                text = match.group(3)
                
                if 'active' in classes:
                    new_classes = 'filter-button active bg-black text-white px-6 py-2.5 rounded-full text-xs font-bold tracking-widest uppercase whitespace-nowrap transition-all shadow-md'
                else:
                    new_classes = 'filter-button bg-[#F3F4F6] text-gray-600 hover:bg-gray-200 hover:text-black px-6 py-2.5 rounded-full text-xs font-bold tracking-widest uppercase whitespace-nowrap transition-all'
                
                return f'<button class="{new_classes}" data-category="{data_cat}">{text}</button>'

            content = re.sub(
                r'<button class="filter-button([^"]*?)"\s+data-category="([^"]+)">([^<]+)</button>',
                replacer,
                content
            )

            # 6. Filter JS Update
            js_old = """      // Update active button styling
      filterButtons.forEach(btn => {
        btn.classList.remove('active');
        btn.classList.remove('text-black', 'border-black');
        btn.classList.add('text-gray-400', 'border-transparent');
      });
      
      // Apply active styling to clicked button
      this.classList.add('active', 'text-black', 'border-black');
      this.classList.remove('text-gray-400', 'border-transparent');"""
            
            js_new = """      // Update active button styling
      filterButtons.forEach(btn => {
        btn.classList.remove('active', 'bg-black', 'text-white', 'shadow-md');
        btn.classList.add('bg-[#F3F4F6]', 'text-gray-600');
      });
      
      // Apply active styling to clicked button
      this.classList.remove('bg-[#F3F4F6]', 'text-gray-600');
      this.classList.add('active', 'bg-black', 'text-white', 'shadow-md');"""
            
            content = content.replace(js_old, js_new)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
        except Exception as e:
            print(f"Error processing {filepath}: {e}")

    # Add scrollbar hide to styles.css
    try:
        with open('styles.css', 'r', encoding='utf-8') as f:
            css = f.read()
        if '.scrollbar-hide' not in css:
            css += '''\n/* Hide scrollbar for filters */
.scrollbar-hide::-webkit-scrollbar {
    display: none;
}
.scrollbar-hide {
    -ms-overflow-style: none;
    scrollbar-width: none;
}\n'''
            with open('styles.css', 'w', encoding='utf-8') as f:
                f.write(css)
    except Exception as e:
        print("CSS Error:", e)

    print("Premium updates applied.")

if __name__ == "__main__":
    main()
