"""
22.	Leia um valor de comprimento em jardas e apresente-o convertido em metros.
A fórmula de conversão é: M = 0,91 * J, sendo J o comprimento em jardas e M o comprimento em metros.
"""
jardas = float(input('Digite o comprimento em jardas: '))
metros = 0.91 * jardas
print(f'{jardas}yd corresponde a {metros}m')
