''' Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
de acordo con a média antingida:
- Média abaixo 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média entre 7.0 ou superior: APROVADO'''

print('\033[1;36m*'*30)
print('SISTEMA DE NOTAS ESCOLARES\033[m')
print('\033[1;36m*\033[m'*30)

n1 = float(input('\n1° Nota: '))
n2 = float(input('2° Nota: '))

# everage - média em english
everage = (n1 + n2) / 2

print('Tirando {:.1f} e {:.1f} a média do aluno é {:.1f}'.format(n1, n2, everage))

if everage < 5:
    print('\033[1;31mSuas notas {:.1f} e {:.1f} não atingiram a média 7. Você está REPROVADO!!\033[m'.format(n1, n2))
elif everage >= 5 and everage < 7:
    print('\033[1;34mSuas notas {:.1f} e {:.1f} não atingiram a média 7. Você está de RECUPERAÇÃO!!\033[m'.format(n1, n2))
elif everage >= 7:
    print('\033[1;32mSuas notas {:.1f} e {:.1f} atingiram a média 7. VOCÊ FOI APROVADO!!\033[m'.format(n1, n2))
