"""
49.	Faça um programa para leia o horário (hora, minuto e segundo) de inicio e a duração, em segundos, de uma experiência biológica.
O programa deve resultar com o novo horário (hora, minuto e segundo) do termino da mesma.
"""
horario_inicio_hora = int(input('Digite a hora do início: '))
horario_inicio_minuto = int(input('Digite o minuto do início: '))
horario_inicio_segundo = int(input('Digite o segundo do início: '))
horario_duracao = int(input('Digite a duração da experiência em segundos: '))
horas = int(horario_duracao / 3600)
resto = horario_duracao % 3600
minutos = int(resto / 60)
segundos = int(resto % 60)
print(f'Hora do término: {horario_inicio_hora + horas}h{horario_inicio_minuto + minutos}min{horario_inicio_segundo + segundos}s')
