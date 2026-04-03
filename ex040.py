#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#- média abaixo de 5.0: REPROVADO
#- média entre 5.0 e 6.9: RECUPERAÇÃO
#- média 7.0 ou superior: APROVADO
nota = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
medio = (nota + nota2) / 2
if medio >= 7:
    print(f'sua media ficou {medio}, Parabens! voce foi aprovado.')
elif medio >= 5:
    print(f'sua media ficou {medio},voce ficou de recuperacao.')
elif medio <= 5:
    print(f'Sua media ficou {medio}, voce ficou reprovado.')