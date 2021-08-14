'''Escreva um programa que faça o computador pensar em um numero de 0 a 5 e peça para o usuario tentar descobrir
qual foi o numero escolhido pelo computador
O programa deverá escrever na tela se o usuario ganhou ou perdeu'''

from random import randint
from time import sleep
pc = randint(0, 5) # Faz o computador sortear um numero no parametro que dei
print('===========*===========*===========*===========*===========*=========== ')
print('Tente adivinhar em que número eu estou pensando entre 0 e 5')
print('===========*===========*===========*===========*===========*=========== ')

jogador = int(input('Qual número eu pensei? ')) # Jogador tentando adivinhar

print('LOADING...')
sleep(2) # usando o modulo sleep para ele esperar 2 segundos para executar

if jogador == pc:
    print('PARABÉNS!!! Você me venceu :D')
else:
    print('EU VENCI!!! Eu pensei no número {} e não no número {} :)'.format(pc, jogador))

