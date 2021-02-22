"""
Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido.
"""
num_controle = 0
for i in range(10):
    numero = int(input(f'Digite o número {i+1}: '))
    if numero <= num_controle:
        num_controle = numero
print(num_controle)
