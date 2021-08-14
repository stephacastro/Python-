# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area
# e quantidade de tinta necessaria para pinta-la, sabendo que cada litro de pinta uma area de 2m²

largura = float(input('Qual é a largura da parede: '))
altura = float(input('Qual é a altura da parede: '))

area = largura * altura
tinta = area / 2

print('Sua parede tem a dimensão de {} x {} e a sua área é de {}m²'.format(largura, altura, area))
print('Para pintar uma area de {} metros² é necessario {}l de tinta'.format(area, tinta))