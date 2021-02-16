"""
43.	Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:
*	o total a pagar com desconto de 10%;
*	o valor de cada parcela, no parcelamento de 3x sem juros;
*	a comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com des¬conto)
*	a comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total)
"""
valor_venda = float(input('Digite um valor: '))
valor_pagar_desconto = valor_venda * 0.9
valor_parcela = valor_venda / 3.0
comissao_vendedor_a_vista = valor_pagar_desconto * 0.05
comissao_vendedor_parcelado = valor_venda * 0.05
print(f"""Total a pagar com desconto: {valor_pagar_desconto}
Valor de cada parcela (3x): {valor_parcela:.2f}
Comissão do vendedor, venda a vista: {comissao_vendedor_a_vista}
Comissão do vendedor, venda a prazo: {comissao_vendedor_parcelado}""")
