import re

for filepath in ['pack-detalhe.html', 'produto-detalhe.html']:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove the JS setup for Add to Cart completely
    content = re.sub(r'// Add to cart setup.*?var btn = document\.getElementById\(\'addToCartBtn\'\);.*?btn\.dataset\.itemCustom2Options = p\.custom2_options;', '', content, flags=re.DOTALL)
    
    # Let's just blindly remove any line with addToCartBtn
    lines = content.split('\n')
    new_lines = [line for line in lines if 'addToCartBtn' not in line]
    content = '\n'.join(new_lines)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
