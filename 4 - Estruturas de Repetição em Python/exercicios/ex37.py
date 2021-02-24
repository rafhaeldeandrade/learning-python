"""
37. Escreve um programa que verifique quais números entre 1000 e 9999 (inclusive)
pos­suem a seguinte propriedade: a soma dos dígitos de mais baixa ordem com os dois
dígitos de mais alta ordem elevada ao quadrado é igual ao próprio numero.
Por exemplo para o inteiro 3025, temos que:
30 + 25 = 55
55^2 = 3025
"""
for i in range(1000, 10000):
    string_numero = str(i)
    soma_numero = int(string_numero[0:2]) + int(string_numero[2:4])
    if soma_numero ** 2 == i:
        print(i, end=' ')
