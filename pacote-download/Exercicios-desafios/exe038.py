'''Escreva um programa que leia dois numeros inteiros e compare-os. Mostrando na tela
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais'''

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

if n1 > n2:
    print('O primeiro valor é maior!')
elif n2 > n1:
    print('O segundo valor é maior!')
elif n1 == n2:
    print('Não existe valor maior, os dois são iguais!')

# Segundo modo de fazert este exercicio

'''
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

if n1 > n2:
    print('O primeiro valor é maior!')
elif n2 > n1:
    print('O segundo valor é maior!')
else:
    print('Não existe valor maior, os dois são iguais!')
'''