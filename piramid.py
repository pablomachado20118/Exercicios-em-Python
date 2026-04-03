#Um desafio que vi na internet e achei legal
num = int(input('Digite qual vai ser a base da piramide: '))
for i in range(1, num + 1):
    print(' ' * (num - i) + '*' * (2 * i - 1))