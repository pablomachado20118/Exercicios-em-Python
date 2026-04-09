#Crie um modulo que tenha as funcoes incorporadas aumentar(), diminiur (), dobro() e metade().
#faca tambem um programa que importe esse modulo e use algumas dessas funcoes.

import Modulo
p = float(input('Digite o valor do produto?  R$' ))
print(f'A metade de {p} é {Modulo.metade(p)}')
print(f'O dobro de {p} é {Modulo.dobro(p)}')
print(f'Aumentando 10%, temos {Modulo.aumento(p,10)}')
print(f'Reduzindo 13%, temos {Modulo.diminuir(p,13)}')