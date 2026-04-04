#crie um programa onde o usuario digite uma expressao qualquer que use parenteses. Seu programa devera analisar se a expressao passada esta com os parenteses abertos e fechados na ordem correta.
expressao = str(input('Digite uma expressão: '))
count1 = expressao.count('(')
count2 = expressao.count(')')
if count1 == count2:
    print('Sua expressão é válida!')
else:
    print('Sua expressão é inválida!')