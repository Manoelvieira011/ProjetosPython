import pandas as pd
import matplotlib.pyplot as plt

# Carregando os dados de vendas a partir de um arquivo CSV
data = pd.read_csv('dados_vendas.csv')

# Exibindo as primeiras linhas do conjunto de dados
print(data.head())

# Obtendo informações básicas sobre os dados
print(data.info())

# Calculando o total de vendas
total_vendas = data['Valor'].sum()
print(f'Total de vendas: R${total_vendas:.2f}')

# Calculando a média de vendas por categoria de produto
vendas_por_categoria = data.groupby('Categoria')['Valor'].mean()
print('Média de vendas por categoria:')
print(vendas_por_categoria)

# Criando um gráfico de barras para visualizar as vendas por categoria
vendas_por_categoria.plot(kind='bar')
plt.xlabel('Categoria')
plt.ylabel('Valor Médio das Vendas')
plt.title('Vendas por Categoria')
plt.show()
