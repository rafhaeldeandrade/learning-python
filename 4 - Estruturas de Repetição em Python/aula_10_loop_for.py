"""
Loop é uma estrutura de repetição
For é uma dessas estruturas.

C ou JAVA:
for(int i=0; i < 10; i++){
    //commands
}

Python
for item in iteravel:
    //commands

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis.
Valores iteráveis:
* String
nome = 'Python'

* Lista
nome = ['Linguagem', 'Python']

* range()
numeros = range(10)

nome = 'Linguagem Python'
lista= [1, 2, 3, 4, 5, 6, 7, 8, 9]
#exemplo 1
for letra in nome:
    print(letra)

#exemplo 2
for numero in lista:
    print(numero)

#exemplo 3
for numero in range(1, 10):
    print(numero)

range(valor_de_inicio, valor_final) <- valor_final não é inclusive! Último valor será valor_final - 1
ex: range(1, 10)
for i in range(1, 10):
    print(i)

1
2
3
4
5
6
7
8
9
10 <- Não imprime.

Se não especificar o valor_de_inicio, o default é 0.
range(10)
0
1
2
3
4
5
6
7
8
9
10 <- Não imprime.

-------------------------------------------------------------------------------

#enumerate(nome)
#((0, 'L'), (1, 'i'), (2, 'n'), (3, 'g')...)
for indice, letra in enumerate(nome):
    print(nome[indice])

for indice, letra in enumerate(nome):
    print(letra)

Quando não precisamos de um valor, podemos descartá-lo utilizando um underline (_)
for _, letra in enumerate(nome):
    print(letra)

for valor in enumerate(nome):
    print(valor)

-------------------------------------------------------------------------------

qtd = int(input('Quantas vezes esse loop deve rodar?: '))

for numero in range(1, qtd+1):
    print(f'Imprimindo {numero}/{qtd}')

qtd = int(input('Quantas vezes esse loop deve rodar?: '))
soma = 0

for i in range(1, qtd+1):
    valor = int(input(f'Informe o valor {i}/{qtd}: '))
    soma += valor

print(f'A soma dos valores informados é: {soma}')

nome = 'Linguagem Python'

for letra in nome:
    print(letra, end='')
"""
for i in range(1, 11):
    print('\U0001F601' * i)

for _ in range(5):
    for i in range(1, 11):
        print('\U0001F601' * i)
