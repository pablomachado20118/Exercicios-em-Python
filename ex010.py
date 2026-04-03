#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,27
din = float(input('Quantos reais voce tem na sua carteira? '))
print('com R${}, voce consegue comprar ${:.2f}'.format(din, din/3.27))

