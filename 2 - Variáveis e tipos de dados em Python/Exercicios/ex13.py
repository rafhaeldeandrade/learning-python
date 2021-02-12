"""
13.	Leia uma distância em quilômetros e apresente-a convertida em milhas.
A fórmula de conversão é: M = K / 1.61 = sendo K a distância em quilômetros e M em milhas.
"""
distancia_quilometros = float(input('Digite uma distância em quilômetros: '))
distancia_milhas = distancia_quilometros / 1.61
print(f'A distância {distancia_quilometros}km corresponde a {distancia_milhas} milhas')
