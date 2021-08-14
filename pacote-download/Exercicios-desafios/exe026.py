'''Faça um programa que leia uma frase pelo teclado e mostre:
Quantas vezes aárece a letra A
Em que posição ela aparece pela primeira vez
Em que posição ela aparece a ultima vez'''

frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A'))) #rfind procura a string de tras para frente