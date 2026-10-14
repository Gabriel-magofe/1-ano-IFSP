import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# 1. Carregar os dados
df = pd.read_csv('relatorio_vendas.csv')
# Converter a coluna Data para o tipo datetime do Pandas (garante ordenação correta no gráfico)
df['Data'] = pd.to_datetime(df['Data'])
# 2. Configurar a figura do Matplotlib
plt.figure(figsize=(10, 5))
# 3. Plotar os dados carregados
plt.plot(df['Data'], df['Vendas_R$'], marker='o', color='navy',
linestyle='-', label='Vendas (R$)')
# 4. Estilizar o gráfico
plt.title('Evolução Diária de Vendas - Dados Carregados do Arquivo',
fontsize=14, fontweight='bold')
plt.xlabel('Data', fontsize=12)
plt.ylabel('Valor de Vendas (R$)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
# 5. Exibir o gráfico
plt.show()