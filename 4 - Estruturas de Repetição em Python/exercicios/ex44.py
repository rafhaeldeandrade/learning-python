"""
44. Leia um número inteiro positivo do usuário, então, calcule e imprima a sequência Fibonacci
até o primeiro número superior ao número lido. Exemplo, se o usuário informou o número 30,
a sequência a ser impressa será 1 1 2 3 5 8 13 21 34	
"""
num_a = 1
num_b = 0
soma = 0
parar = int(input('Digite um número inteiro positivo: '))

if parar <= 0:
    print('Erro. Digite um número válido.')
else:
    while True:
        if (num_a + num_b) > parar:
            print(f'{num_a + num_b}', end=' ')
            break
        else:
            soma = num_a + num_b
            num_b = num_a
            num_a = soma
            print(f'{soma}', end=' ')
