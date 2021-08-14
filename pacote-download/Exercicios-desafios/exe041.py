''' A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atlela
e mostre a sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER'''

from datetime import date

# year - ano em english
year = date.today().year

print('\033[1;36m='*33)
print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO\033[m')
print('\033[1;36m=\033[m'*33)

print('\nINFORME SEU ANO DE NASCIMENTO PARA SABER SUA CATEGORIA')

# birth - nascimento em english
birth = int(input('Ano de nascimento: '))

# age- idade em english
age = year - birth

print('A idade do atleta é {} anos'.format(age))

if age <= 9:
    print('Categoria: MIRIM')
elif age <= 14:
    print('Categoria: INFANTIL')
elif age <= 19:
    print('Categoria: JÚNIOR')
elif age <= 25:
    print('Categoria: SÊNIOR')
elif age > 25:
    print('Categoria: MASTER')