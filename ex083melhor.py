#crie um programa onde o usuario digite uma expressao qualquer que use parenteses. Seu programa devera analisar se a expressao passada esta com os parenteses abertos e fechados na ordem correta.
expressao = str(input('Digite uma expressão: '))
pilha = []
for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão é inválida!')
