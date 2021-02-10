"""
Tipo númerico
"""

num = 1_000_000_000_000 #podemos separar por undescore para facilitar a leitura de algum número muito grande

print(type(num)) #retorna <class 'int'>
print(num)

num = 25
print(num / 2) #return float
print(num // 2) #return int
print(num ** 2) #potência
print(num % 2) #módulo, retorna o resto da divisão de num por 2

num += 1
print(num) #num = num + 1

num -= 1
print(num) #num = num - 1

num *= 2
print(num) #num = num * 2

num /= 3
print(num) #num = num / 3
