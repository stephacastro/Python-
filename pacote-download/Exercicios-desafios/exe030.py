'''Crie um programa que leia um numero inteiro e mostre na tela se ele é par ou impar'''

numero = int(input('Digite um número: '))

resultado = numero % 2

if resultado == 0:
    print('O número {} é PAR'.format(numero))
else:
    print('O número {} é IMPAR'.format(numero))

