#crie um programa que leia varios numeros inteiros pelo teclado. No final da execução, mostre a media entre todos os valores e qual foi o maior e o menor valor digitado. O programa deve perguntar se o usuario quer ou nao continuar a digitar valores.
resposta = 'S'
contador = 0
soma = 0
maior = 0
menor = 1000
while resposta == 'S':
    num1 = int(input('Digite um numero: '))
    contador += 1
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    soma += num1
    if num1 > maior:
        maior = num1
    if num1 < menor:
        menor = num1
print(f'Voce digitou {contador} numeros, e a media deles é {soma/contador}')
print(f'O maior numero foi {maior}, e o menor foi {menor}')