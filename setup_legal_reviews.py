import glob
import re

# 1. Create termos.html
termos_content = """<!DOCTYPE html>
<html lang="pt">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Termos e Condições | Adil Móveis</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://unpkg.com/feather-icons"></script>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css">
</head>
<body class="bg-[#FDFBF7] text-[#111111] font-['Inter'] antialiased pt-20">

  <!-- Header is injected via sidebar.js or we can just assume it has the global menu -->
  <div id="sidebar-container"></div>
  <script src="sidebar.js"></script>

  <main class="container mx-auto px-4 max-w-4xl py-16">
    <h1 class="text-4xl md:text-5xl font-light tracking-widest mb-12 uppercase text-center">Termos e Condições</h1>
    
    <div class="prose prose-lg mx-auto text-gray-700 space-y-8">
      <section>
        <h2 class="text-2xl font-semibold text-black mb-4">1. Âmbito e Objeto</h2>
        <p>As presentes Condições Gerais destinam-se a regular os termos e as condições por que se regerá a prestação do Serviço da Loja Online da Adil Móveis, gerida pela sociedade comercial Adil Lda, com sede na Rua Dr. António Elvas 28B, 2810-110 Almada.</p>
      </section>

      <section>
        <h2 class="text-2xl font-semibold text-black mb-4">2. Encomendas e Pagamentos</h2>
        <p>Ao realizar uma encomenda, o cliente aceita os preços e as descrições dos produtos disponíveis. Disponibilizamos pagamentos 100% seguros através de Referência Multibanco, MBWay e Cartões de Crédito (via Stripe/Snipcart).</p>
      </section>

      <section>
        <h2 class="text-2xl font-semibold text-black mb-4">3. Política de Devoluções e Reembolsos</h2>
        <p>Nos termos da legislação em vigor, o cliente dispõe de um prazo de 14 dias para resolver o contrato sem pagamento de indemnização e sem necessidade de indicar o motivo. <strong>Exceções:</strong> Produtos fabricados de acordo com especificações do consumidor ou manifestamente personalizados (ex: sofás com tecidos ou medidas escolhidas à medida) não são suscetíveis de devolução.</p>
        <p>Os custos de transporte de devoluções por arrependimento ficam a cargo do cliente. Em caso de defeito de fabrico, a Adil Móveis responsabiliza-se integralmente pela recolha e substituição.</p>
      </section>

      <section>
        <h2 class="text-2xl font-semibold text-black mb-4">4. Entregas e Montagem</h2>
        <p>As entregas e montagens são efetuadas gratuitamente para compras dentro do raio estipulado (ex: 50km). Para zonas fora deste raio, o custo de transporte será calculado no carrinho de compras ou sujeito a orçamento prévio.</p>
      </section>
    </div>
  </main>

  <footer class="bg-black py-8 mt-16">
    <div class="container mx-auto px-4 text-center text-sm text-gray-500">
      <p>&copy; 2026 Adil Móveis. Todos os direitos reservados.</p>
    </div>
  </footer>

  <script>feather.replace();</script>
</body>
</html>
"""

# 2. Create privacidade.html
privacidade_content = """<!DOCTYPE html>
<html lang="pt">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Política de Privacidade | Adil Móveis</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://unpkg.com/feather-icons"></script>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css">
</head>
<body class="bg-[#FDFBF7] text-[#111111] font-['Inter'] antialiased pt-20">

  <div id="sidebar-container"></div>
  <script src="sidebar.js"></script>

  <main class="container mx-auto px-4 max-w-4xl py-16">
    <h1 class="text-4xl md:text-5xl font-light tracking-widest mb-12 uppercase text-center">Política de Privacidade</h1>
    
    <div class="prose prose-lg mx-auto text-gray-700 space-y-8">
      <section>
        <h2 class="text-2xl font-semibold text-black mb-4">1. Proteção de Dados</h2>
        <p>A Adil Móveis garante a confidencialidade de todos os dados fornecidos pelos seus clientes. A recolha e tratamento de dados realiza-se de forma segura, o que impede a sua perda ou manipulação.</p>
      </section>

      <section>
        <h2 class="text-2xl font-semibold text-black mb-4">2. Utilização da Informação</h2>
        <p>Os dados recolhidos neste site destinam-se ao processamento das encomendas e comunicação com os Clientes, processamento de pedidos de informação e de eventuais reclamações, bem como a respetiva utilização para efeitos de marketing direto (apenas com o consentimento prévio do cliente).</p>
      </section>

      <section>
        <h2 class="text-2xl font-semibold text-black mb-4">3. Os seus direitos</h2>
        <p>Todos os Clientes têm o direito de acesso, retificação, cancelamento e oposição dos seus dados. Caso deseje, a qualquer momento, deixar de fazer parte da base de dados da Adil Móveis, poderá exercer esse direito através de contacto direto para o nosso email.</p>
      </section>
    </div>
  </main>

  <footer class="bg-black py-8 mt-16">
    <div class="container mx-auto px-4 text-center text-sm text-gray-500">
      <p>&copy; 2026 Adil Móveis. Todos os direitos reservados.</p>
    </div>
  </footer>

  <script>feather.replace();</script>
</body>
</html>
"""

