import pandas as pd

df = pd.read_csv('salary.xlsx - Sheet1.csv')

# 1. Quantas linhas e quantas colunas tem o dataset?
df.shape

# 2. Qual a média salarial? Qual é o maior salário? O menor salário?
df['salary_in_usd'].mean()
df['salary_in_usd'].max()
df['salary_in_usd'].min()

# 3. Crie um df com apenas as colunas job_title, salary, company_location, company_size, remote_ratio?
df_reduzido = df[['job_title', 'salary', 'company_location', 'company_size', 'remote_ratio']]
df_reduzido.head()

# 4. Qual é o maior e menor salário de um “Data Scientist”? Onde fica essas empresas?
df_ds = df[df['job_title'] == 'Data Scientist']
df_ds.nlargest(1, 'salary_in_usd')[['salary_in_usd', 'company_location']]
df_ds.nsmallest(1, 'salary_in_usd')[['salary_in_usd', 'company_location']]

# 5. Qual a profissão com a maior média salarial? E a menor?
df.groupby('job_title')['salary_in_usd'].mean().idxmax()
df.groupby('job_title')['salary_in_usd'].mean().idxmin()

# 6. Quais as profissões com a média salarial maior que a média geral?
media_geral = df['salary_in_usd'].mean()
medias_profissoes = df.groupby('job_title')['salary_in_usd'].mean()
medias_profissoes[medias_profissoes > media_geral].index.tolist()

# 7. Qual a localização com maior média salarial?
df.groupby('company_location')['salary_in_usd'].mean().idxmax()

# 8. Quais as profissões que existem no Brasil (BR)?
df[df['company_location'] == 'BR']['job_title'].unique()

# 9. Qual a média salarial no Brasil?
df[df['company_location'] == 'BR']['salary_in_usd'].mean()

# 10. Quantas profissões existem no Brasil?
df[df['company_location'] == 'BR']['job_title'].nunique()

# 11. Qual a profissão que mais ganha no Brasil? (Considerando média por cargo)
df[df['company_location'] == 'BR'].groupby('job_title')['salary_in_usd'].mean().idxmax()

# 12. Quantas profissões tem nos US e que trabalham em empresas grandes (L)?
df[(df['company_location'] == 'US') & (df['company_size'] == 'L')]['job_title'].nunique()

# 13. Qual é a média salarial das empresas médias (M) no Canada (CA)?
df[(df['company_location'] == 'CA') & (df['company_size'] == 'M')]['salary_in_usd'].mean()

# 14. Qual é o país com mais profissões? E qual é o com menos?
df.groupby('company_location')['job_title'].nunique().idxmax()
df.groupby('company_location')['job_title'].nunique().idxmin()

# 15. Quem ganha mais que trabalha remoto, presencial ou híbrido? 
# (Retorna 0=Presencial, 50=Híbrido, 100=Remoto)
df.groupby('remote_ratio')['salary_in_usd'].mean().idxmax()

# 16. Qual o país com maior numero de profissões trabalhando 100% remoto?
df[df['remote_ratio'] == 100].groupby('company_location')['job_title'].nunique().idxmax()