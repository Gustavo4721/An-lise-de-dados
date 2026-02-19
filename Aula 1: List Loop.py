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
    quadrado = numero ** 2\