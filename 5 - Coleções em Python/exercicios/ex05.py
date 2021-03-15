"""
5 - Leia um vetor de 10 posições. Contar e escrever quantos valores pares ele
possui
"""
par = 0
vetor = input('Digite um vetor de 10 posições separados por espaço (ex: 1 2 3 4 5 6 7 8 9 10): ').split()
for i in range(10):
    if int(vetor[i]) % 2 == 0:
        par += 1
print(f'Existem {par} valores pares nesse vetor.')
