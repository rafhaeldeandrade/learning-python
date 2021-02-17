"""
2.	Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número.
Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.
"""
numero_recebido = float(input('Digite um número: '))

if numero_recebido > 0:
    print(f'A raiz quadrada de {numero_recebido} é: {(numero_recebido ** 0.5):.4f}')
else:
    print('Número inválido.')
