# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas;
# - Quantas letras ao todo (sem considerar os espaços);
# - Quantas letras tem o primeiro nome;
name = input('Qual o seu nome completo? ')
dividido = name.split()
teste = name.replace(' ', '')
print(name.upper())
print(name.lower())
print(f'Quantidade de letras ao todo: {len(teste)}')
print(f'Quantidade de letras no primeiro nome: {len(dividido[0])}')