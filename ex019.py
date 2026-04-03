#Um professor quer sortear um dois seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
import random
al1 = input('qual o nome do primeiro aluno? ')
al2 = input('qual o nome do segundo aluno? ')
al3 = input('qual o nome do terceiro aluno? ')
al4 = input('qual o nome do quarto aluno? ')
al0 = (al1, al2, al3, al4)
print(f'O aluno escolhido foi {random.choice(al0)}')
