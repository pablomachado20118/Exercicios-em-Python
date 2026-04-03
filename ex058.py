#Melhore o jogo do desafio 028 onde o computador vai pensar em um numero entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
import random
num = 0
vezes = 0
cpu = random.randint(1,10)
print('Sou seu computador...')
print('Acabei de pensar em um numero entre 1 e 10')
print('sera que voce consegue adivinhar qual foi?')
while num != cpu:
    num = int(input('Qual seu palpite? ' ))
    if num > cpu:
        print('Menos... tente mais uma vez')
    elif num < cpu:
        print('Mais... tente mais uma vez')
    vezes += 1
print(f'Acertou com {vezes} tentativas. Parabens!')