import pandas as pd
import random

# Nome do seu arquivo
arquivo = "07-08 BASE V8.xlsx"

# Nome da aba
aba = "Disponíveis > 0,01"

# Lista de nomes para preencher
clientes = [
    "SD CRED", "VIVA", "J&E", "UNICRED", "JDFE", "CSMAIS", "ALCRED",
    "CONQUISTA", "CLASS CREDI", "Libera Já", "Creditus", "VMD", "ARAUJO"
]

# Carrega a planilha
df = pd.read_excel(arquivo, sheet_name=aba)

# Preenche a coluna CLIENTE com nomes aleatórios
df["CLIENTE"] = [random.choice(clientes) for _ in range(len(df))]

# Salva o novo arquivo
df.to_excel("07-08 BASE V8 - CLIENTES PREENCHIDOS.xlsx", index=False)
