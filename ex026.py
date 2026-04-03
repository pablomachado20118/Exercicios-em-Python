#Faça um programa que leia uma frase pelo teclado e mostre:
# - Quantas vezes aparece a letra "A"
# - Em que posição ela aparece a primeira vez
# - Em que posição ela aparece a última vez
texto = input('Digite uma frase: ').lower().strip()
print(f'A letra a aparece no texto {texto.count("a")} vezes')
print(f'O primeiro a aparece na posicao {texto.find('a') + 1}')
print(f'O Ultimo A aparece na posicao {texto.rfind('a') + 1}')

