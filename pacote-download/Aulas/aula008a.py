# importando apenas uma funcionalidade da biblioteca
from math import sqrt, floor

num = int(input('Digite um número: '))

#quando importa apenas 1 funcionalidade não precisa chamar a biblioteca, pode chamar a funci direto
raiz = sqrt(num)

# usando o floor para arredondar p baixo o resultado da raiz
print('A raiz quadrada de {} é igual á {:.2f}'.format(num, floor(raiz)))
