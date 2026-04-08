#faca um programa que tenha uma lista chamada numeros e duas funcoes chamdas  sorteia() e somapar().
#A primeira funcao  vai sortear 5 numeros e vai coloca-los dentro da  lista
#A  segunda funcao  vai mostrar a soma entre todos os valores PARES sorteados pela funcao anterior
import random
lista = []
resultado = 0

def sorteia():
    resultado = (random.sample(range(1, 11), 5))
    for c in resultado:
        lista.append(c)
    print(f'Sorteando 5 valores : {lista}')


def somapar():
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {lista}, temos {soma}')


sorteia()
somapar()