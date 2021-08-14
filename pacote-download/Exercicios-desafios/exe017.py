# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo
# retangulo, calcule e mostre o comprimento da hipotenusa

# metodo tradicional
'''cateto1 = float(input('Digite o comprimento do cateto oposto: '))
cateto2 = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = (cateto1 ** 2 + cateto2 ** 2) **(1/2)

print("A hipotenusa vai medir {:.2f}".format(hipotenusa))'''

# calculando usando a biblioteca hypot

from math import hypot

cateto1 = float(input('Digite o comprimento do cateto oposto: '))
cateto2 = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = hypot(cateto1, cateto2)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))
