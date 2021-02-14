"""
38.	Leia o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo que ele recebeu um aumento de 25%.
"""
salario = float(input('Digite o salário de um funcionário: '))
aumento_porcentagem = 25
novo_salario = salario + (salario * aumento_porcentagem / 100)
print(f'O novo salário é de: {novo_salario}')
