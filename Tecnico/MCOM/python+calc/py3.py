import pandas as pd
# Criando um DataFrame a partir de um dicionário
dados = {
'Nome': ['Ana', 'Bruno', 'Carla', 'Diego'],
'Idade': [25, 30, 35, 40],
'Cidade': ['São Paulo', 'Rio de Janeiro', 'Curitiba', 'Belo Horizonte'],
'Salario': [4500.00, 7200.00, 5800.00, 3900.00]
}
df = pd.DataFrame(dados)
print("--- DataFrame de Funcionários ---")
print(df)
# Atributos de Inspeção Básica
print("\nDimensões da tabela (linhas, colunas):", df.shape)
print("Nomes das Colunas:", list(df.columns))
print("\nTipos de Dados em cada coluna:")
print(df.dtypes)