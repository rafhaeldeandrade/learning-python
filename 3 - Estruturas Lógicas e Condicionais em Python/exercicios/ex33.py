"""
33. Um produto vai sofrer aumento de acordo com a tabela abaixo. Leia o preço antigo,
calcule e escreva o preço novo, escreva uma mensagem em função do preço novo (de acordo com a segunda tabela)

PREÇO ANTIGO        PERCENTUAL DE AUMENTO
até R$50            5%
entre R$50 e R$100  10%
acima de R$100      15%

PREÇO NOVO                      MENSAGEM
até R$80                        Barato
entre R$80 e R$120 (inclusive)  Normal
entre R$120 e R$200 (inclusive) Caro
acima de R$200                  Muito caro
"""
preco_antigo = float(input('Digite o preço antigo: '))

if preco_antigo < 50:
    print('Barato')
elif preco_antigo <= 100:
    if preco_antigo + preco_antigo * 0.1 < 80:
        print('Barato')
    else:
        print('Normal')
else:
    if preco_antigo + preco_antigo * 0.15 > 80 and preco_antigo + preco_antigo * 0.15 <= 120:
        print('Normal')
    elif preco_antigo + preco_antigo * 0.15 > 120 and preco_antigo + preco_antigo * 0.15 <= 200:
        print('Caro')
    else:
        print('Muito caro')
