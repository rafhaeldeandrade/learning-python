"""
Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado das componentes deste vetor,
armazenando o resultado em outro vetor. Os conjuntos têm 1O elementos cada. Imprimir todos os conjuntos.
"""
num_quadrado = []
num = input("""Digite um conjunto de números inteiros com 10 elementos, separados por espaço.
Exemplo:
1 2 3 59 673 34 83 364 33 56
Seu conjunto: """).split()

for i in range(10):
    num[i] = int(num[i])
    num_quadrado.append(num[i] ** 2)
print(num)
print(num_quadrado)
