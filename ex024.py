#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".
city = input('Informe o nome da cidade: ').strip().lower()
dividido = city.split()
print(f'Sua cidade comeca com "Santo"? {'santo' in dividido[0]}"')
