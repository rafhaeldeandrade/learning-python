"""
5. Faça um programa que peça para o usuário digitar 10 valores e some-os
"""
soma = 0
for i in range(10):
    valor = int(input(f'Digite o valor {i+1}: '))
    soma += valor
print(soma)
