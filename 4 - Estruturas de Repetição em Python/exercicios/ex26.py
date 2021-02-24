"""
Faca um algoritmo que encontre o primeiro múltiplo de 11, 13 ou 17 após um número dado.
"""
numero_dado = int(input('Digite um número: '))

while True:
    if (numero_dado + 1) % 11 == 0 or (numero_dado + 1) % 13 == 0 or (numero_dado + 1) % 17 == 0:
        print(numero_dado + 1)
        break
    numero_dado += 1
