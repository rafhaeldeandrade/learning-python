"""
20.	Dados três valores, A, B, C, verificar se eles podem ser valores dos lados de um triângulo e, se forem,
se é um triângulo escaleno, equilátero ou isóscele, considerando os seguin¬tes conceitos:
*	O comprimento de cada lado de um triângulo é menor do que a soma dos outros dois lados.
*	Chama-se equilátero o triângulo que tem três lados iguais.
*	Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
*	Recebe o nome de escaleno o triângulo que tem os très lados diferentes.
"""
lado_um = float(input('Digite o primeiro lado do triangulo: '))
lado_dois = float(input('Digite o segundo lado do triangulo: '))
lado_tres = float(input('Digite o terceiro lado do triangulo: '))

if lado_um > lado_dois + lado_tres or lado_dois > lado_um + lado_tres or lado_tres > lado_um + lado_dois:
    print('Digite corretamente os valores.')
elif lado_um == lado_dois and lado_um == lado_tres:
    print('É um triângulo equilátero.')
elif lado_um == lado_dois or lado_dois == lado_tres or lado_tres == lado_um:
    print('É um triângulo isósceles.')
else:
    print('É um triângulo escaleno.')
