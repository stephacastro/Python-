# Crie um programa que leia quanto uma pessoa tem na carteira e mostre quantos dolares ela poderia
# comprar

carteira = float(input('Quanto você tem de dinheiro na carteira? R$ '))

conversao = carteira / 3.27

print('Com R$ {:.2f} reais é possivel comprar R$ {:.2f} dolares'.format(carteira, conversao))