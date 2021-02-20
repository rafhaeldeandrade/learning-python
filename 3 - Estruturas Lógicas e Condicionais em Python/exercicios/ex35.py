"""
35. Leia uma data e determine se ela é válida, ou seja, verifique se o mês está entre 1 e 12,
e se o dia existe naquele mês. Note que fevereiro tem 29 dias em anos bissextos e 28 dias em anos
não bissextos.
"""
ano = int(input('Digite o ano (ex: 1993): '))
mes = int(input('Digite o mês do ano (1 a 12):'))
dia = int(input('Digite o dia (1 a 31): '))

if mes == 1:
    if dia >= 1 and dia <= 31:
        print('Data válida')
    else:
        print('Data inválida')
elif mes == 2:
    if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
        if dia >= 1 and dia <= 29:
            print('Data válida')
        else:
            print('Data inválida')
    elif dia >= 1 and dia <= 28:
        print('Data válida')
    else:
        print('Data inválida')
elif mes == 3:
    if dia >= 1 and dia <= 31:
        print('Data válida')
    else:
        print('Data inválida')
elif mes == 4:
    if dia >= 1 and dia <= 30:
        print('Data válida')
    else:
        print('Data inválida')
elif mes == 5:
    if dia >= 1 and dia <= 31:
        print('Data válida')
    else:
        print('Data inválida')
elif mes == 6:
    if dia >= 1 and dia <= 30:
        print('Data válida')
    else:
        print('Data inválida')
elif mes == 7:
    if dia >= 1 and dia <= 31:
        print('Data válida')
    else:
        print('Data inválida')
elif mes == 8:
    if dia >= 1 and dia <= 31:
        print('Data válida')
    else:
        print('Data inválida')
elif mes == 9:
    if dia >= 1 and dia <= 30:
        print('Data válida')
    else:
        print('Data inválida')
elif mes == 10:
    if dia >= 1 and dia <= 31:
        print('Data válida')
    else:
        print('Data inválida')
elif mes == 11:
    if dia >= 1 and dia <= 30:
        print('Data válida')
    else:
        print('Data inválida')
elif mes == 12:
    if dia >= 1 and dia <= 31:
        print('Data válida')
    else:
        print('Data inválida')
else:
    print('Digite um mês válido, de 1 a 12.')
