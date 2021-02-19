"""
14.	A nota final de um estudante é calculada a partir de três notas atribuídas entre o intervalo de 0 até 10,
respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame final.
A média das três notas mencionadas anteriormente obedece aos pesos: 
Trabalho de Laboratório: 2;
Avaliação Semestral: 3;
Exame Final: 5.
De acordo com o resultado, mostre na tela se o aluno está reprovado (média entre 0 e 2,9),
de recuperação (entre 3 e 4,9) ou se foi aprovado.
Faça todas as verificações necessárias.
"""
nota_um = float(input('Digite a primeira nota: '))
nota_dois = float(input('Digite a segunda nota: '))
nota_tres = float(input('Digite a terceira nota: '))

if nota_um and nota_dois and nota_tres >= 0 and nota_um and nota_dois and nota_tres <= 10:
    nota_media = (nota_um * 2 + nota_dois * 3 + nota_tres * 5) / 9
    if nota_media <= 2.9:
        print(f'Aluno está reprovado, média: {nota_media:2f}')
    elif nota_media >= 3 and nota_media <= 4.9:
        print(f'Aluno está de recuperação, média: {nota_media:.2f}')
    else:
        print(f'Aluno está aprovado, média: {nota_media:2f}')
else:
    print('Os valores para as notas devem estar entre 0 e 10')
