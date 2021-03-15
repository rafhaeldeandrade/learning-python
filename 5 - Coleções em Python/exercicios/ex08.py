"""
Crie um programa que leia 6 valores inteiros e, em seguida, mostre na tela os
valores lidos na ordem inversa.
"""
vetor = []
for i in range(1, 7):
    valor_inteiro = int(input(f'Digite o valor {i}: '))
    vetor.append(valor_inteiro)
for i in range(-1, -7, -1):
    print(vetor[i])
