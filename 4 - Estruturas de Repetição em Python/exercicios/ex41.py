"""
41.	Faça um programa que calcula a associação em paralelo de dois resistores Rl e R2
fornecidos pelo usuário via teclado. O programa fica pedindo estes valores e calculando
até que o usuário entre com um valor para resistência igual a 0
R = R1 * R2 / (R1 + R2)
"""
while True:
    r1 = float(input('Digite a resistência do primeiro resistor: '))
    r2 = float(input('Digite a resistência do segundo resistor: '))
    if r1 <= 0 or r2 <= 0:
        break
    else:
        r = r1 * r2 / (r1 + r2)
        print(r)
