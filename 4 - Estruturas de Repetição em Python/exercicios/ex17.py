"""
17.	Faça um programa que leia um número inteiro positivo N e calcule a soma dos N primeiros
números naturais.
"""
n = int(input('Digite um número inteiro positivo: '))
soma = 0

if n > 0:
    for i in range(1, n+1):
        soma += i
    print(f'A soma dos números é: {soma}.')
else:
    print('Erro. Digite um número inteiro positivo.')
