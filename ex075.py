#desenvolva um programa que leia quatro numeros pelo teclado e guarde-os em uma tupla. no final, mostre:
# a) quantas vezes apareceu o valor 9
# b) em que posicao foi digitado o primeiro valor 3
# c) quais foram os numeros pares
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
num3 = int(input('Digite mais um numero: '))
num4 = int(input('Digite o ultimo numero: '))
par = 0
tupla = (num1, num2, num3, num4)
os9 = tupla.count(9)
for c in tupla:
    if c % 2 == 0:
        par += 1

print(f'O numero 9 apareceu {os9} vezes')
if 3 in tupla:
    print(f'O primeiro numero 3 apareceu na posicao {tupla.index(3) + 1}')
else:
    print('O valor 3 nao for encontrado!!')
print(f'Os valores pares digitados foram {par}')