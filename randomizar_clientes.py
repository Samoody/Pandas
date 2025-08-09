import pandas as pd
import random
import zipfile
import os

# ==== CONFIGURAÇÕES ====
# Nome do arquivo original
arquivo_entrada = "07-08 BASE V8 - CLIENTES PREENCHIDOS.xlsx"
# Nome do arquivo final Excel
arquivo_saida_excel = "07-08 BASE V8 - CLIENTES RANDOMIZADOS.xlsx"
# Nome do arquivo final ZIP
arquivo_saida_zip = "07-08 BASE V8 - CLIENTES RANDOMIZADOS.zip"

# Lista de clientes para remover
clientes_remover = ["VMD", "CLASS CREDI", "CSMAIS"]

# ==== PROCESSO ====
# Ler o arquivo Excel
df = pd.read_excel(arquivo_entrada)

# Obter lista de clientes restantes
clientes_restantes = [c for c in df["CLIENTE"].dropna().unique() if c not in clientes_remover]

# Randomizar clientes nos registros
df["CLIENTE"] = [random.choice(clientes_restantes) for _ in range(len(df))]

# Salvar Excel atualizado
df.to_excel(arquivo_saida_excel, index=False)

# Criar arquivo ZIP
with zipfile.ZipFile(arquivo_saida_zip, 'w', zipfile.ZIP_DEFLATED) as zf:
    zf.write(arquivo_saida_excel, arcname=os.path.basename(arquivo_saida_excel))

print(f"Arquivo gerado: {arquivo_saida_zip}")
