import os

filepath = 'pack-detalhe.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Let's replace the layout block between <!-- Product Layout --> and <!-- Related Products -->
start_tag = '<!-- Product Layout -->'
end_tag = '<!-- ── Related Products ─────────────────────────────── -->'

start_idx = content.find(start_tag)
end_idx = content.find(end_tag)

if start_idx == -1 or end_idx == -1:
    print("Error: Could not find start or end tags!")
    exit(1)

new_layout = """<!-- Product Layout -->
        <div id="product-container" style="display:none;">
          
          <!-- TOP SECTION: Two-column layout (Image + Intro & Actions) -->
          <div class="flex flex-col lg:flex-row gap-12 lg:gap-16 items-start mb-12">
            
            <!-- LEFT COLUMN: Images (60%) -->
            <div class="w-full lg:w-[60%]">
              <div class="pdp-main-image-wrap" id="mainImageWrap" style="position:relative; padding-top:66.67%; border-radius:12px; overflow:hidden; background:#F7F4F0; box-shadow:0 4px 20px rgba(0,0,0,0.02);">
                <img id="mainImage" src="images/logo_sem_fundo.png" alt="Produto" style="position:absolute; top:0; left:0; width:100%; height:100%; object-fit:cover; object-position:center;">
                <!-- Discount Badge -->
                <div id="discount-badge-img" style="display:none;position:absolute;top:20px;left:20px;background:#C8B598;color:#fff;font-size:11px;font-weight:800;letter-spacing:0.15em;text-transform:uppercase;padding:6px 16px;border-radius:30px;z-index:2;box-shadow:0 4px 10px rgba(0,0,0,0.1);"></div>
              </div>
              
              <!-- Gallery Thumbnails -->
              <div id="gallery-container" style="display:flex;gap:12px;margin-top:20px;overflow-x:auto;padding-bottom:10px;"></div>
            </div>
            
            <!-- RIGHT COLUMN: Intro, Price & Main Buttons (40%) -->
            <div class="w-full lg:w-[40%]">
              <div style="background:#fff; border:1px solid #E8E3DC; border-radius:12px; padding:2.25rem; box-shadow:0 10px 40px rgba(0,0,0,0.03);">
                
                <!-- Category Label -->
                <p id="product-category-label" style="font-size:10px;font-weight:700;letter-spacing:0.3em;text-transform:uppercase;color:#C8B598;margin-bottom:0.75rem;">PACK ESPECIAL</p>
                
                <!-- Title -->
                <h1 id="dynamic-title" style="font-family:'Playfair Display',serif;font-size:clamp(1.6rem,3vw,2.4rem);font-weight:400;color:#1a1a1a;line-height:1.2;margin-bottom:1.25rem;">Produto</h1>
                
                <!-- Price -->
                <div id="price-block" style="margin-bottom:1.5rem;">
                  <div id="productPrice" style="font-family:'Inter',sans-serif;font-size:1.6rem;font-weight:500;color:#1a1a1a;"></div>
                  <div id="price-original-wrap" style="display:none;margin-top:4px;">
                    <span id="price-original" style="font-size:0.95rem;color:#6b6b6b;text-decoration:line-through;margin-right:8px;"></span>
                    <span id="discount-pct-badge" style="font-size:11px;font-weight:700;background:#C8B598;color:#fff;padding:2px 8px;border-radius:2px;"></span>
                  </div>
                </div>
                
                <!-- Short Intro Description -->
                <div style="margin-bottom:1.5rem; padding-bottom:1.5rem; border-bottom:1px solid #E8E3DC;">
                  <p id="dynamic-intro" style="font-size:0.95rem;color:#1a1a1a;line-height:1.7;font-weight:400;"></p>
                </div>
                
                <!-- Primary Actions -->
                <button id="addToCartBtn" class="snipcart-add-item" style="width:100%;background:#C8B598;color:#fff;border:none;padding:1rem 2rem;font-size:11px;font-weight:700;letter-spacing:0.2em;text-transform:uppercase;font-family:'Inter',sans-serif;cursor:pointer;border-radius:3px;display:flex;align-items:center;justify-content:center;gap:10px;transition:background 0.3s ease;margin-bottom:1rem;" onmouseover="this.style.background='#b09e85'" onmouseout="this.style.background='#C8B598'">
                  <i data-feather="shopping-bag" style="width:18px;height:18px;"></i>
                  <span>Adicionar ao Carrinho</span>
                </button>
                
                <a id="quoteWhatsAppBtn" href="#" target="_blank" style="display:none;width:100%;background:#25D366;color:#fff;border:none;padding:1rem 2rem;font-size:11px;font-weight:700;letter-spacing:0.2em;text-transform:uppercase;font-family:'Inter',sans-serif;cursor:pointer;border-radius:3px;display:flex;align-items:center;justify-content:center;gap:10px;transition:background 0.3s ease;margin-bottom:1rem;text-decoration:none;" onmouseover="this.style.background='#20ba5a'" onmouseout="this.style.background='#25D366'">
                  <i data-feather="message-circle" style="width:18px;height:18px;"></i>
                  <span>Pedir Orçamento via WhatsApp</span>
                </a>
                
                <!-- Helper Buttons -->
                <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:1.5rem;">
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
                <div style="display:grid;grid-template-columns:1fr;gap:8px;">
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
                </div>
                
              </div>
            </div>
            
          </div>
          
          <!-- BOTTOM SECTION: Two-column layout for Details/Specs & Included Items -->
          <div style="margin-top:3rem; padding-top:3rem; border-top:1px solid #E8E3DC;" class="flex flex-col lg:flex-row gap-12 lg:gap-16 items-start">
            
            <!-- BOTTOM LEFT: Detailed specifications & Fabric note (60% width) -->
            <div class="w-full lg:w-[60%] flex flex-col gap-8">
              
              <!-- Detailed specifications card -->
              <div style="background:#fff; border:1px solid #E8E3DC; border-radius:12px; padding:2.5rem; box-shadow:0 4px 20px rgba(0,0,0,0.01);">
                <p style="font-size:9px;font-weight:700;letter-spacing:0.25em;text-transform:uppercase;color:#C8B598;margin-bottom:0.75rem;">DETALHES DO CONJUNTO</p>
                <h3 style="font-family:'Playfair Display',serif;font-size:1.75rem;color:#1a1a1a;margin-bottom:1.5rem;">Vantagens e Especificações</h3>
                <div id="dynamic-details" style="font-size:1rem;color:#6b6b6b;line-height:1.8;font-weight:300;"></div>
              </div>
              
              <!-- Fabric Selection Note -->
              <div style="background:#fcf9f5; border:1px dashed #C8B598; padding:1.5rem; border-radius:12px; text-align:center;">
                <span style="font-size:20px; display:block; margin-bottom:0.5rem;">🎨</span>
                <strong style="color:#1a1a1a; font-size:12px; font-weight:800; letter-spacing:0.1em; text-transform:uppercase; display:block; margin-bottom:0.5rem;">Mais de 100 Tecidos e Cores Disponíveis!</strong>
                <p style="color:#6b6b6b; font-size:11.5px; line-height:1.6; margin:0; max-width:550px; margin-left:auto; margin-right:auto;">
                  Trabalhamos com catálogos premium (tecnologia anti-mancha, pet-friendly e repelentes de água). Como as cores variam nos ecrãs, convidamo-lo a <a href="contactos.html" style="color:#C8B598; text-decoration:underline; font-weight:bold;">visitar a nossa loja</a> ou a <a href="https://wa.me/351960209396" target="_blank" style="color:#25D366; text-decoration:underline; font-weight:bold;">contactar-nos via WhatsApp</a> para lhe enviarmos vídeos reais das amostras.
                </p>
              </div>
              
            </div>
            
            <!-- BOTTOM RIGHT: Included Items Grid & Scheduling (40% width) -->
            <div class="w-full lg:w-[40%] flex flex-col gap-6">
              
              <!-- Included items container -->
              <div style="background:#fff; border:1px solid #E8E3DC; border-radius:12px; padding:2rem; box-shadow:0 4px 20px rgba(0,0,0,0.01);">
                <p style="font-size:9px;font-weight:700;letter-spacing:0.25em;text-transform:uppercase;color:#C8B598;margin-bottom:0.5rem;">COMPOSIÇÃO DO CONJUNTO</p>
                <h3 style="font-family:'Playfair Display',serif;font-size:1.5rem;color:#1a1a1a;margin-bottom:1.25rem;">Peças Incluídas no Pack:</h3>
                <div id="pack-included-items" class="flex flex-col gap-4" style="margin-bottom:1.5rem;"></div>
              </div>
              
              <!-- Agendar Visita CTA -->
              <a href="contactos.html" style="display:flex;align-items:center;justify-content:center;gap:10px;width:100%;padding:1.1rem;background:#F5F0E8;border:1px solid #C8B598;color:#1a1a1a;font-size:10px;font-weight:700;letter-spacing:0.2em;text-transform:uppercase;text-decoration:none;border-radius:12px;transition:all 0.25s;box-shadow:0 4px 20px rgba(0,0,0,0.01);" onmouseover="this.style.background='#C8B598';this.style.color='#fff';" onmouseout="this.style.background='#F5F0E8';this.style.color:#1a1a1a;">
                <i data-feather="calendar" style="width:16px;height:16px;"></i>
                Agendar Visita à Loja · Adil Móveis Feijó
              </a>
              
            </div>
            
          </div>
          
        </div>
        """

