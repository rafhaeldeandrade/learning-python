"""
Calcule as raízes da equação de 2o grau:

lembrando que:

x = -b +- sqrt(delta) / 2a

delta = b * b - 4ac
"""
a = float(input('Digite a variável A da equação: '))
b = float(input('Digite a variável B da equação: '))
c = float(input('Digite a variável C da equação: '))
delta = (b ** 2) - (4 * a * c)

if a == 0:
    print('Não é uma equação de segundo grau.')
elif delta < 0:
    print('Não existe raiz.')
elif delta == 0:
    raiz = (- b + (delta ** 0.5)) / (2 * a)
    print(f'Raiz única, {raiz}')
else:
    raiz_um = (- b + (delta ** 0.5)) / (2 * a)
    raiz_dois = (- b - (delta ** 0.5)) / (2 * a)
    print(f'Primeira raiz: {raiz_um}\nSegunda raiz: {raiz_dois}')
