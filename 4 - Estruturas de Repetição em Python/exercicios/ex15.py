"""
15.	Faça um programa que leia um número inteiro positivo ímpar N e imprima todos os
números ímpares de 1 até N em ordem crescente.
"""
n = int(input('Digite um número inteiro positivo ímpar: '))

if n % 2 == 1 and n > 0:
    for i in range(1, n+1, 2):
        print(i)
else:
    print('Erro. Digite um número inteiro positivo ímpar.')
