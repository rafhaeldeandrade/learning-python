"""
27. Em Matemática , o número harmônico designado por H(n) define-se como sendo a soma da série harmónica.
H(n) = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n
Faça um programa que leia um valor n inteiro e positivo e apresente o valor de H(n).
"""
numero = int(input('Digite um número inteiro positivo: '))
soma = 1

if numero > 0:
    for i in range(2, numero + 1):
        soma += (1/i)
else:
    print('Erro. O número digitado deve ser maior que 0.')
print(f'H({numero}): {soma:.3f}')
