#Escreva um programa para aprovar o empréstime para compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
print('Bom dia! vou te ajudar a conseguir o emprestimo para sua casa')
print('-'*61)
casa = float(input('qual o valor da casa: '))
salario = float(input('qual o seu salario? '))
anos = int(input('Vai pagar o emprestimo em quantos anos: '))
mes = anos * 12
valor = casa / mes
salario30 = salario * 0.3
print(f'30% do seu salário é: R$ {salario30:.2f}')
print(f'O valor da prestação mensal é: R$ {valor:.2f}')
if valor > salario30:
    print('emprestimo reprovado!')
else:
    print('emprestimo aprovado!')
