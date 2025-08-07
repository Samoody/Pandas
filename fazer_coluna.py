import pandas as pd

# Caminho do arquivo de entrada
file_path = "06-08 - BASE V8.xlsx"

# Carregar a base principal
df_base = pd.read_excel(file_path)

# Lista de clientes a adicionar
clientes_para_adicionar = [
    "SD CRED", "VIVA", "J&E", "UNICRED", "JDFE", "CSMAIS",
    "ALCRED", "CONQUISTA", "CLASS CREDI", "Libera Já", "Creditus", "VMD", "ARAUJO"
]

# Criar um DataFrame com os clientes
df_clientes = pd.DataFrame({"CLIENTES": clientes_para_adicionar})

# Salvar em um novo arquivo com duas abas
output_path = "BASE_V8_COM_ABA_CLIENTES.xlsx"
with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
    df_base.to_excel(writer, index=False, sheet_name="Base")
    df_clientes.to_excel(writer, index=False, sheet_name="CLIENTES")
