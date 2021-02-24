"""
28.	Faça um programa que leia um valor	inteiro e positivo, calcule o mostre o valor E,
conforme a fórmula a seguir
E = 1+ 1/1! + 1/2! + 1/3! + ... + 1/N!
"""
numero = int(input('Digite um número inteiro e positivo: '))
soma = 1

if numero > 0:
    soma_interna = 1
    for i in range(1, numero + 1):
        for j in range(1, i + 1):
            soma_interna *= j
        soma += (1/soma_interna)
        soma_interna = 1
else:
    print('Erro. O número digitado deve ser maior que 0.')
print(soma)
