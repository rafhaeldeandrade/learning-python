"""
50.	Chico tem 1.50 metro e cresce 2 centímetr1os por ano, enquanto Zé tem 1.10 metros
e cresce 3 centímetros por ano. Escreva um programa calcule e imprima quantos anos serão
necessários para que Zé seja maior que Chico.
"""
altura_chico = 150
altura_ze = 110
contador = 0

while True:
    altura_chico += 2
    altura_ze += 3
    contador += 1
    if altura_ze > altura_chico:
        print(f'Quantidade de anos: {contador}')
        break
