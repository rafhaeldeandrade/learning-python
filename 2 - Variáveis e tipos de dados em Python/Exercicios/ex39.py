"""
39.	A importância de R$ 780.000,00 será dividida entre três ganhadores de um concurso.
Sendo que da quantia total:
*	O primeiro ganhador receberá 46%;
*	O segundo receberá 32%;
*   O terceiro receberá o restante;
Calcule e imprima a quantia ganha por cada um dos ganhadores.
"""
importancia_total = 780_000
primeiro_ganhador = 0.46 * importancia_total
segundo_ganhador = 0.32 * importancia_total
terceiro_ganhador = importancia_total - primeiro_ganhador - segundo_ganhador
print(f'O primeiro ganhador receberá: {primeiro_ganhador}; o segundo: {segundo_ganhador} e o terceiro: {terceiro_ganhador}')
