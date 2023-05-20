# Descrição do programa
Programa irá ealizar análises de em um conjunto de dados de vendas usando as bibliotecas pandas e matplotlib.

Nesse exemplo, supus que os dados de vendas estão armazenados em um arquivo CSV chamado "dados_vendas.csv". A partir desse arquivo, usei a função read_csv do Pandas para carregar os dados em um DataFrame.

Em seguida, usei o método head para exibir as primeiras linhas do conjunto de dados e info para obter informações básicas sobre as colunas e tipos de dados.

Calculei o total de vendas somando a coluna 'Valor' do DataFrame.

Em seguida, usei o método groupby para agrupar os dados por categoria de produto e calcular a média de vendas em cada categoria. Essas informações são exibidas e, em seguida, um gráfico de barras é criado usando o método plot do Pandas e personalido usando funções do Matplotlib.

# Importante para rodar o programa
instalar aa bibliotlecas necessárias através do comando:
pip install pandas matplotlib