#O Mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. 
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
al1 = ('akaza')
al2 = 'toji'
al3 = 'guts'
al4 = 'musashi'
al0 = (random.sample([al1,al2,al3,al4],k=4))
print(f'A ordem de apresentacao dos trabalhos é {al0}')