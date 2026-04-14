"""
===========================================================
QUESTÕES DE REVISÃO – AP1
===========================================================
Tópicos cobertos:
  1. Python Básico (Listas e Dicionários)
  2. Carregando e Explorando Dados (CSV e Excel)
  3. Filtros e Seleções
  4. Cálculos e Novas Colunas
  5. Agrupamentos (GroupBy)
  6. Ranking e Ordenação
  7. APIs (Laboratório de Finanças – BCB)

Datasets utilizados:
  - exercicios/titanic.csv
  - exercicios/notas.csv
  - exercicios/salary.xlsx

APIs utilizadas:
  - BCB (Banco Central do Brasil) – PTAX Dólar
  - ViaCEP
  - BrasilAPI (Bancos)
  - IBGE (Estados)
===========================================================
"""

import pandas as pd
import requests

# Caminhos dos arquivos (ajuste se necessário)
PATH_TITANIC = "exercicios/titanic.csv"
PATH_NOTAS   = "exercicios/notas.csv"
PATH_SALARY  = "exercicios/salary.xlsx"


# ===========================================================
# PARTE 1 – PYTHON BÁSICO (Listas e Dicionários)
# ===========================================================

# ----------------------------------------------------------
# Questão 1
# Crie um dicionário chamado 'aluno' com as chaves:
# 'nome', 'idade' e 'curso'. Preencha com seus próprios dados.
# Depois, imprima cada valor usando as chaves.
# ----------------------------------------------------------

# RESOLVA AQUI:


# ----------------------------------------------------------
# Questão 2
# Dado o dicionário abaixo, faça as operações indicadas:
produtos = {
    "caneta": 2.50,
    "mochila": 120.00,
    "caderno": 35.00,
    "notebook": 4500.00
}
# a) Adicione o produto "mouse" com preço 89.90
# b) Altere o preço da "caneta" para 3.00
# c) Remova o produto "mochila"
# d) Imprima o dicionário final
# ----------------------------------------------------------

# RESOLVA AQUI:


# ----------------------------------------------------------
# Questão 3
# Dado o dicionário de notas abaixo, calcule e imprima
# a média da turma usando um loop for.
notas_turma = {
    "Alice":   8.5,
    "Bruno":   7.0,
    "Carla":   9.2,
    "Daniel":  6.8,
    "Eduarda": 7.5
}
# ----------------------------------------------------------

# RESOLVA AQUI:


# ----------------------------------------------------------
# Questão 4
# Dado o dicionário abaixo, crie um NOVO dicionário chamado
# 'caros' contendo apenas os produtos com preço ACIMA de 50.
catalogo = {"caneta": 10, "mochila": 80, "caderno": 45, "notebook": 3000}
# ----------------------------------------------------------

# RESOLVA AQUI:


# ----------------------------------------------------------
# Questão 5
# Dado o dicionário aninhado abaixo, adicione o aluno "Lucas"
# com idade 20 e notas [7, 8, 9]. Em seguida, calcule e
# imprima a média de cada aluno e diga quem tem a maior média.
turma = {
    "Ana":     {"idade": 17, "notas": [8, 9, 7]},
    "Pedro":   {"idade": 18, "notas": [6, 7, 8]},
    "Mariana": {"idade": 17, "notas": [9, 10, 8]}
}
# ----------------------------------------------------------

# RESOLVA AQUI:


# ===========================================================
# PARTE 2 – CARREGANDO E EXPLORANDO DADOS
# ===========================================================

# ----------------------------------------------------------
# Questão 6
# Carregue o arquivo titanic.csv em um DataFrame chamado df_titanic.
# Responda:
# a) Quantas linhas e colunas existem?
# b) Quais são os tipos de dados de cada coluna?
# c) Existem valores nulos em alguma coluna?
# ----------------------------------------------------------

# RESOLVA AQUI:
df_titanic = pd.read_csv('titanic.csv')
df_titanic.shape
df_titanic.dtypes
df_titanic.isnull().sum()

# ----------------------------------------------------------
# Questão 7
# Carregue o arquivo notas.csv em um DataFrame chamado df_notas.
# Responda:
# a) Quantos anos diferentes aparecem na coluna 'year'?
# b) Qual é a média da coluna 'score'?
# c) Qual é o desvio padrão de 'score'?
# ----------------------------------------------------------

# RESOLVA AQUI:
df_notas = pd.read_csv('notas.csv')
df_notas['year'].nunique()
df_notas['score'].mean()
df_notas['score'].std()

