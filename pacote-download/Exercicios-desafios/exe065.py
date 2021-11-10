''' Crie um programa que leia varios valores numeros inteiros pelo teclado. No final da execução, mostre a média
entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuario se ele quer
ou não continuar a digitar valores '''

resposta = 'S'
soma = 0
quant = 0
media = 0

while resposta == 'S':
    numero = int('Digite um número: ')
    soma = soma + numero
    quant = quant + 1
    if quant == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()
media = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))