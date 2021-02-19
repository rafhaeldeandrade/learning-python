"""
16.	Usando switch, escreva um programa que leia um inteiro entre l e 12 e imprima o mês correspondente a este numero.
Isto é, janeiro se l, fevereiro se 2, e assim por diante.
"""
switch_mes_ano = int(input('Digite um número inteiro entre 1 e 12: '))

if switch_mes_ano < 1 or switch_mes_ano > 12:
    print('Digite um número inteiro entre 1 e 12.')
elif switch_mes_ano == 1:
    print('1 corresponde a janeiro')
elif switch_mes_ano == 2:
    print('2 corresponde a fevereiro')
elif switch_mes_ano == 3:
    print('3 corresponde a março')
elif switch_mes_ano == 4:
    print('4 corresponde a abril')
elif switch_mes_ano == 5:
    print('5 corresponde a maio')
elif switch_mes_ano == 6:
    print('6 corresponde a junho')
elif switch_mes_ano == 7:
    print('7 corresponde a julho')
elif switch_mes_ano == 8:
    print('8 corresponde a agosto')
elif switch_mes_ano == 9:
    print('9 corresponde a setembro')
elif switch_mes_ano == 10:
    print('10 corresponde a outubro')
elif switch_mes_ano == 11:
    print('11 corresponde a novembro')
else:
    print('12 corresponde a dezembro')
