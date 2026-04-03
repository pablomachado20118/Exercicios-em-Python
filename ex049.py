#refaca o desafio 009, mostrando a tabuada de um numero que o usuario escolher, so que agora utilizando um laço for.
num = int(input('Digite um numero: '))
for c in range(0, 11):
    print('{} x {} = {}'.format(num, c, num * c))
