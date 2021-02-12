"""21.	Leia um valor de massa em libras e apresente-o convertido em quilogramas.
A fórmula de conversão é: K = L * 0,45, sendo K a massa em quilogramas e L a massa em libras.
"""
libras = float(input('Digite a massa em libras: '))
quilogramas = libras * 0.45
print(f'{libras}lb corresponde a {quilogramas}kg')
