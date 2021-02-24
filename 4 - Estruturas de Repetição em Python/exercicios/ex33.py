"""
33. Dados n e dois números inteiros positivos, i e j, diferentes de 0, imprimir
em ordem crescente os n primeiros naturais que são múltiplos de i ou de j e ou de ambos.
Exemplo: Para n = 6, i = 2 e j = 3 a saída devera ser: 2,3,4,6,8,10.
"""
n = int(input('Digite quantos números serão impressos: '))
numero_um = int(input('Digite o primeiro número inteiro positivo: '))
numero_dois = int(input('Digite o segundo número inteiro positivo: '))
contagem = 0

if n > 0 and numero_um > 0 and numero_dois > 0:
    while True:
        if numero_um > numero_dois:
            for i in range(1, n + 1):
                print(i*numero_dois, end=' ')
                contagem += 1
                if contagem >= n:
                    break
                print(i*numero_um, end=' ')
                contagem += 1
                if contagem >= n:
                    break
        if contagem >= n:
            break
        else:
            for i in range(1, n + 1):
                print(i*numero_um, end=' ')
                contagem += 1
                if contagem >= n:
                    break
                print(i*numero_dois, end=' ')
                contagem += 1
                if contagem >= n:
                    break
        if contagem >= n:
            break
else:
    print('Erro. Os números digitados precisam ser maiores que 0.')
