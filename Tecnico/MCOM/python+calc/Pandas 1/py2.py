import pandas as pd
# Criando uma Series a partir de uma lista simples
idades = pd.Series([25, 30, 35, 40], name="Idades_Alunos")
print("--- Series de Idades ---")
print(idades)
# Acessando atributos da Series
print("\nValores:", idades.values)
print("Índices:", idades.index)
print("Tipo de Dados:", idades.dtype)
# Criando uma Series com rótulos customizados
temperaturas = pd.Series([22.5, 24.0, 19.8],
index=['Segunda', 'Terça', 'Quarta'], name="Temp_Celsius")
print("\n--- Series com Índices Personalizados ---")
print(temperaturas)
# Acesso por rótulo
print("\nTemperatura na Terça-feira:", temperaturas['Terça'])