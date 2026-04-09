# Questão 1

frutas = ["maçã", "banana", "laranja", "uva"]

# Questão 2

print(frutas[0])
print(frutas[-1])

# Questão 3

frutas.append("manga")

# Questão 4

frutas.remove("banana")

# Questão 5

indice = frutas.index("laranja")
frutas[indice] = "abacaxi"

# Questão 6

números = list(range(1, 11))

# Questão 7

print(sum(números))

# Questão 8

print(min(números))
print(max(números))

# Questão 9

print(list(reversed(números)))

# Questão 10

cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba"]

# Questão 11

print(sorted(cidades))

# Questão 12

cidades.append("Porto Alegre")
print(cidades)

# Questão 13

indice2 = cidades.index("Curitiba")
print(indice2)

# Questão 14

cidades.remove("Rio de Janeiro")
print(cidades)

# Questão 15

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

# Questão 16

lista3 = lista1 + lista2

# Questão 17

print(lista3)

# Questão 18

animais_domesticos = ["cachorro", "gato", "coelho"]
animais_selvagens = ["leão", "tigre", "urso"]

# Questão 19

todos_animais = animais_domesticos + animais_selvagens

# Questão 20

print(todos_animais)

# Questão 21

nomes = ["Ana", "Pedro", "Maria", "João"]

# Questão 22

for nomes in nomes:
    print(nomes)

# Questão 23

nomes_maiusculos = []
for nomes in nomes:
    nomes_maiusculos.append(nomes.upper())
print(nomes_maiusculos)

# Questão 24

lista4 = list(range(1, 21))
for pares in lista4:
    if pares % 2 == 0:
        print(pares)

# Questão 25

lista4_quadrados = []
for quadrado in lista4:
    lista4_quadrados.append(quadrado ** 2)
print(lista4_quadrados)

# Questão 26

palavras = ["python", "java", "c", "javascript"]
for caracteres in palavras:
    print(len(caracteres))

# Questão 27

idades = [12, 18, 25, 40, 60]
for idade in idades:
    if idade >= 18:
        print("Maior de idade")
    else:
        print("Menor de idade")

# Questão 28

notas = [5.5, 7.0, 8.3, 4.9, 6.2]
aprovados = []
reprovados = []
for nota in notas:
    if nota >= 7:
        aprovados.append(nota)
    else:
        reprovados.append(nota)
print(len(aprovados))
print(len(reprovados))

# Questão 29

palavras = ["arara", "banana", "radar", "python"]
for palavra in palavras:
    palavra_invertida = palavra[::-1]
    if palavra == palavra_invertida:
        print(f"A palavra {palavra} é um palíndromo!")
    else:
        print(f"A palavra {palavra} não é um palíndromo!")

# Questão 30

compras = ["arroz", "feijão", "batata", "carne"]
for compra in compras:
    print(f"Preciso comprar: {compra}")

# Questão 31

numero = 1
while numero <= 10: 
    print(numero)
    numero = numero + 1
print("Loop concluído!")

# Questão 32

while True:
    numero_inteiro = int(input("Insira um número!"))
    if numero_inteiro == 0:
        break
    print(f"Você digitou o número {numero_inteiro}. Tente novamente!")
print("Você digitou 0. O programa foi finalizado!")

# Questão 33

soma = 0
numero_atual = 1
while numero_atual <= 100:
    soma = soma + numero_atual
    numero_atual = numero_atual + 1
print(f"A soma dos números de 1 a 100 é igual a: {soma}")

# Questão 34

while True:
    numero_inteiro1 = int(input(print("Insira um número!")))
    if numero_inteiro1 == 7:
        break
    print(f"Você digitou o número {numero_inteiro1}. Tente novamente!")
print("Você digitou 7. O programa foi finalizado!")

# Questão 35

numero = 2
while numero <= 20:
    print(numero)
    numero = numero + 2
print("Loop finalizado!")