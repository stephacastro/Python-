# faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de
# aumento

salario_funcionario = float(input('\nInforme o seu salário atual R$ '))

salario = salario_funcionario
aumento = 15
novo_salario = salario + (salario * aumento / 100)

print('\nO seu salário anterior ao aumento de 15% era de R$ {:.2f} reais\n'.format(salario_funcionario))
print('O seu novo salário com aumento de 15% é R$ {:.2f} reais'.format(novo_salario))


# calculo de porcentagem simplificado valor*desconto / 100 (10*5/100)