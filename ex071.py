#crie um programa que simule o funcionamento de um caixa eletronico. no inicio pergunte ao usuario qual sera o valor a ser sacado (numero inteiro) e o programa vai 
# informar quantas cedulas de cada valor serao entregues. obs: considere que o caixa possui cedulas de 50, 20, 10 e 1 real.
print('Bem vindo a caixa')
valor = int(input('Qual o valor voce quer sacar? R$ '))
valor50 = valor // 50
sobra50 = valor % 50
valor20 = sobra50 // 20
sobra20 = sobra50 % 20
valor10 = sobra20 // 10
sobra10 = sobra20 % 10
valor1 = sobra10 // 1
print(f'Total de {valor50} cedulas de R$50\nTotal de {valor20} cedulas de R$20\nTotal de {valor10} cedulas de R$10\nTotal de {valor1} cedulas de R$1')