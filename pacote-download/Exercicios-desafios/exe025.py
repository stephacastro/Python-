''' Crie um programa que leia o nome de uma pessoa e diga se ela tem SILVA no nome '''

nome = str(input('Qual é o seu nome completo: ')).strip()
n1 = nome
print('-------------------------*-------------------------\n'
      'Seu nome tem Silva? ')
print('silva' in n1.lower())