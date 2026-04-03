#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
num3 = int(input('Digite outro numero: '))
num4 = int(input('Digite outro numero: '))
num5 = int(input('Digite outro numero: '))
num6 = int(input('Digite outro numero: '))
if num1 % 2 == 1:
    num1 = 0
if num2 % 2 == 1:
    num2 = 0
if num3 % 2 == 1:
    num3 = 0
if num4 % 2 == 1:
    num4 = 0
if num5 % 2 == 1:
    num5 = 0
if num6 % 2 == 1:
    num6 = 0
soma = num1 + num2 + num3 + num4 + num5 + num6
print(soma)