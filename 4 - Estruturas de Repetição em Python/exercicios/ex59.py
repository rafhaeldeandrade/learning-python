"""
59. Escreva um programa que leia o número de habitantes de uma determinada cidade e para cada habitante
entre com os seguintes dados: consumo do mês e o código do consumidor
(1- Residencial, 2- Comercial, 3- Industrial). No final imprima o maior, o menor e a média de consumo
dos habitantes; e por fim o total do consumo de cada categoria de consumidor
"""
num_hab = int(input('Digite o número de habitantes: '))
maior_kwh = 0
menor_kwh = 999_999_999_999_999_999_999_999
soma_kwh = 0
res_kwh = 0
com_kwh = 0
ind_kwh = 0

for i in range(1, num_hab + 1):
    consumo = int(input(f'Digite o consumo do mês pro habitante {i}: '))
    codigo_consumidor = input("""Código do consumidor.
Digite 1 para Residência
Digite 2 para Comercial
Digite 3 para Industrial
Sua opção: """)
    if consumo > maior_kwh:
        maior_kwh = consumo
    if consumo < menor_kwh:
        menor_kwh = consumo
    soma_kwh += consumo
    if codigo_consumidor == '1':
        res_kwh += consumo
    elif codigo_consumidor == '2':
        com_kwh += consumo
    else:
        ind_kwh += consumo
print(f"""O maior consumo foi de: {maior_kwh};
O menor consumo foi de: {menor_kwh};
A média de consumo foi de: {soma_kwh/num_hab};
Consumo residencial: {res_kwh};
Consumo comercial: {com_kwh};
Consumo industrial: {ind_kwh}""")
