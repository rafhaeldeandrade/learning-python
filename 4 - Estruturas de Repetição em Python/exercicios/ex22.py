"""
22. Escreva um programa oompleto que permita a qualquer aluno introduzir, pelo teclado, uma sequência arbitrária de notas
(válidas no intervalo de 10 a 20) e que mostre na tela, como resultado, a correspondente média aritmética.
O número de notas com que o aluno pretenda efetuar o cálculo não será fornecido ao programa, o qual terminará quando for
introduzido um valor que não seja válido como nota de aprovação.
"""
qtd = 0
soma = 0
while True:
    nota = int(input('Digite uma nota entre 10 e 20: '))
    if nota > 9 and nota < 21:
        soma += nota
        qtd += 1
    else:
        break
if qtd > 0:
    print(f'A média aritmética das notas digitadas é: {soma/qtd}')
else:
    print('Nenhuma nota válida foi digitada.')
