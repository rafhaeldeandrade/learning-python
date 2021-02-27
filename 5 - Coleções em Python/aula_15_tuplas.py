"""
Tuplas

Existem basicamente duas diferenças básicas entre listas e tuplas
1. As tuplas são representadas por parenteses ()
2. As tuplas são imutáveis; ao se criar uma tupla, ela não muda; toda operação em uma tupla gera uma nova tupla. 

* Tuplas são mais rápidas que listas.
* Tuplas deixam seu código mais seguro pois trabalhar com coleções imutáveis traz segurança.
"""
tupla1 = (1, 2, 3, 4, 5)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5
print(tupla2)
print(type(tupla2))

#Tupla com 1 elemento
tupla3 = (4)
print(tupla3) 
print(type(tupla3)) #não é uma tupla

tupla4 = (4,)
print(tupla4) 
print(type(tupla4)) #é uma tupla

tupla5 = 5,
print(tupla5)
print(type(tupla5)) #é uma tupla

tupla6 = tuple(range(11))
print(tupla6)

#Desempacotamento de tupla
tupla7 = ('Geek University', 'Programação em Python')
escola, curso = tupla7
print(escola)
print(curso)

#Métodos para adição e remoção nas tuplas não existem, dado o fato das tuplas serem imutáveis.

#Soma*, Valor máximo*, Valor mínimo*, e tamanho.
#* se os valores forem todos inteiros ou float
tupla8 = 1, 2, 3, 4, 5, 6
print(sum(tupla8))
print(min(tupla8))
print(max(tupla8))
print(len(tupla8))

#Concatenação de tuplas
tupla9 = (1, 2, 3)
print(tupla9)
tupla10 = (4, 5, 6)
print(tupla10)

print(tupla9 + tupla10)
print(tupla9)
print(tupla10)

#verificar se determinado valor está na tupla
tupla11 = (1, 2, 3)
print(2 in tupla11)

#Iterar sobre uma tupla
for num in tupla11:
    print(num)

for indice, valor in enumerate(tupla11):
    print(indice, valor)

#Contar elementos em uma tupla
tupla12 = ('a', 'b', 'b', 'c', 'a')
print(tupla12.count('a'))
print(tupla12.count('b'))
print(tupla12.count('c'))

#Devemos utilizar tuplas sempre que não precisarmos modificar os dados contidos na coleção
tupla_meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

#O acesso aos valores é semelhante às listas
print(tupla_meses[5])

#Iterar com while
i = 0
while i < len(tupla_meses):
    print(tupla_meses[i])
    i += 1

#Verificar qual o índice do valor
print(tupla_meses.index('Março'))
