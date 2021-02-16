"""
48.	Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos.
"""
segundos_inteiro = int(input('Digite um valor inteiro em segundos: '))
horas = int(segundos_inteiro / 3600)
resto = segundos_inteiro % 3600
minutos = int(resto / 60)
segundos = int(resto % 60)
print(f'Horas: {horas}h, minutos: {minutos}min, segundos: {segundos}s')
