'''Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome Santo'''

cidade = str(input('Em que cidade você nasceu: ')).strip()
a = cidade
print('SANTO' in a.upper())
