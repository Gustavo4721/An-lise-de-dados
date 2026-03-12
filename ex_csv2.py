# LISTA DE EXERCÍCIOS – ANÁLISE DE DADOS COM PANDAS Dataset: Ranking
# Mundial de Universidades (notas.csv)

# ============================================================

# EXPLORAÇÃO INICIAL (EDA BÁSICA)

import pandas as pd
df = pd.read_csv('/Users/gustavomendes/Faculdade/3° Semestre/Programação para Análise de Dados/notas.csv')

# ============================================================

# Exercício 1 – Conhecendo o Dataset 

# 1. Quantas linhas e colunas existem?

df.shape[0] # Acessa a contagem de linhas
df.shape[1] # Acessa a contagem de colunas

linhas, colunas = df.shape
print(f'Linhas: {linhas}, Colunas: {colunas}')

# 2. Quais são os tipos de dados? 

print(df.dtypes) # Extração direta dos tipos

# 3. Existe coluna com valores ausentes?

df.isna().sum() # Retorna quantidade de valores nulos por coluna

# 4. Qual é o período de anos disponível? 

ano_inicial = df['year'].min() # Acessa o valor mínimo da coluna
ano_final = df['year'].max() # Acessa o valor máximo da coluna

print(f'Período disponível: {ano_inicial} a {ano_final}')

# 5. Quantos países diferentes existem?

df['country'].nunique() # Retorna a contagem de valores distintos da coluna

# Exercício 2 – Estatísticas Gerais 

# 1. Média do score

df['score'].mean() # Retorna a média dos valores da coluna

# 2. Maior score

df['score'].max() # Acessa o valor máximo da coluna

# 3.Menor score 

df['score'].min() # Acessa o valor máximo da coluna

# 4. Média do score por ano 

df.groupby('year')['score'].mean() # Utilizada para estruturar informações em partes gerenciáveis

## O primeiro bloco define os critérios de separação
# #O segundo bloco define quais dados serão analisados

# 5. Desvio padrão do score

df['score'].std() # Calcula o desvio padrão dos valores da coluna

# ============================================================
# FILTROS E SELEÇÕES
# ============================================================

# Exercício 3 – Top Universidades 

# 1. Mostre as 10 melhores universidades do mundo (menor world_rank) 

top_10 = df[df['year'] == 2015].sort_values(by='world_rank', ascending=True).head(10)
print(top_10[['world_rank', 'institution', 'year']])

## .sort_values(by='coluna') Organiza as linhas da coluna
## ascending = True Organiza na ordem crescente
## Head(Número) Isola as linhas

# 2. Mostre as 5 melhores universidades do Brasil (se existirem)

top_5_brasil = df[(df['country'] == 'Brazil') & (df['year'] == 2015)].sort_values(by='world_rank', ascending=True).head(5)
print(top_5_brasil[['world_rank', 'institution', 'year']])

# 3. Mostre universidades com score maior que 90

top_90 = df[df['score'] > 90]
print(top_90[['institution', 'score']])

# 4. Mostre universidades dos EUA com score maior que 80

top_eua_80 = df[(df['country'] == 'USA') & (df['score'] > 80)]
print(top_eua_80[['institution', 'score']])

# Exercício 4 – Seleção Avançada 

# 1. Mostre apenas as colunas: institution, country e score 

df_selecao = df[['institution', 'country', 'score']]
print(df_selecao)

# 2. Mostre universidades entre rank 50 e 100 

top_50_100 = df[df['world_rank'].between(50, 100)]
print(top_50_100)

# 3. Mostre universidades cujo país é “United Kingdom”

# ============================================================ PARTE 3 –
# MISSING VALUES
# ============================================================

# Exercício 5 – Valores Ausentes 

# 1. Quantos valores nulos existem na coluna broad_impact? 

nulos_broad_impact = df['broad_impact'].isna().sum()
print(nulos_broad_impact)

# 2. Qual percentual do dataset é nulo? 

percentual_total = (df.isna().sum().sum() / df.size) * 100
print(round(percentual_total, 2))

# 3. Remova linhas com broad_impact nulo

df.dropna(subset=['broad_impact'], inplace=True)

# 4. Preencha valores nulos com a média 



# 5. Compare a média antes e depois do preenchimento

# ============================================================ PARTE 4 –
# GROUPBY (ANÁLISE POR PAÍS E ANO)
# ============================================================

# Exercício 6 – Análise por País 
# 1. Média do score por país 
# 2. País com maior média de score 
# 3. Quantidade de universidades por país 
# 4. Top 10 países com mais universidades

# Exercício 7 – Análise por Ano 
# 1. Média do score por ano 
# 2. Qual ano teve maior média? 
# 3. Faça um gráfico da evolução do score médio ao longo do tempo