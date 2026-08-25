
(function() {
  const urlParams = new URLSearchParams(window.location.search);
  if (urlParams.get('admin') === '1') {
    localStorage.setItem('admin', 'true');
  }

  if (localStorage.getItem('admin') !== 'true') {
    document.documentElement.style.display = 'none'; // hide immediately
    document.addEventListener('DOMContentLoaded', function() {
      document.documentElement.style.display = '';
      document.body.innerHTML = `
        <div style="display:flex; flex-direction:column; justify-content:center; align-items:center; height:100vh; background:#111; color:#fff; text-align:center; font-family:'Inter',sans-serif; padding:2rem;">
          <h1 style="font-size:3.5rem; font-weight:700; letter-spacing:0.1em; color:#C8B598; margin-bottom:1.5rem; font-family:'Playfair Display',serif; font-style:italic;">Adil Móveis</h1>
          <p style="font-size:1.2rem; font-weight:300; letter-spacing:0.05em; max-width:600px; line-height:1.6; color:#ccc;">
            Estamos de momento a preparar novidades incríveis e a melhorar o nosso catálogo online. 
            <br><br>
            Voltamos em breve!
          </p>
          <a href="https://wa.me/351960209396" target="_blank" style="margin-top:3rem; padding:1.2rem 2.5rem; background:#C8B598; color:#fff; text-decoration:none; border-radius:4px; font-weight:700; font-size:13px; letter-spacing:0.15em; text-transform:uppercase; transition:background 0.3s;" onmouseover="this.style.background='#b09e85'" onmouseout="this.style.background='#C8B598'">Falar connosco no WhatsApp</a>
        </div>
      `;
    });
  }
})();
