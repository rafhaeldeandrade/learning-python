"""
Faça um programa que receba do usuário um vetor com 10 posições. Em seguida
deverá ser impresso o maior e o menor elemento do vetor.
"""
vetor = input('Digite um vetor com 10 valores separados por espaço, ex: 1 2 3 4 5 6 7 8 9 10: ').split()
if len(vetor) != 10:
    print(f'Você digitou um vetor com {len(vetor)} posição/posições. Dígite um vetor com 10 valores.')
else:
    for i in range(len(vetor)):
        vetor[i] = int(vetor[i])
    print(f'Valor mínimo do vetor: {min(vetor)}\nValor máximo do vetor: {max(vetor)}')
