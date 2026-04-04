#Crie um programa onde o usuario possa digitar cinco valores numericos e cadastre-os em uma lista, ja na posicao correta de insercao (sem usar o sort()). No final, mostre a lista ordenada na tela.
numeros = []
for c in range(0, 5):
    n = int(input('Digite um numero: '))
    if c == 0 or n > numeros[-1]:
        numeros.append(n)
        print('Valor adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(numeros):
            if n <= numeros[pos]:
                numeros.insert(pos, n)
                print(f'Valor adicionado na posicao {pos} da lista...')
                break
            pos += 1
print(f'Os valores digitados em ordem crescente sao: {numeros}')
