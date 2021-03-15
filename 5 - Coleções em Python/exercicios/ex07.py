"""
7 - Escreva um programa que leia 10 números e armazene em um vetor. Imprima o
vetor, o maior elemento e a posição em que ele se encontra.
"""
vetor = []
for i in range(10):
    int(input(f'Digite um número inteiro para a posição {i}: '))
    vetor.append(i)
print(f'Vetor: {vetor}\nMaior elemento: {max(vetor)}\nPosição do maior elemento: {vetor.index(max(vetor))}')
