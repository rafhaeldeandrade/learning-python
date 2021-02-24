"""
14.	Faça um programa que leia um número inteiro positivo par N e imprima todos os números
pares de 0 até N em ordem decrescente.
"""
n = int(input('Digite um número inteiro positivo par: '))

if n % 2 == 0 and n > 0:
    for i in range(n, -1, -2):
        print(i)
else:
    print('Erro. Digite um número inteiro positivo par.')
