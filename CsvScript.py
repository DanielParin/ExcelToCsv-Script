import pandas as pd

excel = "NameExcel.xlsx"
df = pd.read_excel(excel)


csv = "NameCsv.csv"
df.to_csv(csv, sep=';', index=False)