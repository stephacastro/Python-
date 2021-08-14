# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
# quantidade de dias pelos quais ele foi alugado . Calcule o preço a pagar, sabendo que o carro
# custa R$60 por dia e R$0,15 por km rodado

diaria = int(input('\nPor quantos dias alugado? '))
km = float(input('\nQuantos KM rodado?  '))


di = diaria * 60
k = km * 0.15
total = di + k

print('\nO preço a pagar é R${:.2f}'.format(total))

# simplificando (diaria * 60) + (km * 0.15)