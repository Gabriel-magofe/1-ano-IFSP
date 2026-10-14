import pandas as pd
import numpy as np
# Definindo uma semente aleatória para reproduzibilidade
np.random.seed(42)
# Gerando dados fictícios com NumPy
datas = pd.date_range(start='2026-01-01', periods=30, freq='D')
vendas = np.random.randint(100, 500, size=30)
visitas = vendas * np.random.uniform(1.5, 3.0, size=30)
# Criando o DataFrame
df_gerado = pd.DataFrame({
'Data': datas,
'Vendas_R$': vendas,
'Visitas_Site': np.round(visitas, 0)
})
# Salvando o arquivo CSV em disco
df_gerado.to_csv('relatorio_vendas.csv', index=False, encoding='utf-8')
print("Arquivo 'relatorio_vendas.csv' gerado com sucesso!")