''' Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsidrando os espaços '''

frase = str(input('Digite uma frase: ')).strip().upper() #strip p tirar os espaços e upper p transformar em maiusculo

palavras = frase.split() #separando cada palavra e criando uma lista
junto = ''.join(palavras) #juntando as palavras sem espaço
inverso = ''

for letra in range(len(junto) -1, -1, -1):
    inverso = inverso + junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palídromo!')
else:
    print('A frase não é um palídromo!')