# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

metros = float(input('Quantos metros deseja converter? '))

centimentros = metros * 100
milimetros = metros * 1000

print('{} metros convertidos em centimetros é igual á : {} '.format(metros, centimentros))
print('{} metros convertidos em milimetros é igual á : {} '.format(metros, milimetros))