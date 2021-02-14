"""
42.	Receba o salário-base de um funcionário.
Calcule e imprima o salário a receber, sabendo- se que esse funcionário tem uma gratificação de 5% sobre o salário-base.
Além disso, ele paga 7% de imposto sobre o salário-base.
"""
salario_base = float(input('Digite o salário base de um funcionário: '))
print(f'O salário final é: {salario_base + (salario_base * 0.05) - (salario_base * 0.07)}')
