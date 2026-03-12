import pandas as pd

# -------------------------------------------------
# BLOCO 1: criar DataFrame e inspecionar estrutura
# -------------------------------------------------
dados_vendas = {
    "mes": ["Jan", "Jan", "Fev", "Fev", "Mar", "Mar"],
    "filial": ["Centro", "Norte", "Centro", "Norte", "Centro", "Norte"],
    "vendas": [12000, 9500, 13500, 10200, 14100, 11000],
    "clientes": [210, 180, 225, 190, 235, 205],
}

# a) Crie o DataFrame df_vendas usando dados_vendas
df_vendas = pd.DataFrame(dados_vendas)

# b) Mostre as 5 primeiras linhas
df_vendas.head()

# c) Mostre o formato (linhas, colunas)
df_vendas.shape

# d) Mostre os tipos de dados das colunas
df_vendas.dtypes

# -------------------------------------------------
# BLOCO 2: selecionar colunas e linhas
# -------------------------------------------------
# a) Mostre apenas as colunas "mes" e "vendas"
df_vendas[['mes', 'vendas']]

# b) Mostre somente a primeira linha
df_vendas.iloc[[0]]

# c) Mostre as linhas de indice 2 ate 4
df_vendas.iloc[2:5]

# -------------------------------------------------
# BLOCO 3: filtros com condicoes de negocio
# -------------------------------------------------
# a) Filtre vendas acima de 12000
df_vendas[df_vendas['vendas'] > 12000]

# b) Filtre apenas a filial "Centro"
df_vendas[df_vendas['filial'] == 'Centro']

# c) Filtre vendas acima de 11000 na filial "Norte"
df_vendas[(df_vendas['vendas'] > 11000) & (df_vendas['filial'] == 'Norte')]

# -------------------------------------------------
# BLOCO 4: novas colunas e metricas
# -------------------------------------------------
# a) Crie a coluna "ticket_medio" = vendas / clientes
df_vendas['ticket_medio'] = df_vendas['vendas'] / df_vendas['clientes']

# b) Crie a coluna "meta_batida" com True para vendas >= 13000
df_vendas['meta_batida'] = df_vendas['vendas'] >= 13000

# c) Mostre apenas "filial", "mes", "ticket_medio", "meta_batida"
df_vendas[['filial', 'mes', 'ticket_medio', 'meta_batida']]

# -------------------------------------------------
# BLOCO 5: agregacao com groupby
# -------------------------------------------------
# a) Calcule total de vendas por filial
df_vendas.groupby('filial')['vendas'].sum()

# b) Calcule media de clientes por mes
df_vendas.groupby('mes')['clientes'].mean()

# c) Descubra a filial com maior total de vendas
df_vendas.groupby('filial')['vendas'].sum().idxmax()

# -------------------------------------------------
# BLOCO 6: ordenacao e ranking
# -------------------------------------------------
# a) Ordene df_vendas por "vendas" em ordem decrescente
df_vendas.sort_values('vendas', ascending=False)

# b) Pegue os 3 maiores resultados de vendas
df_vendas.nlargest(3, 'vendas')

# c) Mostre um ranking com "filial", "mes", "vendas"
df_vendas[['filial', 'mes', 'vendas']].sort_values('vendas', ascending=False)

# -------------------------------------------------
# BLOCO 7: desafio final de analise
# -------------------------------------------------
# 1) Gere um resumo por filial com: total_vendas, media_ticket_medio, total_clientes
resumo_filial = df_vendas.groupby('filial').agg(
    total_vendas=('vendas', 'sum'),
    media_ticket_medio=('ticket_medio', 'mean'),
    total_clientes=('clientes', 'sum')
)

# 2) Ordene o resumo por total_vendas (desc)
resumo_filial = resumo_filial.sort_values('total_vendas', ascending=False)

# 3) Exiba qual filial teve melhor desempenho geral
resumo_filial.index[0]


# ===========================================================
# PARTE 1 – Estrutura lista + dicionário
# ===========================================================
dados_list_dict = [{
    "Column A":[1, 2, 3],
    "Column B":[4, 5, 6],
    "Column C":[7, 8, 9]
}]

# EXERCÍCIO 1 – Explorando a estrutura
# 1. Qual é o tipo de dados_list_dict?
type(dados_list_dict)

# 2. Qual é o tipo do primeiro elemento?
type(dados_list_dict[0])

# 3. Como acessar a lista da "Column A"?
dados_list_dict[0]["Column A"]

# 4. Como acessar o segundo elemento da "Column C"?
dados_list_dict[0]["Column C"][1]

# EXERCÍCIO 2 – Convertendo para DataFrame
# 1. Converta dados_list_dict[0] em um DataFrame chamado df1
df1 = pd.DataFrame(dados_list_dict[0])

# 2. Mostre: shape e tipos das colunas
df1.shape
df1.dtypes

# 3. Calcule: soma de cada coluna e média de cada coluna
df1.sum()
df1.mean()

# EXERCÍCIO 3 – Criando novas colunas
# 1. Crie coluna "Total" = soma das colunas
df1['Total'] = df1[['Column A', 'Column B', 'Column C']].sum(axis=1)

