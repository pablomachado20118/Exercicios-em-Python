#faça um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Qual o valor do produto? R$'))
print(f'O valor do produto era R${preco},com o desconto de %5, o produto ficou em R${preco * 0.95 :.2f}')