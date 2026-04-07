#crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
jogadores = {}
for c in range(1, 5):
    jogador = randint(1, 6)
    print(f'O jogador {c} tirou {jogador} no dado.')
    jogadores[f'jogador{c}'] = jogador
ordenado = dict(sorted(jogadores.items(), key=lambda item: item[1], reverse=True))
print('-='*20)
print('Ranking dos jogadores:')
for i, v in enumerate(ordenado.items()):
    print(f'{i+1}º lugar: {v[0]} com {v[1]} no dado.')