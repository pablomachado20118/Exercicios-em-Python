#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
ano = int(input('Digite um ano qualquer: '))
if ano % 100 == 0:
    print('Ano bixsexto' if ano % 400 == 0 else 'Nao é ano bixsexto')
if ano % 4 == 0:
    print('Ano bixsexto') if ano % 100 != 0 else print('')