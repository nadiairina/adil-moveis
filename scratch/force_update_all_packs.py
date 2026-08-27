import os

filepath = 'pack-detalhe.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Exact descriptions to place
p1_desc = """A sua sala merece este upgrade de conforto e estilo! 🛋️✨<br><br>Imagine chegar a casa, relaxar no sofá perfeito e desfrutar de um ambiente acolhedor e moderno.<br><br>• <strong>Sofá à sua medida:</strong> Tecidos antimancha, cores sofisticadas e o conforto ideal para as noites de cinema em família.<br>• <strong>Mobiliário de Linhas Modernas:</strong> A base de TV perfeita para manter a sua sala organizada, elegante e luminosa.<br>• <strong>Personalização Total:</strong> Escolha os acabamentos de madeira e tecidos que combinam com o seu espaço.<br><br>💰 <strong>Preço especial de conjunto:</strong> Poupe mais ao levar o conjunto completo de sala!<br><br>👉 <em>Visite o nosso showroom no Feijó e sinta o conforto ao vivo!</em>"""

p2_desc = """O luxo e a elegância que a sua casa sempre mereceu! 👑✨<br><br>Para quem não abre mão do máximo espaço, design refinado e conforto absoluto.<br><br>• <strong>Sofá Chaise Longue Generoso:</strong> Espaço de sobra para toda a família com assentos profundos e apoio ergonómico.<br>• <strong>Conjunto Completo Malmo:</strong> Base de TV e Mesa de Centro a condizer, com acabamentos em madeira nobre e linhas sofisticadas.<br>• <strong>Cores & Texturas Exclusivas:</strong> Escolha entre mais de 30 opções de tecidos e texturas premium.<br><br>💰 <strong>Vantagem de Conjunto Premium:</strong> Solução completa de sala com condições exclusivas de lançamento.<br><br>👉 <em>Fale connosco no WhatsApp ou venha experimentar no Feijó!</em>"""

p3_desc = """O quarto de casal perfeito, pronto a usar e sem complicações! 🛏️💤<br><br>Renove o seu quarto de uma só vez com tudo o que precisa para noites de sono reparador e máxima arrumação.<br><br>• <strong>Cama de Casal Madrid com Arrumação:</strong> Design intemporal com opção de 4 gavetões embutidos para rentabilizar o espaço.<br>• <strong>Colchão Super Ortopédico:</strong> Firmeza equilibrada para o alinhamento correto da coluna.<br>• 🎁 <strong>OFERTA VIP:</strong> 2 Almofadas Soft de oferta com este conjunto!<br><br>💰 <strong>Poupança Máxima:</strong> O conjunto completo pelo melhor valor do mercado, com entrega e montagem gratuitas (até 50km).<br><br>👉 <em>Personalize as cores do seu quarto na nossa loja no Feijó!</em>"""

p4_desc = """Reunir a família e os amigos nunca teve tanto estilo! 🍷🍽️<br><br>Da refeição rápida do dia a dia aos grandes jantares de festa, a sua sala de jantar pronta para todas as ocasiões.<br><br>• <strong>Mesa Extensível Paris:</strong> Fechada para poupar espaço no dia a dia, aberta para receber toda a gente confortavelmente.<br>• <strong>4 Cadeiras Estofadas de Elevado Conforto:</strong> Pés robustos e tecido macio e resistente para longas conversas à mesa.<br>• <strong>Acabamentos Personalizáveis:</strong> Cores de tampo e tecidos à escolha para combinar com a sua decoração.<br><br>💰 <strong>Conjunto Completo de Jantar:</strong> Leve a mesa e as 4 cadeiras com desconto especial de pack.<br><br>👉 <em>Venha escolher a sua combinação no nosso showroom!</em>"""

# Replace in pack-1
import re
content = re.sub(
    r'("pack-1":\s*\{[\s\S]*?description:\s*)"[\s\S]*?"',
    r'\1"' + p1_desc.replace('"', '\\"') + '"',
    content,
    count=1
)

# Replace in pack-2
content = re.sub(
    r'("pack-2":\s*\{[\s\S]*?description:\s*)"[\s\S]*?"',
    r'\1"' + p2_desc.replace('"', '\\"') + '"',
    content,
    count=1
)

# Replace in pack-3
content = re.sub(
    r'("pack-3":\s*\{[\s\S]*?description:\s*)"[\s\S]*?"',
    r'\1"' + p3_desc.replace('"', '\\"') + '"',
    content,
    count=1
)

# Replace in pack-4
content = re.sub(
    r'("pack-4":\s*\{[\s\S]*?description:\s*)"[\s\S]*?"',
    r'\1"' + p4_desc.replace('"', '\\"') + '"',
    content,
    count=1
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated pack-detalhe.html descriptions for Pack 1, 2, 3, 4!")
