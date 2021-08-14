'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda
vai se alistar ao serviço militar, se é a hora exata de se alistar ou se ja passou do tempo de alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo'''

from datetime import date

ano = date.today().year

nascimento = int(input('Digite o ano de nascimento: '))
sexo = str(input('Digite o sexo: ')).upper()
idade = ano - nascimento

print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, ano))

if sexo == 'F':
    print('\033[1;32mVocê não tem que se alistar para o serviço militar!\033[m')
elif idade == 18:
    print('\033[1;31mVocê precisa se alistar IMEDIATAMENTE!\033[m')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o seu alistamento!'.format(saldo))
    ano = ano + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos!'.format(saldo))
    ano = saldo - ano
    print('Seu alistamento foi em {}'.format(ano))


















