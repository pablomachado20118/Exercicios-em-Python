#faca um programa que tenha um funcao chamada escreva(), que receba um texto qualquer como parametro e mostre uma mensagem com tamanho adaptavel, de acordo com o tamanho do texto digitado.
def escreva(txt):
    tamanho = len(txt) + 4
    print('-' * tamanho)
    print(f'{txt:^{tamanho}}')
    print('-' * tamanho)

escreva('Olá, mundo!')
escreva(str(input('Digite um texto: ')))