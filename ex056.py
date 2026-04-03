#desenvolva um programa que leia o nome, idade e sexo de quatro pessoas. No final do programa, mostre:
#A media de idade do grupo
#qual é o nome do homem mais velho
#quantas mulheres tem menos de 20 anos
idademaior = 0
nomemaior = 0
somaidade = 0
mulhera20 = 0
for c in range(1, 5):
    print(f' ____ {c} pessoa ____')
    nome = str(input(f'Digite o nome da pessoa: '))
    idade = int(input(f'Digite a idade da pessoa: '))
    sexo = str(input(f'Digite o sexo da pessoa (M/F): ')).upper()
    somaidade += idade
    if sexo == "M":
        if idade > idademaior:
            idademaior = idade
            nomemaior = nome
    if sexo == 'F' and idade < 20:
        mulhera20 += 1
mediaidadetotal = somaidade / 4
print(f'A media de idade do grupo é de {mediaidadetotal} anos')
print(f"O homem mais velho tem {idademaior} anos e se chama {nomemaior}")
print(f'no grupo tem {mulhera20} mulheres com menos de 20 anos')