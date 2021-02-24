"""
24. Escreva um programa que leia um número inteiro e calcule a soma de todos os divisores desse número,
com exceção dele próprio.
Ex: a soma dos divisores do mjmero 66 é 1 + 2 + 3 + 6 + 11 + 22 + 33 = 78
"""
n = int(input('Digite um número positivo: '))
soma = 0

if n > 0:
    for i in range(1, n):
        if n % i == 0:
            soma += i
    print(f'A soma dos divisores do número {n} é {soma}')
else:
    print('Erro. Digite um número correto.')
