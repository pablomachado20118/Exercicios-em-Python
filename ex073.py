#crie uma tupla com os 20 primeiros colocados do campeonato brasileiro de futebol, na ordem de colocação. depois mostre:
# a) os 5 primeiros times
# b) os 4 ultimos times
# c) times em ordem alfabetica
# d) em que posicao esta o time da chapecoense
# feito em 01/04/2026
tabela = ('Palmeiras','Athletico Paranaense','São Paulo','Fluminense','Flamengo','Bahia','Coritiba SAF','Grêmio','Vasco da Gama Saf','Vitória','Corinthians','Internacional','Atlético Mineiro','Red Bull Bragantino','Chapecoense','Santos Fc','Mirassol','Remo','Cruzeiro')
print('='*50)
print(f'Lista de times do Brasileirão: {tabela}')
print('='*50)
print(f'Os 5 primeiros são : {tabela[0:5]}')
print('='*50)
print(f'Os 4 ultimos são : {tabela[-4:]}')
print('='*50)
print(f'Times em ordem alfabetica: {sorted(tabela)}')
print('='*50)
print(f'O Chapecoense está na {tabela.index('Chapecoense')} posicao.')
print('='*50)