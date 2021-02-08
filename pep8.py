"""
PEP - Python Enhancement Proposals
São propostas de melhorias para a linguagem Python

The zen of Python
import this

[1] - Utilize CamelCase para nomes de classes:

class Calculadora: #certo
    pass

class calculadora_cientifica: #errado
    pass

class CalculadoraCientifica: #certo
    pass


[2] - Utilize nomes em minúsculo, separados por underscore _, para funções e variáveis:

def my_function: #certo
    pass

def myFunction: #errado

numero = 2 #certo

numero_impar = 3 #certo


[3] - Utilize 4 espaços para identação, evite usar TAB se a IDE não "traduzir" para espaço:

if minha_lista: #certo
    print("Não está vazia")

if minha_lista: #errado
  print("Não está vazia")


[4] - Linhas em branco:

* Separar funções e definições de classe com duas linhas em branco;
* Métodos dentro de uma classe devem ser separados com uma única linha em branco.


[5] - Imports

* Sempre devem ser feitos em linhas separadas:

#errado
import sys, os 

#certo
import sys
import os

#certo [não há problemas em utilizar]
from types import StryngType, ListType

* Caso haja muitos imports de um mesmo pacote, recomenda-se fazer:
from types import(
    StringType,
    ListType,
    SetType,
    OutroType
)

* Imports devem ser colocados no topo do arquivo, logo após docstring ou quaisquer comentários e
antes de constantes ou variáveis.


[6] - Espaço em instruções e expressões:
#errado
funcao( algo [ 1 ], { outro:2})

#certo
funcao(algo[1], {outro: 2})

#errado
algo (1)

#certo
algo(1)

#errado
my_x      = 25
my_y      = 30
my_string = "Olá"

#certo
my_x = 25
my_y = 30
my_string = "Olá"


[7] - Termine sempre uma instrução com uma linha em branco
"""
import this
