'''Faça um programa que calcule a soma entre os numeros impares que são multiplos de três e que se encontram no
intervalo de 1 até 500.'''

soma = 0
cont = 0

for contador in range(1, 501, 2):
    if contador % 3 == 0:
        cont = cont + 1
        soma = soma + contador
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))

