#faca um programa que leia um numero inteiro e mostre se ele é ou não um numero primo.
num = int(input('digite um numero: '))
divisores = 0
for c in range(1 , num + 1):
    if num % c == 0:
        divisores += 1
if divisores == 2:
    print('O numero {} é primo pq tem {} divisores'.format(num, divisores))
else:
    print('O numero {} não é primo pq tem {} divisores'.format(num, divisores))