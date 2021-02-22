"""
6. Faça um programa que leia 10 inteiros e imprima sua média
"""
soma = 0
for i in range(10):
    valor = int(input(f'Digite o valor {i+1}: '))
    soma += valor
print(soma / 10)
