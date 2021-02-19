"""
26.	Leia a distância em Km e a quantidade de litros de gasolina consumidos por um carro em um percurso,
calcule o consumo em Km/l e escreva uma mensagem de acordo com a tabela abaixo:
CONSUMO	(Km/l)	MENSAGEM
menor que	8	Venda o carro!
entre	8 e 14	Económico!
maior que	14	Super económico!
"""
distancia = float(input('Digite a distância do percurso: '))
combustivel = float(input('Digite a quantidade de combustível gasta nesse percurso: '))

if distancia / combustivel < 8:
    print('Venda o carro!')
elif distancia / combustivel >= 8 and distancia / combustivel <= 14:
    print('Econômico!')
else:
    print('Super econômico!')
