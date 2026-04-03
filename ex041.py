#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#- até 9 anos: MIRIM
#- até 14 anos: INFANTIL
#- até 19 anos: JUNIOR
#- até 25 anos: SENIOR
#- acima de 25 anos: MASTER
from datetime import datetime
ano = int(input('Digite o ano de nascimento: '))
anoatual = datetime.now().year
idade = anoatual - ano
if idade <= 9:
    print(f'Voce tem {idade} anos, sua categoria é Mirim.')
elif idade <= 14:
    print(f'Voce tem {idade} anos, sua categoria é Infantil.')
elif idade <= 19:
    print(f'Voce tem {idade} anos, sua categoria é Junior.')
elif idade <= 25:
    print(f'Voce tem {idade} anos, sua categoria é Senior.')
else:
    print(f'Voce tem {idade} anos, sua categoria é Master.')