"""
Faça um programa que leia um número inteiro N e depois  imprima os N primeiros números naturais ímpares.
"""
qtd = int(input('Quantos números deveremos imprimir: '))
qtd_impar = 0

if qtd <= 0:
    print('Digite um valor maior que 0.')
else:
    for i in range(1, qtd * 3):
        if qtd_impar == qtd:
            break
        elif i % 2 != 0:
            print(i)
            qtd_impar += 1
