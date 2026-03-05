import pandas as pd

df = pd.read_csv('/Users/gustavomendes/Faculdade/3° Semestre/Programação para Análise de Dados/notas.csv')

df.shape
df.dtypes
df.isnull().sum()
df.columns
df.loc[:, "year"].unique()
df.loc[:, "country"].unique()
df.dtypes
df.isna().sum()
df.head()
df.tail()