'''O mesmo professor do exercicio anterior (19) qyer sortear a ordem de aprensentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada'''

from random import shuffle

n1 = input('1° aluno: ')
n2 = input('2° aluno: ')
n3 = input('3° aluno: ')
n4 = input('4° aluno: ')

lista = [n1, n2, n3, n4]
shuffle(lista)

print('A ordem de apresentação é\n{}'.format(lista))

'''from random import sample

n1 = input('1° aluno: ')
n2 = input('2° aluno: ')
n3 = input('3° aluno: ')
n4 = input('4° aluno: ')

lista = [n1, n2, n3, n4]
ordem = sample(lista, k=4)

print('A ordem de apresentação é\n{}'.format(ordem))
'''