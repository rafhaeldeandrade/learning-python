"""
35. Faça um programa que some os números impares contidos em um intervalo definido pelo usuário.
O usuário o valor inicial do intervalo e o valor final deste intervalo e o programa deve somar
todos os números ímpares oontidos neste intervalo. Caso o usuário digite um intervalo inválido
(começando por um valor maior que o valor final) deve ser escrito uma mensagem de erro na tela,
"Intervalo de valores inválido" e o programa termina.
Exemplo de tela de saída:
Digite o valor incial e o valor final: 5 10
Soma dos ímpares nesse intervalo: 21
"""
intervalo = input('Digite o valor inicial e o final do intervalo (ex: 5 10): ').split()
soma = 0

if int(intervalo[0]) < int(intervalo[1]):
    for i in range(int(intervalo[0]), int(intervalo[1]) + 1):
        if i % 2 != 0:
            soma += i
    print(f'Soma dos ímpares nesse intervalo: {soma}')
else:
    print('Intervalo de valores inválido.')
