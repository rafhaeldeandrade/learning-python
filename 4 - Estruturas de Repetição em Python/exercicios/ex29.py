"""
29.	Escreva um programa para calcular o valor da série.
S = 0 + 1/2! + 2/4! + 3/6! + 4/8! + 5/10!
"""
soma = 0
soma_interna = 1
for i in range(1, 6):
    for j in range(1, i*2+1):
        soma_interna *= j
    soma += (i/soma_interna)
    soma_interna = 1
print(f'O valor da série é: {soma}')