with open("termos.html", "w", encoding="utf-8") as f:
    f.write(termos_content)
    
with open("privacidade.html", "w", encoding="utf-8") as f:
    f.write(privacidade_content)


# 3. Update testemunhos.html to use the real reviews
testemunhos_replacement = """
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <!-- Review 1 -->
        <div class="bg-white p-8 rounded-lg shadow-sm border border-[#EAE6DF] hover:shadow-md transition-shadow">
          <div class="flex text-[#C8B598] mb-4">
            <i data-feather="star" class="w-5 h-5 fill-current"></i><i data-feather="star" class="w-5 h-5 fill-current"></i><i data-feather="star" class="w-5 h-5 fill-current"></i><i data-feather="star" class="w-5 h-5 fill-current"></i><i data-feather="star" class="w-5 h-5 fill-current"></i>
          </div>
          <p class="text-gray-600 mb-6 italic">"Excelentes profissionais, de confiança e tudo de boa qualidade. Aos anos que sou cliente e recomendo!"</p>
          <div class="flex items-center">
            <div class="w-10 h-10 bg-gray-200 rounded-full flex items-center justify-center text-gray-600 font-bold mr-3">CB</div>
            <div>
              <p class="font-bold text-sm">Carla Belo</p>
              <p class="text-xs text-gray-500">Cliente via Google</p>
            </div>
          </div>
        </div>

        <!-- Review 2 -->
        <div class="bg-white p-8 rounded-lg shadow-sm border border-[#EAE6DF] hover:shadow-md transition-shadow">
          <div class="flex text-[#C8B598] mb-4">
            <i data-feather="star" class="w-5 h-5 fill-current"></i><i data-feather="star" class="w-5 h-5 fill-current"></i><i data-feather="star" class="w-5 h-5 fill-current"></i><i data-feather="star" class="w-5 h-5 fill-current"></i><i data-feather="star" class="w-5 h-5 fill-current"></i>
          </div>
          <p class="text-gray-600 mb-6 italic">"Fantástica variedade de produtos, sempre com uma atenção ao cliente muito acima da média, mantendo preços muito competitivos na relação qualidade/preço. Recomendo fortemente este estabelecimento. 👍"</p>
          <div class="flex items-center">
            <div class="w-10 h-10 bg-gray-200 rounded-full flex items-center justify-center text-gray-600 font-bold mr-3">PP</div>
            <div>
              <p class="font-bold text-sm">Paulo Pires</p>
              <p class="text-xs text-gray-500">Cliente via Google</p>
            </div>
          </div>
        </div>

        <!-- Review 3 -->
        <div class="bg-white p-8 rounded-lg shadow-sm border border-[#EAE6DF] hover:shadow-md transition-shadow">
          <div class="flex text-[#C8B598] mb-4">
            <i data-feather="star" class="w-5 h-5 fill-current"></i><i data-feather="star" class="w-5 h-5 fill-current"></i><i data-feather="star" class="w-5 h-5 fill-current"></i><i data-feather="star" class="w-5 h-5 fill-current"></i><i data-feather="star" class="w-5 h-5 fill-current"></i>
          </div>
          <p class="text-gray-600 mb-6 italic">"Já sou cliente há muitos anos. Recomendo esta loja, pessoal 5 estrelas."</p>
          <div class="flex items-center">
            <div class="w-10 h-10 bg-gray-200 rounded-full flex items-center justify-center text-gray-600 font-bold mr-3">ID</div>
            <div>
              <p class="font-bold text-sm">Ilda Dias</p>
              <p class="text-xs text-gray-500">Cliente via Google</p>
            </div>
          </div>
        </div>
        
        <!-- Review 4 -->
        <div class="bg-white p-8 rounded-lg shadow-sm border border-[#EAE6DF] hover:shadow-md transition-shadow">
          <div class="flex text-[#C8B598] mb-4">
            <i data-feather="star" class="w-5 h-5 fill-current"></i><i data-feather="star" class="w-5 h-5 fill-current"></i><i data-feather="star" class="w-5 h-5 fill-current"></i><i data-feather="star" class="w-5 h-5 fill-current"></i><i data-feather="star" class="w-5 h-5 text-gray-300"></i>
          </div>
          <p class="text-gray-600 mb-6 italic">"Móveis de excelente qualidade e preço acessível."</p>
          <div class="flex items-center">
            <div class="w-10 h-10 bg-gray-200 rounded-full flex items-center justify-center text-gray-600 font-bold mr-3">CO</div>
            <div>
              <p class="font-bold text-sm">Carlos Onofre</p>
              <p class="text-xs text-gray-500">Cliente via Google</p>
            </div>
          </div>
        </div>
        
        <!-- Review 5 -->
        <div class="bg-white p-8 rounded-lg shadow-sm border border-[#EAE6DF] hover:shadow-md transition-shadow">
          <div class="flex text-[#C8B598] mb-4">
            <i data-feather="star" class="w-5 h-5 fill-current"></i><i data-feather="star" class="w-5 h-5 fill-current"></i><i data-feather="star" class="w-5 h-5 fill-current"></i><i data-feather="star" class="w-5 h-5 fill-current"></i><i data-feather="star" class="w-5 h-5 fill-current"></i>
          </div>
          <p class="text-gray-600 mb-6 italic">"Muito bem atendido. Gostei."</p>
          <div class="flex items-center">
            <div class="w-10 h-10 bg-gray-200 rounded-full flex items-center justify-center text-gray-600 font-bold mr-3">MR</div>
            <div>
              <p class="font-bold text-sm">Mário Ramos</p>
              <p class="text-xs text-gray-500">Cliente via Google</p>
            </div>
          </div>
        </div>
      </div>
"""

