"""
36.	Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro.
O volume de um cilindro circular é calculado por meio da seguinte fórmula: V = PI * raio2 * altura, onde PI = 3.141592.
"""
altura_cilindro = float(input('Digite a altura do cilindro: '))
raio_cilindiro = float(input('Digite o raio do cilindro: '))
volume_cilindro = 3.141592 * (raio_cilindiro ** 2) * altura_cilindro
print(f'O volume do cilindro é: {volume_cilindro}')
