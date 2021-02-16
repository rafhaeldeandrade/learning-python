"""
52. Três amigos jogaram na loteria.
Caso eles ganhem, o prêmio deve ser repartido proporcionalmente ao valor que cada deu um para a realização da aposta.
Faça um programa que leia quanto cada apostador investiu, o valor do prêmio, e imprima quanto cada um ganharia
do prêmio com base no valor investido.
"""
investimento_pessoa_um = int(input('Digite o valor que a pessoa um investiu: '))
investimento_pessoa_dois = int(input('Digite o valor que a pessoa dois investiu: '))
investimento_pessoa_tres = int(input('Digite o valor que a pessoa três investiu: '))
valor_do_premio = float(input('Digite o valor total do prêmio: '))
valor_total_investido = investimento_pessoa_um + investimento_pessoa_dois + investimento_pessoa_tres
pessoa_um_recebe = investimento_pessoa_um / valor_total_investido
pessoa_dois_recebe = investimento_pessoa_dois / valor_total_investido
pessoa_tres_recebe = investimento_pessoa_tres / valor_total_investido
print(f"""Pessoa um receberá aprox.: {(pessoa_um_recebe * valor_do_premio):.2f} R$
Pessoa dois receberá aprox.: {(pessoa_dois_recebe * valor_do_premio):.2f} R$
Pessoa três receberá aprox.: {(pessoa_tres_recebe * valor_do_premio):.2f} R$""")
