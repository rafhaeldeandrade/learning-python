"""
Tipo float

aka decimal, real

O separador de casas decimais é o . (ponto) e não a , (vírgula)
"""
#errado no ponto de vista de querermos um float, pois isso está gerando uma tupla
valor = 1, 44
print(valor)
print(type(valor))

#certo
valor = 1.44
print(valor)
print(type(valor))

#é possível fazer dupla atribuição
valor1, valor2 = 2, 50
print(valor1)
print(valor2)

#converter um float para int, perdendo precisão
print(type(valor))
res = int(valor)
print(res)
print(type(res))

#trabalhar com números complexos
variavel_complexa = 5j
print(type(variavel_complexa))
