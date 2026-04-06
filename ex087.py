#aprimore o desafio anterior, mostrando no final:
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.
matriz = list()
dados = list()
somapar = 0
somater = 0
numeromaior = 0
for c in range(0, 3):
    for v in range(0, 3):
        numero = (int(input(f'Digite um valor para [{c}, {v}]: ')))
        dados.append(numero)
        if numero % 2 == 0:
            somapar += numero
        if v == 2:
            somater += numero
    if c == 1:
        numeromaior = max(dados)
    matriz.append(dados[:])
    dados.clear()
print('=-=' * 10)
for w in range(0, 3):
    print(matriz[w])
print('_' * 30)
print(f"A soma de todos os numeros pares é {somapar}.")
print(f'A soma dos numeros da terceira coluna é {somater}.')
print(f'O maior numero da segunda linha é {numeromaior}.')