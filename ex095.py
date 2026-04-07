#Aprimore o desafia  093 para  que ele funciona com varios jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
jogador = {}
jogadores = []
gols = []
while True:
    jogador['Nome'] = str(input('Nome do jogador: ')).strip()
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    for p in range(1, partidas + 1):
        gols.append(int(input(f'Quantos gols na partida {p}? ')))
        jogador['Gols'] = gols[:]
        jogador['Total'] = sum(gols)
    jogadores.append(jogador.copy())
    jogador.clear()
    gols.clear()
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resposta == 'N':
        break
print(jogadores)
print('-' * 40)
print(f'{"cod":>3} {"Nome":<10} {"gols":>8} {"total":>8}')
print('-' * 40)
for i, j in enumerate(jogadores):
    print(f'{i:>3} {j["Nome"]:<10} {str(j["Gols"]):>8} {j["Total"]:>8}')
print('-' * 40)
while True:
    busca = int(input('Mostrar  dados de  qual jogardor? (999 para parar) '))
    if busca == 999:
        break
    if  busca >= len(jogadores):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[busca]["Nome"]}:')
        for i, g in enumerate(jogadores[busca]['Gols']):
            print(f'    No jogo {i + 1} fez {g} gols.')

