"""
37.	Faça um programa que leia o valor de um produto e imprima o valor com desconto, tendo em vista que o desconto foi de 12%
"""
valor_produto = float(input('Digite o valor do produto: '))
valor_desconto = 12
valor_final = valor_produto - (valor_produto * valor_desconto / 100)
print(f'O valor do produto com desconto é: {valor_final}')
