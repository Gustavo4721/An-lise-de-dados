# LISTA DE EXERCÍCIOS – ANÁLISE DE DADOS COM PANDAS Dataset: Ranking
# Mundial de Universidades (notas.csv)

import pandas as pd

df = pd.read_csv('notas.csv')

# ============================================================
# EXPLORAÇÃO INICIAL (EDA BÁSICA)
# ============================================================

# Exercício 1 – Conhecendo o Dataset 
# 1. Quantas linhas e colunas existem?
df.shape

# 2. Quais são os tipos de dados? 
df.dtypes

# 3. Existe coluna com valores ausentes?
df.isnull().any()

# 4. Qual é o período de anos disponível? 
df['year'].min(), df['year'].max()

# 5. Quantos países diferentes existem?
df['country'].nunique()

# Exercício 2 – Estatísticas Gerais 
# 1. Média do score 
df['score'].mean()

# 2. Maior score 
df['score'].max()

# 3.Menor score 
df['score'].min()

# 4. Média do score por ano 
df.groupby('year')['score'].mean()

# 5. Desvio padrão do score
df['score'].std()

# ============================================================
# FILTROS E SELEÇÕES
# ============================================================

# Exercício 3 – Top Universidades 
# 1. Mostre as 10 melhores universidades do mundo (menor world_rank) 
df.nsmallest(10, 'world_rank')

# 2. Mostre as 5 melhores universidades do Brasil (se existirem) 
df[df['country'] == 'Brazil'].nsmallest(5, 'world_rank')

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

# ============================================================ PARTE 3 –
# MISSING VALUES
# ============================================================

# Exercício 5 – Valores Ausentes 
# 1. Quantos valores nulos existem na coluna broad_impact? 
df['broad_impact'].isnull().sum()

# 2. Qual percentual do dataset é nulo? 
(df.isnull().sum() / len(df)) * 100

# 3. Remova linhas com broad_impact nulo 
df.dropna(subset=['broad_impact'])

# 4. Preencha valores nulos com a média 
df['broad_impact'].fillna(df['broad_impact'].mean())

# 5. Compare a média antes e depois do preenchimento
df['broad_impact'].mean(), df['broad_impact'].fillna(df['broad_impact'].mean()).mean()

# ============================================================ PARTE 4 –
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
df['country'].value_counts().head(10)

# Exercício 7 – Análise por Ano 
# 1. Média do score por ano 
df.groupby('year')['score'].mean()

# 2. Qual ano teve maior média? 
df.groupby('year')['score'].mean().idxmax()

# 3. Faça um gráfico da evolução do score médio ao longo do tempo
df.groupby('year')['score'].mean().plot(kind='line')