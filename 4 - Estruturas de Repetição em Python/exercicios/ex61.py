"""
61.	Faça um programa que calcule o maior número palíndromo feito a partir do produto de dois números de 3 dígitos.
Ex.: O maior palíndromo feito a partir do produto de dois números de dois dígitos é 9009 = 91*99
"""
valor_um = 0
valor_dois = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        if str(i * j) == str(i * j)[::-1]:
            valor_um = i
            valor_dois = j
print(f'Maior palíndromo feito a partir do produto de dois números de três dígitos é: {valor_um} * {valor_dois}')
