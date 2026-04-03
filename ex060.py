#Faça um programa que leia um numero qualquer e mostre o seu fatorial.
num = int(input('Digite um numero: '))
valor = num
print(num, end=' ')
while num != 1:
    num -= 1
    valor *= num
    print(f'x {num} ', end='')
print(f'= {valor}')
