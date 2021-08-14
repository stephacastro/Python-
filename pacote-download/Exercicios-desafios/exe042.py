'''Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes'''

print('\033[1;36m-*\033[m'*20)
print('         \033[4;30mAnalisando Triângulo\033[m')
print('\033[1;36m-*\033[m'*20)

r1 = float(input('1° segmento: '))
r2 = float(input('2° segmento: '))
r3 = float(input('3° segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos FORMAM um Triânguilo', end = '')
    if r1 == r2 and r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos NÃO formam um Triângulo')



