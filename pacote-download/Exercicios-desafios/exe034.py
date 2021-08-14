'''Escreva um programa que pergunte o salário de ym funcionário e calcule o valor do aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%'''

print('\033[31m*************************************************************************\033[m')
salario = float(input('Informe o salário do funcionário R$'))
print('\033[31m*************************************************************************\033[m')

if salario <= 1250:
    novosalario = salario + (salario * 15 / 100)
else:
    novosalario = salario + (salario * 10 / 100)
print('\nO funcionário que ganhava R${:.2f} reais agora passa a ganhar R${:.2f} reais'.format(salario, novosalario))