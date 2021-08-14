'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.'''

print('=========================*** Radar Inteligente ***==========================')

velocidade = int(input('Qual é a velocidade: '))

multa = (velocidade-80) * 7

if velocidade > 80:
    print('MULTADO!!! Você ultrapassou o limite de velocidade permitido que é 80Km/h')
    print('O valor da multa é de R${:.2f} reais'.format(multa))
else:
    print('PARABÉNS!!! Você está dirigindo com segurança!')