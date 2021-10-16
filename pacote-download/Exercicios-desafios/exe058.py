'''Melhore o jogo de adivinhação do desafio 28 onde o computador vai 'pensar' em um número entre 0 e 10. Só que
agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer'''

from random import randint

pc = randint(0, 10)

print('===========*===========*===========*===========*===========*=========== ')
print('Tente adivinhar em que número eu estou pensando entre 0 e 10')
print('===========*===========*===========*===========*===========*=========== ')

acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpite = palpite + 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('Mais... Tente mais uma vez!')
        elif jogador > pc:
            print('Menos... Tente mais uma vez!')
print('Você acertou com {} tentativas. Parabéns!!'.format(palpite))
