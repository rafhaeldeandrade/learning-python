"""
24,	Uma empresa vende o mesmo produto para quatro diferentes estados.
Cada estado possui uma taxa diferente de imposto sobre o produto (MG 7%; SP 12%; RJ 15%; MS 8%)
Faça um programa em que o usuário entre com o valor e o estado destino do produto e o programa
retorne o preço final do produto acrescido do imposto do estado em que efe será vendido.
Se o estado digitado não for válido, mostrar uma mensagem de erro.
"""
valor = float(input('Digite o valor do produto: '))
estado = input("""Digite a sigla do estado:
MG para Minas Gerais
SP para São Paulo
RJ para Rio de Janeiro
MS para Mato Grosso do Sul
Sua opção é: """)

if estado == 'MG':
    print(f'O preço final do produto é {valor + valor * 0.07}')
elif estado == 'SP':
    print(f'O preço final do produto é {valor + valor * 0.12}')
elif estado == 'RJ':
    print(f'O preço final do produto é {valor + valor * 0.15}')
elif estado == 'MS':
    print(f'O preço final do produto é {valor + valor * 0.08}')
else:
    print('Estado inválido, digite corretamente.')
