"""
46.	Faça um programa que leia um número inteiro positivo de três dígitos (de 100 a 999).
Gere outro número formado pelos dígitos invertidos do número lido. Exemplo:
"""
numero = int(input('Digite três digitos, para formar um numero de 100 a 999: '))
numero_invertido = str(numero)
print(f'O número gerado pelos dígitos invertidos é: {numero_invertido[::-1]}')
