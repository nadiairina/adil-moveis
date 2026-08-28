import os

filepath = 'pack-detalhe.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Locate the card rendering string and increase size
old_string = """            return '<a href="' + targetUrl + '" style="display:flex; align-items:center; gap:16px; background:#fff; border:1px solid #E8E3DC; border-radius:8px; padding:12px; transition:all 0.3s; text-decoration:none; color:inherit;" class="hover:shadow-sm hover:border-[#C8B598]">' +
                   '  <div style="width:70px; height:70px; min-width:70px; background:#F7F4F0; border-radius:6px; overflow:hidden; position:relative; display:flex; align-items:center; justify-content:center;">' +
                   '    <img src="' + itemImage + '" alt="' + item.name + '" style="width:100%; height:100%; object-fit:contain; mix-blend-mode:darken; padding:4px;" onerror="this.src=\\'images/logo_sem_fundo.png\\'" />' +
                   '  </div>'"""

new_string = """            return '<a href="' + targetUrl + '" style="display:flex; align-items:center; gap:16px; background:#fff; border:1px solid #E8E3DC; border-radius:8px; padding:12px; transition:all 0.3s; text-decoration:none; color:inherit;" class="hover:shadow-sm hover:border-[#C8B598]">' +
                   '  <div style="width:110px; height:110px; min-width:110px; background:#F7F4F0; border-radius:6px; overflow:hidden; position:relative; display:flex; align-items:center; justify-content:center;">' +
                   '    <img src="' + itemImage + '" alt="' + item.name + '" style="width:100%; height:100%; object-fit:contain; mix-blend-mode:darken; padding:6px;" onerror="this.src=\\'images/logo_sem_fundo.png\\'" />' +
                   '  </div>'"""

if old_string in content:
    content = content.replace(old_string, new_string)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully increased thumbnail size to 110px!")
else:
    print("Error: Could not find old_string to replace!")