# Let's read testemunhos.html and replace the grid
try:
    with open("testemunhos.html", "r", encoding="utf-8") as f:
        t_content = f.read()
        
    # Find the grid that holds reviews and replace it
    # We look for `<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">` and replace up to the end of the grid.
    # A simpler way is regex:
    import re
    t_content = re.sub(r'<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">.*?(?=</main>)', testemunhos_replacement + "\n    ", t_content, flags=re.DOTALL)
    
    with open("testemunhos.html", "w", encoding="utf-8") as f:
        f.write(t_content)
except Exception as e:
    print(f"Error updating testemunhos: {e}")

# 4. Update Footer in all HTML files to include links to Termos and Privacidade
# We will find the "Apoio" column in the footer
old_apoio_col = r'<li><a href="contactos\.html" class="hover:text-white transition-colors">Contactos</a></li>'
new_apoio_col = """<li><a href="contactos.html" class="hover:text-white transition-colors">Contactos</a></li>
              <li><a href="termos.html" class="hover:text-white transition-colors">Termos e Condições</a></li>
              <li><a href="privacidade.html" class="hover:text-white transition-colors">Política de Privacidade</a></li>"""

for filepath in glob.glob("*.html"):
    if filepath in ["dashboard.html"]:
        continue
    with open(filepath, "r", encoding="utf-8") as f:
        c = f.read()
    
    if "termos.html" not in c:
        c = re.sub(old_apoio_col, new_apoio_col, c)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(c)

print("Created legal pages, updated reviews, and added links to global footer.")
