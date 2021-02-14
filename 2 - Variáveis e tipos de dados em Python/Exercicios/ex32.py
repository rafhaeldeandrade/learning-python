"""
32.	Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dobro.
"""
numero_inteiro = int(input('Digite um número inteiro: '))
resultado = ((numero_inteiro * 3) + 1) + ((numero_inteiro * 2) - 1)
print(f'A soma do sucessor de seu triplo com o antecessor de seu dobro é {resultado}')
