'''Faça um programa que leia o nome completo de uma pessoa, mostrandi en segyida o primeiro e o ultimo nome
separadamente.'''

nome = str(input('Digite o seu nome completo: ')).strip()
lista = nome.split()

print('É um prazer te conhecer {} !!!'.format(nome))

print('Seu primeiro nome é {}'.format(lista[0]))
print('Seu último nome é {}'.format(lista[len(lista)-1]))



