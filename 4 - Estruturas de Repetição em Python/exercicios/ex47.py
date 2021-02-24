"""
47.	Faça um programa que apresente um menu de opções para o calculo das seguintes operações entre dois números.:
*	adição (opção 1)
*	subtração (opção 2)
*	multiplicação (opção 3)
*	divisão (opção 4)
*	saída (opção 5)
O programa deve possibilitar ao usuário a escolha da operação desejada, a exibição do resultado e a volta ao menu de opções.
O programa só termina quando for escolhida a opção de saída (opção 5).
"""
while True:
    menu = input("""Menu de opções
Digite 1 para adição
Digite 2 para subtração
Digite 3 para multiplicação
Digite 4 para divisão
Digite 5 para sair
Sua opção: """)

    if menu == '1':
        print('Adição')
        numero_um = float(input('Digite o primeiro número: '))
        numero_dois = float(input('Digite o segundo número: '))
        print(f'{numero_um} + {numero_dois} = {numero_um + numero_dois}')
    elif menu == '2':
        print('Subtração')
        numero_um = float(input('Digite o primeiro número: '))
        numero_dois = float(input('Digite o segundo número: '))
        print(f'{numero_um} - {numero_dois} = {numero_um - numero_dois}')
    elif menu == '3':
        print('Multiplicação')
        numero_um = float(input('Digite o primeiro número: '))
        numero_dois = float(input('Digite o segundo número: '))
        print(f'{numero_um} * {numero_dois} = {numero_um * numero_dois}')
    elif menu == '4':
        print('Divisão')
        numero_um = float(input('Digite o primeiro número: '))
        numero_dois = float(input('Digite o segundo número: '))
        if numero_dois == 0:
            print('O segundo número não pode ser 0.')
        else:
            print(f'{numero_um} / {numero_dois} = {numero_um / numero_dois}')
    elif menu == '5':
        print('Saindo...')
    else:
        print('Opção errada. Digite uma opção entre 1 e 5')
