#Metade
def metade(txt, v = False):
    m = txt / 2
    if v == False:
        return m
    else:
        return f'R${m:.2f}'

#Dobro
def dobro(txt, v= False):
    d = txt * 2
    if v == False:
        return d
    else:
        return f'R${d:.2f}'

#aumento
def aumento(valor , porcento, v = False):
    a = valor * (1 + (porcento /100))
    if v == False:
        return a
    else:
        return f'R${a:.2f}'

#Diminuir
def diminuir(valor, porcento, v = False):
    a = valor * (1 - (porcento / 100))
    if v == False:
        return a
    else:
        return f'R${a:.2f}'

#deixar formado para dinheiro
def moeda(num):
    return f'R${num:.2f}'

#Resumo
def resumo(num, aumento=0, reducao=0):
    print('-' *30)
    print(f'{'RESUMO DO VALOR':^30}')
    print('-' *30)
    print(f'{'Preço analisado:':<20}', end=' ')
    print(f'R${num:.2f}')
    print(f'{'Dobro do preço:':<20}', end=' ')
    print(f'R${(num * 2):.2f}')
    print(f'{'Metade do preco:':<20}', end=' ')
    print(f'R${(num / 2):.2f}')
    print(f'{f"{aumento}% de aumento:":<20}', end=' ')
    print(f'R${num * (1 + (aumento /100 )):.2f}')
    print(f'{f"{reducao}% de reducao:":<20}',end= ' ')
    print(f'R${num * (1 - (reducao /100)):.2f}')

#dados monetario
#MEU DEUS QUE ORGULHO
def leiadinheiro(valor):
    c = f'{valor}'.replace(',' , '.')
    f = f'{c}'.replace('.','0')
    if f.isnumeric() == True:
        c = float(c)
        return resumo(c)
    else:
        print(F'ERRO!!! {c} é um preco invado!!')
        return leiadinheiro(input('Digite o preco: R$'))
