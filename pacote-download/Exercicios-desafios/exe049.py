''' Refaça o desafio 009, mostrando a tabuada de um numero que o usuario escolher, só que agora utilizando
um laço FOR '''

tabuada = int(input('Digite a tabuada: '))

for contador in range(1, 11):
    print('{} x {:2} = {}'.format(tabuada, contador, tabuada*contador))


