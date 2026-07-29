import pandas as pd
import json

excel_file = '../Excel de produtos - Site.xlsx'
xls = pd.ExcelFile(excel_file)

# We want to check Folha1
df = pd.read_excel(xls, sheet_name='Folha1')

# List of keywords from the OCR
keywords = ['Trevor', 'Robson', 'Amazónia', 'Argo', 'Eros', 'Daytona', 'Orly', 'Alvin', 'George', 'Mónika', 'Megan', 'Robbie', 'Mistik', 'Philipe', 'Ozil',
            'Sirio', 'Fredy', 'Connor', 'Lion', 'Dover', 'Stick', 'Star',
            'Charly', 'Moon', 'Paris', 'Sagres', 'Madrid', 'Milão', 'Chiado', 'Viena',
            'Malmo', 'Estrado', 'Jones']

found_rows = []

for index, row in df.iterrows():
    row_str = " ".join([str(x) for x in row.values if pd.notna(x)])
    matched = []
    for kw in keywords:
        if kw.lower() in row_str.lower():
            matched.append(kw)
    if matched:
        cells = [str(x) for x in row.values if pd.notna(x)]
        found_rows.append(f"Match {matched}: {cells[:3]}")

with open('excel_verification.txt', 'w') as f:
    for r in found_rows:
        f.write(r + '\n')

print(f"Found {len(found_rows)} matching rows in Excel.")
