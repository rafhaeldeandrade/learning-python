"""
3.	Leia um numero real. Se o número for positivo imprima a raiz quadrada. Do contrário, imprima o numero ao quadrado.
"""
numero_real = float(input('Digite um número real: '))

if numero_real > 0:
    print(f'Raiz quadrada de {numero_real} é: {numero_real ** 0.5}')
else:
    print(f'{numero_real} ao quadrado é igual a: {numero_real ** 2}')
