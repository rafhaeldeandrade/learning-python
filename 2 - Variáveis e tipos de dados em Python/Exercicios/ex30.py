"""
30.	Leia um valor em real e a cotação do dólar. Em seguida, imprima o valor correspondente em dólares.
"""
real = float(input('Digite o valor em real: '))
cotacao_dolar = float(input('1 dólar corresponde a quantos reais?: '))
resultado = real / cotacao_dolar
print(f'{resultado} dólares')
