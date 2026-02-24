# Questão 21

nomes = ["Ana", "Pedro", "Maria", "João"]

# Questão 22

for nome in nomes:
    print(nome)

# Questão 23

nomes_maiusculos = []

for nome in nomes:
    nome_maisculo = nome.upper()
    nomes_maiusculos.append(nome_maisculo)

print(nomes_maiusculos)

# Questão 24

numeros = range(0,20)
numeros_pares = []

for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)

print(numeros_pares)

# Questão 25

quadrados = []

for numero in numeros:
    quadrado = numero ** 2
    quadrados.append(quadrado)

print(quadrados)

# Questão 26

palavras = ["python", "java", "c", "javascript"]
caracteres = []

for palavra in palavras:
    caractere = len(palavra)
    caracteres.append(caractere)

print(caracteres)