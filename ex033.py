# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
num1 = float(input('Digite um numero: '))
num2 = float(input('Digte outro numero: '))
num3 = float(input('Digite o ultimo numero: '))
if num1 > num2 > num3:
    print(f'O maior numero é o {num1} e o menor é o {num3}')
if num1 > num3 > num2:
    print(f'O maior numero é o {num1} e o menor é o {num2}')
if num2 > num1 > num3:
    print(f'O maior numero é o {num2} e o menor é o {num3}')
if num2 > num3 > num1:
    print(f'O maior numero é o {num2} e o menor é o {num1}')
if num3 > num1 > num2:
    print(f'O maior numero é o {num3} e o menor é o {num2}')
if num3 > num2 > num1:
    print(f'O maior numero é o {num3} e o menor é o {num1}')
if num3 == num2 == num1:
    print(f'O maior numero é o {num3} e o menor é o {num1}')