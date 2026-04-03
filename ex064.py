#crie um programa que leia varios numeros inteiros pelo teclado. o programa so vai parar quando o usuario digitar 999, que é a condição de parada. no final mostre quantos numeros foram digitados e qual foi a soma entre eles (desconsiderando o flag)
contador = -1
num = 0
num1 = 0
while num != 999:
    contador += 1
    num = int(input('Digite um numero [999 para parar]: '))
    if num != 999:
        num1 += num
print(f'voce digitou {contador} numeros e a soma entre eles é {num1}')