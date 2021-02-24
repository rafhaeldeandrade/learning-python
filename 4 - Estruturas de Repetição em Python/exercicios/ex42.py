"""
42.	Faça um programa que leia um conjunto não determinado de valores, um de cada vez
e escreva para cada um dos valores lidos, o quadrado, o cubo e a raiz quadrada. Finalize
a entrada de dados com um valor negativo ou zero.
"""
while True:
    numero = float(input('Digite um número: '))
    if numero <= 0:
        break
    else:
        print(f'{numero ** 2}, {numero ** 3}, {numero ** 0.5}')
