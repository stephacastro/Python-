'''Crie um programa que leia o nome completo de uma pessoa e mostra: O nome com todas as letras maisculas / o nome
com todas as letras minisculas / quantas letras ao todo sem considerar espeços / quantas letras tem o primeiro nome'''

nome = str(input('Digite o seu nome completo: ')).strip()
print('\n************Analisando o seu nome************\n',
      '\nSeu nome em letras maiúsculas é {}'.format(nome.upper()),
      '\nSeu nome em letras manúsculas é {}'.format(nome.lower()))

print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))

dividido = nome.split()
print('Seu primeiro nome tem {} letras'.format(len(dividido[0])))
