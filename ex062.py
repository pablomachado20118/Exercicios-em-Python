#melhore o desafio 061, perguntando para o usuario se ele quer mostrar mais alguns termos.
termo = int(input('Primeiro termo: '))
razao = int(input('digite a razao da PA: '))
total = termo + (razao * 8)
print(termo, end=' ')
while termo <= total:
    termo += razao
    print(termo, end=' ')
mais = int(input('\nQuer ver mais quantos termos: '))
total2 = termo + (razao * (mais -1))
while termo <= total2:
    termo += razao
    print(termo, end=' ')
print('')
print('FIM')