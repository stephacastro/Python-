'''Faça um programa que jogue par ou impar com o computador. O jogo só sera interrompido quando o jogador perder,
mostre o total de vitórias consectivas que ele conquistou no final do jogo.'''

from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0,11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o cumputador {computador}. Total de {total}')
    if total % 2 == 0:
        print('DEU PAR!')
    else:
        print('DEU IMPAR!')
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU!!')
            v = v +1
        else:
            print('VOCÊ PERDEU!!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCÊ VENCEU!!')
            v = v + 1
        else:
            print('VOCÊ PERDEU!!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! VOCÊ VENCEU {v} VEZES')
