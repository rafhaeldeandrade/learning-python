"""
54.	Faça um programa que reoeba um número inteiro maior do que 1, e verifique se o número
fornecido é primo ou não.
"""
numero = int(input('Digite um número inteiro maior que 1: '))
primo = True

if numero > 1:
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break
else:
    print('Erro, o número digitado precisa ser maior que 1.')
if primo:
    print(f'O número {numero} é primo.')
else:
    print(f'O número {numero} não é primo')
