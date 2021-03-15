"""
10 - Faça um programa para ler a nota da prova de 15 alunos e armazene num
vetor, calcule e imprima a média geral. 
"""
vetor = []
soma_notas = 0
media = 0
for i in range(1, 16):
    nota = float(input(f'Digite a nota da prova do aluno {i}: '))
    vetor.append(nota)
for i in range(len(vetor)):
    soma_notas += vetor[i]
media = soma_notas / len(vetor)
print(f'Média geral: {media:.2f}')
