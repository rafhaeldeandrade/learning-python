"""
49.	O funcionário chamado Carlos. tem um colega chamado João que recebe um salário
que equivale a um terço do seu salário. Carlos gosta de fazer aplicações na caderneta
de poupança e vai aplicar seu salário integralmente nela, pois está rendendo 2% ao mês.
João aplicará seu salário integralmente no fundo de renda fixa, que está rendendo 5%
ao mês. Construa um programa que deverá calcular e mostrar a quantidade de meses
necessários para que o valor pertencente a João iguale ou ultrapasse o valor pertencente
a Carlos.
"""
salario_carlos = 900
salario_joao = 300
contador = 0

while True:
    salario_carlos += salario_carlos * 0.02
    salario_joao += salario_joao * 0.05
    contador += 1
    if salario_joao >= salario_carlos:
        print(f'Quantidade de meses: {contador}')
        break
