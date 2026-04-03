#faca um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
pesomaior = 0
pesomenor = 1000
for c in range(1, 6):
    peso = float(input(f'qual o peso da {c} pessoa: '))
    if pesomaior < peso:
        pesomaior = peso
    elif pesomenor > peso:
        pesomenor = peso
print(f'O maior peso lido foi {pesomaior}')
print(f'O menor peso lido foi {pesomenor}')