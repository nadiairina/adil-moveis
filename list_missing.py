import json

with open('products.js', 'r', encoding='utf-8') as f:
    content = f.read()

json_str = content.replace('const window_products = ', '').rstrip(';\n')
products = json.loads(json_str)

missing = []
for pid, p in products.items():
    if 'sem-imagem' in p['image']:
        missing.append((p['name'], f"{pid}.jpg"))

for m in missing:
    print(f"- **{m[0]}**: Gravar como `{m[1]}`")
