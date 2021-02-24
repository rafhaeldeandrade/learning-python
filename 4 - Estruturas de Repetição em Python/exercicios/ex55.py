"""
55. Escreva um programa que leia um inteiro não negativo n e imprima
a soma dos n primei­ros números primos.
"""
numero = int(input('Digite um número inteiro não negativo: '))
contador = 2
num_de_primos = 0
soma_de_primos = 0
contagem_primo = 0

if numero > 0:
    while num_de_primos < numero:
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
else:
    print('Digite um número maior que 0')
print(f'Soma dos n primeiros primos: {soma_de_primos}')
