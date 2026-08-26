NEW_HEADER = """<!-- Global Promo Banner -->
<div style="background-color:#EDF4F8;color:#1a1a1a;padding:8px 0;font-size:13px;font-weight:700;letter-spacing:0.15em;z-index:50;position:relative;border-bottom:1px solid #D4E4EE;overflow:hidden;white-space:nowrap;">
  <div class="animate-marquee" style="display:inline-block;white-space:nowrap;">
    <span style="margin:0 2.5rem;display:inline-block;">🚚 ENTREGA, MONTAGEM E RECOLHA GRÁTIS NUM RAIO DE 50KM (LISBOA E SETÚBAL)</span>
    <span style="margin:0 2.5rem;display:inline-block;">🚚 ENTREGA, MONTAGEM E RECOLHA GRÁTIS NUM RAIO DE 50KM (LISBOA E SETÚBAL)</span>
    <span style="margin:0 2.5rem;display:inline-block;">🛋️ 38 ANOS DE CONFIANÇA EM MOBILIÁRIO DE QUALIDADE</span>
    <span style="margin:0 2.5rem;display:inline-block;">🚚 ENTREGA, MONTAGEM E RECOLHA GRÁTIS NUM RAIO DE 50KM (LISBOA E SETÚBAL)</span>
    <span style="margin:0 2.5rem;display:inline-block;">🛋️ 38 ANOS DE CONFIANÇA EM MOBILIÁRIO DE QUALIDADE</span>
    <span style="margin:0 2.5rem;display:inline-block;">🚚 ENTREGA, MONTAGEM E RECOLHA GRÁTIS NUM RAIO DE 50KM (LISBOA E SETÚBAL)</span>
    <span style="margin:0 2.5rem;display:inline-block;">🛋️ 38 ANOS DE CONFIANÇA EM MOBILIÁRIO DE QUALIDADE</span>
    <span style="margin:0 2.5rem;display:inline-block;">🚚 ENTREGA, MONTAGEM E RECOLHA GRÁTIS NUM RAIO DE 50KM (LISBOA E SETÚBAL)</span>
  </div>
</div>

<!-- STICKY NAVBAR -->
<header class="sticky top-0 z-50 transition-all duration-300 shadow-sm" id="site-header" style="background-color:#F5F0E8;border-bottom:1px solid #E8E3DC;">
  <div class="container mx-auto px-4 lg:px-8">
    <div class="flex items-center justify-between relative" style="height:86px;">
      <!-- Logo -->
      <a class="flex-shrink-0 flex items-center" href="index.html" style="margin-left:4px;">
        <div style="width:76px;height:76px;border-radius:50%;background:#ffffff;border:1px solid #E8E3DC;display:flex;align-items:center;justify-content:center;overflow:hidden;flex-shrink:0;box-shadow:0 2px 8px rgba(0,0,0,0.04);">
          <img alt="Adil Móveis" src="images/logo_sem_fundo.png" style="width:82%;height:auto;object-fit:contain;"/>
        </div>
      </a>
      <!-- Desktop Menu (Centered) -->
      <nav class="hidden lg:flex flex-1 items-center justify-center gap-6 xl:gap-8 px-2" id="desktop-nav" style="z-index:10;">
        <a class="nav-link" data-page="index.html" href="index.html">INÍCIO</a>
        <a class="nav-link" data-page="quartos.html" href="quartos.html">QUARTOS</a>
        <a class="nav-link" data-page="salas.html" href="salas.html">SALAS</a>
        <a class="nav-link" data-page="colchoes.html" href="colchoes.html">COLCHÕES</a>
        <a class="nav-link" data-page="kids.html" href="kids.html">KIDS</a>
      </nav>
      <!-- Right Side -->
      <div class="flex items-center gap-4">
        <a class="hidden sm:inline-block" href="packs.html" onmouseout="this.style.background='#EBF2F7';this.style.transform='translateY(0)';" onmouseover="this.style.background='#D6E4F0';this.style.transform='translateY(-2px)';" style="font-size:9px;font-weight:800;text-transform:uppercase;letter-spacing:0.2em;color:#1E3A8A;background:#EBF2F7;border:2px solid #1E3A8A;padding:7px 20px;transition:all 0.3s;border-radius:30px;text-decoration:none;box-shadow:0 4px 15px rgba(30,58,138,0.1);">PACKS ESPECIAIS</a>
        <a class="hidden lg:inline-block" href="contactos.html" onmouseout="this.style.background='transparent';this.style.color='#1a1a1a';" onmouseover="this.style.background='#C8B598';this.style.color='#fff';" style="font-size:9px;font-weight:700;text-transform:uppercase;letter-spacing:0.2em;background:transparent;color:#1a1a1a;border:2px solid #C8B598;padding:7px 18px;transition:all 0.3s;border-radius:20px;text-decoration:none;">AGENDAR VISITA</a>
        <button onclick="openSearchModal()" style="background:transparent;border:none;cursor:pointer;color:#1a1a1a;padding:4px;margin-right:2px;" title="Pesquisar">
          <svg fill="none" height="20" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24" width="20"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
        </button>
        <button class="ml-1" id="menuButton" style="background:transparent;border:none;cursor:pointer;color:#1a1a1a;padding:4px;">
          <svg fill="none" height="22" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24" width="22"><line x1="3" x2="21" y1="12" y2="12"></line><line x1="3" x2="21" y1="6" y2="6"></line><line x1="3" x2="21" y1="18" y2="18"></line></svg>
        </button>
      </div>
    </div>
  </div>
  <!-- Mobile Menu Overlay -->
  <div class="fixed inset-0 z-50 hidden" id="menuOverlay" style="background:rgba(0,0,0,0.45);">
    <div class="absolute top-0 right-0 h-full flex flex-col" id="menuSidebar" style="width:320px;max-width:88vw;background:#FDFCFA;transform:translateX(100%);transition:transform 0.3s cubic-bezier(0.4,0,0.2,1);box-shadow:-4px 0 30px rgba(0,0,0,0.12);border-left:1px solid #E8E3DC;">
      <!-- Sidebar Header -->
      <div style="padding:1.5rem;border-bottom:1px solid #E8E3DC;display:flex;justify-content:space-between;align-items:center;">
        <span style="font-size:9px;font-weight:700;letter-spacing:0.25em;text-transform:uppercase;color:#6b6b6b;">MENU</span>
        <button id="closeMenuBtn" style="background:transparent;border:none;cursor:pointer;color:#1a1a1a;">
          <svg fill="none" height="22" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24" width="22" xmlns="http://www.w3.org/2000/svg"><line x1="18" x2="6" y1="6" y2="18"></line><line x1="6" x2="18" y1="6" y2="18"></line></svg>
        </button>
      </div>
      <!-- Links -->
      <div style="flex:1;overflow-y:auto;padding:2rem 1.5rem;">
        <p style="font-size:9px;font-weight:700;letter-spacing:0.2em;text-transform:uppercase;color:#C8B598;margin-bottom:1rem;">Loja</p>
        <nav style="display:flex;flex-direction:column;gap:1rem;margin-bottom:2rem;">
          <a href="quartos.html" style="font-size:1rem;font-weight:400;color:#1a1a1a;text-decoration:none;letter-spacing:0.02em;transition:color 0.2s;" onmouseover="this.style.color='#C8B598'" onmouseout="this.style.color='#1a1a1a'">Quartos</a>
          <a href="salas.html" style="font-size:1rem;font-weight:400;color:#1a1a1a;text-decoration:none;letter-spacing:0.02em;transition:color 0.2s;" onmouseover="this.style.color='#C8B598'" onmouseout="this.style.color='#1a1a1a'">Salas</a>
          <a href="colchoes.html" style="font-size:1rem;font-weight:400;color:#1a1a1a;text-decoration:none;letter-spacing:0.02em;transition:color 0.2s;" onmouseover="this.style.color='#C8B598'" onmouseout="this.style.color='#1a1a1a'">Colchões</a>
          <a href="kids.html" style="font-size:1rem;font-weight:400;color:#1a1a1a;text-decoration:none;letter-spacing:0.02em;transition:color 0.2s;" onmouseover="this.style.color='#C8B598'" onmouseout="this.style.color='#1a1a1a'">Kids</a>
          <a href="packs.html" style="font-size:1rem;font-weight:600;color:#1E3A8A;text-decoration:none;letter-spacing:0.02em;transition:color 0.2s;" onmouseover="this.style.color='#C8B598'" onmouseout="this.style.color='#1E3A8A'">✨ Packs Especiais</a>
          <a href="catalogos.html" style="font-size:1rem;font-weight:400;color:#1a1a1a;text-decoration:none;letter-spacing:0.02em;transition:color 0.2s;" onmouseover="this.style.color='#C8B598'" onmouseout="this.style.color='#1a1a1a'">Catálogos PDF</a>
        </nav>
        <p style="font-size:9px;font-weight:700;letter-spacing:0.2em;text-transform:uppercase;color:#C8B598;margin-bottom:1rem;">Institucional</p>
        <nav style="display:flex;flex-direction:column;gap:1rem;margin-bottom:2.5rem;">
          <a href="empresa.html" style="font-size:0.95rem;font-weight:400;color:#6b6b6b;text-decoration:none;transition:color 0.2s;" onmouseover="this.style.color='#1a1a1a'" onmouseout="this.style.color='#6b6b6b'">A Nossa História</a>
          <a href="contactos.html" style="font-size:0.95rem;font-weight:400;color:#6b6b6b;text-decoration:none;transition:color 0.2s;" onmouseover="this.style.color='#1a1a1a'" onmouseout="this.style.color='#6b6b6b'">Contactos & Lojas</a>
          <a href="servicos.html" style="font-size:0.95rem;font-weight:400;color:#6b6b6b;text-decoration:none;transition:color 0.2s;" onmouseover="this.style.color='#1a1a1a'" onmouseout="this.style.color='#6b6b6b'">Serviços & Montagem</a>
          <a href="faq.html" style="font-size:0.95rem;font-weight:400;color:#6b6b6b;text-decoration:none;transition:color 0.2s;" onmouseover="this.style.color='#1a1a1a'" onmouseout="this.style.color='#6b6b6b'">Perguntas Frequentes</a>
        </nav>
        <a href="contactos.html?agendar=true" style="display:block;text-align:center;background:#C8B598;color:#fff;font-size:10px;font-weight:700;letter-spacing:0.2em;text-transform:uppercase;padding:12px 20px;border-radius:2px;text-decoration:none;transition:background 0.2s;" onmouseover="this.style.background='#b09e85'" onmouseout="this.style.background='#C8B598'">Agendar Visita</a>
      </div>
    </div>
  </div>
</header>

<script>
  document.addEventListener('DOMContentLoaded', function() {
    var menuBtn = document.getElementById('menuButton');
    var closeBtn = document.getElementById('closeMenuBtn');
    var overlay  = document.getElementById('menuOverlay');
    var sidebar  = document.getElementById('menuSidebar');
    
    function openMenu() {
      if (overlay && sidebar) {
        overlay.classList.remove('hidden');
        document.body.style.overflow = 'hidden';
        setTimeout(function() { sidebar.style.transform = 'translateX(0)'; }, 10);
      }
    }
    function closeMenu() {
      if (sidebar && overlay) {
        sidebar.style.transform = 'translateX(100%)';
        setTimeout(function() { overlay.classList.add('hidden'); }, 310);
        document.body.style.overflow = '';
      }
    }
    
    if (menuBtn)  menuBtn.addEventListener('click', openMenu);
    if (closeBtn) closeBtn.addEventListener('click', closeMenu);
    if (overlay)  overlay.addEventListener('click', function(e) { if (e.target === overlay) closeMenu(); });
  });
</script>
"""
