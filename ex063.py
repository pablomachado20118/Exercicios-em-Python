#escreva um programa que leia um numero inteiro e mostre os n primeiros elementos de uma sequencia de fibonacci
contador = 0
num = int(input('Digite um numero inteiro:'))
num1 = 0
num2 = 1
print(num1)
print(num2)
while num >= 3:
    soma = num1 + num2
    print(soma)
    num -= 1
    contador += 1
    if contador % 2 == 0:
        num2 = soma
    elif contador % 2 == 1:
        num1 = soma
