"""
Leia uma velocidade em km/h (quilômetros por hora) e apresente-a convertida em m/s (metros por segundo)
A fórmula da conversão é M = K/3.6, sendo K a velocidade em km/h e M em m/s
"""
velocidade_km = float(input('Digite uma velocidade em km/s: '))
print(f'A velocidade {velocidade_km}km/h em m/s é: {velocidade_km / 3.6}m/s')
