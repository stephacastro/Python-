''' Faça um programa que leia o peso de 5 pessoas. NO final, mostre qyal foi o maior e o menor lidos. '''

maior = 0
menor = 0

for cont in range(1, 6):
    peso = float(input('Peso da {}° pessoa: '.format(cont)))
    if cont == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é {} Kg'.format(maior))
print('O menor peso é {} Kg'.format(menor))
