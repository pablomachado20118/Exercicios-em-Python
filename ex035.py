#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
num1 = float(input('Digite um numero: '))
num2 = float(input('Digite outro numero: '))
num3 = float(input('Digite o ultimo numero: '))
if num1 + num2 > num3:
    if num1 + num3 > num2:
        if num3 + num2 > num1:
            print(f'os numeros {num1}, {num2} e {num3} podem formar um triangulo!')
        else:
            print(f'Os numeros {num1},{num2} e {num3} nao podem formar um triangulo!')
    else:
        print(f'Os numeros {num1},{num2} e {num2} nao podem formar um triangulo!')
else:
    print(f'Os numeros {num1},{num2} e {num2} nao podem formar um triangulo!')