#faca um programa que tenha uma  funcao chamada maior(), que recebe varios paramentros com valores inteiros.
#seu programa tem que analisar todos  os  valores e dizer qual deles é  o maior.
def maior(* num):
    maior = 0
    for i, n  in enumerate(num):
        if i == 0:
            maior = n
        else:
            if maior < n:
                maior = n
    print('analisando os valores passados...')
    print(f'{num} foram  informados {len(num)} valores ao todo')
    print(f'O maior valor informado foi {maior}')


maior(2,3,4,5,6,8,3)
maior(2,4,0)
maior()