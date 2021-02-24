"""
52. Escreva um programa que receba como entrada o valor do saque realizado
pelo cliente de um banco e retorne quantas notas de cada valor serão necessárias
para atender ao saque com a menor quantidade de notas possível.
Serão utilizadas notas de 100, 50, 20, 10, 5, 2 e 1 real.
"""
saque = int(input('Digite um valor de saque: '))

saque_cem = int(saque / 100)
resto_cem = saque % 100
saque_cinquenta = int(resto_cem / 50)
resto_cinquenta = resto_cem % 50
saque_vinte = int(resto_cinquenta / 20)
resto_vinte = resto_cinquenta % 20
saque_dez = int(resto_vinte / 10)
resto_dez = resto_vinte % 10
saque_cinco = int(resto_dez / 5)
resto_cinco = resto_dez % 5
saque_dois = int(resto_cinco / 2)
resto_dois = resto_cinco % 2
saque_um = resto_dois / 1

if saque_cem > 0:
    print(f'{saque_cem} nota(s) de cem')

if saque_cinquenta > 0:
    print(f'{saque_cinquenta} nota(s) de cinquenta')

if saque_vinte > 0:
    print(f'{saque_vinte} nota(s) de vinte')

if saque_dez > 0:
    print(f'{saque_dez} nota(s) de dez')

if saque_cinco > 0:
    print(f'{saque_cinco} nota(s) de cinco')

if saque_dois > 0:
    print(f'{saque_dois} nota(s) de dois')

if saque_um > 0:
    print(f'{saque_um} nota(s) de um')
