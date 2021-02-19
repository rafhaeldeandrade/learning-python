"""
29.	Faça uma prova de matemática para crianças que estão aprendendo a somar números inteiros menores do que 100.
Escolha números aleatórios entre 1 e 100, e mostre na tela a pergunta: qual é a soma de a + b, onde a e b são os números aleatórios.
Peça a resposta. Faça cinco perguntas ao aluno, e mostre para ele as perguntas e as respostas corretas,
além de quantas vezes o aluno acertou.
"""
import random

numero_aleatorio_um = random.randint(1, 100)
numero_aleatorio_dois = random.randint(1, 100)
numero_aleatorio_tres = random.randint(1, 100)
numero_aleatorio_quatro = random.randint(1, 100)
numero_aleatorio_cinco = random.randint(1, 100)
numero_aleatorio_seis = random.randint(1, 100)
numero_aleatorio_sete = random.randint(1, 100)
numero_aleatorio_oito = random.randint(1, 100)
numero_aleatorio_nove = random.randint(1, 100)
numero_aleatorio_dez = random.randint(1, 100)
acertos = 0

resultado_um = int(input(f'Quanto é {numero_aleatorio_um} + {numero_aleatorio_dois}?: '))
resultado_dois = int(input(f'Quanto é {numero_aleatorio_tres} + {numero_aleatorio_quatro}?: '))
resultado_tres = int(input(f'Quanto é {numero_aleatorio_cinco} + {numero_aleatorio_seis}?: '))
resultado_quatro = int(input(f'Quanto é {numero_aleatorio_sete} + {numero_aleatorio_oito}?: '))
resultado_cinco = int(input(f'Quanto é {numero_aleatorio_nove} + {numero_aleatorio_dez}?: '))

if numero_aleatorio_um + numero_aleatorio_dois == resultado_um:
    print(f'O resultado de {numero_aleatorio_um} + {numero_aleatorio_dois} é {numero_aleatorio_um + numero_aleatorio_dois}')
    acertos += 1
else:
    print(f'O resultado de {numero_aleatorio_um} + {numero_aleatorio_dois} é {numero_aleatorio_um + numero_aleatorio_dois}')

if numero_aleatorio_tres + numero_aleatorio_quatro == resultado_dois:
    print(f'O resultado de {numero_aleatorio_tres} + {numero_aleatorio_quatro} é {numero_aleatorio_tres + numero_aleatorio_quatro}')
    acertos += 1
else:
    print(f'O resultado de {numero_aleatorio_tres} + {numero_aleatorio_quatro} é {numero_aleatorio_tres + numero_aleatorio_quatro}')

if numero_aleatorio_cinco + numero_aleatorio_seis == resultado_tres:
    print(f'O resultado de {numero_aleatorio_cinco} + {numero_aleatorio_seis} é {numero_aleatorio_cinco + numero_aleatorio_seis}')
    acertos += 1
else:
    print(f'O resultado de {numero_aleatorio_cinco} + {numero_aleatorio_seis} é {numero_aleatorio_cinco + numero_aleatorio_seis}')

if numero_aleatorio_sete + numero_aleatorio_oito == resultado_quatro:
    print(f'O resultado de {numero_aleatorio_sete} + {numero_aleatorio_oito} é {numero_aleatorio_sete + numero_aleatorio_oito}')
    acertos += 1
else:
    print(f'O resultado de {numero_aleatorio_sete} + {numero_aleatorio_oito} é {numero_aleatorio_sete + numero_aleatorio_oito}')

if numero_aleatorio_nove + numero_aleatorio_dez == resultado_cinco:
    print(f'O resultado de {numero_aleatorio_nove} + {numero_aleatorio_dez} é {numero_aleatorio_nove + numero_aleatorio_dez}')
    acertos += 1
else:
    print(f'O resultado de {numero_aleatorio_nove} + {numero_aleatorio_dez} {numero_aleatorio_nove + numero_aleatorio_dez}')

print(f'Você acertou {acertos} vezes!')
