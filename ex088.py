#faca um programa que ajude um jogador da mega sena a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
import random
lista = list()
num = int(input('Quantos jogos voce quer que eu sorteie? '))
for c in range(0, num):
    jogos = random.sample(range(1, 61), 6)
    jogos.sort()
    lista.append(jogos)
    print(jogos)
print(lista)