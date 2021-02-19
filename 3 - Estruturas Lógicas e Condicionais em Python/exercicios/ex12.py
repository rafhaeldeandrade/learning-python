"""
12.	Ler um número inteiro. Se o número lido for negativo, escreva a mensagem “Número inválido”.
Se o número for positivo, calcular o logaritmo deste numero.
"""
import math

numero = int(input('Digite um número inteiro: '))

if numero > 0:
    print(math.log(numero, 10))
else:
    print('Número inválido')
