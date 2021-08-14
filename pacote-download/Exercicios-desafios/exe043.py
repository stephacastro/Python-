'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu indice de massa corporal(IMC)
e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Obesidade
- Acima de 40: Obesidade mórbida'''

# weight - peso em english
weight = float(input('Qual é o seu peso? (Kg) '))
# height - altura em english
height = float(input('Qual é a sua altura? (M) '))

imc = weight / (height ** 2)

print('\nSeu peso é {} kg, sua altura é {}m e seu IMC é {:.1f}'.format(weight, height, imc))

if imc < 18.5:
    print('\nCUIDADO!! Você esta Abaixo do Peso normal')
elif imc >= 18.5 and imc < 25:
    print('\nPARABÉNS! Você esta no Peso Ideal!')
elif imc >= 25 and imc < 30:
    print('\nATENÇÃO! Você esta em Sobrepeso')
elif imc >= 30 and imc < 40:
    print('\nFIQUEI ATENTO!! Você esta em Obesidade')
elif imc > 40:
    print('\nCUIDADO!! Você esta em Obesidade Mórbida')

''' Outro jeito de fazer que o python entende 
if imc < 18.5:
    print('CUIDADO!! Você esta Abaixo do Peso normal')
elif  18.5 <= imc < 25:
    print('PARABÉNS! Você esta no Peso Ideal!')
elif  25 <= imc < 30:
    print('ATENÇÃO! Você esta em Sobrepeso')
elif 30 <= imc < 40:
    print('FIQUEI ATENTO!! Você esta em Obesidade')
elif imc > 40:
    print('CUIDADO!! Você esta em Obesidade Mórbida')
'''
