'''Condições aninhadas'''

# Estrutura condicional aninhada (uma estrutura dentro da outra)
nome = str(input('Qual é o seu nome? '))

if nome == 'Stephanie':
    print('Seu nome é incrivel!!')
elif nome == 'Maria' or nome == 'João' or nome == 'Emanuelli':
    print('Seu nome é bem polular no Brasil!!')
elif nome in 'Renata Ana Carla Tatiana':
    print('Que nome interessante!')
else:
    print('O seu nome é bem comum...')

print('Tenha uma boa noite {}'.format(nome))