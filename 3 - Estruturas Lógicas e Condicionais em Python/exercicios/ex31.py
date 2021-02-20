"""
31.	Faça um programa que receba a altura e o peso de uma pessoa.
De acordo com a tabela a seguir, verifique e mostra qual a classificação dessa pessoa.

Altura	                        Peso
                Até 60  Entre 60 e 90 (inclusive)   Acima de 90
Menor que 1,20    A                D                    G
De 1,20 a 1,70    B                E                    H
Maior que 1,70    C                F                    I
"""
altura = int(input('Digite sua altura em centímetros (número inteiro): '))
peso = float(input('Digite seu peso em KGs (número real): '))

if altura < 120:
    if peso <= 60:
        print('Classificação A')
    elif peso <= 90:
        print('Classificação D')
    else:
        print('Classificação G')
elif altura <= 170:
    if peso <= 60:
        print('Classificação B')
    elif peso <= 90:
        print('Classificação e')
    else:
        print('Classificação h')
else:
    if peso <= 60:
        print('Classificação C')
    elif peso <= 90:
        print('Classificação F')
    else:
        print('Classificação I')
