#crie um programa que simule o funcionamento de um caixa eletronico. no inicio pergunte ao usuario qual sera o valor a ser sacado (numero inteiro) e o programa vai 
# informar quantas cedulas de cada valor serao entregues. obs: considere que o caixa possui cedulas de 50, 20, 10 e 1 real.
valor = int(input("Quanto você quer sacar? R$"))

for cedula in [50, 20, 10, 1]:
    quantidade = valor // cedula
    valor %= cedula
    if quantidade > 0:
        print(f"{quantidade} cédula(s) de R${cedula}")