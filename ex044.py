#Elabore um programa que calcule o preço a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço formal
# - Acima de 3x no cartão: 20% de juros
valor = float(input('Digite o valor do produto: R$'))
print(f'preco normal do produto é R${valor}')
print(f'a vista no dinheiro/cheque, tem 10% de desconto, ficando R${valor * 0.9}')
print(f'a vista no cartao, tem 5% de desconto, ficando R${valor * 0.95}')
print(f'2 vezes no cartao, o preco é normal R${valor}')
print(f'mais de 3 vezes no cartao, entra 20% de juros, ficando R${valor * 1.2}')