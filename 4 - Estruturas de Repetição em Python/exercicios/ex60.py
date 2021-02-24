"""
60.	Faça um programa que leia vários números, calcule e mostre:
(a)	A soma dos números digitados.
(o) A quantidade de números digitados
(e) A média dos números digitados
(d) O maior número digitado
(e) O menor número digitado
(f ) A média dos números pares
Finalize a entrada de dados caso o usuário informe o valor 0.
"""
soma_numeros = 0
qtd_numeros = 0
maior_numero = 0
menor_numero = 999_999_999_999_999_999_999_999
soma_numeros_pares = 0
qtd_numeros_pares = 0
while True:
    numero = int(input('Digite um número, digite 0 se quiser finalizar a entrada de dados: '))
    if numero == 0:
        break
    soma_numeros += numero
    qtd_numeros += 1
    if numero > maior_numero:
        maior_numero = numero
    if numero < menor_numero:
        menor_numero = numero
    if numero % 2 == 0:
        soma_numeros_pares += numero
        qtd_numeros_pares += 1
print(f"""Soma dos números digitados: {soma_numeros};
Quantidade de números digitados: {qtd_numeros};
Média dos números digitados: {soma_numeros/qtd_numeros};
Maior número digitado: {maior_numero};
Menor número digitado: {menor_numero};
Média dos números pares: {soma_numeros_pares/qtd_numeros_pares}""")
