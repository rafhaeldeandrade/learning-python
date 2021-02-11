"""
Leia uma temperatura em graus Celsius  e apresente-a convertida em graus Kelvin.
A fórmula é: K = C + 273.15, onde C é a temperatura em Celsius e K a temperatura em Kelvin.
"""
temperatura_celsius = float(input('Digite uma temperatura em graus Celsius: '))
temperatura_kelvin = temperatura_celsius + 273.15
print(f'A temperatura {temperatura_celsius} graus Celsius em Kelvin é: {temperatura_kelvin}')
