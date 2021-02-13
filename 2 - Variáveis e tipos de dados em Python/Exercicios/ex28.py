"""
28.	Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos três valores lidos.
"""
valor_um = float(input('Digite o primeiro valor: '))
valor_dois = float(input('Digite o segundo valor: '))
valor_tres = float(input('Digite o terceiro valor: '))
resultado = (valor_um ** 2) + (valor_dois ** 2) + (valor_tres ** 2)
print(f'A soma dos quadrados dos três valores é: {resultado}')
