import pandas as pd
import glob

excel_files = glob.glob('../*.xls*')
for f in excel_files:
    try:
        xls = pd.ExcelFile(f)
        for sheet in xls.sheet_names:
            df = pd.read_excel(xls, sheet_name=sheet)
            for index, row in df.iterrows():
                row_str = " ".join([str(x) for x in row.values if pd.notna(x)])
                if 'Trevor' in row_str or 'Robson' in row_str or 'Amazónia' in row_str:
                    print(f"Found in {f} - Sheet {sheet}: {row_str[:100]}")
    except Exception as e:
        print(f"Error reading {f}: {e}")
