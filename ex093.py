#crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
futebol = {}
futebol['Nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {futebol["Nome"]} jogou? '))
for c in range(1, partidas + 1):
    futebol[f'partida{c}'] = int(input(f'Quantos gols na partida {c}? '))
