"""
28.	Faça um programa que leia três números inteiros positivos e efetue o cálculo
de uma das seguintes médias de acordo com um valor numérico digitado pelo usuário:
(a)	Geométrica: (x * y * z) ** 1/3
(b)	Ponderada: (x * 2 + y * 3 + z) / 6
(c)	Harmónica: 1 / (1/x + 1/y + 1/z)
(d)	Aritmética: x + y + z / 3
"""
x = int(input('Digite o primeiro valor inteiro positivo: '))
y = int(input('Digite o segundo valor inteiro positivo: '))
z = int(input('Digite o terceiro valor inteiro positivo: '))
opcao = input("""Digite: 
a para média geométrica
b para média ponderada
c para media harmônica
d para média aritmética
Sua opção é: """)

if x < 1 or y < 1 or z < 1:
    print('Digite um número inteiro positivo')
elif opcao == 'a':
    media_geometrica = (x * y * z) ** (1/3)
    print(f'A média geométrica é: {media_geometrica}')
elif opcao == 'b':
    media_ponderada = (x * 2 + y * 3 + z) / 6
    print(f'A média ponderada é: {media_ponderada}')
elif opcao == 'c':
    media_harmonica = 1 / (1/x + 1/y + 1/z)
    print(f'A média harmônica é: {media_harmonica}')
elif opcao == 'd':
    media_aritmetica = (x + y + z) / 3
    print(f'A média aritmética é: {media_aritmetica}')
else:
    print('Escolha a opção corretamente; a, b, c ou d')
