"""
Estruturas lógicas: or (ou); and (e); not (não).

Operadores unários:
    * NOT
    * IS

Operadores binários:
    * OR
    * AND
"""

ativo = True
logado = True

if ativo and logado:
    print('Bem-vindo, usuário(a).')
else:
    print('Você precisa ativar sua conta, por favor cheque seu e-mail.')

#se não estiver ativo, faça:
if not ativo:
    print('Você precisa ativar sua conta, por favor cheque seu e-mail.')
else:
    print('Bem-vindo, usuário(a).')

print(not True)
print(not False)
