"""
17.	Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que:
(basemaior + basemenor) * altura
Lembre-se a base maior e a base menor devem ser números maiores que zero
"""
base_maior = float(input('Digite a base maior do trapézio: '))
base_menor = float(input('Digite a base menor do trapézio: '))
altura = float(input('Digite a altura do trapézio: '))

if base_maior < 0 or base_menor < 0:
    print('As bases precisam ser maiores que 0')
else:
    print(f'Base maior: {base_maior}\nBase menor: {base_menor}\nAltura: {altura}\nA área é: {(base_maior + base_menor) * altura}')
