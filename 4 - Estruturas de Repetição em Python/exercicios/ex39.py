"""
39. Faça um programa que calcule a área de um triângulo, cuja base e altura são fornecidas pelo usuário.
Esse programa não pode permitir a entrada de dados inválidos, ou seja, medidas menores ou iguais a O.
"""
base = float(input('Digitre a base do triângulo: '))
altura = float(input('Digite a altura do triângulo: '))

if base > 0 and altura > 0:
    print(f'A área do triângulo é {(base * altura) / 2}')
else:
    print('Erro, números devem ser maiores que 0.')
