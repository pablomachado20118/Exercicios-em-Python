#Desenvolva um programa que pergunte a distancia de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
dis = int(input('Qual vai ser a distancia da sua viagem em Km?: '))
if dis <= 200:
    print(f'Para fazer sua viagem de {dis}Km, voce terá que pagar R${dis * 0.5}')
else:
    print(f'Para fazer sua viagem de {dis}Km, voce tera que pagar R${dis * 0.45}')