''' Crie um programa que leia números inteiros pelo teclado, O programa só vai parar quando o usuario digitar
o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre
elas (desconsiderando a flag)'''

s = 0
cont = 0
while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    s = s + n
    cont = cont + 1
print(f'A soma dos {cont} números é {s}')
