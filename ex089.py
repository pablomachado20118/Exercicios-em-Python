#crie um porgrama que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta. No final mostre um boletim contendo a media de cada um e permita que o usuario possa mostrar as notas de cada aluno individualmente.
listona = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    listona.append([nome, [nota1, nota2], media])
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resposta == 'N':
        break
print('No.  NOME                MEDIA')
print('_' * 30)
for c in range(0, len(listona)):
    print(f'{c} - {listona[c][0]:<20} - {listona[c][2]}')
while True:
    opcao = int(input('Mostrar notas de qual aluno? (999 para parar) '))
    if opcao == 999:
        print('FINALIZANDO O PROGRAMA...')
        break
    else:
        print(f'Notas de {listona[opcao][0]} são {listona[opcao][1]}')