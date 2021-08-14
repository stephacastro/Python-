# Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela sua porção
# inteira - ex: Digite um numero: 6.126 e tem a parte inteira 6

from math import floor

num = float(input('Digite um número real: '))
real = floor(num)
print('O numero real de {} é igual a porção inteira {}'.format(num, real))

# Outra forma de transformar um numero real em numero inteiro sem importar modulo/biblioteca
'''num = float(input('Digite um numero real: '))
print('O numero real de {} é igual a porção inteira {}'.format(num, int(num)'''

