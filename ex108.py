#adapte o codigo do desafio 107, criando uma funcao adicional chamada moeda() que consiga mostrar os valores como um valor monetario formatado.

import Modulo
p = float(input('Digite o valor do produto?  R$' ))
print(f'A metade de {p} é {Modulo.moeda(Modulo.metade(p))}')
print(f'O dobro de {p} é {Modulo.moeda(Modulo.dobro(p))}')
print(f'Aumentando 10%, temos {Modulo.moeda(Modulo.aumento(p,10))}')
print(f'Reduzindo 13%, temos {Modulo.moeda(Modulo.diminuir(p,13))}')