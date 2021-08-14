n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))

soma = n1 +n2
multi = n1 * n2
divi = n1 / n2
diin = n1 // n2
potencia = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(soma, multi, divi))
print('A divisão inteira é {} e a potência é {}'.format(diin, potencia))