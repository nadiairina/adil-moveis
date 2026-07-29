import re

def main():
    try:
        with open('carreira.html', 'r', encoding='utf-8') as f:
            carreira_html = f.read()
            
        with open('dashboard.html', 'r', encoding='utf-8') as f:
            dashboard_html = f.read()

        # Extract checklist css from dashboard
        css_match = re.search(r'(\/\* ===== CHECKLISTS ===== \*\/.*?)(?=\/\* =====|\<\/style\>)', dashboard_html, re.DOTALL)
        checklist_css = css_match.group(1) if css_match else ""

        if checklist_css and "===== CHECKLISTS =====" not in carreira_html:
            carreira_html = carreira_html.replace('</style>', f'\n    {checklist_css.strip()}\n  </style>')
            
        tasks_html = """
      <!-- AS MINHAS TAREFAS -->
      <div class="card" style="margin-bottom: 1.5rem;">
        <div class="card-title">📋 As Minhas Tarefas (Marketing e Planeamento)</div>
        <div class="card-subtitle">Checklist de tarefas da Nádia para o arranque do E-commerce.</div>
        <div class="checklist">
          <div class="check-item">
            <span class="check-icon todo"></span>
            <div class="check-content">
              <span class="check-title">Publicar 1º Reel do Teaser (Redes Sociais)</span>
              <span class="check-desc">Gravar um vídeo curto de bastidores na loja física e publicar.</span>
            </div>
          </div>
          <div class="check-item">
            <span class="check-icon done">✓</span>
            <div class="check-content">
              <span class="check-title">Configurar MailerLite & Cupão VIP</span>
              <span class="check-desc">Criar conta e configurar envio automático do BEMVINDO10.</span>
            </div>
          </div>
          <div class="check-item">
            <span class="check-icon done">✓</span>
            <div class="check-content">
              <span class="check-title">Escrever Email de Boas-Vindas</span>
              <span class="check-desc">Acolhimento e entrega do código promocional.</span>
            </div>
          </div>
          <div class="check-item">
            <span class="check-icon todo"></span>
            <div class="check-content">
              <span class="check-title">Rastreio de Vendas Offline</span>
              <span class="check-desc">Incentivo para usar o desconto nas lojas físicas do Feijó.</span>
            </div>
          </div>
          <div class="check-item">
            <span class="check-icon todo"></span>
            <div class="check-content">
              <span class="check-title">Sistema "Marcar Visita" no Site</span>
              <span class="check-desc">Formulário de agendamento de consultoria de decoração/sono.</span>
            </div>
          </div>
          <div class="check-item">
            <span class="check-icon todo"></span>
            <div class="check-content">
              <span class="check-title">Newsletters Promocionais de Lançamento</span>
              <span class="check-desc">Preparar emails focados em fechar vendas (packs com desconto).</span>
            </div>
          </div>
        </div>
      </div>
"""
        
        if "AS MINHAS TAREFAS" not in carreira_html:
            carreira_html = carreira_html.replace('<!-- CRONOGRAMA DE TRANSIÇÃO -->', tasks_html + '      <!-- CRONOGRAMA DE TRANSIÇÃO -->')
            
        # Remove whatsapp button
        whatsapp_html_match = re.search(r'<!-- WhatsApp Floating Pill -->.*?</a>', carreira_html, re.DOTALL)
        if whatsapp_html_match:
            carreira_html = carreira_html.replace(whatsapp_html_match.group(0), '')
            
        with open('carreira.html', 'w', encoding='utf-8') as f:
            f.write(carreira_html)
            
        print("Updated carreira.html successfully!")
    except Exception as e:
        print("Error:", e)

main()
