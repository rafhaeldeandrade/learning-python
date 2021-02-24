"""
53. Escreva um programa que leia um número inteiro positivo n e em seguida imprima n.
linhas do chamado Triangulo de Floyd. Para n = , temos.:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
"""
numero = int(input('Digite o número de linhas: '))
contador = 1
digitos = 1

for i in range(1, numero + 1):
    while digitos <= i:
        print(contador, end=' ')
        contador += 1
        digitos += 1
    digitos = 1
    print('\n')
