"""
Dicionários

Em algumas linguagens os dicionários em Python são conhecidos como maps.

Dicionários são coleções do tipo chave:valor
Dicionários são representados por {}
print(type({})

Ex: {'br': 'Brasil', 'py': 'Paraguai', 'eua': 'Estados Unidos'}

* Chave e valor são separados por dois pontos (:);
* Tanto chave quanto valor podem sem de qualquer tipo de dado;
* Podemos misturar tipos de dados.
"""
#Criar dicionários
#Mais comum
paises = {'br': 'Brasil', 'py': 'Paraguai', 'eua': 'Estados Unidos'}
print(paises)
print(type({}))

#Menos comum
paises = dict(br='Brasil', py='Paraguai', eua='Estados Unidos')
print(paises)
print(type({}))

#Acessar elementos
print(paises['br'])
print(paises['py'])
#print(paises['ru']) #Caso a chave não exista retorna um KeyError

print(paises.get('br'))
print(paises.get('py'))
print(paises.get('ru')) #Caso a chave não existe, retorna None e não dá erro.

#pais = paises.get('ru')
pais = paises.get('py')
if pais:
    print('Encontrei o país.')
else:
    print('Não encontrei o país.')

print(paises.get('ru', 'País não encontrado')) #get(chave, valor_padrao_caso_a_chave_nao_exista)

#Verificar se determinada chave se encontra em um dicionário
print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']

#Podemos utilizar qualquer tipo de dado (int, float, string, boolean) inclusive listas, tuplas, dicionários como chaves de dicionários
localidades = {
(35.2332, 44.0029): 'Escritório em Tokyo',
(2.3423, 54.3212): 'Escritório em Nova Iorque',
(98.8224, 65.6325): 'Escritório em São Paulo'
}
print(localidades)

#Adicionar elementos
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)
receita['abr'] = 400
print(receita)

novo_dado = {'mai': 500}
receita.update(novo_dado) #receita.update({'mai': 500})
print(receita)

#Atualizar dados
receita['mai'] = 550
print(receita)
receita.update({'mai': 600})
print(receita)

#A forma de atualizarmos ou adicionarmos novos elementos é a mesma
#Não podem ter chaves repetidas em dicionários

#Remover dados de um dicionário
receita.pop('mar') #Precisamos sempre informar a chave, caso não encontre um KeyError é retornado
print(receita)

del receita['abr']
print(receita)

"""
Imagine que você tem um comércio eletrônico onde temos um carrinho de compras na qual adicionamos produtos
Carrinho de Compras:
    Produto 1:
        * Nome;
        * Quantidade;
        * Preço.
    Produto 2
        * Nome;
        * Quantidade;
        * Preco.
"""
# Com listas você precisará saber qual o indíce de cada valor
carrinho = []
produto1 = ['Playstation 4', 1, 2300.0]
produto2 = ['God of War 4', 2, 150.0]
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

#Com tuplas você também precisará saber qual o índice de cada valor
produto1 = ('Playstation 4', 1, 2300.0)
produto2 = ('God of War 4', 2, 150.0)
carrinho = (produto1, produto2)
print(carrinho)

#Com dicionários fica mais explícito
carrinho = []
produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preco': 2300.0}
produto2 = {'nome': 'God of War 4', 'quantidade': 2, 'preco': 150.0}
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

#Métodos de dicionários
d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

#Limpar o dicionário
d.clear()
print(d)

#Copiando um dicionário para outro
#Deep copy
d = dict(a=1, b=2, c=3)
novo = d.copy()
print(novo)
novo['d'] = 4
print(d)
print(novo)

#Shallow copy
d = dict(a=1, b=2, c=3)
novo = d
novo['d'] = 4
print(novo)
print(d)

#Forma não usual de criação de dicionários
#Método fromkeys() recebe dois parâmetros: um iterável e um valor
outro = {}.fromkeys('a', 'b')
print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)

veja = {}.fromkeys('teste', 'valor')
print(veja)
veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)
