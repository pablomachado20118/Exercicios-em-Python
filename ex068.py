#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
import random
print('Vamos jogar Par ou Impar')
count = 0
soma = 0
while True:
    num = int(input('Diga um valor: '))
    escolha = input('Par ou Impar [P/I]? ').strip().upper()[0]
    cpu = random.randint(0, 10)
    soma = num + cpu
    print(f'Voce jogou {num} e o computador {cpu}. total deu {soma}')
    if escolha == 'P':
        if soma % 2 == 0:
            print('Voce venceu!!\nVamos jogar novamente...')
        elif soma % 2 == 1:
            print(f'Voce perdeu!!\nGamer OVER! Voce venceu {count} vezes!')
            break
    elif escolha == 'I':
        if soma % 2 == 0:
            print(f'Voce perdeu!!\nGamer OVER! Voce venceu {count} vezes!')
            break
        elif soma % 2 == 1:
            print('Voce venceu!!\nVamos jogar novamente...')
    count += 1

