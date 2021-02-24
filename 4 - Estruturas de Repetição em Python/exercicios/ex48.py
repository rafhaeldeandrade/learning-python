"""
48. Faça um programa que some os termos de valor par da sequência de Fibonacci, cujos
valores não ultrapassem quatro milhões.
"""
num_a = 1
num_b = 0
soma = 0
total = 0
contador = 0

while True:
    soma = num_a + num_b
    num_b = num_a
    num_a = soma
    if num_a > 4_000_000:
        break
    else:
        total += soma
print(f'{total}')