# Replace the layout
content = content[:start_idx] + new_layout + content[end_idx:]

# Now let's update the Javascript code in pack-detalhe.html to split the description into intro and details.
# Let's find:
#         // Description
#         if (p.description || p.dimensions) {
#           var descHtml = p.description || '';
#           if (p.dimensions) {
#             descHtml += '<br><br><strong style="color:#1a1a1a;font-weight:600;">Dimensões:</strong> ' + p.dimensions;
#           }
#           document.getElementById('dynamic-desc').innerHTML = descHtml;
#         } else {
#           document.getElementById('dynamic-desc-container').style.display = 'none';
#         }

old_desc_logic = """        // Description
        if (p.description || p.dimensions) {
          var descHtml = p.description || '';
          if (p.dimensions) {
            descHtml += '<br><br><strong style="color:#1a1a1a;font-weight:600;">Dimensões:</strong> ' + p.dimensions;
          }
          document.getElementById('dynamic-desc').innerHTML = descHtml;
        } else {
          document.getElementById('dynamic-desc-container').style.display = 'none';
        }"""

new_desc_logic = """        // Split description into Short Intro (for top right) and Details (for bottom left)
        if (p.description) {
          var descHtml = p.description;
          var parts = descHtml.split('<br><br>');
          
          var introHtml = "";
          var detailsHtml = "";
          
          if (parts.length > 2) {
            // First two paragraphs go to the top-right introduction
            introHtml = parts.slice(0, 2).join('<br><br>');
            // Remaining bullet points/text go to the bottom details section
            detailsHtml = parts.slice(2).join('<br><br>');
          } else {
            introHtml = descHtml;
            detailsHtml = "Crie a combinação de mobiliário ideal para a sua casa. Várias opções de medidas, cores e estofos sob consulta diretamente no nosso showroom ou via WhatsApp.";
          }
          
          if (p.dimensions) {
            detailsHtml += '<br><br><strong style="color:#1a1a1a;font-weight:600;">Dimensões do Conjunto:</strong> ' + p.dimensions;
          }
          
          document.getElementById('dynamic-intro').innerHTML = introHtml;
          document.getElementById('dynamic-details').innerHTML = detailsHtml;
        } else {
          document.getElementById('dynamic-intro').innerHTML = "Disponível para personalização e orçamento sob consulta.";
          document.getElementById('dynamic-details').innerHTML = "Entre em contacto connosco para saber todas as especificações deste pack.";
        }"""

