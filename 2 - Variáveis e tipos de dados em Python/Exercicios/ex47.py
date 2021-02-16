"""
Leia um número inteiro de 4 dígitos (de 1000 a 9999) e imprima 1 dígito por linha.
"""
numero_inteiro = int(input('Digite um número inteiro de quatro dígitos (de 1000 a 9999): '))
numero_string = str(numero_inteiro)
print(f"""{numero_string[0]}
{numero_string[1]}
{numero_string[2]}
{numero_string[3]}""")
