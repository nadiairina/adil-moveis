import os
import re

directory = '/Users/nadiairina/Desktop/adil móveis/adil-moveis'
html_files = [f for f in os.listdir(directory) if f.endswith('.html')]

new_footer = """<footer class="bg-black text-white py-8" style="font-family:'Inter',sans-serif; border-top:1px solid #1a1a1a;">
  <div style="max-width:1200px; margin:0 auto; padding:0 1.5rem;">
    <!-- Main row: logo/contacts on left, clean horizontal menu on right -->
    <div style="display:flex; flex-direction:row; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:1.5rem; margin-bottom:1.5rem; padding-bottom:1.5rem; border-bottom:1px solid #222;">
      
      <!-- Left side: logo and contacts -->
      <div style="display:flex; align-items:center; gap:1rem;">
        <div style="width:48px; height:48px; border-radius:50%; background:#ffffff; display:flex; align-items:center; justify-content:center; overflow:hidden;">
          <img src="images/logo.png" alt="Adil Móveis" style="width:85%; height:auto; object-fit:contain; mix-blend-mode:multiply;">
        </div>
        <div>
          <p style="font-size:10px; font-weight:700; letter-spacing:0.2em; text-transform:uppercase; color:#C8B598; margin:0 0 2px 0;">Adil Móveis</p>
          <p style="font-size:10px; color:#666; margin:0;">Showroom no Feijó, Almada</p>
        </div>
      </div>
      
      <!-- Middle: Contacts -->
      <div style="display:flex; flex-wrap:wrap; gap:1.5rem; font-size:11px; color:#aaa;">
        <a href="tel:212582788" style="color:inherit; text-decoration:none; transition:color 0.2s;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#aaa'">📞 212 582 788</a>
        <a href="https://wa.me/351960209396" target="_blank" style="color:inherit; text-decoration:none; transition:color 0.2s;" onmouseover="this.style.color='#25D366'" onmouseout="this.style.color='#aaa'">💬 960 209 396</a>
        <a href="mailto:adil.moveis@hotmail.com" style="color:inherit; text-decoration:none; transition:color 0.2s;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#aaa'">✉️ adil.moveis@hotmail.com</a>
      </div>

      <!-- Right side: Socials -->
      <div style="display:flex; gap:1rem;">
        <a href="https://www.facebook.com/p/Adil-M%C3%B3veis-100063641348118/" target="_blank" style="color:#aaa; transition:color 0.2s;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#aaa'">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg>
        </a>
        <a href="https://www.instagram.com/adilmoveis/" target="_blank" style="color:#aaa; transition:color 0.2s;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#aaa'">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
        </a>
      </div>

    </div>

    <!-- Bottom row: horizontal navigation and copyright -->
    <div style="display:flex; flex-direction:row; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:1rem; font-size:11px; color:#666;">
      
      <!-- Horizontal links -->
      <div style="display:flex; flex-wrap:wrap; gap:1.5rem; font-weight:600; text-transform:uppercase; letter-spacing:0.1em;">
        <a href="index.html" style="color:#aaa; text-decoration:none; transition:color 0.2s;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#aaa'">Início</a>
        <a href="quartos.html" style="color:#aaa; text-decoration:none; transition:color 0.2s;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#aaa'">Quartos</a>
        <a href="colchoes.html" style="color:#aaa; text-decoration:none; transition:color 0.2s;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#aaa'">Colchões</a>
        <a href="salas.html" style="color:#aaa; text-decoration:none; transition:color 0.2s;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#aaa'">Salas</a>
        <a href="kids.html" style="color:#aaa; text-decoration:none; transition:color 0.2s;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#aaa'">Kids</a>
        <a href="contactos.html" style="color:#aaa; text-decoration:none; transition:color 0.2s;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#aaa'">Contactos</a>
      </div>
      
      <!-- Copyright -->
      <div style="text-align:right;">
        &copy; <span id="currentYear"></span><span id="footer-year"></span> Adil Móveis. Todos os direitos reservados.
        <span style="margin:0 6px;">·</span>
        Desenvolvido por <a href="https://nadiairina.github.io/Nadia-Portfolio/" target="_blank" style="color:#aaa; text-decoration:underline;">Nadia Irina</a>
      </div>

    </div>
  </div>
</footer>"""

for file in html_files:
    filepath = os.path.join(directory, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex search and replace footer
    content = re.sub(r'<footer[\s\S]*?</footer>', new_footer, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("All footers replaced with the ultra-slim fancy version.")
