import glob
import re

html_files = [
    "quartos.html", "salas.html", "cozinha.html", "colchoes.html", 
    "conjuntos.html", "kids.html", "escritorio.html", "complementos.html"
]

# The old button pattern might vary slightly, but generally:
# class="filter-button px-6 py-3 bg-[#f0ede6] hover:bg-navy hover:text-white transition-all rounded-md active"
# Let's replace the whole class string.
old_class_pattern = r'class="filter-button[^"]*"'

# New classes for inactive buttons
new_class = 'class="filter-button pb-2 text-gray-400 hover:text-black uppercase tracking-widest text-xs font-bold border-b-2 border-transparent hover:border-black transition-all"'
# New class for the active button ("Todos")
new_class_active = 'class="filter-button pb-2 text-black uppercase tracking-widest text-xs font-bold border-b-2 border-black transition-all active"'

for filepath in html_files:
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        if "filter-button" in content:
            # First, replace ALL filter buttons with the inactive class
            content = re.sub(old_class_pattern, new_class, content)
            
            # Then, find the "Todos" button and make it active
            # The "Todos" button usually has `data-category="all">Todos</button>`
            # Let's be careful with the exact string
            todos_pattern = new_class + r'( data-category="all">)'
            content = re.sub(todos_pattern, new_class_active + r'\1', content)
            
            # Update the JS so it toggles the new classes
            # The JS currently does:
            # btn.classList.remove('active');
            # btn.classList.remove('bg-navy', 'text-white');
            # btn.classList.add('bg-[#f0ede6]');
            
            js_old_remove = r"btn\.classList\.remove\('bg-navy',\s*'text-white'\);"
            js_old_add = r"btn\.classList\.add\('bg-\[\#f0ede6\]'\);"
            js_new_remove = r"btn.classList.remove('text-black', 'border-black');\n        btn.classList.add('text-gray-400', 'border-transparent');"
            
            js_this_add = r"this\.classList\.add\('active',\s*'bg-navy',\s*'text-white'\);"
            js_this_remove = r"this\.classList\.remove\('bg-\[\#f0ede6\]'\);"
            js_new_this = r"this.classList.add('active', 'text-black', 'border-black');\n      this.classList.remove('text-gray-400', 'border-transparent');"
            
            content = re.sub(js_old_remove + r'\s*' + js_old_add, js_new_remove, content)
            content = re.sub(js_this_add + r'\s*' + js_this_remove, js_new_this, content)
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Modernized filters in {filepath}")
    except Exception as e:
        print(f"Error {filepath}: {e}")
