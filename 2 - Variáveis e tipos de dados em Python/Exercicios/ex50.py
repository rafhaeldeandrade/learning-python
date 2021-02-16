"""
50.	Implemente um programa que calcule o ano de nascimento de uma pessoa a partir de sua idade e do ano atual.
Não leva em consideração o mês, pode errar em muitos casos
"""
idade = int(input('Digite sua idade: '))
ano_atual = int(input('Digite o ano atual: '))
print(f'Ano de nascimento: {ano_atual - idade}')
