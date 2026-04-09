#crie um programa que tenha uma funcao fatorial() que receba dois parametros:o primeiro que indique o numero a calcular e o outro chamado show, que sera um valor logico(opcional) indicando se será mostrado ou nao na tela o processo de calculo do fatorial.

def fatorial(num, show=False):
    fato = 1
    for valor in range(num,0,-1):
        fato *= valor
        if show == True:
            if valor == 1:
                print(f'{valor}', end= ' = ')
            else:
                print(f'{valor}', end=' x ')

        
    return fato

print(f'{fatorial(5, show=True)}')