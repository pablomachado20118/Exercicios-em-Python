#faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        break
    print(f'{num} x 1 = {num * 1}\n{num} x 2 = {num * 2}\n{num} x 3 = {num * 3}\n{num} x 4 = {num * 4}\n{num} x 5 = {num * 5}\n{num} x 6 = {num * 6}\n{num} x 7 = {num * 7}\n{num} x 8 = {num * 8}\n{num} x 9 = {num * 9}\n{num} x 10 = {num * 10}')