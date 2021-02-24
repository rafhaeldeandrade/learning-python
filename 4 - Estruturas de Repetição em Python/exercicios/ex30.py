"""
30.	Faça programas para calcular as .seguintes .s.equências.:
1 + 2 + 3 + 4 +	5 ... + n
1 - 2 + 3 - 4 + 5 ... + (2n - 1)
1 + 3 + 5 + 7 + 9 ... + (2n - 1)
"""
n = int(input('Digite um número inteiro positivo: '))
soma = 0

if n > 0:
    for i in range(1, n + 1):
        soma += i
    print(soma)
    soma = 0
    for i in range(1, n + 1):
        if i % 2 == 1:
            soma += i
        else:
            soma -= i
    print(soma)
    soma = 0
    for i in range(1, n + 1, 2):
        soma += i
    print(soma)
else:
    print('Erro. O número deve ser maior que 0.')
