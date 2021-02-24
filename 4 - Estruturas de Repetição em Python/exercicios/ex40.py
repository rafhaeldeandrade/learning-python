"""
40.	Elabore um programa que faça leltura de vários números inteiros, até que se digite um número negativo.
O programa tem que retornar o maior e o menor número lido
"""
maior = 0
menor = 100_000_000_000_000_000_000
while True:
    numero = int(input('Digite um número inteiro: '))
    
    if numero >= 0:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
    else:
        break
print(f'Maior: {maior}\nMenor: {menor}')
