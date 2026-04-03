#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
maior = 0
for c in range(1 , 8):
    frase = int(input(f'Digite o ano de nascimento da {c} pessoa: '))
    if frase < 2005:
        maior += 1
print(f'Temos {maior} pessoas maiores e {7 - maior} menores de idade.')