#faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
#- se ele ainda vai se alistar ao serviço militar
#- se é a hora de se alistar
#- se já passou do tempo de alistamento
from datetime import datetime
ano = int(input('qual o seu ano de nascimento?: '))
ano_atual = datetime.now().year
if ano_atual - ano < 18:
    print(f'voce vai precisar se alistar no exercito daqui a {18 - (ano_atual - ano)} anos')
elif ano_atual - ano == 18:
    print('Voce precisa se alistar')
elif ano_atual - ano > 18:
    print(f'voce ja se alistou a {(ano_atual - ano) - 18} anos')

