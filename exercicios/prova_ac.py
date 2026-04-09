# Questão 1: Carregar o DataFrame
# LER arquivo titanic.csv em um DataFrame pandas chamado df?
import pandas as pd
df = pd.read_csv('titanic.csv')

# Questão 2: Filtrar passageiros do sexo feminino
# Filtrar o DataFrame para mostrar apenas as Mulheres?
# (Dica: Filtar onde a coluna "Sex" é igual a "female")
df_feminino = df[df['Sex'] == 'female']

# Questão 3: Contar sobreviventes
# Quantos passageiros Sobreviveram?
# (Dica: Sobreviventes têm o valor 1 na coluna "Survived")
df_sobreviventes = df[df['Survived'] == 1]
quantidade_sobreviventes = len(df_sobreviventes)
print(quantidade_sobreviventes)

# Questão 4: Quantos Homens Sobreviveram?
df_sobreviventes_homens = df[(df['Sex'] == 'male') & (df['Survived'] == 1)]
quantidade_sobreviventes_homens = len(df_sobreviventes_homens)
print(quantidade_sobreviventes_homens)

# Questão 5: Calcular Nome "John"
# Calcular quantos passageiros tem o nome "John"?
# (Dica: Usar a coluna "Name")
df_john = df[df['Name'].str.contains('John', case=False, na=False)]
quantidade_john = len(df_john)
print(quantidade_john)