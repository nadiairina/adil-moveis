import os

favicon_tag = '<link rel="icon" type="image/png" href="images/logo.png">'

for file in os.listdir('.'):
    if file.endswith('.html'):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'rel="icon"' not in content:
            # Find the closing </head> or just append after <title>
            if '</head>' in content:
                content = content.replace('</head>', f'    {favicon_tag}\n  </head>')
                with open(file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Added favicon to {file}")
