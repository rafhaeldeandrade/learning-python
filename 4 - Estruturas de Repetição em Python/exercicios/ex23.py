"""
23. Faça um algoritmo que leia um número positivo e imprima seus divisores.
"""
n = int(input('Digite um número positivo: '))

if n > 0:
    for i in range(1, n+1):
        if n % i == 0:
            print(i, end=' ')
