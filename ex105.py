#faca um programa que tenha uma funcao notas() que pode receber varias notas de alunos e vai retornar um dicionario com as seguintes informacoes.
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - a media da turma
# - a Situacao(opcional). media < 6 = ruim. 6 <= media <= 7 = Razoavel. Media > 7 = Boa

def notas(* num, sit= False):
    maior = menor = soma = 0
    total = len(num)
    for c,valor in enumerate(num):
        if c == 0:
            soma += valor
            maior = valor
            menor = valor
        else:
            soma += valor
            if valor > maior:
                maior = valor
            if valor < menor:
                menor = valor
        media = soma / total
        if media < 6:
            situacao = 'ruim'
        if 6 <= media <= 7:
            situacao = 'razoavel'
        if media > 7:
            situacao = 'boa'
    if sit == False:
        return {f'Total':{total},'menor':{menor},'Maior':{maior},'Media':{media}}
    else:
        return {f'Total':{total},'menor':{menor},'Maior':{maior},'Media':{media}, 'Situacao':{situacao}}

1


    

resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)