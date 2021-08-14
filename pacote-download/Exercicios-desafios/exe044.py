'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
e condição de pagamento:
- á vista dinheiro/cheque: 10% de desconto
- á vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros '''

print('\033[1;36;40m========== LOJAS NO PRECINHO ==========\033[m')

preco = float(input('\n\033[1;31mPreço das compras R$ \033[m'))

print('\n\033[1;33m***** FORMAS DE PAGAMENTO *****',
      '\n[ 1 ] á vista dinheiro/cheque',
      '\n[ 2 ] á vista no cartão',
      '\n[ 3 ] 2x no cartão',
      '\n[ 4 ] 3x ou mais no cartão\033[m')

opcao = int(input('\n\033[1;31mQual é a opção? \033[m'))

if opcao == 1:
    desconto = preco - (preco * 10 / 100)
    print('\n\033[1;34mSua compra será á vista em dinheiro/cheque terá 10% de DESCONTO!\033[m')
    print('\033[1;34mSua compra de R${:.2f} reais vai custar R${:.2f} reais no final!\033[m'.format(preco, desconto))
elif opcao == 2:
    desconto = preco - (preco * 5 / 100)
    print('\033[1;34mSua compra á vista no cartão terá 5% de DESCONTO!\033[m')
    print('\033[1;34mSua compra de R${:.2f} reais vai custar R${:.2f} reais no final!\033[m'.format(preco, desconto))
elif opcao == 3:
    parcela = preco / 2
    print('\033[1;34mSua compra será parcelada em 2x de R${:.2f} reais SEM JUROS!\033[m'.format(parcela))
    print('\033[1;34mSua compra de {:.2f} reais vai custar {:.2f} reais no final'.format(preco, preco))
elif opcao == 4:
    parcela = int(input('\033[1;31mQuantas parcelas? \033[m'))
    acres = preco + (preco * 20 / 100)
    valor = acres / parcela
    print('\033[1;34mSua compra será parcelada em {}x de {} reais com JUROS!\033[m'.format(parcela, valor))
    print('\033[1;34mSua compra de {:.2f} reais vai custar {:.2f} reais no final\033[m'.format(preco, acres))
else:
    total = preco
    print('\n\033[1;31mOPÇÃO INVÁLIDA, TENTE NOVAMENTE!!!\033[m')
    print('\033[1;34mSua compra de {:.2f} reais vai custar {:.2f} reais no final'.format(preco, preco))
