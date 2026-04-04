#Crie um programa onde o usuario posso digitar varios valores numericos e cadastre-os em uma lista. Caso o numero ja exista la dentro, ele nao sera adicionado. No final, serao exibidos todos os valores unicos digitados, em ordem crescente.
numeros = []
while True:
    n = int(input('Digite um numero: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Nao vou adicionar...')
    r = str(input('Quer continuar? [S/N] ')).strip().upper()
    if r == 'N':
        break
numeros.sort()
print(f'Os valores digitados em ordem crescente sao: {numeros}')