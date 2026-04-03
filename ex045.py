#Crie um programa que faça o computador jogar Jokenpô com você.
import random
jogo = ['pedra', 'papel', 'tesoura']
cpu = random.choice(jogo)
player = input('Jokenpo(pedra/papel/tesoura): ').lower()

if cpu == 'pedra':
    if player == 'papel':
        print(f'Voce ganhou da maquina, ela escolheu {cpu} e voce {player}.')
    elif player == 'tesoura':
        print(f'Voce perdeu, ela escolheu {cpu} e voce {player}.')
    elif player == 'pedra':
        print(f'voces empataram, os dois escolheram {cpu}')
elif cpu == 'papel':
    if player == 'tesoura':
        print(f'Voce ganhou da maquina, ela escolheu {cpu} e voce {player}.')
    elif player == 'pedra':
        print(f'Voce perdeu, ela escolheu {cpu} e voce {player}.')
    elif player == 'papel':
        print(f'voces empataram, os dois escolheram {cpu}')
elif cpu == 'tesoura':
    if player == 'pedra':
        print(f'Voce ganhou da maquina, ela escolheu {cpu} e voce {player}.')
    elif player == 'papel':
        print(f'Voce perdeu, ela escolheu {cpu} e voce {player}.')
    elif player == 'tesoura':
        print(f'voces empataram, os dois escolheram {cpu}')