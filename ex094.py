#Crie um programa que eia nome, sexo e idade de varias pessoas, guardando os dados  de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas
#B) A média de idade do grupo
#C) Uma lista com todas as mulheres
#D) Uma lista com todas as pessoas com idade acima da média
Pessoas = {}
grupo = []
idade = 0
while True:
    Pessoas['Nome'] = str(input('Nome: ')).strip()
    Pessoas['Sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
    Pessoas['Idade'] = int(input('Idade: '))
    grupo.append(Pessoas.copy())
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resposta == 'N':
        break
print(f'  -  O Grupo tem {len(grupo)} pessoas.')
for i in grupo:
    idade += i['Idade']
print(f'  -  A média de idade do grupo é {idade/len(grupo):.2f} anos.')
print(f'  -  As mulheres cadastradas foram:', end='')
for m in grupo:
    if m['Sexo'] == 'F':
        print(f' {m["Nome"]}', end=' ')
print(f'\n  -  As pessoas com idade acima da média são:', end='')
for i in grupo:
    if i['Idade'] > idade/len(grupo):
        print(f' {i["Nome"]}', end=' ')
