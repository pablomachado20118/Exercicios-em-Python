#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
numeros = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
usuario = int(input('Digite um numero de 0 a 20: '))
while usuario < 0 or usuario > 20:
    usuario = int(input('Erro!! Numero invalido!! Digite um numero de 0 a 20: '))
print(f'Voce digitou o numero {numeros[usuario]}')