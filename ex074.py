#crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla. depois disso, mostre a listagem de numeros gerados
#  e indique o menor e o maior valor que estão na tupla.
from random import randint
menor = maior = 0
num = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print(f'Os valores sorteados foram: {num}')
for c in range(0,5):
    if c == 1:
        menor = maior = num[c]
    else:
        if num[c] < menor:
            menor = num[c]
        elif num[c] > maior:
            maior = num[c]
print(f'O maior numero sorteado foi {maior}')
print(f'O menor numero sorteado foi {menor}')

