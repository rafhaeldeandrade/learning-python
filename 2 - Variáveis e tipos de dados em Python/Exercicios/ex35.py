"""
35.	Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação: hipotenusa = a2 + b2.
Faça um programa que receba os valores de a e b e calcule o valor da hipotenusa através da equação.
Imprima o resultado dessa operação.
"""
cateto_um = float(input('Digite o valor do primeiro cateto: '))
cateto_dois = float(input('Digite o valor do segundo cateto: '))
hipotenusa = ((cateto_um ** 2) + (cateto_dois ** 2)) ** 0.5
print(f'A hipotenusa do triangulo é: {hipotenusa}')
