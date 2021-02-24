"""
56.	Faça um programa que calcule a soma de todos os números primos abaixo de dois milhões
"""
contador = 2
num_de_primos = 0
soma_de_primos = 0
contagem_primo = 0
while contador < 2_000_000:
    for i in range(1, contador+1):
        if contador % i == 0:
            contagem_primo += 1
    if contagem_primo == 2:
        soma_de_primos += contador
        num_de_primos += 1
        contador += 1
        contagem_primo = 0
    else:
        contagem_primo = 0
        contador += 1
print(soma_de_primos)
