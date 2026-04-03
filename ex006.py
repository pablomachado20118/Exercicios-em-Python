#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
num = int(input('Escolha um numero inteiro: '))
print('Voce escolheu  o numero {} \n'
      'O dobro do seu numero é {}.\n'
      'O triplo do seu numero é {}. \n'
      'A Raiz quadrada do seu numero é {:.5f}. '.format(num, num * 2, num * 3, num**(1/2)))


