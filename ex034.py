#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do aumento. Para salários superiores a R$ 1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Qual o seu salario?: '))
if salario > 1250:
    print(f'O seu salario de R${salario}, foi para R${salario * 1.1}')
else:
    print(f'O seu salario de R${salario}, foi para R${salario * 1.15}')