from bs4 import BeautifulSoup

with open('colchoes.html', 'r') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

grid = soup.find('div', class_=lambda x: x and 'grid' in x and 'gap-8' in x)
if grid:
    grid.clear()
    
    colchoes = [
        {"name": "Evolution", "image": "images/sem-imagem.svg", "phrase": "A evolução do seu descanso."},
        {"name": "Freshcool", "image": "images/sem-imagem.svg", "phrase": "Frescura e conforto extremo."},
        {"name": "Max Body", "image": "images/sem-imagem.svg", "phrase": "Suporte total para o seu corpo."},
        {"name": "Airflow", "image": "images/sem-imagem.svg", "phrase": "Respiração avançada e noite tranquila."}
    ]
    
    for c in colchoes:
        html = f"""
        <div class="bg-white rounded overflow-hidden border border-[#E8E3DC] hover:shadow-lg transition-shadow relative text-center" data-aos="fade-up">
            <div class="relative w-full" style="aspect-ratio: 16/9; overflow:hidden; background:#F7F4F0;">
                <img src="{c['image']}" alt="Colchão" class="absolute inset-0 w-full h-full object-cover transition-transform duration-500 hover:scale-105" />
            </div>
            <div class="p-6" style="background:#FDFCFA; border-top:1px solid #E8E3DC;">
                <p style="font-family:'Playfair Display',serif; font-size:22px; font-weight:600; font-style:italic; color:#c8b598; margin:0;">
                    "{c['name']}"
                </p>
                <p style="font-family:'Inter',sans-serif; font-size:14px; font-weight:400; color:#6b6b6b; margin-top:10px;">
                    Destaque Exclusivo
                </p>
            </div>
        </div>
        """
        grid.append(BeautifulSoup(html, 'html.parser'))
        
    with open('colchoes.html', 'w') as f:
        f.write(str(soup))
    print("Updated colchoes.html")
