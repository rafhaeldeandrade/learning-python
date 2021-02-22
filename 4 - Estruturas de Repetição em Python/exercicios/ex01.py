"""
1. Faça um programa que determine o mostre os cinco primeiros, múltiplos de 3, conside­rando números maiores que 0.
"""
qtd = 0
for num in range(1, 100):
    if qtd == 5:
        break
    if num % 3 == 0:
        print(num)
        qtd += 1
