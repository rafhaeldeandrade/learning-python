"""
26.	Leia um valor de área em metros quadrados m2 e apresente-o convertido em hectares.
A fórmula de conversão é: H = M * 0,0001, sendo M a área em metros quadrados e H a área em hectares.
"""
metros_quadrados = float(input('Digite a área em metros quadrados: '))
hectares = metros_quadrados * 0.0001
print(f'{metros_quadrados}m2 corresponde a {hectares}ha')
