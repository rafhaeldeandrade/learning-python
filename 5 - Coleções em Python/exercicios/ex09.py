"""
9 - Crie um programa que leia 6 valores inteiros pares e, em seguida, mostre na
tela os valores lidos em ordem inversa.
"""
vetor = []
for i in range(1, 7):
    valor_inteiro = int(input(f'Digite um valor par para a posição {i}: '))
    if valor_inteiro % 2 != 0:
        print('O valor digitado TEM que ser par.')
        exit()
    else:
        vetor.append(valor_inteiro)
for i in range(-1, -7, -1):
    print(vetor[i])
