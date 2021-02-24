"""
18. Escreva um algoritmo que leia certa quantidade de números
 e imprima o maior deles e quantas vezes o maior número foi lido.
A quantidade de números a serem lidos deve ser fornecida pelo usuário.
"""
n = int(input('Quantos números devem ser lidos?: '))
qtd = 0
maior = 0

if n > 0:
    for i in range(1, n+1):
        numero = int(input(f'Digite o numero {i}/{n}: '))
        if numero > maior:
            qtd = 1
            maior = numero
        elif numero == maior:
            qtd += 1
else:
    print('Digite um número inteiro maior que 0.')
print(f'O maior número foi {maior} e apareceu {qtd} vez(es)')
