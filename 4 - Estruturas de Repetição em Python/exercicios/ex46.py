"""
46. Faça um programa que gera um número aleatório de 1 a 1000.
O usuário deve tentar acertar qual o número foi gerado, a cada tentativa o programa deverá
informar se o chute é menor ou maior que o número gerado.
O programa acaba quando o usuário acerta o número gerado.
O programa deve informar em quantas tentativas o número foi descoberto.
"""
import random

qtd = 0
numero = random.randint(1, 1000)
while True:
    tentativa = int(input('Chute um número: '))
    if tentativa > numero:
        print('O número gerado é menor do que a tentativa.')
        qtd += 1
    elif tentativa < numero:
        print('O número gerado é maior do que a tentativa.')
        qtd += 1
    else:
        print(f'Acertou o número gerado em {qtd} tentativa(s)')
        break
