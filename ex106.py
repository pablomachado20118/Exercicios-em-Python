#faca um mini-sistema que utilize o interactive help do python.O usuario vai digitar o comando e o manual vai aparecer.Quando o usuario digitar a palavra 'FIM' o programa se encerrará.

from time import sleep
def manual(text):
    return help(text)


while True:
    print('~' * 18)
    print(' Sistema de ajuda')
    print('~' * 18)
    c = input('Funcao ou blibioteca: ')
    if c == 'Fim':
        print('Até logo')
        break   
    sleep(1)
    print(manual(c))
