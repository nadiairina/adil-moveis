import os

filepath = 'pack-detalhe.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Let's locate the exact block between <!-- Product Layout --> and <!-- Related Products -->
start_tag = '<!-- Product Layout -->'
end_tag = '<!-- ── Related Products ─────────────────────────────── -->'

start_idx = content.find(start_tag)
end_idx = content.find(end_tag)

if start_idx == -1 or end_idx == -1:
    print("Error: Could not find start or end tags in HTML!")
    exit(1)

# Let's build the new, elegant two-column layout
new_layout = """<!-- Product Layout -->
        <div id="product-container" style="display:none;">
          
          <!-- Two-Column Hero Row -->
          <div class="flex flex-col lg:flex-row gap-12 lg:gap-16 items-start mb-16">
            
            <!-- LEFT COLUMN: Images (60% on desktop) -->
            <div class="w-full lg:w-[60%]">
              <!-- Main Image Wrap -->
              <div class="pdp-main-image-wrap" id="mainImageWrap" style="position:relative; padding-top:66.67%; border-radius:12px; overflow:hidden; background:#F7F4F0; box-shadow:0 4px 20px rgba(0,0,0,0.02);">
                <img id="mainImage" src="images/logo_sem_fundo.png" alt="Produto" style="position:absolute; top:0; left:0; width:100%; height:100%; object-fit:cover; object-position:center;">
                <!-- Discount Badge -->
                <div id="discount-badge-img" style="display:none;position:absolute;top:20px;left:20px;background:#C8B598;color:#fff;font-size:11px;font-weight:800;letter-spacing:0.15em;text-transform:uppercase;padding:6px 16px;border-radius:30px;z-index:2;box-shadow:0 4px 10px rgba(0,0,0,0.1);"></div>
              </div>
              
              <!-- Gallery Thumbnails -->
              <div id="gallery-container" style="display:flex;gap:12px;margin-top:20px;overflow-x:auto;padding-bottom:10px;"></div>
            </div>
            
            <!-- RIGHT COLUMN: Product Info & Actions (40% on desktop) -->
            <div class="w-full lg:w-[40%]">
              <div style="background:#fff; border:1px solid #E8E3DC; border-radius:12px; padding:2.5rem; box-shadow:0 10px 40px rgba(0,0,0,0.03);">
                
                <!-- Category Label -->
                <p id="product-category-label" style="font-size:10px;font-weight:700;letter-spacing:0.3em;text-transform:uppercase;color:#C8B598;margin-bottom:0.75rem;">PACK ESPECIAL</p>
                
                <!-- Product/Pack Name -->
                <h1 id="dynamic-title" style="font-family:'Playfair Display',serif;font-size:clamp(1.6rem,3vw,2.4rem);font-weight:400;color:#1a1a1a;line-height:1.2;margin-bottom:1.25rem;">Produto</h1>
                
                <!-- Price block -->
                <div id="price-block" style="margin-bottom:1.75rem;">
                  <div id="productPrice" style="font-family:'Inter',sans-serif;font-size:1.6rem;font-weight:500;color:#1a1a1a;"></div>
                  <div id="price-original-wrap" style="display:none;margin-top:4px;">
                    <span id="price-original" style="font-size:0.95rem;color:#6b6b6b;text-decoration:line-through;margin-right:8px;"></span>
                    <span id="discount-pct-badge" style="font-size:11px;font-weight:700;background:#C8B598;color:#fff;padding:2px 8px;border-radius:2px;"></span>
                  </div>
                </div>
                
                <!-- Description (moved to right side for balanced top section) -->
                <div id="dynamic-desc-container" style="margin-bottom:2rem;padding-bottom:2rem;border-bottom:1px solid #E8E3DC;">
                  <p id="dynamic-desc" style="font-size:1rem;color:#6b6b6b;line-height:1.8;font-weight:300;"></p>
                </div>
                
                <!-- Custom Option 1 -->
                <div id="custom1-container" style="display:none;margin-bottom:1.5rem;">
                  <h3 id="custom1-title" style="font-size:10px;font-weight:700;letter-spacing:0.2em;text-transform:uppercase;color:#1a1a1a;margin-bottom:0.75rem;">Opção 1</h3>
                  <div id="custom1-options" style="display:flex;flex-wrap:wrap;gap:8px;"></div>
                </div>
                
                <!-- Custom Option 2 -->
                <div id="custom2-container" style="display:none;margin-bottom:1.5rem;">
                  <h3 style="font-size:10px;font-weight:700;letter-spacing:0.2em;text-transform:uppercase;color:#1a1a1a;margin-bottom:0.75rem;display:flex;justify-content:space-between;align-items:center;">
                    <span id="custom2-title">Opção 2</span>
                  </h3>
                  <div id="custom2-options" style="display:flex;flex-wrap:wrap;gap:8px;"></div>
                </div>
                
                <!-- Add to Cart (Snipcart) -->
                <button id="addToCartBtn" class="snipcart-add-item" style="width:100%;background:#C8B598;color:#fff;border:none;padding:1rem 2rem;font-size:11px;font-weight:700;letter-spacing:0.2em;text-transform:uppercase;font-family:'Inter',sans-serif;cursor:pointer;border-radius:3px;display:flex;align-items:center;justify-content:center;gap:10px;transition:background 0.3s ease;margin-bottom:1rem;" onmouseover="this.style.background='#b09e85'" onmouseout="this.style.background='#C8B598'">
                  <i data-feather="shopping-bag" style="width:18px;height:18px;"></i>
                  <span>Adicionar ao Carrinho</span>
                </button>
                
                <!-- WhatsApp Quote Button -->
                <a id="quoteWhatsAppBtn" href="#" target="_blank" style="display:none;width:100%;background:#25D366;color:#fff;border:none;padding:1rem 2rem;font-size:11px;font-weight:700;letter-spacing:0.2em;text-transform:uppercase;font-family:'Inter',sans-serif;cursor:pointer;border-radius:3px;display:flex;align-items:center;justify-content:center;gap:10px;transition:background 0.3s ease;margin-bottom:1rem;text-decoration:none;" onmouseover="this.style.background='#20ba5a'" onmouseout="this.style.background='#25D366'">
                  <i data-feather="message-circle" style="width:18px;height:18px;"></i>
                  <span>Pedir Orçamento via WhatsApp</span>
                </a>
                
                <!-- Helper Buttons -->
                <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:1.75rem;">
                  <a href="contactos.html" style="display:flex;align-items:center;justify-content:center;gap:8px;padding:0.85rem;border:1px solid #C8B598;color:#C8B598;font-size:10px;font-weight:700;letter-spacing:0.15em;text-transform:uppercase;text-decoration:none;border-radius:3px;transition:all 0.2s;" onmouseover="this.style.background='#C8B598';this.style.color='#fff';" onmouseout="this.style.background='transparent';this.style.color='#C8B598';">
                    <i data-feather="map-pin" style="width:15px;height:15px;"></i>
                    Ver na Loja
                  </a>
                  <a href="https://wa.me/351960209396" target="_blank" style="display:flex;align-items:center;justify-content:center;gap:8px;padding:0.85rem;border:1px solid #E8E3DC;color:#6b6b6b;font-size:10px;font-weight:700;letter-spacing:0.15em;text-transform:uppercase;text-decoration:none;border-radius:3px;transition:all 0.2s;" onmouseover="this.style.background='#25D366';this.style.color='#fff';this.style.borderColor='#25D366';" onmouseout="this.style.background='transparent';this.style.color='#6b6b6b';this.style.borderColor='#E8E3DC';">
                    <i data-feather="message-circle" style="width:15px;height:15px;"></i>
                    Dúvidas?
                  </a>
                </div>
                
                <!-- Trust Badges -->
                <div style="display:grid;grid-template-columns:1fr;gap:8px;margin-bottom:1.5rem;">
                  <div class="trust-badge">
                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="1" y="3" width="15" height="13"></rect><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"></polygon><circle cx="5.5" cy="18.5" r="2.5"></circle><circle cx="18.5" cy="18.5" r="2.5"></circle></svg>
                    <span>Entrega Grátis · 50km Lisboa & Setúbal</span>
                  </div>
                  <div class="trust-badge">
                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path></svg>
                    <span>Montagem Profissional Incluída</span>
                  </div>
                  <div class="trust-badge">
                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
                    <span>Garantia 3 Anos</span>
                  </div>
                  <div class="trust-badge">
                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="1 4 1 10 7 10"></polyline><path d="M3.51 15a9 9 0 1 0 .49-3.5"></path></svg>
                    <span>Recolha de Móveis Usados Grátis</span>
                  </div>
                </div>
                
                <!-- Nota sobre Tecidos -->
                <div style="background:#fcf9f5; border:1px dashed #C8B598; padding:1.25rem; border-radius:3px; margin-bottom:1.5rem; text-align:center;">
                  <span style="font-size:16px; display:block; margin-bottom:0.5rem;">🎨</span>
                  <strong style="color:#1a1a1a; font-size:12px; font-weight:800; letter-spacing:0.1em; text-transform:uppercase; display:block; margin-bottom:0.5rem;">Mais de 100 Tecidos Disponíveis!</strong>
                  <p style="color:#6b6b6b; font-size:11px; line-height:1.5; margin:0;">
                    Trabalhamos com catálogos premium (tecnologia anti-mancha, pet-friendly e repelentes de água). Como as cores variam nos ecrãs, convidamo-lo a <a href="contactos.html" style="color:#C8B598; text-decoration:underline; font-weight:bold;">visitar a nossa loja</a> ou a <a href="https://wa.me/351960209396" target="_blank" style="color:#25D366; text-decoration:underline; font-weight:bold;">contactar-nos via WhatsApp</a> para lhe enviarmos vídeos reais das amostras.
                  </p>
                </div>
                
                <!-- Agendar Visita CTA -->
                <a href="contactos.html" style="display:flex;align-items:center;justify-content:center;gap:10px;width:100%;padding:1rem;background:#F5F0E8;border:1px solid #C8B598;color:#1a1a1a;font-size:10px;font-weight:700;letter-spacing:0.2em;text-transform:uppercase;text-decoration:none;border-radius:3px;transition:all 0.25s;" onmouseover="this.style.background='#C8B598';this.style.color='#fff';" onmouseout="this.style.background='#F5F0E8';this.style.color:#1a1a1a;">
                  <i data-feather="calendar" style="width:16px;height:16px;"></i>
                  Agendar Visita à Loja · Adil Móveis Feijó
                </a>
                
              </div>
            </div>
            
          </div>
          
          <!-- BOTTOM: Full-Width Included Items -->
          <div style="margin-top:4rem; padding-top:4rem; border-top:1px solid #E8E3DC;">
            <p style="font-size:9px;font-weight:700;letter-spacing:0.25em;text-transform:uppercase;color:#C8B598;margin-bottom:0.5rem;">COMPOSIÇÃO DO CONJUNTO</p>
            <h3 style="font-family:'Playfair Display',serif;font-size:1.75rem;color:#1a1a1a;margin-bottom:1.5rem;">Peças Incluídas no Pack:</h3>
            <div id="pack-included-items" class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6" style="margin-bottom:1.5rem;"></div>
          </div>
          
        </div>
        """

# Replace the layout in pack-detalhe.html
content = content[:start_idx] + new_layout + content[end_idx:]

# Let's also simplify the JavaScript selector in lines 790-805
# Since we removed dynamic-title-top and dynamic-title-side, we only have dynamic-title.
content = content.replace("var tTop = document.getElementById('dynamic-title-top'); if (tTop) tTop.textContent = p.name;\n        var tSide = document.getElementById('dynamic-title-side'); if (tSide) tSide.textContent = p.name;", "")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Successfully restructured pack-detalhe.html to two-column design!")
