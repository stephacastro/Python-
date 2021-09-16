'''Faça um programa que leia o sexo de uma pessoa, mas só aceite valores M ou F. Caso. Caso esteja errado,
peça a digitação novamente até ter um valor correto'''

'''m = 'M'
f = 'F'
while m == 'M' or f == 'F':
    sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
    if sexo != 'M' or sexo != 'F':
        print('Você digitou um dado invalido. Tente novamente!')
        if sexo == 'M' or sexo == 'F':
            print('Sexo {} registrado com sucesso!!'.format(sexo))
            m = 'Z'
            f = 'Q'
print('Obrigada :)'''

# Outra forma de fazer

sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))

