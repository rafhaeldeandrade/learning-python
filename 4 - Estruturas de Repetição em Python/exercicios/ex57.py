"""
57.	Faça um programa que conte quantos números primos existem entre a e b, onde a e b
são números informados pelo usuário.
"""
num_a = int(input('Digite o número de início da sequência: '))
num_b = int(input('Digite o número final da sequência: '))
contagem_de_primos = 0

if num_a > num_b and num_a > 0 and num_b > 0:
    for i in range(num_b, num_a + 1):
        for j in range(1, i + 1):
            if i % j == 0:
                contagem_de_primos += 1
        if contagem_de_primos == 2:
            print(i, end=' ')
            contagem_de_primos = 0
        else:
            contagem_de_primos = 0
elif num_b > num_a and num_a > 0 and num_b > 0:
    for i in range(num_a, num_b + 1):
        for j in range(1, i + 1):
            if i % j == 0:
                contagem_de_primos += 1
        if contagem_de_primos == 2:
            print(i, end=' ')
            contagem_de_primos = 0
        else:
            contagem_de_primos = 0
else:
    print('Digite os números corretamente, valores maiores que 0')
