#crie um programa que crie uma matriz de dimensao 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
matriz = list()
for c in range(0, 3):
    for f in range(0, 3):
        matriz.append(int(input(f'Digite um valor para [{c}, {f}]: ')))
print('=-=' * 10)
print([matriz[0], matriz[1], matriz[2]])
print([matriz[3], matriz[4], matriz[5]])
print([matriz[6], matriz[7], matriz[8]])