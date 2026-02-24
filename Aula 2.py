import pandas as pd

df = pd.read_csv('/Users/gustavomendes/Faculdade/3° Semestre/Programação para Análise de Dados/notas.csv')

df.shape
df.columns
df.dtypes
df.isna().sum()
df.head()
df.tail()