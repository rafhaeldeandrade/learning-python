"""
16.	Leia um valor de comprimento em polegadas e apresente-o convertido em centímetros.
A fórmula de conversão é: C = P * 2.54, sendo C o comprimento em centímetros e P o comprimento em polegadas.
"""
polegadas = float(input('Digite um comprimento em polegadas: '))
centimetros = polegadas * 2.54
print(f'{polegadas}pol corresponde a {centimetros}cm')
