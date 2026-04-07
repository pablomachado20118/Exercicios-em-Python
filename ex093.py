#crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
futebol = {}
total = 0
futebol['Nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {futebol["Nome"]} jogou? '))
for c in range(1, partidas + 1):
    gols = int(input(f'Quantos gols na partida {c}? '))
    futebol[f'Partida {c}'] = gols
    total += gols
futebol['Total'] = total
print(futebol)
print(f'O jogador {futebol["Nome"]} jogou  {partidas} partidas')
for c in range(1, partidas + 1):
    print(f'    Na partida {c} fez  {futebol[f"Partida {c}"]} gols')
print(f'Foi um total de {futebol["Total"]} gols')
