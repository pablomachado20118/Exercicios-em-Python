#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e
#  a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2 metros quadrados.
altura = float(input( 'Qual a altura da parede que voce quer pintar? '))
largura = float(input('Qual a largura da parede que voce quer pintar? '))
print(f'A area da sua parede é de {altura * largura}m²\n'
      f'E precisa de {(altura * largura)/2 :.2f} litros de tinta')
