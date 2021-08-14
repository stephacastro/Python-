'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar
um triângulo'''

print('\033[1;36m-*\033[m'*20)
print('         \033[4;30mAnalisando Triângulo\033[m')
print('\033[1;36m-*\033[m'*20)

r1 = float(input('1° segmento: '))
r2 = float(input('2° segmento: '))
r3 = float(input('3° segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos FORMAM um Triânguilo')
else:
    print('Os segmentos NÃO formam um Triângulo')

