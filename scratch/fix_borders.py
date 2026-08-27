import os

# 1. Update produto-detalhe.html
pdp_path = 'produto-detalhe.html'
if os.path.exists(pdp_path):
    with open(pdp_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update .pdp-main-image-wrap
    old_wrap = '''      .pdp-main-image-wrap {
        aspect-ratio: 4/3;
        background-color: #f7f4f0;
        overflow: hidden;
        border-radius: 8px;
        border: 1px solid #E8E3DC;
        cursor: zoom-in;
        position: relative;
      }'''
    
    new_wrap = '''      .pdp-main-image-wrap {
        aspect-ratio: 4/3;
        background-color: transparent;
        overflow: hidden;
        border-radius: 8px;
        border: none;
        cursor: zoom-in;
        position: relative;
      }'''
    
    # Update .pdp-thumb background
    old_thumb = '''      .pdp-thumb {
        width: 76px; height: 76px;
        flex-shrink: 0;
        border-radius: 6px;
        border: 2px solid transparent;
        overflow: hidden;
        cursor: pointer;
        background: #f7f4f0;
        transition: border-color 0.2s ease;
      }'''
      
    new_thumb = '''      .pdp-thumb {
        width: 76px; height: 76px;
        flex-shrink: 0;
        border-radius: 6px;
        border: 2px solid transparent;
        overflow: hidden;
        cursor: pointer;
        background: transparent;
        transition: border-color 0.2s ease;
      }'''
      
    if old_wrap in content:
        content = content.replace(old_wrap, new_wrap)
        print('Updated .pdp-main-image-wrap in produto-detalhe.html')
    else:
        # Fallback with less strict spaces
        content = content.replace('background-color: #f7f4f0;', 'background-color: transparent;', 1)
        content = content.replace('border: 1px solid #E8E3DC;', 'border: none;', 1)
        print('Applied fallback replacement for main wrap in produto-detalhe.html')
        
    if old_thumb in content:
        content = content.replace(old_thumb, new_thumb)
        print('Updated .pdp-thumb in produto-detalhe.html')
    else:
        content = content.replace('background: #f7f4f0;', 'background: transparent;', 1)
        print('Applied fallback replacement for thumb in produto-detalhe.html')
        
    with open(pdp_path, 'w', encoding='utf-8') as f:
        f.write(content)

# 2. Update pack-detalhe.html
pack_path = 'pack-detalhe.html'
if os.path.exists(pack_path):
    with open(pack_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if old_wrap in content:
        content = content.replace(old_wrap, new_wrap)
        print('Updated .pdp-main-image-wrap in pack-detalhe.html')
    else:
        content = content.replace('background-color: #f7f4f0;', 'background-color: transparent;', 1)
        content = content.replace('border: 1px solid #E8E3DC;', 'border: none;', 1)
        print('Applied fallback replacement for main wrap in pack-detalhe.html')
        
    if old_thumb in content:
        content = content.replace(old_thumb, new_thumb)
        print('Updated .pdp-thumb in pack-detalhe.html')
    else:
        content = content.replace('background: #f7f4f0;', 'background: transparent;', 1)
        print('Applied fallback replacement for thumb in pack-detalhe.html')
        
    with open(pack_path, 'w', encoding='utf-8') as f:
        f.write(content)

# 3. Update styles.css for card grids
styles_path = 'styles.css'
if os.path.exists(styles_path):
    with open(styles_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    old_card_bg = '''.product .relative {
  position: relative;
  overflow: hidden;
  min-height: 260px;
  background-color: #f7f4f0;
}'''

    new_card_bg = """.product .relative {
  position: relative;
  overflow: hidden;
  min-height: 260px;
  background-color: transparent;
}"""

    if old_card_bg in content:
        content = content.replace(old_card_bg, new_card_bg)
        print('Updated card relative background in styles.css')
    else:
        # Simple replace
        content = content.replace('background-color: #f7f4f0;', 'background-color: transparent;')
        print('Applied fallback replacement for card background in styles.css')
        
    with open(styles_path, 'w', encoding='utf-8') as f:
        f.write(content)

print('All border and background adjustments completed successfully!')
