"""
14.	Leia um ângulo em graus e apresente-o convertido em radianos.
A fórmula de conversão é: R = G * PI/180, sendo G o ângulo em graus e R em radianos e PI = 3.14.
"""
angulo_graus = float(input('Digite um angulo em graus: '))
angulo_radianos = angulo_graus * 3.14 / 180
print(f'O ângulo {angulo_graus} graus corresponde a {angulo_radianos} radianos')
