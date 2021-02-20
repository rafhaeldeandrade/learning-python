"""
40.	O custo ao consumidor de um carro novo é a soma do custo de fábrica,
da comissão do distribuidor, e dos impostos. A comissão e os impostos são calculados sobre o custo de fábrica,
de acordo com a tabela abaixo. Leia o custo de fábrica e escreva o custo ao consumidor.

CUSTO DE FABRICA	            % DO DISTRIBUIDOR	% DOS IMPOSTOS
até R$12.000,00	                    5	                isento
entre R$12.000,00 e 25.000,00	    10	                15
acima de R$25.000,00	            15                  20
"""
custo_fabrica = float(input('Digite o custo de fábrica: '))

if custo_fabrica <= 12_000:
    custo_consumidor = custo_fabrica + custo_fabrica * 0.05
elif custo_fabrica <= 25_000:
    custo_consumidor = custo_fabrica + custo_fabrica * 0.1 + custo_fabrica * 0.15
else:
    custo_consumidor = custo_fabrica + custo_fabrica * 0.15 + custo_fabrica * 0.2

print(f'O preço pro consumidor é: R${custo_consumidor:.2f}')
