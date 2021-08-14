# Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada

# criando uma interação com o usuario
n1 = int(input('Digite um valor: '))

# criando variaveis e atribuindo operações logicas a elas
dobro = n1 * 2
triplo = n1 * 3
raiz = n1 ** (1/2)

# escrevendo mensagens e os resultados na tela
print('O dobro de {} é igual á {}'.format(n1, dobro))
print('O triplo de {} é igual á {}'.format(n1, triplo))
print('A raiz quadrada de {} é igual á {:.2f}'.format(n1, raiz))
