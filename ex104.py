#crie um programa que tenha a funcao leiaInt(), que vai funcionar de forma semelhante a funcao input() do Python, só que fazendo a validacão para a ceitar apenas um valor numerico.


def leiaInt(num):
    while True:
        if num.isnumeric() == True:
            return f'Voce acabou de digitar o numero {num}'
        else:
            print('ERRO! Digite um numero inteiro valido')
            return leiaInt(input('Digite um numero: '))



c = leiaInt(input('Digite um numero: '))
print(c)