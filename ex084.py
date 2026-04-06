#faca um programa que leia nome e peso de varias pessoas, guardando tudo em uma lista. No final mostre:
#A) Quantas pessoas foram cadastradas
#B) Uma listagem com as pessoas que pesam mais de 100kg
#C) Uma listagem com as pessoas que pesam menos de 70kg
lista = list()
dados = []
listaleve = list()
listapesada = list()
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    lista.append(dados[:])
    resposta = str(input('Quer continuar? [S/N} ')).strip().upper()
    if dados[1] <= 70:
        listaleve.append(dados[0])
    elif dados[1] >= 100:
        listapesada.append(dados[0])
    dados.clear()
    if resposta == 'N':
        break
print('_' * 30)
print(f'Foram cadastradas {len(lista)} pessoas.')
print(f'as pessoas que pesam menos de 70kg sao {listaleve}')
print(f'as pessoas que pesam mais de 100kg sao {listapesada}')