"""
7.	Faça um programa que receba dois números e mostre o maior.
Se por acaso, os dois números forem iguais, imprima a mensagem Números iguais.
"""
numero_um = float(input('Digite o primeiro número: '))
numero_dois = float(input('Digite o segundo número: '))

if numero_um > numero_dois:
    print(f'{numero_um} é maior')
elif numero_um < numero_dois:
    print(f'{numero_dois} é maior')
else:
    print(f'Os números são iguais.')
