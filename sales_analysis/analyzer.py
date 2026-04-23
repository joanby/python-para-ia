import os

print("Directorio actual: ", os.getcwd())

data_path = "data/sales.csv"

if os.path.exists(data_path):
    print(f"✅ Encontrado {data_path}")
else:
    print(f"❌ No se ha encontrado {data_path}")
    print("Asegurate de que se está ejecutando todo en la carpeta de sales-analysis")