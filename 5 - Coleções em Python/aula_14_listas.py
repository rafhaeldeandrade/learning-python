"""
Listas

Listas em python funcionam como vetores/matrizes (arrays) em outras linguagens
A diferença é que as listas são DINÂMICAS e aceitam QUALQUER tipo de dado.

Java/C:
* Arrays sempre tem tamanho e tipo de dado fixo;
Nestas linguagens se você criar um array de int com tamanho 5, ele SEMPRE será do tipo int e com tamanho 5.

Python
* Dinâmicas pois não precisamos setar o tamanho da lista ao criá-la, simplesmente vamos adicionando mais elementos.
* Não possuem tipo de dado fixo, podemos colocar qualquer tipo de dado dentro delas.
* Listas em Python são representadas por colchetes: []
"""
print(type([]))
lista1 = [1, 34, 5, 6, 7889, 12, 312, 76, 1] #lista com inteiros.
lista2 = ['R', 'a', 'f', 'h', 'a', 'e', 'l'] #lista com strings.
lista3 = [] #lista vazia
lista4 = list(range(11)) #cria uma lista com 11 valores, de 0 a 10.
lista5 = list('Rafhael') #cria uma lista a partir de uma string, cada letra é um valor.

#Checar se um valor está contido na lista:
num = 34 
if 34 in lista1: #Encontraria se num fosse: 1, 34, 5, 6, 7889, 12, 312 ou 76
    print(f'Encontrei o {num}.')
else:
    print(f'Não encontrei o {num}.')

letra = 'a'
if letra in lista2: #Encontraria se letra fosse: 'R', 'a', 'f', 'h', 'e' ou 'l'
    print(f'Encontrei a letra {letra}.')
else:
    print(f'Não encontrei a letra {letra}.')

#Podemos ordenar uma lista:
#lista1.sort()
print(lista1)

#Podemos contar o número de ocorrências de um valor em uma lista:
print(lista1.count(1))
print(lista5.count('a'))

#Podemos adicionar valores em uma lista:
#append() adiciona o valor no final da lista, e um elemento por vez.
print(lista1)
lista1.append(55) 
print(lista1)
lista1.append([35, 44, 66]) #lista dentro de outra lista, aceita qualquer tipo de dado.
print(lista1)

if [35, 44, 66] in lista1:
    print('Encontrei a lista.')
else:
    print('Não encontrei a lista.')

if [1, 34, 5] in lista1:
    print('Encontrei a lista.')
else:
    print('Não encontrei a lista.')

#extend() recebe um iterável e adiciona cada elemento deste na lista
lista1.extend([55, 66, 77, 88])
print(lista1)

#Adicionar um valor na lista informando o índice, não substitui o valor.
lista1.insert(2, 'insert')
print(lista1)

#Juntar duas listas:
#lista1 = lista1 + lista2
lista1.extend(lista2)
print(lista1)

#Imprimir a lista inversa
#lista1.reverse()
#print(lista1)
print(lista1[::-1]) #slice

#Copiar uma lista
lista6 = lista2.copy()
print(lista6)

#tamanho da lista
print(len(lista1))

#Remover o último valor da lista ou passando o índice:
lista1.pop() #Além de remover a última posição, retorna com o valor removido
print(lista1)
lista1.pop(2) #Além de remover o valor do índice escolhido, retorna com o valor removido
print(lista1)

#Remover todos os elementos, zerar a lista
print(lista5)
lista5.clear()
print(lista5)

nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

#Converter uma string para uma lista
#Por padrão o split separa os elementos da lista pelos espaços entre elas
curso = 'Programação em Python'
print(curso)
curso = curso.split()
print(curso)

#Passando a vírgula como parâmetro, agora ele separa pelas vírgulas
curso = 'Programação,em,Python'
print(curso)
curso = curso.split(',')
print(curso)

#Converter uma lista para string
#curso = ' '.join(curso)
#print(curso)
curso = '%'.join(curso)
print(curso)

#Iterar sobre listas
for elemento in lista1:
    print(elemento)

#Criar listas com variáveis
numeros = [1, 2, 3, 4, 5]
print(numeros)
num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5
numeros = [num1, num2, num3, num4, num5]
print(numeros)

#Fazemos acesso aos elementos de forma indexada
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0]) #verde
print(cores[1]) #amarelo
print(cores[2]) #azul
print(cores[3]) #branco

#Fazer acesso aos elementos de forma indexada inversa
print(cores[-1]) #branco
print(cores[-2]) #azul
print(cores[-3]) #amarelo
print(cores[-4]) #verde
#print(cores[-5]) #IndexError

print('for')
for cor in cores:
    print(cor)

print('while')
indice = 0
while indice < len(cores):
    print(cores[indice])
    indice += 1

print('for com enumerate')
for indice, cor in enumerate(cores):
    print(indice, cor)

#Métodos úteis

#Encontrar o índice de um elemento na lista
numeros = [5, 6, 7, 8, 5, 9, 10]
print(numeros.index(6))
print(numeros.index(9))
print(numeros.index(5))
#Buscar o valor dentro de um range
#numeros.index(valor_a_ser_buscado, qual_indice_começar, qual_indice_parar)
print(numeros.index(5, 1))
print(numeros.index(5, 3, 5))

#Slice de lista
#lista[índice_inicio:índice_final:passo]
lista = [1, 2, 3, 4]
print(lista[1:]) #Iniciando no índice 1 e pegando todo o resto
print(lista[:3]) #Iniciando no índice 0 e pegando até o índice 3 (não inclusive)
print(lista[::2]) #Iniciando no índice 0 e pegando os índices com passo 2 (0, 2, 4, 6..)

#Soma*, valor máximo*, valor mínimo*, tamanho
#* se todos os valores forem int ou float
lista = [1, 2, 3, 4, 5]
print(sum(lista))
print(max(lista))
print(min(lista))
print(len(lista))

#Transformar uma lista em tupla
tuple = tuple(lista)
print(tuple)
print(type(tuple))

#Desempacotando listas
lista_numeros = [1, 2, 3]
num1, num2, num3 = lista_numeros
print(num1)
print(num2)
print(num3)

#Deep copy
lista = [1, 2, 3]
print(lista)

nova = lista.copy()
print(nova)

nova.append(4)
print(lista)
print(nova)

# Shallow copy
lista = [1, 2, 3]
nova = lista
print(nova)
print(lista)
nova.append(4)
print(nova)
print(lista)
