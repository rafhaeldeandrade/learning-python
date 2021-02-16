"""
53,	Faça um programa para ler as dimensões de um terreno (comprimento c e largura l),
bem como o preço do metro quadrado de tela p. Imprima o custo para cercar este mesmo terreno com tela. 
"""
comprimento_terreno = float(input('Digite o comprimento do terreno: '))
largura_terreno = float(input('Digite a largura do terreno: '))
metro_tela_valor = float(input('Digite o valor do metro de tela: '))
print(f'O valor total será de {comprimento_terreno * largura_terreno * metro_tela_valor} R$')
