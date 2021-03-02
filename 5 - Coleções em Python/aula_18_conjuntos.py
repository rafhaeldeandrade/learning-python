"""
Conjuntos (Sets)

* Conjuntos em qualquer linguagem de programação, estamos fazendo referência à teoria dos conjuntos da matemática
* No python os conjuntos são chamados de Sets

Da mesma forma que na matemática:
* Sets não possuem valores duplicados;
* Sets não possuem valores ordenados;
* Elementos não são acessados via índice, ou seja, conjuntos não são indexados

Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas não nos importamos com a ordenação
deles. Quando não precisamos nos preocupar com chaves, valores e itens duplicados.

Os sets são referenciados com {}
"""
# Definindo um conjunto / Forma 1

s = set({1, 2, 3, 4, 5, 6, 7, 2, 2, 1})
print(s)
print(type(s))

# Ao criarmos um conjunto, caso seja adicionado um valor já existente, o mesmo será ignorado sem gerar erros.

# Forma 2

s = {1, 2, 3, 4, 5, 5, 6}
print(s)
print(type(s))

# Verificar se determinado elemento está contido no set

if 3 in s:
    print('tem o 3')
else:
    print('não tem o 3')

lista = [99, 3, 2, 2, 1, 5, 6, 7, 3, 2]
print(f'Lista: {lista} com {len(lista)} elementos')

tupla = (99, 3, 2, 2, 1, 5, 6, 7, 3, 2)
print(f'Tupla: {tupla} com {len(tupla)} elementos')

dicionario = {}.fromkeys([99, 3, 2, 2, 1, 5, 6, 7, 3, 2], 'dict')
print(f'Dicionario: {dicionario} com {len(dicionario)} elementos')

set = {99, 3, 2, 2, 1, 5, 6, 7, 3, 2}
print(f'Set: {set} com {len(set)} elementos')

# Assim como todas as outras coleções em Python, podemos colocar qualquer tipo de dado em Sets

s = {1, '2', True, 34.45}
print(s)
print(type(s))

# Podemos iterar em um set normalmente.
for valor in s:
    print(valor)

# Adicionar elementos em um set
s = {1, 2, 3, 4, 4, 5}
print(s)
s.add(6) # add() recebe como parametro o valor, não o índice.
print(s)

# Remover elementos em um set
s = {1, 2, 3, 4, 4, 5}
print(s)
s.remove(4)
print(s)

s = {1, 2, 3, 4, 4, 5}
print(s)
s.discard(2)
print(s)

# Copiar um set
# Deep copy
s = {1, 2, 3, 4, 5}
novo = s.copy()
print(s)
print(novo)
novo.add(6)
print(s)
print(novo)

# Shallow copy
s = {1, 2, 3, 4, 5}
novo = s
print(s)
print(novo)
novo.add(6)
print(s)
print(novo)

# Métodos matemáticos de conjuntos
alunos_python = {'Pedro', 'Julia', 'Ricardo', 'Jonas'}
alunos_java = {'Pedro', 'Julia', 'Raphael', 'Caroline'}

# Gerar um set com os alunos únicos, com union()
alunos_unicos = alunos_python.union(alunos_java)
print(alunos_unicos)

# Gerar um set com os alunos que estão em ambos os cursos, intersection()
alunos_ambos = alunos_python.intersection(alunos_java)
print(alunos_ambos)

# Gerar um conjunto dos alunos que não estão nos outros cursos, difference()
so_python = alunos_python.difference(alunos_java)
so_java = alunos_java.difference(alunos_python)
print(so_python)
print(so_java)

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho:
# * Somente se todos os elementos forem int ou float
s = {1, 2, 3, 4, 5}
print(sum(s))
print(max(s))
print(min(s))
print(len(s))
