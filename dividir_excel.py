import pandas as pd
import os

# Caminho até a pasta Downloads do usuário
pasta_downloads = os.path.expanduser("~/Downloads")
nome_arquivo = "base qi.xlsx"
caminho_arquivo = os.path.join(pasta_downloads, nome_arquivo)

# Verifica se o arquivo existe
if not os.path.exists(caminho_arquivo):
    print(f"❌ Arquivo não encontrado: {caminho_arquivo}")
    exit()

# Lê o arquivo Excel
print(f"📥 Lendo o arquivo: {nome_arquivo}")
df = pd.read_excel(caminho_arquivo)

# Número total de registros
total = len(df)
parte = total // 3

# Divide o DataFrame
parte1 = df.iloc[:parte]
parte2 = df.iloc[parte:parte*2]
parte3 = df.iloc[parte*2:]

# Caminhos de saída
saida1 = os.path.join(pasta_downloads, "base_qi_parte1.xlsx")
saida2 = os.path.join(pasta_downloads, "base_qi_parte2.xlsx")
saida3 = os.path.join(pasta_downloads, "base_qi_parte3.xlsx")

# Salva os arquivos
parte1.to_excel(saida1, index=False)
parte2.to_excel(saida2, index=False)
parte3.to_excel(saida3, index=False)

print("✅ Arquivos salvos na pasta Downloads:")
print(f"- {saida1}")
print(f"- {saida2}")
print(f"- {saida3}")
