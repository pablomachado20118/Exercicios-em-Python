#faca  um programa que tenha uma funcao chamada area(), que receba as dimensoes de um terreno retangular (largura e comprimento) e mostre a area do terreno.
def area(largura, comprimento):
    a = largura * comprimento
    print(f'A area do terreno é de {a}m².')


print('-' * 30)
print(f'{"CALCULO DE AREA DE TERRENO":^30}')
print('-' * 30)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(largura, comprimento)