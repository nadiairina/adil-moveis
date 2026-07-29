import pandas as pd
import json

excel_file = '../Excel de produtos - Site.xlsx'
xls = pd.ExcelFile(excel_file)

# Load both sheets
df1 = pd.read_excel(xls, sheet_name='Folha1')
df2 = pd.read_excel(xls, sheet_name='Folha2')

# Create a mapping of keyword to description
# For Folha2 (Sofas and Cadeiroes), Column 1 is Name, Column 2 is Description
# We'll just iterate rows and assume first string is name, second is description
desc_map = {}

def extract_from_df(df):
    for index, row in df.iterrows():
        # Clean row values
        vals = [str(x).strip() for x in row.values if pd.notna(x) and str(x).strip() != '']
        if len(vals) >= 2:
            # Let's say the first val might be the name and second the description
            # This is naive but works for Folha2
            desc_map[vals[0].lower()] = vals[1]
            
            # Also add every word as a potential key just in case
            words = vals[0].split()
            for w in words:
                if len(w) > 3:
                    if w.lower() not in desc_map:
                        desc_map[w.lower()] = vals[1]

extract_from_df(df1)
extract_from_df(df2)

with open('products.js', 'r', encoding='utf-8') as f:
    content = f.read()

json_str = content.replace('const window_products = ', '').rstrip(';\n')
products = json.loads(json_str)

updated_count = 0
for pid, p in products.items():
    name_words = p['name'].split()
    for w in name_words:
        w_clean = w.lower().replace('sofá', '').replace('cadeira', '')
        if len(w_clean) > 3 and w_clean in desc_map:
            p['description'] = desc_map[w_clean]
            updated_count += 1
            break

with open('products.js', 'w', encoding='utf-8') as f:
    f.write("const window_products = ")
    json.dump(products, f, indent=2, ensure_ascii=False)
    f.write(";\n")

print(f"Updated {updated_count} descriptions in products.js")
