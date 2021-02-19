"""
18.	Faça um programa que mostre ao usuário um menu com 4 opções de operações ma-temáticas (as básicas, por exemplo).
O usuário escolhe uma das opções e o seu pro-grama então pede dois valores numéricos e realiza a operação,
mostrando o resultado e saindo.
"""
operacao = int(input('Digite 1 para somar, 2 para subtrair, 3 para dividir ou 4 para multiplicar: '))

if operacao < 1 or operacao > 4:
    print('Digite um numero entre 1 e 4!')
elif operacao == 1:
    numero_um = float(input('Vamos somar 2 números, digite o primeiro: '))
    numero_dois = float(input('Digite o segundo número: '))
    print(f'O resultado de {numero_um} + {numero_dois} é: {numero_um + numero_dois}')
elif operacao == 2:
    numero_um = float(input('Vamos subtrair um número de outro, digite o minuendo: '))
    numero_dois = float(input('Digite o subtraendo: '))
    print(f'O resultado de {numero_um} - {numero_dois} é: {numero_um - numero_dois}')
elif operacao == 3:
    numero_um = float(input('Vamos dividir um número pelo outro, digite o dividendo: '))
    numero_dois = float(input('Digite o divisor, maior que 0: '))
    if numero_dois == 0:
        print('O divisor tem que ser maior que 0')
    print(f'O resultado de {numero_um} / {numero_dois} é: {numero_um / numero_dois}')
else:
    numero_um = float(input('Vamos multiplicar dois números, digite o primeiro: '))
    numero_dois = float(input('Digite o segundo número: '))
    print(f'O resultado de {numero_um} * {numero_dois} é: {numero_um * numero_dois}')
