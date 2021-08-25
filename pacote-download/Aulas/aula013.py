''' Estruturas de repetição
for c in range(1,10):
    passo # dentro do laço - esta se repetindo conforme o limitador
pega # fora do laço
for - laço/para 
in - no
range - intervalo
'''

for var in range(0, 6):
    print('oi')
print('FIM')

for c in range(0, 10, 2):
    print(c)

var = int(input('Digite um número: '))
for var in range(0, var+1):
    print(var)
print('FIM')

ini = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

for b in range (ini, fim+1, passo):
    print(b)
print('FIM')

s = 0
for a in range(0, 4):
    n = int(input('Digite um valor: '))
    s = s + n
print('A soma dos números é igual á {}'.format(s))