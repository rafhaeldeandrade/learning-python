"""
21.	Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação esco¬lhida. Escreva uma mensagem de erro se a opção for inválida.
Escolha a opção:
1-	Soma de 2 números.
2-	Diferença entre 2 números (maior pelo menor).
3-	Produto entre 2 números.
4-	Divisão entre 2 números (o denominador não pode ser zero).
"""
operacao = int(input('Digite 1 para somar, 2 para subtrair, 3 para dividir ou 4 para multiplicar: '))

if operacao < 1 or operacao > 4:
    print('Digite um numero entre 1 e 4!')
elif operacao == 1:
    numero_um = float(input('Vamos somar 2 números, digite o primeiro: '))
    numero_dois = float(input('Digite o segundo número: '))
    print(f'O resultado de {numero_um} + {numero_dois} é: {numero_um + numero_dois}')
elif operacao == 2:
    numero_um = float(input('Vamos subtrair um número de outro, maior pelo menor: '))
    numero_dois = float(input('Digite o segundo número: '))
    if numero_um > numero_dois:
        print(f'O resultado de {numero_um} - {numero_dois} é: {numero_um - numero_dois}')
    else:
        print(f'O resultado de {numero_dois} - {numero_um} é: {numero_dois - numero_um}')
elif operacao == 3:
    numero_um = float(input('Vamos multiplicar dois números, digite o primeiro: '))
    numero_dois = float(input('Digite o segundo número: '))
    print(f'O resultado de {numero_um} * {numero_dois} é: {numero_um * numero_dois}')
else:
    numero_um = float(input('Vamos dividir um número pelo outro, digite o dividendo: '))
    numero_dois = float(input('Digite o divisor, maior que 0: '))
    if numero_dois == 0:
        print('O divisor tem que ser maior que 0')
    print(f'O resultado de {numero_um} / {numero_dois} é: {numero_um / numero_dois}')
