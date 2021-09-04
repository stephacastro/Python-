''' Faça um programa que leia um numero inteiro e diga se ele é ou não um numero primo'''

num = int(input('Digite um número: '))
tot = 0

for contador in range(1, num + 1):
    if num % contador == 0:
        print('\033[33m', end=' ')
        tot = tot + 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(contador), end=' ')
print('\nO número {} foi divisivel {} vezes'.format(num, tot))

if tot == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