# 2. Crie coluna "Media" = média por linha
df1['Media'] = df1[['Column A', 'Column B', 'Column C']].mean(axis=1)

# 3. Filtre linhas onde Total > 10
df1[df1['Total'] > 10]

# EXERCÍCIO 4 – Conversões estruturais
# 1. Converta df1 para lista de dicionários
df1.to_dict(orient="records")

# Converta df1 para dicionário de listas
df1.to_dict(orient="list")

# EXERCÍCIO 5 – Trabalhando com lista
# 1. Transforme a coluna "Column A" em uma lista chamada lista_a.
lista_a = df1["Column A"].tolist()

# 2. Multiplique cada elemento da lista por 10.
lista_a_x10 = [x * 10 for x in lista_a]

# 3. Crie uma nova coluna chamada "Column A x10" com essa nova lista.
df1["Column A x10"] = lista_a_x10


# ===========================================================
# BASE DE DADOS
# ===========================================================
dados = [
    {"id_pais": 0, "nome_pais": "Brasil", "id_produto": 101, "descricao": "Produto A",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-01", "valor": 5000},
    {"id_pais": 0, "nome_pais": "Brasil", "id_produto": 102, "descricao": "Produto B",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-01", "valor": 3000},
    {"id_pais": 1, "nome_pais": "Argentina", "id_produto": 101, "descricao": "Produto A",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-02", "valor": 4000},
    {"id_pais": 1, "nome_pais": "Argentina", "id_produto": 102, "descricao": "Produto B",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-02", "valor": 6000},
    {"id_pais": 0, "nome_pais": "Brasil", "id_produto": 101, "descricao": "Produto A",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-03", "valor": 7000},
]

# PARTE 1 – EXPLORAÇÃO INICIAL
# 1. Qual o tipo da variável dados?
type(dados)

# 2. Quantos registros existem?
len(dados)

# 3. Quais são as chaves do primeiro dicionário?
list(dados[0].keys())

# 4. Liste todos os países existentes (sem repetição).
list(set(d["nome_pais"] for d in dados))

# PARTE 2 – CONVERSÃO PARA DATAFRAME
# 1. Converta dados para DataFrame chamado df
df = pd.DataFrame(dados)

# 2. Mostre shape, tipos e primeiras linhas
df.shape
df.dtypes
df.head()

# 3. Converta a coluna periodo para datetime
df['periodo'] = pd.to_datetime(df['periodo'])

# PARTE 3 – FILTROS E ORDENAÇÃO
# 1. Filtre apenas Brasil
df[df['nome_pais'] == 'Brasil']

# 2. Filtre apenas Produto A
df[df['descricao'] == 'Produto A']

# 3. Filtre valor > 4000
df[df['valor'] > 4000]

# 4. Combine Brasil + Produto A
df[(df['nome_pais'] == 'Brasil') & (df['descricao'] == 'Produto A')]

# Ordenação
# 1. Ordene por valor crescente
df.sort_values('valor', ascending=True)

# 2. Ordene por valor decrescente
df.sort_values('valor', ascending=False)

# 3. Ordene por periodo e depois por valor
df.sort_values(['periodo', 'valor'])

# PARTE 4 – AGREGAÇÕES
# 1. Total exportado por país
df.groupby('nome_pais')['valor'].sum()

# 2. Total exportado por produto
df.groupby('descricao')['valor'].sum()

# 3. Média por país
df.groupby('nome_pais')['valor'].mean()

# 4. Quantidade de operações por país
df.groupby('nome_pais').size()

# Agrupe por nome_pais e descricao. Calcule soma, média e contagem
df.groupby(['nome_pais', 'descricao'])['valor'].agg(['sum', 'mean', 'count'])
# Explicação: Esta tabela representa o detalhamento financeiro e volumétrico (valor total, valor médio e frequência de transações) segmentado para cada produto dentro de cada país.

# PARTE 5 – PIVOT TABLE
# Pivot por Produto
pivot_prod = df.pivot_table(index='periodo', columns='descricao', values='valor', aggfunc='sum')

# 1. Qual produto vendeu mais?
pivot_prod.sum().idxmax()

# 2. Qual mês teve maior valor total?
pivot_prod.sum(axis=1).idxmax()

# 3. Existe mês sem venda?
pivot_prod.isnull().any().any()

# Pivot por País
pivot_pais = df.pivot_table(index='periodo', columns='nome_pais', values='valor', aggfunc='sum')
# Explicação: A tabela cruza o eixo temporal com os países, permitindo analisar a evolução mensal do volume de exportações para o Brasil e para a Argentina de forma comparativa.

# PARTE 6 – FEATURE ENGINEERING
# 1. Extraia ano e mês da coluna periodo
df['ano'] = df['periodo'].dt.year
df['mes'] = df['periodo'].dt.month

# 2. Crie coluna valor_mil (valor / 1000)
df['valor_mil'] = df['valor'] / 1000

# 3. Calcule crescimento percentual por produto mês a mês
df['crescimento_pct'] = df.sort_values('periodo').groupby('descricao')['valor'].pct_change() * 100