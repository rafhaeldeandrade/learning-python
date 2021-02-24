"""
11.	Faça um programa que leia um número inteiro positivo N e imprima todos os números
naturais de 0 até N em ordem crescente.
"""
n = int(input('Digite um número natural positivo: '))

if n > 0:
    for i in range(n+1):
        print(i)
else:
    print('Erro. Digite um número inteiro natural positivo.')
