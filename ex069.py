#crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos
#B) quantos homens foram cadastrados
#C) quantas mulheres tem menos de 20 anos
print('Cadastre uma pessoa')
count = idade = maior = homens = mulher20 = 0
while True:
    idade = int(input('Idade: '))
    while idade < 0 or idade > 100:
        idade = int(input('Idade inválida! Digita de novo (0 a 100): '))
    if idade > 18:
        maior += 1
    sexo = input('Sexo [M/F]: ').upper().strip()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1
    opcao = input('Quer continuar? [S/N]').upper().strip()[0]
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if opcao == 'N':
        break
print('total de pessoas com mais de 18 anos: {}'.format(maior))
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulher20} mulheres com menos de 20 anos')