#faca um programa que tenha uma funcao chamada contador() que receba tres parametros: inicio, fim e passo e realize a contagem. Seu programa tem que realizar tres contagens atraves da funcao criada: de 1 a 10, de 10 a 0 e uma contagem personalizada.

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if inicio > fim and passo > 0:
        passo = -passo
    for c in range(inicio, fim, passo):
        print(c, end=' ')
    print('FIM!')

contador(1, 11, 1)
contador(10, 0, -1)
print('Agora é sua vez de personalizar a contagem!')
inicio  = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
