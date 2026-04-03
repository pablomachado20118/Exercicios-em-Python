#desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
num1 = int(input("Digite o primeiro termo: "))
num2 = int(input('digite a razao: '))
for c in range(num1, num1 + (num2 * 10), num2):
    print(c)