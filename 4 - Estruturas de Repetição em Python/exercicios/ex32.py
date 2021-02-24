"""
32. Faça um programa que simula o lançamento de dois dados, d1 e d2, n vezes, e tem como
saída o número de cada dado e a relação entre eles (>, < ou =) de cada lançamento
"""
import random

n = int(input('Digite o número de vezes que os dados irão rolar: '))

for i in range(n):
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    if d1 > d2:
        print(f'd1 é maior que d2. d1: {d1}, d2: {d2}')
    else:
        print(f'd2 é maior que d1. d2: {d1}, d1: {d2}')
