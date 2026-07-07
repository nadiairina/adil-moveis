import os
import re
import glob

NEW_HEADER = """    <!-- Global Promo Banner -->
    <div style="background-color:#C8B598;color:#1a1a1a;padding:5px 0;font-size:9px;font-weight:700;letter-spacing:0.15em;z-index:50;position:relative;border-bottom:1px solid #b09e85;overflow:hidden;white-space:nowrap;">
      <div class="animate-marquee" style="display:inline-block;white-space:nowrap;">
        <span style="margin:0 2.5rem;display:inline-block;">🚚 ENTREGA, MONTAGEM E RECOLHA GRÁTIS NUM RAIO DE 50KM (LISBOA E SETÚBAL)</span>
        <span style="margin:0 2.5rem;display:inline-block;">🚚 ENTREGA, MONTAGEM E RECOLHA GRÁTIS NUM RAIO DE 50KM (LISBOA E SETÚBAL)</span>
        <span style="margin:0 2.5rem;display:inline-block;">🛋️ 37 ANOS DE CONFIANÇA EM MOBILIÁRIO DE QUALIDADE</span>
        <span style="margin:0 2.5rem;display:inline-block;">🚚 ENTREGA, MONTAGEM E RECOLHA GRÁTIS NUM RAIO DE 50KM (LISBOA E SETÚBAL)</span>
        <span style="margin:0 2.5rem;display:inline-block;">🛋️ 37 ANOS DE CONFIANÇA EM MOBILIÁRIO DE QUALIDADE</span>
        <span style="margin:0 2.5rem;display:inline-block;">🚚 ENTREGA, MONTAGEM E RECOLHA GRÁTIS NUM RAIO DE 50KM (LISBOA E SETÚBAL)</span>
        <span style="margin:0 2.5rem;display:inline-block;">🛋️ 37 ANOS DE CONFIANÇA EM MOBILIÁRIO DE QUALIDADE</span>
        <span style="margin:0 2.5rem;display:inline-block;">🚚 ENTREGA, MONTAGEM E RECOLHA GRÁTIS NUM RAIO DE 50KM (LISBOA E SETÚBAL)</span>
      </div>
    </div>
    <!-- STICKY NAVBAR -->
    <header class="sticky top-0 z-50 transition-all duration-300 shadow-sm" id="site-header" style="background-color:#F5F0E8;border-bottom:1px solid #E8E3DC;">
      <div class="container mx-auto px-4 lg:px-8">
        <div class="flex items-center justify-between relative" style="height:72px;">
          
          <!-- Logo -->
          <a href="index.html" class="flex-shrink-0 flex items-center" style="margin-left:4px;">
            <div style="width:52px;height:52px;border-radius:50%;background:#ffffff;border:1px solid #E8E3DC;display:flex;align-items:center;justify-content:center;overflow:hidden;flex-shrink:0;">
              <img src="images/logo.png" alt="Adil Móveis" style="width:85%;height:auto;object-fit:contain;mix-blend-mode:multiply;">
            </div>
          </a>
          
          <!-- Desktop Menu (Centered) -->
          <nav class="hidden lg:flex flex-1 items-center justify-center gap-6 xl:gap-8 px-2" id="desktop-nav" style="z-index:10;">
            <a href="index.html" class="nav-link" data-page="index.html">INÍCIO</a>
            <a href="quartos.html" class="nav-link" data-page="quartos.html">QUARTOS</a>
            <a href="salas.html" class="nav-link" data-page="salas.html">SALAS</a>
            <a href="colchoes.html" class="nav-link" data-page="colchoes.html">COLCHÕES</a>
            <a href="kids.html" class="nav-link" data-page="kids.html">KIDS</a>
          </nav>
          
          <!-- Right Side -->
          <div class="flex items-center gap-4">
            <a href="conjuntos.html" class="hidden xl:inline-block" style="font-size:9px;font-weight:700;text-transform:uppercase;letter-spacing:0.2em;color:#C8B598;border:1px solid #C8B598;padding:6px 16px;transition:all 0.3s;border-radius:2px;text-decoration:none;" onmouseover="this.style.background='#C8B598';this.style.color='white';" onmouseout="this.style.background='transparent';this.style.color='#C8B598';">PACKS</a>
            
            <a href="contactos.html" class="hidden lg:inline-block" style="font-size:9px;font-weight:700;text-transform:uppercase;letter-spacing:0.2em;color:#1a1a1a;border:1px solid #C8B598;background:#C8B598;padding:7px 18px;transition:all 0.3s;border-radius:20px;text-decoration:none;" onmouseover="this.style.background='#b09e85';this.style.borderColor='#b09e85';" onmouseout="this.style.background='#C8B598';this.style.borderColor='#C8B598';">AGENDAR VISITA</a>
            
            <button class="snipcart-checkout flex items-center justify-center border rounded-full text-black hover:border-black transition-colors relative" style="width:42px;height:32px;border-color:#E8E3DC;background:transparent;">
              <i data-feather="shopping-bag" style="width:16px;height:16px;"></i>
              <span class="snipcart-items-count" style="position:absolute;top:-5px;right:-5px;background:#1a1a1a;color:white;font-size:9px;width:17px;height:17px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;">0</span>
            </button>
            
            <button id="menuButton" style="background:transparent;border:none;cursor:pointer;color:#1a1a1a;padding:4px;" class="ml-1">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
            </button>
          </div>
          
        </div>
      </div>
      
      <!-- Mobile Menu Overlay -->
      <div id="menuOverlay" class="fixed inset-0 z-50 hidden" style="background:rgba(0,0,0,0.45);">
        <div id="menuSidebar" class="absolute top-0 right-0 h-full flex flex-col" style="width:320px;max-width:88vw;background:#FDFCFA;transform:translateX(100%);transition:transform 0.3s cubic-bezier(0.4,0,0.2,1);box-shadow:-4px 0 30px rgba(0,0,0,0.12);border-left:1px solid #E8E3DC;">
          <!-- Sidebar Header -->
          <div style="padding:1.5rem;border-bottom:1px solid #E8E3DC;display:flex;justify-content:space-between;align-items:center;">
            <span style="font-size:9px;font-weight:700;letter-spacing:0.25em;text-transform:uppercase;color:#6b6b6b;">MENU</span>
            <button id="closeMenuBtn" style="background:transparent;border:none;cursor:pointer;color:#1a1a1a;">
              <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
            </button>
          </div>
          
          <!-- Links -->
          <div style="flex:1;overflow-y:auto;padding:2rem 1.5rem;">
            <p style="font-size:9px;font-weight:700;letter-spacing:0.2em;text-transform:uppercase;color:#C8B598;margin-bottom:1rem;">Loja</p>
            <nav style="display:flex;flex-direction:column;gap:1rem;margin-bottom:2rem;">
              <a href="quartos.html" style="font-size:1rem;font-weight:400;color:#1a1a1a;text-decoration:none;letter-spacing:0.02em;transition:color 0.2s;" onmouseover="this.style.color='#C8B598'" onmouseout="this.style.color='#1a1a1a'">Quartos</a>
              <a href="salas.html" style="font-size:1rem;font-weight:400;color:#1a1a1a;text-decoration:none;letter-spacing:0.02em;transition:color 0.2s;" onmouseover="this.style.color='#C8B598'" onmouseout="this.style.color='#1a1a1a'">Salas</a>
              <a href="colchoes.html" style="font-size:1rem;font-weight:400;color:#1a1a1a;text-decoration:none;letter-spacing:0.02em;transition:color 0.2s;" onmouseover="this.style.color='#C8B598'" onmouseout="this.style.color='#1a1a1a'">Colchões</a>
              <a href="kids.html" style="font-size:1rem;font-weight:400;color:#1a1a1a;text-decoration:none;letter-spacing:0.02em;transition:color 0.2s;" onmouseover="this.style.color='#C8B598'" onmouseout="this.style.color='#1a1a1a'">Kids / Crianças</a>
              <a href="escritorio.html" style="font-size:1rem;font-weight:400;color:#1a1a1a;text-decoration:none;letter-spacing:0.02em;transition:color 0.2s;" onmouseover="this.style.color='#C8B598'" onmouseout="this.style.color='#1a1a1a'">Escritório</a>
              <a href="complementos.html" style="font-size:1rem;font-weight:400;color:#1a1a1a;text-decoration:none;letter-spacing:0.02em;transition:color 0.2s;" onmouseover="this.style.color='#C8B598'" onmouseout="this.style.color='#1a1a1a'">Complementos</a>
              <a href="conjuntos.html" style="font-size:1rem;font-weight:600;color:#C8B598;text-decoration:none;letter-spacing:0.02em;">✦ Packs Especiais</a>
              <a href="catalogos.html" style="font-size:0.85rem;font-weight:400;color:#6b6b6b;text-decoration:none;letter-spacing:0.02em;transition:color 0.2s;" onmouseover="this.style.color='#1a1a1a'" onmouseout="this.style.color='#6b6b6b'">Catálogos PDF</a>
            </nav>
            
            <p style="font-size:9px;font-weight:700;letter-spacing:0.2em;text-transform:uppercase;color:#C8B598;margin-bottom:1rem;padding-top:1.5rem;border-top:1px solid #E8E3DC;">Empresa & Apoio</p>
            <nav style="display:flex;flex-direction:column;gap:0.85rem;">
              <a href="empresa.html" style="font-size:0.85rem;color:#6b6b6b;text-decoration:none;transition:color 0.2s;" onmouseover="this.style.color='#1a1a1a'" onmouseout="this.style.color='#6b6b6b'">A Nossa História</a>
              <a href="testemunhos.html" style="font-size:0.85rem;color:#6b6b6b;text-decoration:none;transition:color 0.2s;" onmouseover="this.style.color='#1a1a1a'" onmouseout="this.style.color='#6b6b6b'">Testemunhos</a>
              <a href="tecidos.html" style="font-size:0.85rem;color:#6b6b6b;text-decoration:none;transition:color 0.2s;" onmouseover="this.style.color='#1a1a1a'" onmouseout="this.style.color='#6b6b6b'">Guia de Tecidos</a>
              <a href="faq.html" style="font-size:0.85rem;color:#6b6b6b;text-decoration:none;transition:color 0.2s;" onmouseover="this.style.color='#1a1a1a'" onmouseout="this.style.color='#6b6b6b'">Perguntas Frequentes</a>
              <a href="envios.html" style="font-size:0.85rem;color:#6b6b6b;text-decoration:none;transition:color 0.2s;" onmouseover="this.style.color='#1a1a1a'" onmouseout="this.style.color='#6b6b6b'">Envios e Devoluções</a>
              <a href="contactos.html" style="font-size:0.85rem;color:#6b6b6b;text-decoration:none;transition:color 0.2s;" onmouseover="this.style.color='#1a1a1a'" onmouseout="this.style.color='#6b6b6b'">Contactos & Lojas</a>
            </nav>
          </div>
          
          <!-- Sidebar Footer -->
          <div style="padding:1.5rem;background:#F5F0E8;border-top:1px solid #E8E3DC;">
            <a href="contactos.html" style="display:flex;align-items:center;justify-content:center;width:100%;padding:0.85rem;margin-bottom:0.75rem;background:#C8B598;color:#fff;font-size:10px;font-weight:700;letter-spacing:0.2em;text-transform:uppercase;text-decoration:none;transition:background 0.2s;" onmouseover="this.style.background='#b09e85'" onmouseout="this.style.background='#C8B598'">
              Agendar Visita à Loja
            </a>
            <a href="tel:212582788" style="display:flex;align-items:center;justify-content:center;gap:0.5rem;font-size:0.9rem;font-weight:700;color:#1a1a1a;text-decoration:none;margin-bottom:0.5rem;">
              📞 212 582 788
            </a>
            <a href="https://wa.me/351912582788" target="_blank" style="display:flex;align-items:center;justify-content:center;gap:0.5rem;font-size:0.8rem;color:#25d366;text-decoration:none;">
              💬 912 582 788
            </a>
          </div>
        </div>
      </div>
      
      <!-- Script for menu & active nav link -->
      <script>
        document.addEventListener('DOMContentLoaded', function() {
          // Active nav highlight
          var currentPage = window.location.pathname.split('/').pop() || 'index.html';
          var navLinks = document.querySelectorAll('#desktop-nav .nav-link');
          navLinks.forEach(function(link) {
            if (link.getAttribute('data-page') === currentPage) {
              link.style.color = '#1a1a1a';
              link.style.borderBottom = '1px solid #1a1a1a';
              link.style.paddingBottom = '2px';
            }
          });
          
          // Sidebar menu
          var menuBtn = document.getElementById('menuButton');
          var closeBtn = document.getElementById('closeMenuBtn');
          var overlay  = document.getElementById('menuOverlay');
          var sidebar  = document.getElementById('menuSidebar');
          
          function openMenu() {
            overlay.classList.remove('hidden');
            document.body.style.overflow = 'hidden';
            setTimeout(function() { sidebar.style.transform = 'translateX(0)'; }, 10);
          }
          function closeMenu() {
            sidebar.style.transform = 'translateX(100%)';
            setTimeout(function() { overlay.classList.add('hidden'); }, 310);
            document.body.style.overflow = '';
          }
          
          if (menuBtn)  menuBtn.addEventListener('click', openMenu);
          if (closeBtn) closeBtn.addEventListener('click', closeMenu);
          if (overlay)  overlay.addEventListener('click', function(e) { if (e.target === overlay) closeMenu(); });
        });
      </script>
    </header>"""

# Find all html files
html_files = glob.glob('*.html')

for filepath in html_files:
    if filepath in ['dashboard.html', 'dashboard-estrategias.html']:
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Try multiple possible start markers
    start_marks = ['<!-- Global Promo Banner -->', '<!-- Top Bar with Social Media', '<header']
    start_idx = -1
    for mark in start_marks:
        idx = content.find(mark)
        if idx != -1:
            start_idx = idx
            break

    if start_idx == -1:
        print(f'✗ No header start found in {filepath}')
        continue

    end_idx = content.find('</header>', start_idx)
    if end_idx == -1:
        print(f'✗ No </header> found in {filepath}')
        continue
    end_idx += len('</header>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content[:start_idx] + NEW_HEADER + content[end_idx:])
    print(f'✓ {filepath}')
