#modifique as funcoes que foram criadas no desafio 107 para que elas aceitem um parametro a mais, informando se o valor retornado por elas vai ser ou nao formatado pela funcao moeda().Desenvolvida no desafio 108

import Modulo
p = float(input('Digite o valor do produto?  R$' ))
print(f'A metade de {p} é {Modulo.metade(p, True)}')
print(f'O dobro de {p} é {Modulo.dobro(p, True)}')
print(f'Aumentando 10%, temos {Modulo.aumento(p,10, True)}')
print(f'Reduzindo 13%, temos {Modulo.diminuir(p,13, False)}')