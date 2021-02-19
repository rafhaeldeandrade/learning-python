"""
15.	Usando switch, escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este numero.
Isto é, domingo se l, segunda-feira se 2, e assim por diante.
"""
switch_dia_semana = int(input("""Digite um numero inteiro entre 1 e 7\nSua escolha é: """))

if switch_dia_semana < 1 or switch_dia_semana > 7:
    print('Digite um número entre 1 e 7')
elif switch_dia_semana == 1:
    print('1 Corresponde a segunda-feira')
elif switch_dia_semana == 2:
    print('2 corresponde a terça-feira')
elif switch_dia_semana == 3:
    print('3 corresponde a quarta-feira')
elif switch_dia_semana == 4:
    print('4 corresponde a quinta-feira')
elif switch_dia_semana == 5:
    print('5 corresponde a sexta-feira')
elif switch_dia_semana == 6:
    print('6 corresponde a sábado')
else:
    print('7 corresponde a domingo')
