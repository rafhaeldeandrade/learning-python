"""
43.	Faça um programa que leia um número indeterminado de idades de indivíduos (pare
quando for informada a idade 0), e calcule a idade média desse grupo.
"""
idade_soma = 0
idade_quantidade = 0
while True:
    idade = int(input('Digite a idade: '))
    if idade <= 0:
        break
    else:
        idade_soma += idade
        idade_quantidade += 1
print(idade_soma / idade_quantidade)
