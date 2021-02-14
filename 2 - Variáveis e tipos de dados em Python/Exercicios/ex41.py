"""
41.	Faça um programa que leia o valor da hora de trabalho (em reais) e número de horas trabalhadas no mês.
Imprima o valor a ser pago ao funcionário, adicionando 10% sobre o valor calculado.
"""
valor_horas_trabalho = float(input('Digite o valor da hora de trabalho: '))
horas_trabalho = int(input('digite o número de horas trabalhadas no mês: '))
valor_a_ser_pago = valor_horas_trabalho * horas_trabalho * 1.1
print(f'O valor a ser pago ao funcionário é de: {valor_a_ser_pago}R$')
