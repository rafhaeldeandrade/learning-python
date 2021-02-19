"""
27.	Escreva um programa que, dada a idade de um nadador, classifique-o em uma das seguintes categorias:
Categoria	Idade
Infantil A  5 a 7
Infantil B  8 a 10
Juvenil A   11 a 13
Juvenil B   14 a 17
Senior      maiores de 18 anos
"""
idade = int(input('Digite a idade do nadador: '))

if idade < 5:
    print('Não tem categoria: ')
elif idade >= 5 and idade <= 7:
    print('Categoria Infantil A')
elif idade > 7 and idade <= 10:
    print('Categoria Infantil B')
elif idade > 10 and idade <= 13:
    print('Categoria Juvenil A')
elif idade > 13 and idade <= 17:
    print('Categoria Juvenil B')
else:
    print('Categoria Senior')
