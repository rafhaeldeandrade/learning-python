"""
Leia uma temperatura em graus Celsius e apresente-a convertida em graus
Fahrenheit. A fórmula da conversão é: F = C * (9.0/5.0) + 32.0, sendo F
a temperatura em Fahrenheit e C a temperatura em Celsius
"""
temperatura_celsius = float(input('Digite uma temperatura em Celsius: '))
temperatura_fahrenheint = temperatura_celsius * (9.0/5.0) + 32.0
print(f'A temperatura {temperatura_celsius} graus Celsius em Fahrenheit é: {temperatura_fahrenheint}')
