#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dias = float(input('Quantos dias voce ficou com o carro alugado? '))
km = float(input('Quantos km voce rodou com o carro? '))
print(f'Usando o carro por {dias} dias e rodando {km} km, o valor ficou em R${dias * 60 + km * 0.15 }')