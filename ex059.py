#crie um programa que leia dois numeros e mostre um menu na tela:
#[1] somar
#[2] multiplicar
#[3] maior
#[4] novos numeros
#[5] sair do programa
c = 4
while c == 4:
    num1 = int(input('Digite um numero: '))
    num2 = int(input('Digite outro numero: '))
    print('[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos numeros \n[5] Sair do programa')
    c = int(input('Qual a sua opcao: '))
    if c == 1:
        print(f'a soma dos numeros {num1} e {num2} é {num1+num2}')
    if c == 2:
        print(f'A multiplicacao entre {num1} e {num2} é igual a {num1*num2}')
    if c == 3:
        if num1 > num2:
            print(f'O maior numero é o {num1}')
        elif num1 < num2:
            print(f'O maior numero é o {num2}')
print('Fim do programa')