# Escreva um programa que converta uma temperatura digitada em C° e converta para °F

temperatura = float(input('Qual é a temperatura °C '))

conversor = temperatura * 1.8 + 32

print('A temperadora em {:.1f} °C convertida em °F é {:.1f}°F'.format(temperatura, conversor))
