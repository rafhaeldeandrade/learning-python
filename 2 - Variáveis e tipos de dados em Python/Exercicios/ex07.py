"""
Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus
Celsius. A fórmula da conversão é: C = 5.0 * (F - 32.0) / 9.0, sendo F
a temperatura em Fahrenheit e C a temperatura em Celsius
"""
temperatura_fahrenheint = float(input('Digite uma temperatura em Fahrenheit: '))
temperatura_celsius = 5.0 * (temperatura_fahrenheint - 32.0) / 9.0
print(f'A temperatura {temperatura_fahrenheint} graus Fahrenheit em Celsius é: {temperatura_celsius}')
