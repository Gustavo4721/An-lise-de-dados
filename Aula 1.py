# Variáveis

nome = "Gustavo"
idade = 19
curso = "Administração"

# Lista

lista = [nome, idade, curso]
print(lista[0])

## Loop

lista_mista = ["cavalo", "pato", 16, 17]
animal = []
numero = []

for item in lista_mista:
    if type(item) == str:
        animal.append(item)
    if type(item) == int:
        numero.append(item)

print(animal)
print(numero)

## While

# Dicionário

dict_mista = {
    "animal": "cavalo",
    1: "pato",
    2: 16,
    3: 17
}

print(dict_mista["animal"])