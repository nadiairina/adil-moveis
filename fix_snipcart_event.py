for filepath in ['pack-detalhe.html', 'produto-detalhe.html']:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    import re
    # Remove the whole snipcart.ready listener
    content = re.sub(r"// Listen to Snipcart added event.*?\}\);", "", content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
