"""
8.	Faça um programa que leia 2 notas de um aluno, verifique se as notas sâo válidas e exiba na tela a média destas notas.
Uma nota válida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0, onde caso a nota não possua um valor válido,
este fato deve ser informado ao usuário e o programa termina.
"""
nota_um = float(input('Digite a primeira nota: '))
nota_dois = float(input('Digite a segunda nota: '))

if nota_um and nota_dois >= 0 and nota_um and nota_dois <= 10:
    print(f'A média das notas é: {(nota_um + nota_dois) / 2}')
else:
    print('Valor inválido, digite números entre 0.0 e 10.0')
