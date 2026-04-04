#Faca um programa que leia 5 valores numericos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posicoes na lista.
numeros = [int(input('Digite um valor para a posicao 0: ')),
           int(input('Digite um valor para a posicao 1: ')),
           int(input('Digite um valor para a posicao 2: ')),
           int(input('Digite um valor para a posicao 3: ')),
           int(input('Digite um valor para a posicao 4: '))]
print(f'Voce digitou os valores {numeros}')
print(f'O maior valor digitado foi {max(numeros)} nas posicoes ', end='')
for i, v in enumerate(numeros):
    if v == max(numeros):
        print(f'{i}... ', end='')
print(f'\nO menor valor digitado foi {min(numeros)} nas posicoes ', end='')
for i, v in enumerate(numeros):
    if v == min(numeros):
        print(f'{i}... ', end='')