# ----------------------------------------------------------
# Questão 8
# Carregue o arquivo salary.xlsx em um DataFrame chamado df_salary.
# Responda:
# a) Quantas linhas e colunas existem?
# b) Qual é o maior salário registrado?
# c) Qual é o menor salário registrado?
# ----------------------------------------------------------

# RESOLVA AQUI:
df_salary = pd.read_excel('salary.xlsx')
df_salary.shape
df_salary['salary'].max()
df_salary['salary'].min()

# ===========================================================
# PARTE 3 – FILTROS E SELEÇÕES
# ===========================================================

# ----------------------------------------------------------
# Questão 9  (Dataset: titanic.csv)
# a) Filtre apenas as passageiras do sexo feminino.
# b) Quantos passageiros sobreviveram? (Survived == 1)
# c) Quantos homens sobreviveram?
# d) Quantos passageiros têm "John" no nome?
# ----------------------------------------------------------

# RESOLVA AQUI:
df_titanic[df_titanic['Sex'] == 'female']
df_titanic[df_titanic['Survived'] == 1]['PassengerId'].nunique()
df_titanic[(df_titanic['Sex'] == 'male') & (df_titanic['Survived'] == 1)]['PassengerId'].nunique()
df_titanic[df_titanic['Name'].str.contains('John')]['PassengerId'].nunique()

# ----------------------------------------------------------
# Questão 10  (Dataset: notas.csv)
# a) Mostre apenas as colunas 'institution', 'country' e 'score'.
# b) Filtre universidades com score maior que 80.
# c) Filtre universidades dos EUA ("USA") com score maior que 80.
# d) Mostre as 10 melhores universidades (menor world_rank).
# ----------------------------------------------------------

# RESOLVA AQUI:
df_notas[['institution', 'country', 'score']]
df_notas[df_notas['score'] > 80]
df_notas[(df_notas['country'] == 'USA') & (df_notas['score'] > 80)]
df_notas.sort_values('world_rank', ascending = True).head(10)
df_notas.nsmallest(10, 'world_rank')

# ----------------------------------------------------------
# Questão 11  (Dataset: salary.xlsx)
# a) Crie um df com apenas as colunas:
#    job_title, salary, company_location, company_size, remote_ratio
# b) Filtre profissões no Brasil ("BR").
# c) Filtre profissões nos EUA ("US") em empresas grandes ("L").
# ----------------------------------------------------------

# RESOLVA AQUI:
df_salary[['job_title', 'salary', 'company_location', 'company_size', 'remote_ratio']]
df_salary[df_salary['company_location'] == 'BR']
df_salary[(df_salary['company_location'] == 'US') & (df_salary['company_size'] == 'L')]

# ----------------------------------------------------------
# Questão 12  (Dataset: notas.csv)
# Use .loc para selecionar linhas onde o país é "Brazil"
# e mostre apenas as colunas 'institution' e 'score'.
# (Dica: crie um filtro antes de usar o .loc)
# ----------------------------------------------------------

# RESOLVA AQUI:
filtro_br = df_notas['country'] == 'Brazil'
df_br = df_notas.loc[filtro_br, ['institution', 'score']]

# ----------------------------------------------------------
# Questão 13  (Dataset: notas.csv)
# Use .str.contains() para filtrar universidades cujo nome
# contenha "Technology" (sem diferenciar maiúsculas/minúsculas).
# ----------------------------------------------------------

# RESOLVA AQUI:
filtro_tech = df_notas['institution'].str.contains('Technology', case = False)
df_tech = df_notas[filtro_tech]

# ===========================================================
# PARTE 4 – CÁLCULOS E NOVAS COLUNAS
# ===========================================================

# ----------------------------------------------------------
# Questão 14  (Dataset: salary.xlsx)
# Crie uma nova coluna chamada 'salary_k' que representa
# o salário em milhares (salary / 1000).
# ----------------------------------------------------------

# RESOLVA AQUI:
df_salary['salary_k'] = df_salary['salary'] / 1000

# ----------------------------------------------------------
# Questão 15  (Dataset: notas.csv)
# a) Qual a média, máximo e mínimo da coluna 'score'?
# b) Quantos valores nulos existem na coluna 'broad_impact'?
# c) Preencha os nulos de 'broad_impact' com a média da coluna.
# ----------------------------------------------------------

# RESOLVA AQUI:
df_notas['score'].mean()
df_notas['score'].max()
df_notas['score'].min()
df_notas['broad_impact'].isnull().sum()
df_notas['broad_impact'] = df_notas['broad_impact'].fillna(df_notas['broad_impact'].mean())

