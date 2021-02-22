"""
Loop while

Forma geral:
while expressão_booleana:
    //execução do loop

O bloco do while será repetido enquanto a expressão booleana for verdadeira;
A condição de parada do loop while é a expressão booleana.

Ex:
num = 0
while num < 10:
    print(num, end=' ')
    num += num
output: 0 1 2 3 4 5 6 7 8 9

resposta = ''
while resposta != 'sim':
    resposta = input('Já acabou?')

while True:
    resposta = input('Você tem noção de que isso é um loop infinito?: ')
"""
num = 0
while num < 10:
    print(num, end=' ')
    num += 1

resposta = ''
while resposta != 'sim':
    resposta = input('Já acabou?')
