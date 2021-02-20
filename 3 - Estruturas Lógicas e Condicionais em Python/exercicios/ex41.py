"""
41. Faça um algoritmo que calcule o IMC de uma pessoa e mostre sua classificação
de acordo com a tabela abaixo:

IMC             Classificação
< 18,5          Abaixo do peso
18,5 - 24,9     Saudável
25 - 29,9       Peso em Excesso
30 - 34,9       Obesidade Grau I
35 - 39,9       Obesidade Grau II (severa)
>= 40           Obesidade Grau III (mórbida)
"""
altura = float(input('Digite sua altura em metros (ex: 1.67): '))
peso = float(input('Digite seu peso em kgs (ex: 67.8): '))
imc = peso / (altura * altura)

if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Saudável')
elif imc < 30:
    print('Peso em excesso')
elif imc < 35:
    print('Obesidade Grau I')
elif imc < 40:
    print('Obesidade Grau II (severa)')
else:
    print('Obesidade Grau III (mórbida)')
