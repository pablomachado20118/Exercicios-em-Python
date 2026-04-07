#crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule a idade do trabalhador e quantos anos ele tem para se aposentar. 35 anos de colaboracao
from datetime import date
dados = {}
dados['Nome'] = str(input('Nome: '))
dados['Idade'] = date.today().year - int(input('Ano de nascimento: '))
dados['ctps'] = int(input('Carteira de Trabalho (0 se não tiver): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: '))
    dados['aposentadoria'] = (dados['contratação'] + 35) - date.today().year
print('-='*30)
for c, i in dados.items():
    print(f'{c} tem o valor {i}')