"""
51. Um funcionário recebe aumento anual. Em 1995 foi contratado por 2000 reais.
Em 1996 recebeu aumento de 1.5%. A partir de 1997, os aumentos sempre correspondem
ao dobro do ano anterior. Faça programa que determine o salário atual do funcionário.
"""
salario_atual = 2000
ano = 1996
aumento = 1

while ano <= 2021:
    salario_atual = salario_atual + salario_atual * 0.015 * aumento
    aumento += 1
    ano += 1
print(f'R${salario_atual:.2f}')
