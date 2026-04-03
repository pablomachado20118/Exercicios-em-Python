#Crie um programa que leia o nome completo de uma pessoa e diga se ela tem "SILVA" no nome.
name = input('Qual o seu nome? ').strip().lower()
print(f'voce tem silva no nome? {'silva' in name}')
