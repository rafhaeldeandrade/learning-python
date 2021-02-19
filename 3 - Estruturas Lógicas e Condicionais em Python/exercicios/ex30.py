"""
30.	Faça um programa que receba três números e mostre-os em ordem crescente.
"""
numero_um = float(input('Digite o primeiro número: '))
numero_dois = float(input('Digite o segundo número: '))
numero_tres = float(input('Digite o terceiro número: '))

if numero_um > numero_dois and numero_dois > numero_tres:
    print(f'Ordem crescente: {numero_tres}, {numero_dois}, {numero_um}')
elif numero_dois > numero_um and numero_um > numero_tres:
    print(f'Ordem crescente: {numero_tres}, {numero_um}, {numero_dois}')
elif numero_dois > numero_tres and numero_tres > numero_um:
    print(f'Ordem crescente: {numero_um}, {numero_tres}, {numero_dois}')
elif numero_tres > numero_um and numero_um > numero_dois:
    print(f'Ordem crescente: {numero_dois}, {numero_um}, {numero_tres}')
elif numero_tres > numero_dois and numero_dois > numero_um:
    print(f'Ordem crescente: {numero_um}, {numero_dois}, {numero_tres}')
else:
    print(f'Ordem crescente: {numero_dois}, {numero_tres}, {numero_um}')
