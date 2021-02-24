"""
19. Escreva um algoritmo que leia um número inteiro entre 100 e 999 e imprima na saída
cada um dos algarismos que compoem o número
"""
numero = int(input('Digite um número inteiro entre 100 e 999: '))

if numero > 99 and numero < 1000:
    for i in str(numero):
        print(i, end=' ')
else:
    print('Erro. O número deve ser inteiro e maior que 0.')
