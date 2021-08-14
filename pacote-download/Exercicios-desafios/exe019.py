'''Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
lendo o nome dekes e escrevendo o nome do escolhido'''

import random

aluno1 = input('1° aluno: ')
aluno2 = input('2° aluno: ')
aluno3 = input('3° aluno: ')
aluno4 = input('4° aluno: ')

lista = [aluno1, aluno2, aluno3, aluno4]
sorteio = random.choice(lista)

print('O aluno escolhido foi: {}'.format(sorteio))

'''Outro modo de fazer 
from randon import choice

aluno1 = input('1° aluno: ')
aluno2 = input('2° aluno: ')
aluno3 = input('3° aluno: ')
aluno4 = input('4° aluno: ')

lista = [aluno1, aluno2, aluno3, aluno4]
sorteio = choice(lista)

print('O aluno escolhido foi: {}'.format(sorteio))
'''