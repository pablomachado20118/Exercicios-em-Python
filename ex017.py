#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
catop = float(input('Qual é o catato oposto? '))
catad = float(input('Qual o cateto adjacente? '))
print(f'O comprimento da hipotenusa é {(catop**2 + catad**2)**(1/2) }')