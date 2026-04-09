#Faca um programa que tenha uma funcao chama ficha(), que receba dois parametros opcionais:o nome de um jogar e quantos gols ele marcou.
#O programa devera ser capaz de mostrar a ficha do jogador, mesmo que algum dado nao tenha sido informado corretamente.
def ficha(nome=0, gols=0):
    global no
    global go
    no = go = 0
    if nome == '':
        no = '<desconhecido>'
    else:
        no = nome
    if gols == '':
        go = 0
    else:
        go = gols
    return (no , go)

nome = (input('Nome do Jogador: '))
gols = (input('Numero de Gols: '))
ficha(nome, gols)
print(f'O Jogador {no} fez {go} gol(s) no campeonato.')

