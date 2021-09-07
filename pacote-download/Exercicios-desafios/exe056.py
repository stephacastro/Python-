''' Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade
do grupo, qual é o nome do homem mais velho e quantas mulheres tem menos de 20 anos. '''

soma = 0
media = 0
maioridadehomem = 0
nomevelho = ''
totalmulher = 0

for pessoa in range(1, 5):
    print('------- {}° PESSOA -------'.format(pessoa))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    soma = soma + idade
    media = soma / 4
    if pessoa == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        totalmulher = totalmulher + 1
mediaidade = soma / 4
print('A média de idade do grupo é {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totalmulher))