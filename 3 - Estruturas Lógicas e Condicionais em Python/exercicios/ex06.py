"""
6.	Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles, assim como a diferença existente entre ambos.
"""
numero_um = int(input('Digite o primeiro número inteiro: '))
numero_dois = int(input('Digite o segundo número inteiro: '))

if numero_um > numero_dois:
    print(f'{numero_um} é maior e a diferença entre os dois é de {numero_um - numero_dois}')
else:
    print(f'{numero_dois} é maior e a diferença entre os dois é de {numero_dois - numero_um}')
