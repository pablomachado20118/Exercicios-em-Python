#Crie um programa que vai ler varios numeros e colocar em uma lista.
#Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente.
#No final, mostre o conteudo das tres listas geradas.
numeros = []
pares = []
impares = []
while True:
    n = int(input('Digite um numero: '))
    numeros.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    resposta = input('Quer continuar? [S/N] ').strip().upper()
    if resposta == 'N':
        break
print(f'a lista de numeros digitados é : {numeros}')
print('_' * 30)
print(f'A lista de numeros pares é : {pares}')
print('_' * 30)
print(f'A lista de numeros impares é : {impares}')