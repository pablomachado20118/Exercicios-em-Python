#crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) Qual é o total gasto na compra.
#B) Quantos produtos custam mais de R$ 1000.
#C) Qual é o nome do produto mais barato.
valor = soma = maior = contador = nomemenor = 0
while True:
    nome = str(input('Digite o nome do produto: '))
    valor = float(input('Digite o valor do produto: '))
    soma += valor
    contador += 1
    if contador == 1:
        menor = valor
        nomemenor = nome
    if valor < menor:
        menor = valor
        nomemenor = nome
    if valor > 1000:
        maior += 1
    opcao = str(input('Quer continuar? [S/N] ')).upper()
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).upper()
    if opcao == 'N':
        break
print(f'Operacao finalizada! \nO total gasto foi {soma}\n{maior} produtos foram mais caros que R$ 1000 reais\nO {nomemenor} foi o produto mais barato comprado, custando R${menor:.2f}')