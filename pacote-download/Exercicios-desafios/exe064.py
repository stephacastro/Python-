''' Crie um programa que leia varios numeros inteiros pelo teclado. O programa só vai parar quando o usuario digitar
o valor 999, que é a condição de parada. No final, mostre quantos numeros foram digitados e qual foi a soma entre
eles (desconsiderando o flag) '''

numero = 0
cont = 0
soma = 0
numero = int(input('Digite um número [999 para parar]: '))

while numero != 999:
    soma = soma + numero
    cont = cont + 1
    numero = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles é {}. '.format(cont, soma))
