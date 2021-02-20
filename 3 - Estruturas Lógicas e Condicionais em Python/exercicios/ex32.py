"""
32.	Escrever um programa que leia o código do produto escolhido do cardápio de uma lan chonete e a quantidade.
O programa deve calcular o valor a ser pago por aquele lanche. 
Considere que a cada execução somente será calculado um pedido.

O cardápio da lan chonete segue o padrão abaixo:
Especificação	Código	Preço
Cachorro Quente	100	    1.20
Bauru Simples	101	    1.30
Bauru com Ovo	102	    1.50
Hambúrguer	    103	    1.20
Cheeseburguer	104	    1.70
Suco	        105	    2.20
Refrigerante	106	    1.00
"""
menu = input("""Cardápio
Lanche          Código      Valor
Cachorro Quente	  100	    1.20
Bauru Simples	  101	    1.30
Bauru com Ovo	  102	    1.50
Hambúrguer        103       1.20
Cheeseburguer	  104	    1.70
Suco	          105	    2.20
Refrigerante	  106	    1.00
Digite o código do seu pedido: """)
quantidade = int(input('Qual a quantidade?: '))

if menu == '100':
    print(f'O valor a ser pago é de {quantidade * 1.20}')
elif menu == '101':
    print(f'O valor a ser pago é de {quantidade * 1.30}')
elif menu == '102':
    print(f'O valor a ser pago é de {quantidade * 1.50}')
elif menu == '103':
    print(f'O valor a ser pago é de {quantidade * 1.20}')
elif menu == '104':
    print(f'O valor a ser pago é de {quantidade * 1.70}')
elif menu == '105':
    print(f'O valor a ser pago é de {quantidade * 2.20}')
elif menu == '106':
    print(f'O valor a ser pago é de {quantidade * 1.0}')
else:
    print('Digite o código corretamente')
