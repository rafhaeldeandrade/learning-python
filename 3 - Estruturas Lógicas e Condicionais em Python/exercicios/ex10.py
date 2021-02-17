"""
10.	Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal,
utilizando as seguintes fórmulas (onde h corresponde à altura em m):
*	Homens: (72,7 * h) - 58
*	Mulheres: (62,1 * h) - 44,7
"""
altura = float(input('Digite a altura em m: '))
sexo = input('Digite H para homem ou M para mulher: ')

if sexo == 'H' or sexo == 'h':
    print(f'O peso ideal é {(72.7 * altura) - 58}kg')
elif sexo == 'M' or sexo == 'm':
    print(f'O peso ideal é {(62.1 * altura) - 44.7}')
else:
    print('Valores inválidos, digite H/h ou M/m para o sexo.')
