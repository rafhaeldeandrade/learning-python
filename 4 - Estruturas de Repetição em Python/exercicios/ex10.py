"""
10. Faça um programa que calcule e mostre a soma dos 50 primeiros números pares.
"""
qtd = 0
soma = 0
for i in range(0, 120):
    if qtd > 50:
        break
    elif i % 2 == 0:
        soma += i
        qtd += 1
print(soma)
