"""
15.	Leia um ângulo em radianos e apresente-o convertido em graus.
A fórmula de conversão é: G = R * 180/PI, sendo G o ângulo em graus e R em radianos e PI = 3.14.
"""
angulo_radianos = float(input('Digite um angulo em radianos: '))
angulo_graus = angulo_radianos * 180 / 3.14
print(f'O ângulo {angulo_radianos} radianos corresponde a {angulo_graus} graus')
