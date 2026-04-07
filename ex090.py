#faca um programa que leia nome e media de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
aluno = {}
aluno['nome'] = str(input('Nome: ')).strip()
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif aluno['media'] < 7:
    aluno['situacao'] = 'Reprovado'
print('-'*30)
for c, i in aluno.items():
    print(f'{c} é igual a {i}')
