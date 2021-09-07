''' Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não
atingiram a maioridade e quantas ja são maiores '''

from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0

for cont in range(1, 8):
    nasc = int(input('Ano de nascimento {}° da pessoa: '.format(cont)))
    idade = atual - nasc
    if idade >= 21:
        totalmaior = totalmaior + 1
    else:
        totalmenor = totalmenor + 1
print('Tivemos o total de {} pessoas maiores de idade'.format(totalmaior))
print('E tivemos o total de {} pessoas menores de idade'.formta(totalmenor))