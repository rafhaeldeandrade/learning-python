"""
Faça um programa que calcule o menor número divisível por cada um dos números de 1 a 20.
Ex: 2520 é o menor número que pode ser dividido por cada um dos números de 1 a 1O, sem sobrar resto.
"""
inicio = 1
contador = 0

while True:
    for i in range(1, 21):
        if inicio % i == 0:
            contador += 1
    if contador == 20:
        break
    else:
        inicio += 1
        contador = 0
print(inicio)
