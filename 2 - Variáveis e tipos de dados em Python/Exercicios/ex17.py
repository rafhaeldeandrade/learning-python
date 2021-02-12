"""
17.	Leia um valor de comprimento em centímetros e apresente-o convertido em polegadas.
A fórmula de conversão é: P = C/2.54 sendo C o comprimento em centímetros e P o comprimento em polegadas.
"""
centimetros = float(input('Digite um comprimento em centimetros: '))
polegadas = centimetros / 2.54
print(f'{centimetros}cm corresponde a {polegadas}pol')