# ----------------------------------------------------------
# Questão 16  (Dataset: titanic.csv)
# Crie uma nova coluna chamada 'sobreviveu_texto' que contém
# "Sim" quando Survived == 1 e "Não" caso contrário.
# (Dica: use df.apply() com lambda)
# ----------------------------------------------------------

# RESOLVA AQUI:
df_titanic['sobreviveu_texto'] = df_titanic['Survived'].apply(lambda x: 'Sim' if x == 1 else 'Não')

# ===========================================================
# PARTE 5 – AGRUPAMENTOS (GROUPBY)
# ===========================================================

# ----------------------------------------------------------
# Questão 17  (Dataset: notas.csv)
# a) Calcule a média do score por país.
# b) Qual país tem a maior média de score?
# c) Quantas universidades cada país tem?
# d) Top 5 países com mais universidades.
# ----------------------------------------------------------

# RESOLVA AQUI:
media_pais = df_notas.groupby('country')['score'].mean()
df_notas.groupby('country')['score'].mean().sort_values(ascending = False).head(1)
print(media_pais.idxmax())
universidades_pais = df_notas.groupby('country')['institution'].count()
print(universidades_pais.sort_values(ascending = False).head(5))

# ----------------------------------------------------------
# Questão 18  (Dataset: salary.xlsx)
# a) Qual profissão tem a maior média salarial?
# b) Qual profissão tem a menor média salarial?
# c) Quais profissões têm média salarial ACIMA da média geral?
# d) Qual a média salarial no Brasil ("BR")?
# ----------------------------------------------------------

# RESOLVA AQUI:
df_salary.groupby('job_title')['salary'].mean().idxmax()
df_salary.groupby('job_title')['salary'].mean().idxmin()
media_prof = df_salary.groupby('job_title')['salary'].mean()
media_geral = df_salary['salary'].mean()
media_acima = media_prof > media_geral
print(media_acima)
br = df_salary[df_salary['company_location'] == 'BR']
media_br = df_salary['salary'].mean()

# ----------------------------------------------------------
# Questão 19  (Dataset: salary.xlsx)
# a) Qual modalidade (remote_ratio) paga mais em média?
#    (0 = Presencial, 50 = Híbrido, 100 = Remoto)
# b) Qual país tem o maior número de profissões trabalhando
#    100% remoto?
# ----------------------------------------------------------

# RESOLVA AQUI:
df_salary.groupby('remote_ratio')['salary'].mean().idxmax()
df_remoto = df_salary[df_salary['remote_ratio'] == 100]
df_remoto.groupby('company_location')['job_title'].count().idxmax()

# ----------------------------------------------------------
# Questão 20  (Dataset: notas.csv)
# a) Calcule a média do score por ano.
# b) Qual ano teve a maior média de score?
# ----------------------------------------------------------

# RESOLVA AQUI:
df_notas.groupby('year')['score'].mean()
df_notas.groupby('year')['score'].mean().idxmax()

# ===========================================================
# PARTE 6 – RANKING E ORDENAÇÃO
# ===========================================================

# ----------------------------------------------------------
# Questão 21  (Dataset: notas.csv)
# a) Ordene o DataFrame pelo score de forma DECRESCENTE.
# b) Crie uma coluna 'rank_score' que rankeia as universidades
#    pelo score (1 = maior score).
# c) Mostre as 5 primeiras linhas após a ordenação.
# ----------------------------------------------------------

# RESOLVA AQUI:
df_notas['score'].sort_values(ascending = False)
df_notas['rank_score'] = df_notas['score'].rank(ascending = False)
print(df_notas[['institution', 'score', 'rank_score']].head(5))

# ----------------------------------------------------------
# Questão 22  (Dataset: salary.xlsx)
# a) Ordene o DataFrame pelo salary de forma DECRESCENTE.
# b) Mostre as 10 profissões mais bem pagas (sem repetição).
# ----------------------------------------------------------

# RESOLVA AQUI:
df_sal_ord = df_salary.sort_values('salary', ascending = False).head(10)
df_sal_ord = df_salary['job_title'].drop_duplicates().head(10)

# ----------------------------------------------------------
# Questão 23  (Dataset: notas.csv)
# Mostre as 5 melhores universidades do Brasil.
# (Dica: filtre por country == "Brazil" e ordene por world_rank)
# ----------------------------------------------------------

# RESOLVA AQUI:
df_uni_br = df_notas[df_notas['country'] == 'Brazil']
df_5 = df_uni_br.sort_values('world_rank', ascending = True).head(5)

# ===========================================================
# PARTE 7 – APIs (Laboratório de Finanças – BCB)
# ===========================================================

