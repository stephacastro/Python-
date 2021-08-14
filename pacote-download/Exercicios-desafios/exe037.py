''' Escreva um programa que leia um número inteiro qualquer e peça para o usuario escolher qual será a base
de conversão / 1- binario / 2 para octal / 3- hexadecimal'''

print('\n\033[1;34m=*=*=*=*=*=*=\033[m CONVERSOR DE BINÁRIO / OCTAL / HEXADECIMAL \033[1;34m=*=*=*=*=*=*=\033[m\n')

num = int(input('\033[1;31mDigite um número: \033[m'))

print('\n\033[4mESCOLHA UMA DAS OPÇÕES ABAIXO PARA CONVERTER\033[m\n')

print('\033[1;36;46m=\033[m'*40)
print('1 - converter para BINÁRIO')
print('2 - converter para OCTAL')
print('3 - converter para HEXADECIMAL')
print('\033[1;36;46m=\033[m'*40)
opcao = int(input('\n\033[1;33mOPÇÃO: \033[m'))

if opcao == 1:
    print('\n\033[1;32m{} convertido para BINÁRIO é igual a {}\033[m'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('\n\033[1;32m{} convertido para OCTAL é igual a {}\033[m'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('\n\033[1;32m{} convertido para HEXADECIAL é igual a {}\033[m'.format(num, hex(num)[2:]))
else:
    print('\n\033[1;31m*OPÇÃO INVÁLIDA*\033[m')

