"""
Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius.
A fórmula é: C = K - 273.15, onde C é a temperatura em Celsius e K a temperatura em Kelvin.
"""
temperatura_kelvin = float(input('Digite uma temperatura em graus Kelvin: '))
temperatura_celsius = temperatura_kelvin - 273.15
print(f'A temperatura {temperatura_kelvin} graus Kelvin em Celsius é: {temperatura_celsius}')
