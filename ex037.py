#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 
# 1 para binário;
# 2 para octal;
# 3 para hexadecimal;
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'vermelho': '\033[31m',}
num = int(input('Digite um numero inteiro: '))
base = int(input(f'-{cores['azul']}1{cores['limpa']} para {cores['amarelo']}binario{cores['limpa']} \n-{cores['azul']}2{cores['limpa']} para {cores['amarelo']}octal{cores['limpa']} \n-{cores['azul']}3{cores['limpa']} para {cores['amarelo']}hexadecimal{cores['limpa']} \nQuer converter para qual base? '))
if base == 1:
    print(f'O numero {num} na base binaria fica {bin(num)[2:]}')
elif base == 2:
    print(f'O numero {num} na base octagonal fica {oct(num)[2:]}')
elif base == 3:
    print(f'O numero {num} na base hexadecimal fica {hex(num)[2:]}')
else:
    print('Vai se fuder')