"""
7. Faça um programa que leia 10 inteiros positivos. ignorando não positivos, e imprima sua média.
"""
soma = 0
qtd = 0
for i in range(10):
    valor = int(input(f'Digite o valor {i+1}: '))
    if valor > 0:
        soma += valor
        qtd += 1
print(soma / qtd)
