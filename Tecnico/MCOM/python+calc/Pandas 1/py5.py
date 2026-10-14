import pandas as pd
import numpy as np
# 1. Carregar o arquivo salvo em disco
df = pd.read_csv('relatorio_vendas.csv')
print("--- 1. Exibindo as primeiras 5 linhas (head) ---")
print(df.head(5))
print("\n--- 2. Exibindo as últimas 3 linhas (tail) ---")
print(df.tail(3))
print("\n--- 3. Informações Estruturais (info) ---")
df.info()
print("\n--- 4. Resumo Estatístico dos Dados (describe) ---")
print(df.describe())