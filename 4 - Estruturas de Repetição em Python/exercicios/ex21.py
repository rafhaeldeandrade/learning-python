"""
21. Faça um programa que receba 2 números. Calcule e mostre:
* A soma dos números pares desse intervalo de números, incluindo os números digitados
* A multiplicação dos números ímpares desse intervalo, incluindo os digitados.
"""
numero_um = int(input('Digite o primeiro numero: '))
numero_dois = int(input('Digite o segundo número'))
soma_par = 0
multiplicacao_impar = 1

if numero_um > numero_dois:
    for i in range(numero_um, numero_dois+1):
        if i % 2 == 0:
            soma_par += i
        else:
            multiplicacao_impar *= i
else:
    for i in range(numero_dois, numero_um+1):
        if i % 2 == 0:
            soma_par += i
        else:
            multiplicacao_impar *= i
print(f'Soma do intervalo: {soma_par}\nProduto do intervalo: {multiplicacao_impar}')
