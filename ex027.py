#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
name = input('Digite seu nome completo: ')
dividido = name.split()
last = int(len(dividido) - 1)
print(dividido[0])
print(dividido[last])