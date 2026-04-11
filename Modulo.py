#Metade
def metade(txt, v = False):
    m = txt / 2
    if v == False:
        return m
    else:
        return f'R${m:.2f}'

#Dobro
def dobro(txt, v= False):
    d = txt * 2
    if v == False:
        return d
    else:
        return f'R${d:.2f}'

#aumento
def aumento(valor , porcento, v = False):
    a = valor * (1 + (porcento /100))
    if v == False:
        return a
    else:
        return f'R${a:.2f}'

#Diminuir
def diminuir(valor, porcento, v = False):
    a = valor * (1 - (porcento / 100))
    if v == False:
        return a
    else:
        return f'R${a:.2f}'

#deixar formado para dinheiro
def moeda(num):
    return f'R${num:.2f}'

#Resumo
def resumo(num, aumento=0, reducao=0):
    print('-' *30)
    print(f'{'RESUMO DO VALOR':^30}')
    print('-' *30)
    print(f'{'Preço analisado:':<20}', end=' ')
    print(f'R${num:.2f}')
    print(f'{'Dobro do preço:':<20}', end=' ')
    print(f'R${(num * 2):.2f}')
    print(f'{'Metade do preco:':<20}', end=' ')
    print(f'R${(num / 2):.2f}')
    print(f'{f"{aumento}% de aumento:":<20}', end=' ')
    print(f'R${num * (1 + (aumento /100 )):.2f}')
    print(f'{f"{reducao}% de reducao:":<20}',end= ' ')
    print(f'R${num * (1 - (reducao /100)):.2f}')

#dados monetario
#MEU DEUS QUE ORGULHO
def leiadinheiro(valor):
    c = f'{valor}'.replace(',' , '.')
    f = f'{c}'.replace('.','0')
    if f.isnumeric() == True:
        c = float(c)
        return resumo(c)
    else:
        print(F'ERRO!!! {c} é um preco invado!!')
        return leiadinheiro(input('Digite o preco: R$'))
    


#Aula questao 113
def leiaint113(msg):
    entrada = str(input(msg))
    while True:
        try:
            int(entrada)
        except:
            print('Erro!! Digite um numero inteiro valido!!')
            entrada = str(input(msg))
        else:
            return entrada



#Aula questao 113
def leiafloat113(msg):
    entrada = str(input(msg))
    while True:
        try:
            float(entrada)
        except:
            print('Erro!! Digite um numero real valido!!')
            entrada = str(input(msg))
        else:
            return entrada


#exercicio 115

def linha(num = 42):
    return '-' * num

def comeco(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    comeco('Menu Principal')
    c = 1
    for i in lista:
        print(f'{c} - {i}')
        c += 1
    print(linha())
    opc = leiafloat113('Sua opcao: ')
    return opc


def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close
    except:
        print('Houve um erro na criacao do arquivo!!')
    else:
        print(f'Arquivo {nome} criado  com sucesso!!')

def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro  ao ler o arquivo')
    else:
        comeco('Pessoas cadastradas')
        for l in a:
            dado = l.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]} anos ')
    finally:
        a.close()


def cadastrar(arq,nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
        


