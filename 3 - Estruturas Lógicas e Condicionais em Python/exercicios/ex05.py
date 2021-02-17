"""
5.	Faça um programa que receba um número inteiro e verifique se este número é par ou ímpar.
"""
numero_inteiro = int(input('Digite um número inteiro: '))

if numero_inteiro % 2 == 0:
    print(f'{numero_inteiro} é par')
else:
    print(f'{numero_inteiro} é ímpar')
