with open('contactos.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Extract the map block
map_block = """<!-- Map Integration -->
              <div class="mt-8 rounded overflow-hidden border border-[#E8E3DC] shadow-sm">
                <iframe 
                  src="https://maps.google.com/maps?q=Rua%20Dr.%20Ant%C3%B3nio%20Elvas%2092,%202810-165%20Feij%C3%B3,%20Almada&t=&z=16&ie=UTF8&iwloc=&output=embed" 
                  width="100%" 
                  height="260" 
                  style="border:0;" 
                  allowfullscreen="" 
                  loading="lazy" 
                  referrerpolicy="no-referrer-when-downgrade">
                </iframe>
              </div>
              
              <a href="https://www.google.com/maps/search/?api=1&query=Adil+Móveis+Almada" target="_blank" rel="noopener" class="mt-4 inline-flex items-center gap-2 bg-[#C8B598] text-[#1a1a1a] px-6 py-3 rounded text-[10px] font-bold tracking-widest uppercase hover:bg-[#b09e85] transition-colors" style="text-decoration:none;">
                📍 Abrir no Google Maps
              </a>"""

# 2. Remove it from the left column
content = content.replace(map_block, "")

# 3. Insert it into the right column
right_col_buttons_end = """<span style="font-size:20px;">📅</span> AGENDAR VISITA À LOJA
                </a>
              </div>"""

new_right_col = right_col_buttons_end + "\n\n              <div class=\"mt-12 pt-8 border-t border-[#E8E3DC]\">\n" + map_block + "\n              </div>"

content = content.replace(right_col_buttons_end, new_right_col)

# 4. Remove the `justify-center h-full` from the right column container so it aligns to the top naturally
content = content.replace('class="flex flex-col justify-center h-full"', 'class="flex flex-col h-full"')

with open('contactos.html', 'w', encoding='utf-8') as f:
    f.write(content)

