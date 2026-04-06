#crie um programa que crie uma matriz de dimensao 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
matriz = list()
dados = list()
for c in range(0, 3):
    for f in range(0, 3):
        dados.append(int(input(f'Digite um valor para [{c}, {f}]: ')))
    matriz.append(dados[:])
    dados.clear()
print('=-=' * 10)
for c in range(0, 3):
    print(matriz[c])