#crie um programa que tenha uma funcao chamada voto() que vai receber como parametro o ano de nascimento de uma pessoa, retornando um valor literal, indicando se uma pessoa tem o voto, Negado, Opcional ou obrigatorio nas eleicoes. idade < 18 = Negado, 18 < idade < 65 = Obrigatorio, idade > 65 = Opcional.

from datetime import date
anoatual = date.today().year
def voto(ano):
    global anoatual
    idade = anoatual - ano
    if idade < 18:
        return 'Negado'
    if 18 <= idade < 65:
        return 'Obrigatorio'
    if idade >= 65:
        return 'Opcional'


v = int(input('Em que ano voce nasceu? '))
t = voto(v)

print(f'Com {anoatual - v} anos: Voto é {t}')