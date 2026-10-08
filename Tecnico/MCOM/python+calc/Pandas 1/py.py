import pandas as pd
import numpy as np

print("Pandas version:", pd.__version__)
print("NumPy version:", np.__version__)

idades=pd.Series([25,30,35,40], name='Idade')
print("---Series---")
print(idades)

dados = {
    'Nome': ['Ana', 'Bruno', 'Carla', 'Diogo'],
    'Idade': [25, 30, 35, 40],
    'Cidades': ['São Paulo', 'Rio de Janeiro', 'Curitiba', 'Belo Horizonte'],
    'Salarios': [4500.00, 7200.00, 5800.00, 3900.00]
}

df = pd.DataFrame(dados)
print("---DataFrame---")
print(df)