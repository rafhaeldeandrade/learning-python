"""
4 - Faça um programa que leia um vetor de 8 posições e, em seguida, leia também
dois valores X e Y quaisquer correspondentes a duas posições no vetor. Ao final
seu programa deverá escrever a soma dos valores encontrados nas respectivas
posições X e Y
"""
vetor = []
for i in range(8):
    valor_vetor = float(input(f'Digite o valor da posição {i}: '))
    vetor.append(valor_vetor)

indice_x = int(input('Digite o primeiro índice do vetor (entre 0 e 7): '))
indice_y = int(input('Digite o segundo índice do vetor (entre 0 e 7): '))

if indice_x < 0 or indice_x > 7 or indice_y < 0 or indice_y > 7:
    print('O valor do índice deve estar entre 0 e 7.')
else:
    print(f'A soma do valor na posição {indice_x} com o valor da posição {indice_y} é: \
{vetor[indice_x] + vetor[indice_y]}.')
