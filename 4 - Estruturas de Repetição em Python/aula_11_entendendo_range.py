"""
Range

* Precisamos conhecer o loop for para usar os ranges
* Precisamos conhecer melhor o range para trabalhar melhor com o for

Range são utilizados para gerar sequências númericas especificadas, não de forma aleatória.

Formas gerais:
range(valor_de_parada)
valor_de_parada não inclusive; início padrão 0 e passo de 1 em 1.
ex:
for num in range(5):
    print(num, end=' ')
output: 0 1 2 3 4

-------------------------------------------------------------------------------

range(valor_de_inicio, valor_de_parada)
valor_de_parada não inclusive; início = valor_de_início e passo de 1 em 1
ex:
for num in range(2, 5):
    print(num, end=' ')
output: 2 3 4

-------------------------------------------------------------------------------

range(valor_de_inicio, valor_de_parada, passo)
valor_de_parada não inclusive; início = valor_de_início e passo especificado
ex:
for num in range(1, 6, 2):
    print(num, end=' ')
output: 1 3 5

-------------------------------------------------------------------------------

range(valor_de_inicio, valor_de_parada, passo_negativo)
valor_de_parada não inclusive; início = valor_de_início e passo especificado
ex:
for num in range(10, 1, -1):
    print(num, end=' ')
output: 10 9 8 7 6 5 4 3 2
"""
lista = list(range(10))
print(lista)

for num in range(5):
    print(num, end=' ')

for num in range(2, 5):
    print(num, end=' ')

for num in range(1, 6, 2):
    print(num, end=' ')

for num in range(10, 1, -1):
    print(num, end=' ')
