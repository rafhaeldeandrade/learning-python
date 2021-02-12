"""
19.	Leia um valor de volume em litros e apresente-o convertido em metros cúbicos m3.
A fórmula de conversão é: M = L/1000 sendo L o volume em litros e M o volume em metros cúbicos.
"""
litros = float(input('Digite o volume em litros: '))
metros_cubicos = litros / 1000
print(f'{litros}l corresponde a {metros_cubicos}m3')
