'''While'''

# While - Enquanto a condição for verdadeira executa - quando se tornar falsa ela sai do laço

"""maca = ''
chao = ''
pula = ''
pega = ''
passo = ''
while not maca:
    if chao:
        passo
    if pula:
        passo
    if pega:
        passo
pega
"""

'''c = 1
while c < 10:
    print(c)
    c = c + 1
print('Fim')'''

'''r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar: [S/N]: ')).upper()
print('Fim')'''

n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
print('Você digitou {} números pares e {} números ímpares'.format(par, impar))

