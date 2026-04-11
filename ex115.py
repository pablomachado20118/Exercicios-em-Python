#crie um pequeno sistema modularizado que permite cadastrar pessoas  pelo seu nome e  idade em um arquivo de texto  simples.
#O sistema  so vai ter 2 opcoes: cadastrar uma nova pessoa e listar todas as pessoas cadastradas. 

import Modulo

arquivo = 'listadoexercicio115.txt'

if not Modulo.arquivoexiste(arquivo):
    Modulo.criararquivo(arquivo)
while True:
    resposta = Modulo.menu(["Ver Pessoas Cadastradas", "Cadastrar nova pessoa", "Sair do programa"])
    if resposta == '1':
        Modulo.lerarquivo(arquivo)
    elif resposta == '2':
        Modulo.comeco('Nova Cadastro')
        nome = str(input('Nome: '))
        idade = Modulo.leiaint113('Idade: ')
        Modulo.cadastrar(arquivo, nome, idade)
    elif resposta == '3':
        print('Saindo do Sistema...')
        break