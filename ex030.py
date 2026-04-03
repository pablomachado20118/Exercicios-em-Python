#Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar.
num = int(input('Digite um numero inteiro: '))
if num % 2 == 0:
    print(f'Voce digitou o numero {num}, um numero par')
else:
    print(f"voce digitou o numero {num}, um numero impar")