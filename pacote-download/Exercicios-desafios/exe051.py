''' Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros
termos dessa progressão'''

print('='*30)
print('    PROGRESSÃO ARITMÉTICA')
print('='*30)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao

for contador in range (primeiro, decimo + razao, razao):
    print('{}'.format(contador), end=' - ')
print('ACABOU')
