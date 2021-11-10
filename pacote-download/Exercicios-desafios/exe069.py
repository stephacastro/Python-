'''Crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada, o programa deverá
perguntar se o usuario quer continuar ou não. No final mostre:
a - quantas pessoas tem mais de 18 anos
b - quantos homens foram cadastrados
c - quantas mulheres tem menos de 20 anos '''

total18 = 0
totalh = 0
totalm20 = 0

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        total18 = total18 + 1
    if sexo == 'M':
        totalh = totalh + 1
    if sexo == 'F' and idade < 20:
        totalm20 = totalm20 + 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {total18}')
print(f'Total de homens cadastrados: {totalh}')
print(f'Total de mulheres com menos de 20 anos: {totalm20}')