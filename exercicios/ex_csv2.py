# LISTA DE EXERCÍCIOS – ANÁLISE DE DADOS COM PANDAS Dataset: Ranking
# Mundial de Universidades (notas.csv)

import pandas as pd
import matplotlib

df = pd.read_csv('notas.csv')

# ============================================================
# EXPLORAÇÃO INICIAL (EDA BÁSICA)
# ============================================================

# Exercício 1 – Conhecendo o Dataset 

# 1. Quantas linhas e colunas existem?
df.shape
df.shape[0]
df.shape[1]

# 2. Quais são os tipos de dados?
df.dtypes

# 3. Existe coluna com valores ausentes?
df.isna().any()

# 4. Qual é o período de anos disponível?
ano_min = df['year'].min()
ano_max = df['year'].max()
print(f'O período de anos disponível é de {ano_min} até {ano_max}')

# 5. Quantos países diferentes existem?
df['country'].nunique()

# Exercício 2 – Estatísticas Gerais 

# 1. Média do score
df['score'].mean()

# 2. Maior score 
df['score'].max()

# 3. Menor score 
df['score'].min

# 4. Média do score por ano 
df.groupby('year')['score'].mean()

# 5. Desvio padrão do score
df['score'].std()

# ============================================================
# FILTROS E SELEÇÕES
# ============================================================

# Exercício 3 – Top Universidades

# 1. Mostre as 10 melhores universidades do mundo (menor world_rank)
df.sort_values(by=['year', 'world_rank']).groupby('year').head(10)

# 2. Mostre as 5 melhores universidades do Brasil
df[df['country'] == 'Brazil'].sort_values(by=['year', 'world_rank']).groupby('year').head(5)

# 3. Mostre universidades com score maior que 90 
df[df['score'] > 90]

# 4. Mostre universidades dos EUA com score maior que 80
df[(df['country'] == 'USA') & (df['score'] > 80)]

# Exercício 4 – Seleção Avançada 

# 1. Mostre apenas as colunas: institution, country e score
df[['institution', 'country', 'score']]

# 2. Mostre universidades entre rank 50 e 100
df[df['world_rank'].between(50, 100)]

# 3. Mostre universidades cujo país é “United Kingdom”
df[df['country'] == 'United Kingdom']

# ============================================================
# MISSING VALUES
# ============================================================

# Exercício 5 – Valores Ausentes 

# 1. Quantos valores nulos existem na coluna broad_impact?
df['broad_impact'].isna().sum()

# 2. Qual percentual do dataset é nulo?
(df.isna().sum().sum() / df.size) * 100

# 3. Remova linhas com broad_impact nulo
media_antes = df['broad_impact'].mean()
df = df.dropna(subset=['broad_impact'])

# 4. Preencha valores nulos com a média
df['broad_impact'] = df['broad_impact'].fillna(media_antes)
media_depois = df['broad_impact'].mean()

# 5. Compare a média antes e depois do preenchimento
print(f'Média antes: {media_antes}')
print(f'Média depois: {media_depois}')

# ============================================================
# GROUPBY (ANÁLISE POR PAÍS E ANO)
# ============================================================

# Exercício 6 – Análise por País

# 1. Média do score por país
df.groupby('country')['score'].mean()

# 2. País com maior média de score
df.groupby('country')['score'].mean().idxmax()

# 3. Quantidade de universidades por país
df.groupby('country')['institution'].nunique()

# 4. Top 10 países com mais universidades
df.groupby('country')['institution'].nunique().sort_values(ascending=False).head(10)

# Exercício 7 – Análise por Ano 

# 1. Média do score por ano
df.groupby('year')['score'].mean()

# 2. Qual ano teve maior média? 
df.groupby('year')['score'].mean().idxmax()

# 3. Faça um gráfico da evolução do score médio ao longo do tempo
df.groupby('year')['score'].mean().plot(kind='line')