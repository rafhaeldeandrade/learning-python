"""
40.	Uma empresa contrata um encanador a R$ 30,00 por dia.
Faça um programa que solicite o número de dias trabalhados pelo encanador e imprima a quantia líquida que deverá ser paga,
sabendo-se que sâo descontados 8% para imposto de renda.
"""
dias_trabalhados = int(input('Digite o número de dias trabalhados: '))
preco_diario = 30.0
imposto_renda = 8.0/100
quantia_liquida = (dias_trabalhados * preco_diario) - (dias_trabalhados * preco_diario * imposto_renda)
print(f'O valor que o encanador receberá depois do imposto descontado é de: {quantia_liquida}')
