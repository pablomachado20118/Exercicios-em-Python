#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais
num1 = int(input('Digite um numero inteiro: '))
num2 = int(input('Digite outro numero inteiro: '))
if num1 > num2:
    print(f'O primeiro numero {num1} é o maior')
elif num2 > num1:
    print(f'O segundo valor {num2} é o maior')
elif num1 == num2:
    print('nao existe valor maior,os dois sao iguail')
