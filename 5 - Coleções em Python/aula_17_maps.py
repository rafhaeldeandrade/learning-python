"""
Continuação da aula 16, dicionários.
"""
receita = {'jan': 100, 'fev': 250, 'mar': 400}

#Iterar sobre dicionários
print(receita)

for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'Chave: {chave} Receita: {receita[chave]}')

#Acessando as chaves
print(receita.keys())
for chave in receita.keys():
    print(chave)

#Acessando os valores
for valor in receita.values():
    print(valor)

#Desempacotamento de dicionários
for chave, valor in receita.items():
    print(f'Chave: {chave} Valor: {valor}')

#Soma*, Valor máximo*, Valor mínimo*, Tamanho
#* Se todos os valores forem int ou float
print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))
