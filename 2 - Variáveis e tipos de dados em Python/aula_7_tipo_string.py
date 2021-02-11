"""
Em python, um dado é considerado string sempre que:

* Estiver entre aspas simples: 'uma string', 'b', '288', 'True', '44.5'
* Estiver entre aspas duplas: "uma string", "b", "288", "True", "44.5"
* Estiver entre aspas simples triplas: '''uma string''', '''b''', '''288''', '''True''', '''44.5'''
"""
# Estiver entre aspas duplas triplas: """uma string""", """b""", """288""", """True""", """44.5"""
"""
nome = 'Testando'
print(nome)
print(type(nome)) # <class 'str'>

nome = "Gina's bar"
print(nome)
print(type(nome)) # <class 'str'>

nome = 'Maria \nAparecida' #\n quebra a linha
print(nome)
print(type(nome)) # <class 'str'>

nome = "Maria \" Aparecida" # Maria " Aparecida
print(nome)
print(type(nome)) # <class 'str'>

nome = 'Maria Aparecida'
print(nome.upper())
print(nome.lower())
print(nome.capitalize())
print(nome.title())
print(nome.split()) # transforma em uma lista de strings

string_teste = 'Maria Aparecida'
# string em python SÃO listas!
#[ 0.   1,   2,   3,   4,   5,   6,   7,   8,   9,   10,  11,  12,  13,  14]
#['M', 'a', 'r', 'i', 'a', ' ', 'A', 'p', 'a', 'r', 'e', 'c', 'i', 'd', 'a']
print(string_teste[0:5]) # slice de string
print(string_teste[6:15]) # slice de string
print(string_teste.split()[0])
"""
string_teste = 'Maria Aparecida'

#[::-1] - > comece do primeiro elemento, vá até o último elemento e inverta.
print(string_teste[::-1])

print(string_teste.replace('a', 'b'))

texto = 'socorram me subino onibus em marrocos'
print(texto)
print(texto[::-1])

nome = 'ana'
print(nome)
print(nome[::-1])
