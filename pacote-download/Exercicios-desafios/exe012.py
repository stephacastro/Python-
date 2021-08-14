# Faça um algoritimo que leia o preço de um produto e mpstro seu novo preço com 5% de desconto

produto = float(input('\nDigite o preço original do produto R$  '))

desconto = produto * 0.05
novo_valor = produto * 0.95

print('\nO preço original do seu produto é R$ {:.2f} reais\n'.format(produto))

print('O novo preço do seu produto com 5% de desconto é R${:.2f} reais'.format(novo_valor))