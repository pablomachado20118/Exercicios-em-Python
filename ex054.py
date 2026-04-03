#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
ano1 = int(input('digite o ano de nascimento: '))
ano2 = int(input('digite o ano de nascimento: '))
ano3 = int(input('digite o ano de nascimento: '))
ano4 = int(input('digite o ano de nascimento: '))
ano5 = int(input('digite o ano de nascimento: '))
ano6 = int(input('digite o ano de nascimento: '))
ano7 = int(input('digite o ano de nascimento: '))
if ano1 < 2005:
    ano1 = 1
else:
    ano1 = 0
if ano2 < 2005:
    ano2 = 1
else:
    ano2 = 0
if ano3 < 2005:
    ano3 = 1
else:
    ano3 = 0
if ano4 < 2005:
    ano4 = 1
else:
    ano4 = 0
if ano5 < 2005:
    ano5 = 1
else:
    ano5 = 0
if ano6 < 2005:
    ano6 = 1
else:
    ano6 = 0
if ano7 < 2005:
    ano7 = 1
else:
    ano7 = 0
soma = ano1 + ano2 + ano3 + ano4 + ano5 + ano6 +ano7
somaa = 7 - soma
print(f'No total {soma} ja sao maiores de 21 anos e {somaa} sao menores')