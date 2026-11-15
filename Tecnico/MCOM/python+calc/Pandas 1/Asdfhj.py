import pandas as pd
empresa = {
    'vendedores': ['Ana', 'Bruno', 'Carla', 'Diego'], 
    'vendas': [1500, 2000, 1800, 2200]
}
df= pd.DataFrame(empresa)
print(list(df.columns))