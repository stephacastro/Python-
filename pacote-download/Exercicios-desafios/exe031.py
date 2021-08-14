'''Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem, cobrando
R$0,50 r por Km e para viagens de até 200k e R$0,45 para viagens mais longas'''

print('\n******************** PENSANDO EM VIAJAR? ********************')

boasvindas = str(input('\nDigite SIM ou NAO: '))

if boasvindas == 'SIM':
    print('\nMUITO BEM!!! Você esta no lugar certo :D')
else:
    print('\nSem problemas!!! Volte sempre :D')

viagem = float(input('\nInforme a distância da sua viagem: '))

print('\nBacana!!! Você esta prestes a começar uma viagem de {}Km'.format(viagem))

preco1 = viagem * 0.50
preco2 = viagem * 0.45
resultado1 = preco1
resultado2 = preco2

if viagem <= 200:
    print('\nO valor da sua passagem é de R${:.2f} reais'.format(resultado1))
else:
    print('\nTemos uma passagem promocional para você no valor de R${:.2f} reais'.format(resultado2))

print('\n************************* BOA VIAGEM *************************')