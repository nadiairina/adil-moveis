import os

# 1. Update pack-detalhe.html
with open('pack-detalhe.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Pack 1
old_p1_desc = 'description: "O <strong>Pack Sala de Sonho</strong> é a combinação perfeita de elegância e comodidade para renovar a sua sala de estar.<br><br><strong>O conjunto inclui:</strong><br>• <strong>Sofá Orly:</strong> 2300 x 950 x 950 mm com tecido personalizável.<br>• <strong>Base de TV Madrid:</strong> 1800 x 485 x 420 mm com 2 portas e 2 gavetas.<br><br><em>Fale connosco no WhatsApp para escolher os tecidos e acabamentos ideais para a sua casa!</em>"'
new_p1_desc = 'description: "A sua sala merece este upgrade de conforto e estilo! 🛋️✨<br><br>Imagine chegar a casa, relaxar no sofá perfeito e desfrutar de um ambiente acolhedor e moderno.<br><br>• <strong>Sofá à sua medida:</strong> Tecidos resistentes, cores sofisticadas e o conforto ideal para as noites de descanso e cinema em família.<br>• <strong>Mobiliário de Linhas Modernas:</strong> Base de TV Madrid perfeita para manter a sua sala organizada, elegante e luminosa.<br>• <strong>Personalização Total:</strong> Escolha os acabamentos de madeira e tecidos que combinam com o seu espaço.<br><br>💰 <strong>Preço especial de conjunto:</strong> Poupe mais ao levar o conjunto completo de sala!<br><br>👉 <em>Fale connosco no WhatsApp ou visite o nosso showroom no Feijó para sentir o conforto ao vivo!</em>"'

content = content.replace(old_p1_desc, new_p1_desc)

# Pack 2
old_p2_desc = 'description: "O <strong>Pack Sala de Sonho Premium</strong> eleva o requinte da sua sala de estar com acabamentos superiores e máxima arrumação.<br><br><strong>O conjunto inclui:</strong><br>• <strong>Sofá Luna Chaise:</strong> L2850 x A950 x P1650 mm em tecido personalizável de alta durabilidade.<br>• <strong>Base de TV Malmo:</strong> L1800 x A530 x P420 mm com portas e gavetas.<br>• <strong>Mesa de Centro Malmo:</strong> L1000 x A350 x P600 mm com tampo elevatório.<br><br><em>Fale connosco no WhatsApp para escolher o tecido do seu sofá e opções de cor das madeiras!</em>"'
new_p2_desc = 'description: "O luxo e a elegância que a sua casa sempre mereceu! 👑✨<br><br>Para quem não abre mão do máximo espaço, design refinado e conforto absoluto.<br><br>• <strong>Sofá Chaise Longue Generoso:</strong> Sofá Luna Chaise com espaço de sobra para toda a família, assentos profundos e apoio ergonómico.<br>• <strong>Conjunto Completo Malmo:</strong> Base de TV e Mesa de Centro a condizer, com acabamentos nobres e tampo funcional.<br>• <strong>Cores & Texturas Exclusivas:</strong> Escolha entre mais de 30 opções de tecidos e texturas premium à sua medida.<br><br>💰 <strong>Vantagem de Conjunto Premium:</strong> Solução completa de sala com condições exclusivas de lançamento.<br><br>👉 <em>Fale connosco no WhatsApp ou venha experimentar no nosso showroom no Feijó!</em>"'

content = content.replace(old_p2_desc, new_p2_desc)

# Pack 3
old_p3_desc = 'description: "O <strong>Pack Aconchego Essencial</strong> é o conjunto de quarto de casal completo pensado para o seu descanso total.<br><br><strong>O conjunto inclui:</strong><br>• <strong>Cama de Casal Madrid:</strong> L1610 x A1100 x P2090 mm (Opção com 4 gavetas e estrado incluído).<br>• <strong>Colchão Super Ortopédico:</strong> Suporte ergonómico de elevada densidade.<br>🎁 <strong>OFERTA EXCLUSIVA:</strong> 2 Almofadas Soft de presente!<br><br><em>Fale connosco no WhatsApp para personalizar o seu pack!</em>"'
new_p3_desc = 'description: "O quarto de casal perfeito, pronto a usar e sem complicações! 🛏️💤<br><br>Renove o seu quarto de uma só vez com tudo o que precisa para noites de sono reparador e máxima arrumação.<br><br>• <strong>Cama de Casal Madrid com Arrumação:</strong> Design intemporal com opção de 4 gavetões embutidos para rentabilizar o espaço.<br>• <strong>Colchão Super Ortopédico:</strong> Firmeza equilibrada para o alinhamento correto da coluna e descanso profundo.<br>• 🎁 <strong>OFERTA VIP:</strong> 2 Almofadas Soft de presente incluídas neste conjunto!<br><br>💰 <strong>Poupança Máxima:</strong> O conjunto completo pelo melhor valor, com entrega e montagem gratuitas num raio de 50km.<br><br>👉 <em>Personalize as cores e acabamentos do seu quarto na nossa loja no Feijó!</em>"'

content = content.replace(old_p3_desc, new_p3_desc)

# Pack 4
old_p4_desc = 'description: "O <strong>Pack À Mesa</strong> é a solução perfeita para reuniões de família e jantares confortáveis.<br><br><strong>O conjunto inclui:</strong><br>• <strong>Mesa de Jantar Extensível Paris:</strong> Fechada L1400 x A790 x P900 mm | Aberta L2300 x A790 x P900 mm (Disponível em 2 Cores: Carvalho Cinza - Branco e Carvalho Natura - Branco).<br>• <strong>4x Cadeiras Estofadas Paris:</strong> Pés e tecido totalmente personalizáveis.<br><br><em>Fale connosco no WhatsApp para escolher os tecidos das cadeiras e obter orçamento!</em>"'
new_p4_desc = 'description: "Reunir a família e os amigos nunca teve tanto estilo! 🍷🍽️<br><br>Da refeição rápida do dia a dia aos grandes jantares de festa, a sua sala de jantar pronta para todas as ocasiões.<br><br>• <strong>Mesa Extensível Paris:</strong> Fechada para poupar espaço no dia a dia, aberta (até 2,30m) para receber toda a gente confortavelmente.<br>• <strong>4 Cadeiras Estofadas de Elevado Conforto:</strong> Pés robustos e tecido macio e resistente para longas conversas à mesa.<br>• <strong>Acabamentos Personalizáveis:</strong> Cores de tampo e tecidos à escolha para combinar perfeitamente com a sua decoração.<br><br>💰 <strong>Conjunto Completo de Jantar:</strong> Leve a mesa e as 4 cadeiras com desconto especial de pack.<br><br>👉 <em>Venha escolher a sua combinação no nosso showroom no Feijó!</em>"'

content = content.replace(old_p4_desc, new_p4_desc)

with open('pack-detalhe.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated pack-detalhe.html with all pack descriptions!")

# 2. Update packs.html
with open('packs.html', 'r', encoding='utf-8') as f:
    p_content = f.read()

p_content = p_content.replace(
    'Sofá Orly de 3 Lugares + Base de TV Madrid.',
    'Poupe em Conjunto: Sofá Orly personalizável + Base de TV Madrid de linhas modernas.'
)
p_content = p_content.replace(
    'Sofá Luna Chaise Longue + Base de TV Malmo + Mesa de Centro Malmo.',
    'Solução VIP Completa: Sofá Luna Chaise generoso + Base de TV Malmo + Mesa de Centro.'
)
p_content = p_content.replace(
    'Cama de Casal Madrid com gavetas + Colchão Super Ortopédico + Oferta de 2 Almofadas Soft.',
    'Quarto Completo: Cama Madrid c/ arrumação + Colchão Super Ortopédico + Oferta 2 Almofadas.'
)
p_content = p_content.replace(
    'Mesa de Jantar Extensível Paris + 4 Cadeiras Estofadas Paris.',
    'Conjunto de Jantar: Mesa Extensível Paris (até 2,30m) + 4 Cadeiras Estofadas personalizáveis.'
)

with open('packs.html', 'w', encoding='utf-8') as f:
    f.write(p_content)
print("Updated packs.html!")

# 3. Update search.html
with open('search.html', 'r', encoding='utf-8') as f:
    s_content = f.read()

s_content = s_content.replace(
    'description: "Pack completo para sala de estar: sofá Orly e base de TV Madrid.",',
    'description: "Pack Sala de Sonho: Sofá Orly personalizável e base de TV Madrid de linhas modernas.",'
)
s_content = s_content.replace(
    'description: "Pack premium para sala: sofá Luna Chaise, base de TV Malmo e mesa de centro Malmo.",',
    'description: "Pack Sala de Sonho Premium: Sofá Luna Chaise, base de TV Malmo e mesa de centro com tampo funcional.",'
)
s_content = s_content.replace(
    'description: "Pack de quarto completo: cama de casal Madrid, colchão Super Ortopédico e 2 almofadas Soft de oferta.",',
    'description: "Pack Aconchego Essencial: Cama de casal Madrid com gavetões, colchão Super Ortopédico e 2 almofadas Soft de oferta.",'
)
s_content = s_content.replace(
    'description: "Pack sala de jantar: mesa extensível Paris e 4 cadeiras estofadas Paris.",',
    'description: "Pack À Mesa: Mesa de jantar extensível Paris e 4 cadeiras estofadas personalizáveis.",'
)

with open('search.html', 'w', encoding='utf-8') as f:
    f.write(s_content)
print("Updated search.html!")
