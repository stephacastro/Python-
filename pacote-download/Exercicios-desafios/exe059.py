'''Crie um programa que leia dois valores e mostre um menu na tela
1 somar
2 multiplicar
3 maior
4 novos numeros
5 sair do programa'''

from time import sleep
v1 = int(input('1° número: '))
v2 = int(input('2° número: '))
opcao = 0

while opcao != 5:
    print('''    [ 1 ] somar 
    [ 2 ] multiplicar 
    [ 3 ] maior 
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('>>>> Qual é a sua opção? '))
    if opcao == 1:
        soma = v1 + v2
        print('A soma entre {} + {} é {}'.format(v1, v2, soma))
    elif opcao == 2:
        mult = v1 * v2
        print('A multiplicação entre{} x {} é {}'.format(v1, v2, mult))
    elif opcao == 3:
        if v1 > v2:
            maior = v1
            print('O número maior entre {} e {} é {}'.format(v1, v2, maior))
        else:
            maior = v2
            print('O número maior entre {} e {} é {}'.format(v1, v2, maior))
    elif opcao == 4:
        v1 = int(input('1° número: '))
        v2 = int(input('2° número: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente!')
    print('=-='*15)
sleep(2)
print('Fim do programa!! Volte sempre :D')



