#faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
angulo = float(input('digite o angulo que voce deseja: '))
rad = math.radians(angulo)
print(f'O valor de seno é {math.sin(rad)}')
print(f'O valor do coseno é {math.cos(rad)}')
print(f'o valor da tangente é {math.tan(rad)}')