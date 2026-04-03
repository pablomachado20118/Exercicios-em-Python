#Desenvolva um programa que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso Ideal
# - Entre 25 e 30: Sobrepeso
# - Entre 30 e 40: Obesidade
# - Acima de 40: Obesidade Mórbida
peso = float(input('Qual o seu peso?'))
altura = float(input('Qual a sua altura?'))
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f'Seu imc é {imc:.1f}, esta abaixo do peso.')
elif imc >= 18.5 and imc <= 25:
    print(f'Seu imc é {imc:.1f},esta com seu peso ideal')
elif imc >= 25 and imc <= 30:
    print(f'Seu imc é {imc:.1f}, esta com sobrepeso')
elif imc >= 30 and imc <= 40:
    print(f'Seu imc é {imc:.1f}, esta com obesidade')
elif imc > 40:
    print(f'seu imc é {imc:.1f}, voce esta co obesidade morbida')