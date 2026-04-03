#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário  
# tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
from time import sleep

num = random.randint(0, 5)
print('Vou pensar em um numero entre 0 e 5.Tente adivinhar...')
escolhido = int(input('Escolha um numero de 0 a 5: '))
print('PROCESSANDO...')
sleep(1)
print(f'eu escolhi {num} voce escolheu o numero {escolhido}')
print('Parabens! Voce acertou' if escolhido == num else 'Que pena! voce errou')


