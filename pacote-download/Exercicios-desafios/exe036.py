'''Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
o salario do comprador e em quantos anos ele vai pagar.
A prestação mensal, não pode exceder 30% do salario ou então o emprestimo será negado'''

print('\033[1;34m=*=*=*=*=*=*=*=*=*=*=**=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*\033[m')
print('                           EMPRÉSTIMO BANCÁRIO ')
print('\033[1;34m=*=*=*=*=*=*=*=*=*=*=**=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*\033[m\n')

casa = float(input('Informe o preço da casa R$ '))
salario = float(input('Informe o seu salário R$ '))
anos = int(input('Durante quantos anos pretende pagar o imóvel: '))

prestacao = casa / (anos * 12)
aprovacao = salario * 30 / 100

print('Para quitar um imóvel no valor de R${:.2f} reais em {} anos '.format(casa, anos), end=''
      'a prestação será de R${:.2f} reais\n'.format(prestacao))

if prestacao <= aprovacao:
    print('\033[1;32mO empréstimo foi APROVADO!!!\033[m')
else:
    print('\033[1;31mO empréstimo foi NEGADO!!!\033[m')