# ----------------------------------------------------------
# Questão 24
# Explique com suas palavras o que é uma API, um endpoint,
# e o que significa o status_code 200.
# ----------------------------------------------------------

"""
RESPONDA AQUI:

API:

Endpoint:

Status_code 200:
"""


# ----------------------------------------------------------
# Questão 25
# Consuma a API do BCB para obter a cotação do dólar PTAX
# em 2024. Use os parâmetros abaixo e:
# a) Transforme a resposta em DataFrame.
# b) Converta a coluna 'valor' para float.
# c) Calcule a média, máximo e mínimo da cotação.
#
# URL:    https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados
# Params: formato="json", dataInicial="01/01/2024", dataFinal="31/12/2024"
# ----------------------------------------------------------

# RESOLVA AQUI:
url_bcb = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados'

parametros = {
    'formato': 'json',
    'dataInicial': '01/01/2024',
    'dataFinal': '31/12/2024'
}

response_bcb = requests.get(url_bcb, params = parametros)
print(response_bcb.status_code)

df_bcb = pd.DataFrame(response_bcb.json())

df_bcb.dtypes
df_bcb['valor'] = df_bcb['valor'].astype(float)
df_bcb.dtypes

df_bcb['valor'].mean()
df_bcb['valor'].max()
df_bcb['valor'].min()

# ----------------------------------------------------------
# Questão 26
# Use a API do BCB para consultar a cotação do dólar em 2023.
# Qual foi o maior valor registrado e em que data ocorreu?
# (Dica: use df.loc[df['valor'].idxmax()])
# ----------------------------------------------------------

# RESOLVA AQUI:

url_bcb1 = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados'

parametros1 = {
    'formato': 'json',
    'dataInicial': '01/01/2023',
    'dataFinal': '31/12/2023'
}

response_bcb1 = requests.get(url_bcb1, params = parametros1)

df_bcb1 = pd.DataFrame(response_bcb1.json())

idx_max = df_bcb1['valor'].idxmax()
linha_max = df_bcb1.loc[idx_max]

# ----------------------------------------------------------
# Questão 27
# Consulte a API do ViaCEP para o CEP 01310-100 (Av. Paulista).
# a) Verifique o status_code.
# b) Transforme o resultado em DataFrame.
# c) Mostre as colunas: cep, logradouro, bairro, localidade, uf.
#
# URL: https://viacep.com.br/ws/01310100/json/
# ----------------------------------------------------------

# RESOLVA AQUI:

url_cep = 'https://viacep.com.br/ws/01310100/json/'

response_cep = requests.get(url_cep)
response_cep.status_code

df_cep = pd.DataFrame([response_cep.json()])

df_cep[['cep', 'logradouro', 'bairro', 'localidade', 'uf']]

# ----------------------------------------------------------
# Questão 28
# Consulte a lista de bancos usando a BrasilAPI.
# a) Transforme em DataFrame.
# b) Quantos bancos existem no total?
# c) Filtre os bancos cujo nome (fullName) contenha "Brasil".
#
# URL: https://brasilapi.com.br/api/banks/v1
# ----------------------------------------------------------

# RESOLVA AQUI:

url_bancos = 'https://brasilapi.com.br/api/banks/v1'

response_bancos = requests.get(url_bancos)
response_bancos.status_code

df_bancos = pd.DataFrame(response_bancos.json())

df_bancos['name'].count()

df_bancos['fullName'] = df_bancos['fullName'].fillna('')
bancos_brasil = df_bancos['fullName'].str.contains('Brasil', case = False)
print(df_bancos.loc[bancos_brasil, ['ispb', 'name', 'code']])

# ----------------------------------------------------------
# Questão 29
# Consulte a API do IBGE para obter a lista de estados brasileiros.
# a) Transforme em DataFrame.
# b) Extraia o nome da região de cada estado (coluna 'regiao').
#    (Dica: use .apply() com lambda e .get())
# c) Mostre apenas: nome, sigla e regiao_nome.
#
# URL: https://servicodados.ibge.gov.br/api/v1/localidades/estados
# ----------------------------------------------------------

# RESOLVA AQUI:

url_ibge = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados'

response_ibge = requests.get(url_ibge)
response_ibge.status_code
df_ibge = pd.DataFrame(response_ibge.json())




# ----------------------------------------------------------
# Questão 30 – DESAFIO INTEGRADOR
# Use a API do BCB para comparar a cotação média do dólar
# entre 2022, 2023 e 2024. Crie um DataFrame resumo com as
# colunas 'ano' e 'media_dolar' e ordene do maior para o menor.
# ----------------------------------------------------------

# RESOLVA AQUI:
