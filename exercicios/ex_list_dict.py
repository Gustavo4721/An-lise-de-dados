# Questão 1

faturamento = [
    {'dia': 'segunda', 'valor': 1200},
    {'dia': 'terça', 'valor': 1500},
    {'dia': 'quarta', 'valor': 900},
    {'dia': 'quinta', 'valor': 1800},
    {'dia': 'sexta', 'valor': 2400}
]

## Questão 1.1

faturamento_total = 0

for venda_diaria in faturamento:
    faturamento_total = faturamento_total + venda_diaria['valor']

print(f'O faturamento total da semana foi de: R${faturamento_total}')

## Questão 1.2

maior_valor = 0
dia_maior_valor = ''

for dia in faturamento:
    if venda_diaria['valor'] > maior_valor:
        maior_valor = venda_diaria['valor']
        dia_maior_valor = venda_diaria['dia']

print(f'O dia de maior faturamento foi {dia_maior_valor} com R${maior_valor}')

## Questão 1.3

quantidade_de_dias = 0

for dia in faturamento:
    quantidade_de_dias = quantidade_de_dias + 1

media_de_vendas = faturamento_total / quantidade_de_dias

print(f'A média de vendas por dia é de R${media_de_vendas}')

# Questão 2

estoque = {
    'notebook': [5, 7, 3],
    'mouse': [20, 25, 18],
    'teclado': [12, 14, 9]
}

## Questão 2.1

for produto, quantidade in estoque.items():
    estoque_total = sum(quantidade)
    print(f'{produto}: {estoque_total}')

## Questão 2.2

menor_estoque = float('inf')
produto_menor_estoque = ''

for produto, quantidade in estoque.items():
    estoque_total = sum(quantidade)
    if estoque_total < menor_estoque:
        menor_estoque = estoque_total
        produto_menor_estoque = produto

print(f'O produto com menor estoque é o {produto_menor_estoque} com {menor_estoque} unidades')

# Questão 2.3

estoques_totais = {}

for produto, quantidade in estoque.items():
    estoque_total = sum(quantidade)
    estoques_totais[estoque_total] = estoque_total

# Questão 3

funcionarios = [
    {'nome': 'Ana', 'salario': 4500, 'departamento': 'RH'},
    {'nome': 'Carlos', 'salario': 7000, 'departamento': 'TI'},
    {'nome': 'Beatriz', 'salario': 5200, 'departamento': 'Financeiro'},
    {'nome': 'João', 'salario': 4800, 'departamento': 'TI'}
]

## Questão 3.1

salario_total = 0

for salario_individual in funcionarios:
    salario_total = salario_total + salario_individual['salario']

print(f'A folha salarial total da empresa é: {salario_total}')

## Questão 3.2

maior_salario = 0
funcionario_maior_salario = ''

for funcionarios in funcionarios:
    if funcionarios['salario'] > maior_salario:
        maior_salario = funcionarios['salario']
        funcionario_maior_salario = funcionarios['nome']

print(f'O funcionário que ganha mais é o(a) {funcionario_maior_salario} com um salário de R${maior_salario}')

## Questão 3.3

salarios_por_departamento = {}

for funcionario in funcionarios:
    departamento = funcionario['departamento']
    salario = funcionario['salario']
    if departamento in salarios_por_departamento:
        salarios_por_departamento[departamento] = salarios_por_departamento[departamento] + salario
    else:
        salarios_por_departamento[departamento] = salario

print(salarios_por_departamento)

# Questão 4

avaliacoes = {
    'loja A': [8, 9, 7, 10, 6],
    'loja B': [5, 7, 6, 8, 7],
    'loja C': [9, 8, 9, 10, 9]
}

## Questão 4.1

for loja, notas in avaliacoes.items():
    media_de_satisfacao = sum(notas) / len(notas)
    print(f'A média de satisfação da {loja} é {media_de_satisfacao}')

## Questão 4.2

maior_media = 0
loja_maior_media = ''

for loja, notas in avaliacoes.items():
    media_de_satisfacao = sum(notas) / len(notas)
    if media_de_satisfacao > maior_media:
        maior_media = media_de_satisfacao
        loja_maior_media = loja

print(f'A loja que tem a maior média de satisfação é a {loja_maior_media} com {media_de_satisfacao}')

## Questão 4.3

medias_das_lojas = {}

for loja, notas in avaliacoes.items():
    media_de_satisfacao = sum(notas) / len(notas)
    medias_das_lojas[loja] = media_de_satisfacao

print(medias_das_lojas)

# Questão 5

vendas = [
    {'vendedor': 'Marcos', 'itens': {'notebook': 2, 'mouse': 5}},
    {'vendedor': 'Lucia', 'itens': {'notebook': 1, 'teclado': 3}},
    {'vendedor': 'Paula,', 'itens': {'mouse': 4, 'teclado': 2}}
]

## Questão 5.1

total_notebooks = 0

for venda in vendas:
    itens_vendidos = venda['itens']
    if 'notebook' in itens_vendidos:
        numero_notebooks = itens_vendidos['notebook']
        total_notebooks = total_notebooks + numero_notebooks

print(f'Foram vendidos {total_notebooks} notebooks no total')

## Questão 5.2

maior_venda = 0
vendedor_mais_vendas = ''

for venda in vendas:
    itens_vendidos = venda['itens']
    vendedor = venda['vendedor']
    soma_itens = sum(itens_vendidos.values())
    if soma_itens > maior_venda:
        maior_venda = soma_itens
        vendedor_mais_vendas = vendedor

print(f'O vendedor com mais vendas é o {vendedor_mais_vendas} com {maior_venda}')

## Questão 5.3

total_por_produto = {}
soma_quantidade = 0

for venda in vendas:
    itens_vendidos = venda['itens']
    for produto, quantidade in itens_vendidos.items():
        if produto in total_por_produto:
            total_por_produto[produto] = total_por_produto[produto] + quantidade
        else:
            total_por_produto[produto] = quantidade

print(total_por_produto)

## Questão 6

produtos = [
    {'nome': 'Notebook', 'preço': 3500},
    {'nome': 'Mouse', 'preço': 80},
    {'nome': 'Teclado', 'preço': 150},
    {'nome': 'Cadeira', 'preço': 900}
]

produtos_classificados = {}

for produto in produtos:
    nome = produto['nome']
    preco = produto['preço']
    if preco <= 100:
        produtos_classificados[nome] = 'barato'
    elif preco >= 101 and preco <= 1000:
        produtos_classificados[nome] = 'médio'
    else:
        produtos_classificados[nome] = 'caro'

print(produtos_classificados)

## Questão 7

funcionarios = [
    {'nome': 'Ana', 'nota': 9},
    {'nome': 'Carlos', 'nota': 6},
    {'nome': 'Beatriz', 'nota': 4},
    {'nome': 'João', 'nota': 7}
]

funcionarios_classificados = {}

for funcionario in funcionarios:
    nome = funcionario['nome']
    nota = funcionario['nota']
    if nota >= 8:
        funcionarios_classificados[nome] = 'Excelente'
    elif nota >= 5 and nota <= 7:
        funcionarios_classificados[nome] = 'Regular'
    else:
        funcionarios_classificados[nome] = 'Precisa melhorar'

print(funcionarios_classificados)

## Questão 8

estoque = {
    'notebook': 3,
    'mouse': 25,
    'teclado': 8,
    'monitor': 2
}

for nome, quantidade in estoque.items():
    if quantidade < 5:
        print(f'{nome}: Estoque crítico')
    elif quantidade >= 5 and quantidade < 10:
        print(f'{nome}: Estoque baixo')
    else:
        print(f'{nome}: Estoque adequado')

## Questão 9

vendas = [
    {'regiao': 'Sul', 'valor': 12000},
    {'regiao': 'Norte', 'valor': 8000},
    {'regiao': 'Sudeste', 'valor': 20000},
    {'regiao': 'Centro-Oeste', 'valor': 5000}
]

regiao_situacao = {}

for venda in vendas:
    regiao = venda['regiao']
    valor = venda['valor']
    if valor >= 10000:
        regiao_situacao[regiao] = 'Meta atingida'
    else:
        regiao_situacao[regiao] = 'Meta não atingida'

vendas_classificadas = [regiao_situacao]
print(vendas_classificadas)

## Questão 10

compras = [
    {'cliente': 'Maria', 'valor': 450},
    {'cliente': 'José', 'valor': 1200},
    {'cliente': 'Clara', 'valor': 3000}
]

cliente_desconto = {}

for compra in compras:
    cliente = compra['cliente']
    valor = compra['valor']
    if valor < 500:
        desconto = valor * 0.05
        valor_final = valor - desconto
        informacoes = {
            'valor': valor,
            'desconto': desconto,
            'valor final': valor_final
        }
        cliente_desconto[cliente] = informacoes
    elif valor >= 500 and valor < 2000:
        desconto = valor * 0.1
        valor_final = valor - desconto
        informacoes = {
            'valor': valor,
            'desconto': desconto,
            'valor final': valor_final
        }
        cliente_desconto[cliente] = informacoes
    else:
        desconto = valor * 0.15
        valor_final = valor - desconto
        informacoes = {
            'valor': valor,
            'desconto': desconto,
            'valor final': valor_final
        }
        cliente_desconto[cliente] = informacoes

print(cliente_desconto)

lista = [1, 'maca', 3]

lista.pop(1)

print(lista)