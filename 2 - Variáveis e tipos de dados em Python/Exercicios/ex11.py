"""
11.	Leia uma velocidade em m/s (metros por segundo) e apresente-a convertida em km/h (quilómetros por hora).
A fórmula de conversão è: K = M * 3.6, sendo K a velocidade em km/h e AI em m/s.
"""
velocidade_ms = float(input('Digite uma velocidade em m/s: '))
velocidade_kmh = velocidade_ms * 3.6
print(f'A velocidade {velocidade_ms}m/s em km/h é: {velocidade_kmh}km/h')
