"""
36. Faça um programa que calcule a diferença entre a soma dos quadrados dos primeiros
100 números naturais e o quadrado da soma. Ex: A soma dos quadrados dos dez pri­meiros
números naturais é: 1^2 + 2^2 ^ ... 10 ^2
O quadrado da soma dos dez primeiros números naturais é (1 + 2 + 3 + ... + 10) ^ 2
A diferença entre a soma dos quadrados dos dez primeiros números naturais e o quadrado
da soma é 3025 - 385 = 2640
"""
soma_quadrado = 0
quadrado_soma = 0
for i in range(1, 101):
    soma_quadrado += i ** 2
    quadrado_soma += i
print(f"""A soma dos quadrados dos 100 primeiros números naturais é: {soma_quadrado}
O quadrado da soma dos 100 primeiros números naturais é: {quadrado_soma}
A diferença entre a soma dos quadrados e o quadrado da soma é: {soma_quadrado - (quadrado_soma ** 2)}""")
