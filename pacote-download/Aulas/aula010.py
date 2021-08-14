'''Condições'''

'''if exemplo.aula() #se for verdadeiro execute
    bloco verdadeiro

else: #se não, execute
    bloco falso'''

nome = str(input('Qual é o seu nome? '))
if nome == 'Stephanie':
    print('Seu nome é incrivel *-*')
else:
    print('Seu nome é muito comum!')
print('Boa noite, {}. Você é muito dedicada!!'.format(nome))
