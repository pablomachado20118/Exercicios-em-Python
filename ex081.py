#Crie um programa que vai ler varios numeros e colocar em uma lista. Depois disso, mostre:
#a) Quantos numeros foram digitados
#b) A lista de valores, ordenada de forma decrescente
#c) Se o valor 5 foi digitado e esta ou nao na lista
lista = []
while True:
    num = int(input('Digite um numero: '))
    lista.append(num)
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resposta == 'N':
        break
print(f'Foram digitados {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'os valores em ordem decrescente sao {lista}')
if 5 in lista:
    print('O valor 5 esta na lista')
else:
    print('O valor 5 nao esta na lista')