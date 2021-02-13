"""
25.	Leia um valor de área em acres e apresente-o convertido em metros quadrados m2.
A fórmula de conversão é: M = A * 4048.58, sendo , a área em metros quadrados e A a érea em acres.
"""
acres = float(input('Digite a área em acres: '))
metros_quadrados = acres * 4048.58
print(f'{acres}ac corresponde a {metros_quadrados}m2')
