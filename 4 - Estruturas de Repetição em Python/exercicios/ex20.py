"""
20. Ler uma sequência de números inteiros e determinar se eles são pares ou não.
Deverá ser informado o número de dados lidos de valores pares. O processo termina quando for digitado
o número 1000.
"""
qtd = int(input('Quantos dados serão lidos?: '))
pares = 0

for i in range(1, qtd+1):
    numero = int(input(f'Digite o número {i}/{qtd}, digite 1000 para sair do programa: '))
    if numero % 2 == 0:
        pares +=1
    elif numero == 1000:
        break
print(f'A quantidade de números pares digitados foi: {pares}.')
