"""
13.	Faça um algoritmo que calcule a média ponderada das notas de 3 provas.
A primeira e a segunda prova têm peso 1 e a terceira tem peso 2.
Ao final, mostrar a média do aluno e indicar se o aluno foi aprovado ou reprovado.
A nota para aprovação deve ser igual ou superior a 60 pontos.
"""
nota_um = float(input('Digite a nota um: '))
nota_dois = float(input('Digite a nota dois: '))
nota_tres = float(input('Digite a nota três: '))

media_ponderada = (nota_um * 1 + nota_dois * 1 + nota_tres * 2) / 4

if media_ponderada >= 60:
    print(f'Aluno aprovado com média {media_ponderada}')
else:
    print(f'Aluno reprovado, média abaixo de 60: {media_ponderada}')
