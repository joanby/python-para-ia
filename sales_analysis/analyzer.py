import os
import json
import pandas as pd

print("Directorio actual: ", os.getcwd())

data_path = "sales_analysis/data/sales.csv"

df = pd.read_csv(data_path)
print(df)
print(f"Tamaño: {df.shape[0]} filas, {df.shape[1]} columnas")

os.makedirs("output", exist_ok=True)

df.to_json("output/sales_data.json", orient="records", indent=2)
df.to_excel("output/sales_data.xlsx", index = False)
df.to_csv("output/sales_data.csv", index = False)

df = pd.read_csv("output/sales_data.csv")
df = pd.read_json("output/sales_data.json")
with open("output/sales_data.json") as f:
    data = json.load(f)
data
df = pd.read_excel("output/sales_data.xlsx")

with open("output/file.txt", 'r') as f:
    text = f.read()
text


import pandas as pd
from sales_analysis.helper import calculate_total, format_currency

df = pd.read_csv(data_path)

totals = []
for index, row in df.iterrows():
    total = calculate_total(row['quantity'], row['price'])
    totals.append(total)

df['total'] = totals

print("Datos de las ventas:")
for index, row in df.iterrows():
    formatted_total = format_currency(row['total'])
    print(f"{row['product']}: {formatted_total}")

grand_total = df['total'].sum()
formatted_grand_total = format_currency(grand_total)
print(f"El total de la factura asciende a {formatted_grand_total}")