content = content.replace(old_desc_logic, new_desc_logic)

# Also update the card rendering inside #pack-included-items to fit the vertical list format!
old_card_renderer = """            return '<a href="' + targetUrl + '" style="background:#fff; border:1px solid #E8E3DC; border-radius:10px; overflow:hidden; transition:all 0.3s; cursor:pointer; text-decoration:none; color:inherit;" class="hover:shadow-md hover:border-[#C8B598] flex flex-col">' +
                   '  <div style="aspect-ratio:1/1; background:#F7F4F0; overflow:hidden; position:relative;">' +
                   '    <img src="' + itemImage + '" alt="' + item.name + '" style="position:absolute; inset:0; width:100%; height:100%; object-fit:contain; mix-blend-mode:darken; padding:8px; transition:transform 0.4s;" class="hover:scale-105" onerror="this.src=\\'images/logo_sem_fundo.png\\'" />' +
                   '  </div>' +
                   '  <div style="padding:12px 14px; text-align:center; border-top:1px solid #E8E3DC; background:#FDFCFA; margin-top:auto;">' +
                   '    <h4 style="font-family:\\'Inter\\',sans-serif; font-size:11px; font-weight:700; text-transform:uppercase; letter-spacing:0.04em; color:#1a1a1a; margin-bottom:4px; line-height:1.3;">' + item.name + '</h4>' +
                   '    <p style="font-size:10px; color:#6b6b6b; margin:0 0 8px 0; line-height:1.3; min-height:26px;">' + item.detail + '</p>' +
                   '    <span style="display:inline-block; font-size:9px; font-weight:700; text-transform:uppercase; letter-spacing:0.1em; color:#C8B598; border-bottom:1px solid transparent; transition:all 0.2s;">Ver Detalhe &rarr;</span>' +
                   '  </div>' +
                   '</a>';"""

new_card_renderer = """            return '<a href="' + targetUrl + '" style="display:flex; align-items:center; gap:16px; background:#fff; border:1px solid #E8E3DC; border-radius:8px; padding:12px; transition:all 0.3s; text-decoration:none; color:inherit;" class="hover:shadow-sm hover:border-[#C8B598]">' +
                   '  <div style="width:70px; height:70px; min-width:70px; background:#F7F4F0; border-radius:6px; overflow:hidden; position:relative; display:flex; align-items:center; justify-content:center;">' +
                   '    <img src="' + itemImage + '" alt="' + item.name + '" style="width:100%; height:100%; object-fit:contain; mix-blend-mode:darken; padding:4px;" onerror="this.src=\\'images/logo_sem_fundo.png\\'" />' +
                   '  </div>' +
                   '  <div style="flex-grow:1;">' +
                   '    <h4 style="font-family:\\'Inter\\',sans-serif; font-size:11px; font-weight:700; text-transform:uppercase; letter-spacing:0.04em; color:#1a1a1a; margin:0 0 2px 0; line-height:1.3;">' + item.name + '</h4>' +
                   '    <p style="font-size:10px; color:#6b6b6b; margin:0; line-height:1.3;">' + item.detail + '</p>' +
                   '  </div>' +
                   '  <span style="font-size:14px; color:#C8B598; font-weight:700; margin-left:auto; padding-left:8px;">&rarr;</span>' +
                   '</a>';"""

content = content.replace(old_card_renderer, new_card_renderer)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Successfully split PDP text and items into hybrid layout!")
