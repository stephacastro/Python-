'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor'''

n1 = int(input('1° número: '))
n2 = int(input('2° número: '))
n3 = int(input('3° número: '))

if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('O valor menor é {}'.format(menor))

if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O valor maior é {}'.format(maior))
