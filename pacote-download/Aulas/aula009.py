'''Fateamento'''
frase = 'Curso em Video Python'
print(frase[10]) #vai encontrar a letra da posição dentro da string
print(frase[1:12]) #vai percorrer da posição 1 até a 12
print(frase[1:18:2]) #vai percorrer da posição 1 até a 18 pulando de 2 em 2 posições
print(frase[:7]) #vai percorrer da primeira posição até a 5
print(frase[15:]) #vai percorrer da posição 15 até o final
print(frase[9::2]) #vai percorrer partindo da posição 9 até o final pulando de 3 em 3 posições

'''Printando um texto longo inteiro na tela usando """ aspas '''
print("""Um dia descobrimos que beijar uma pessoa para esquecer outra é bobagem.
Você não só não esquece a outra pessoa como pensa muito mais nela...
Um dia nós percebemos que as mulheres têm instinto "caçador" e fazem qualquer homem sofrer...""")

'''Analise de string'''
print(len(frase)) #quantas posições tem na string (tamanho da frase)
print(frase.count('c')) #conta a quantidade de letras c dentro da string
print(frase.count('o', 0, 13)) #conta usando o fateamento, quantas letras o tem da posição 0 até 13
print(frase.find('deo')) #encontra a posição que os caracteres parametrizados estão
print(frase.rfind('A')) # rfind procura a string de tras para frente
print('Curso' in frase) #vai retornar tru ou false se tiver ou não a palavra dentro da string

'''Tranformação de string'''
print(frase.replace('Python', 'Android')) #esse metodo encontra a palavra parametrizada na string e subistitui pela outra palavra parametrizada
print(frase.upper()) #transforma os caracteres da string em maiusculo
print(frase.lower()) #transforma os caracteres da string em minusculo
print(frase.capitalize()) #transforma apenas a 1° letra em maiuscula e se na string tiver outra letra maiuscula transforma em minuscula
print(frase.title()) #transforma o primeiro caractere de cada palavra em maiusculo
print(frase.strip()) #remove todos os espaços inuteis no começo e no final da string
print(frase.rstrip()) #remove somente todos os espaços do lado direito da string
print(frase.lstrip()) #remove somente todos os espaços do lado esquerdo da string

'''Divisão de strings'''
print(frase.split()) #faz a separação quando encontrar espaços e transforma em uma lista
print(''.join(frase)) #junta o conjunto de caracteres separados da string