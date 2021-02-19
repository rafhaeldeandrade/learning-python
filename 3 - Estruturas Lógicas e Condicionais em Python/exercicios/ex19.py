"""
19.	Faça um programa para verificar se um determinado número inteiro e divisível por 3 ou 5, mas não simultaneamente pelos dois.
"""
numero = int(input('Digite um número inteiro para checarmos se é divisível por 3 ou 5, mas não simultaneamente: '))

divisivel_por_tres = False
divisivel_por_cinco = False

if numero % 3 == 0:
    divisivel_por_tres = True

if numero % 5 == 0:
    divisivel_por_cinco = True

if divisivel_por_tres and divisivel_por_cinco:
    print('O número é divisível por 3 e 5 simultaneamente')
elif divisivel_por_tres and not divisivel_por_cinco:
    print('O número é divisível por 3, apenas')
elif divisivel_por_cinco and not divisivel_por_tres:
    print('O número é divisível por 5, apenas')
else:
    print('Número não divisível por 3 ou 5')
