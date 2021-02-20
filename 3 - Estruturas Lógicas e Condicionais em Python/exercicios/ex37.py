"""
37.	As tarifas de certo parque de estacionamento são as seguintes:
*	1“ e 2" hora - R$ 1,00 cada
*	3" e 4" hora - R$ 1,40 cada
*	5“ hora e seguintes - R$ 2,00 cada
O número de horas a pagar é sempre inteiro e arredondado por excesso.
Deste modo, quem estacionar durante 61 minutos pagará por duas horas,
que é o mesmo que pagaria se tivesse permanecido 120 minutos.
Os momentos de chegada ao parque e partida deste são apresentados na forma de pares de inteiros,
representando horas e minutos. Por exemplo, o par 12 50 representará “dez para a uma da tarde".
Pretende-se criar um programa que, lidos pelo teclado os momentos de chegada e de partida,
escreva na tela o preço cobrado pelo estacionamento.
Admite-se que a chegada e a partida se dão com intervalo não superior a 24 horas.
Portanto, se uma dada hora de chegada for superior à da partida, isso não é uma situação de erro,
antes significará que a partida ocorreu no dia seguinte ao da chegada.
"""
hora_chegada = input('Digite a hora de chegada (ex: 05 30 = 5 e 30 da manhã): ').split()
hora_partida = input('Digite a hora de partida (ex: 09 30 = 9 e 30 da manhã): ').split()

#if (int(hora_partida[0]) < 0 or int(hora_partida[0]) > 23 or int(hora_partida[1]) < 0 or int(hora_partida[1] > 59)
#    or int(hora_chegada[0]) < 0 or int(hora_chegada[0]) > 23 or int(hora_chegada[1]) < 0 or int(hora_chegada[1] > 59)):
#    print('Digite a hora e minuto corretamente, exemplo: 04 20; 12 30; 23 59')

if int(hora_chegada[0]) > int(hora_partida[0]):
    hora_efetiva = (int(hora_partida[0]) * 60) + int(hora_partida[1]) + (1440 - (int(hora_chegada[0]) * 60)) + (60 - int(hora_chegada[1]))
    print(hora_efetiva)
else:
    hora_efetiva = (int(hora_partida[0]) * 60) + int(hora_partida[1]) - (int(hora_chegada[0]) * 60) + int(hora_chegada[1])

if hora_efetiva < 121:
    print(f'Preço cobrado: R${int(hora_efetiva / 60) * 1}')
elif hora_efetiva <= 300:
    print(f'Preço cobrado: R${int(hora_efetiva / 60) * 1.40}')
else:
    print(f'Preço cobrado: R${int(hora_efetiva / 60) * 2}')
