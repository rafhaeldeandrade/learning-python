"""
12.	Leia uma distância em milhas e apresente-a convertida em quilómetros. 
A fórmula de conversão é: K = 1,61 * M, sendo K a distância em quilómetros e M em milhas.
"""
distancia_milhas = float(input('Digite uma distância em milhas: '))
distancia_quilometros = 1.61 * distancia_milhas
print(f'A distância {distancia_milhas} milhas corresponde a {distancia_quilometros}km')
