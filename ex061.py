#refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
termo = int(input('Primeiro termo: '))
razao = int(input('digite a razao da PA: '))
total = termo + (razao * 8)
print(termo, end=' ')
while termo <= total:
    termo += razao
    print(termo, end=' ')