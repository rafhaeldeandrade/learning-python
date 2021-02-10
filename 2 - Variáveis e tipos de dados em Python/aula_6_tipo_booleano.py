"""
Tipo booleano

Álgebra booleana -> George Boole

2 constantes, verdadeiro e falso.

True -> Verdadeiro
False -> Falso

SEMPRE COM A INICIAL MAIÚSCULA!

#errado
true, false

#certo
True, False
"""

ativo = True
print(ativo)

"""
negação (not)
Fazendo a negação, se o valor booleano for verdadeiro, nos retorná falso e vice-versa.
print(not ativo)
"""

logado = False

"""
ou (or)
Operação binária, depende de dois valores. Um ou outro deve ser verdadeiro.
 True or True -> True
 True or False -> True
 False or True -> True
 False or False -> False
"""
print(ativo or logado)

"""
e (and)
Operação binária, depende de dois valores. Os dois valores devem ser verdadeiros.
 True and True -> True
 True and False -> False
 False and True -> False
 False and False -> False
"""
print(ativo and logado)
