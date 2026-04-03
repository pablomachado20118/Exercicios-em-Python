#crie um programa que simule o funcionamento de um caixa eletronico. no inicio pergunte ao usuario qual sera o valor a ser sacado (numero inteiro) e o programa vai 
# informar quantas cedulas de cada valor serao entregues. obs: considere que o caixa possui cedulas de 50, 20, 10 e 1 real.
valor = int(input('Que valor voce quer sacar? R$'))
total = valor
cedula = 50
totalcedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totalcedula += 1
    else:
        print(f'Total de {totalcedula} cedulas de R${cedula}')
        totalcedula = 0
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        if total == 0:
            break