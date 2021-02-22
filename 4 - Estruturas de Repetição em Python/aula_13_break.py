"""
Saindo de loops com break.

Funciona da mesma forma que nas linguagens C e Java

Utilizamos o break para sair do loop de maneira projetada/forçada
Loops tem condição de parada mas podemos forçar a saída do loop com break.

Exemplos:
for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero, end=' ')
output: 1 2 3 4 5

while True:
    comando = input('Digite SAIR para sair')
    if comando == 'SAIR':
        break

"""
for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero, end=' ')

print('\n')

while True:
    comando = input('Digite SAIR para sair: ')
    if comando == 'SAIR':
        break
