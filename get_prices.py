import pandas as pd
import glob

excel_files = glob.glob('../*.xls*')
for f in excel_files:
    try:
        xls = pd.ExcelFile(f)
        for sheet in xls.sheet_names:
            df = pd.read_excel(xls, sheet_name=sheet)
            for index, row in df.iterrows():
                row_str = " | ".join([str(x) for x in row.values if pd.notna(x)])
                # Look for potential candidates
                if 'Estrado' in row_str or 'Colch' in row_str or 'Cadeira' in row_str:
                    print(f"File: {f.split('/')[-1]} | Sheet: {sheet} | Row: {row_str}")
    except Exception as e:
        pass
